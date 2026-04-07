Name: installer-feature-efi-removable
Version: 0.1
Release: alt1

Summary: Preinstall hook for create /etc/efi_removable.flag
License: GPL-2.0-or-later
Group: System/Configuration/Other

URL: https://altlinux.org

BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot%_datadir/install2/preinstall.d
cat > %buildroot%_datadir/install2/preinstall.d/00-efi-removable-flag.sh << 'EOF'
#!/bin/sh
. install2-sh-functions

touch "$destdir"/etc/efi_removable.flag
EOF
chmod +x %buildroot%_datadir/install2/preinstall.d/00-efi-removable-flag.sh

%files
%_datadir/install2/preinstall.d/00-efi-removable-flag.sh

%changelog
* Tue Apr 07 2026 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build.
