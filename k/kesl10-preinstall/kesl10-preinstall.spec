Name: kesl10-preinstall
Version: 0.1.1
Release: alt1

Summary: Requires set for install  KESL 10
License: GPLv3+
Group: System/X11

Url: http://www.altlinux.org/Kaspersky_Endpoint_Security
Source: %name-%version.tar
Packager: Anna Khrustova <khab@altlinux.org>

ExclusiveArch: %ix86 x86_64

Requires: libxcbutil-keysyms
Requires: libxcb-render-util
Requires: libxcbutil-icccm
Requires: libxcbutil-image
Requires: fsprot-control

%description
kesl10-preinstall setup required packages and set compatibility layer between
Kaspersky Endpoint Security 10 for Linux and ALT 8SP Workstation.
It is required for installation KESL 10 GUI and works with
antivirus as a regular user.

%post
if mountpoint -q /home; then
    if [ ! -f /_NEW_SYSTEM_ ]; then
	control homedir exec
    else
	echo "Don't forget to remove 'noexec' from" >&2
	echo "/home mount options in /etc/fstab!" >&2
	echo "Use command: control homedir exec" >&2
    fi
fi

%files

%changelog
* Thu Apr 08 2021 Anna Khrustova <khab@altlinux.org> 0.1.1-alt1
- Rebuilt with fsprot-control.

* Thu Jan 28 2021 Anna Khrustova <khab@altlinux.org> 0.1.0-alt1
- Initial build.

