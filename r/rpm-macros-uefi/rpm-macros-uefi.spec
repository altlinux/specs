Name: rpm-macros-uefi
Version: 0.1
Release: alt1

Summary: A set of RPM macros to help package UEFI related things
License: Public domain
Group: Development/Other

Url: http://www.altlinux.org/UEFI

# NB: it's *not* noarch due to %%_libdir in a macro

%define macrofile %_rpmmacrosdir/uefi
%define keydir %_sysconfdir/pki/uefi

%description
This package carries helpful macros to package
(and probably sign before that) UEFI binaries.

%prep

%build

%install
mkdir -p %buildroot%_rpmmacrosdir
cat > %buildroot%macrofile << EOF
%%_efi_bootdir /boot/efi
%%_efi_bindir %_libdir/efi

%%_efi_keydir %keydir
%%_efi_keyfile %%{?2:%%2}%%{?!2:altlinux}

%%_efi_sign() \\
BINARY="%%1" \\
case "%%1" in \\
*.efi) BINARY="\${BINARY%%%%.efi}";; \\
esac \\
SIGNED="\$BINARY-signed.efi" \\
ARGS="--key \\"%%_efi_keydir/%%_efi_keyfile.key\\"" \\
ARGS="\$ARGS --cert \\"%%_efi_keydir/%%_efi_keyfile.crt\\"" \\
ARGS="\$ARGS --output \\"\$SIGNED\\" \\"\$BINARY.efi\\"" \\
if sbsign \$ARGS >&2; then \\
	echo "\${SIGNED#%%buildroot}" >> signed.manifest \\
fi \\
%%nil
EOF

%files
%macrofile

%changelog
* Thu Jan 10 2013 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

