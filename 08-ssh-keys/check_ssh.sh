#!/bin/bash

echo "============================="
echo "  SSH Key Setup Checker"
echo "============================="
echo ""

PASS=0
FAIL=0

check() {
    local desc="$1"
    local result="$2"
    if [ "$result" = "ok" ]; then
        echo "  [OK]   $desc"
        PASS=$((PASS + 1))
    else
        echo "  [MISS] $desc"
        FAIL=$((FAIL + 1))
    fi
}

# Check ~/.ssh exists
[ -d "$HOME/.ssh" ] && check ".ssh folder exists" "ok" || check ".ssh folder exists" "fail"

# Check for a private key
if ls "$HOME/.ssh/id_"* 2>/dev/null | grep -qv ".pub"; then
    check "Private key found" "ok"
else
    check "Private key found (run: ssh-keygen -t ed25519)" "fail"
fi

# Check for a public key
if ls "$HOME/.ssh/id_"*.pub 2>/dev/null | grep -q ".pub"; then
    check "Public key found" "ok"
else
    check "Public key found" "fail"
fi

# Check authorized_keys exists
[ -f "$HOME/.ssh/authorized_keys" ] && check "authorized_keys file exists" "ok" || check "authorized_keys file exists" "fail"

# Check permissions on .ssh
PERM=$(stat -c "%a" "$HOME/.ssh" 2>/dev/null)
[ "$PERM" = "700" ] && check ".ssh folder permissions are 700" "ok" || check ".ssh folder permissions should be 700 (run: chmod 700 ~/.ssh)" "fail"

# Check authorized_keys permissions if it exists
if [ -f "$HOME/.ssh/authorized_keys" ]; then
    PERM2=$(stat -c "%a" "$HOME/.ssh/authorized_keys")
    [ "$PERM2" = "600" ] && check "authorized_keys permissions are 600" "ok" || check "authorized_keys permissions should be 600 (run: chmod 600 ~/.ssh/authorized_keys)" "fail"
fi

echo ""
echo "Result: $PASS checks passed, $FAIL need attention"

# Show their public key if it exists
PUB_KEY=$(ls "$HOME/.ssh/id_"*.pub 2>/dev/null | head -1)
if [ -n "$PUB_KEY" ]; then
    echo ""
    echo "Your public key (safe to share):"
    echo "---"
    cat "$PUB_KEY"
    echo "---"
fi
