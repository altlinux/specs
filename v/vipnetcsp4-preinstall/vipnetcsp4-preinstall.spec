Name: vipnetcsp4-preinstall
Version: 0.1.0
Release: alt1

Summary: Requires set for install VipNet CSP 4.x
License: GPLv3+
Group: System/Configuration/Other

Url: https://www.altlinux.org/ViPNet_CSP
Source: %name-%version.tar
Packager: Anna Khrustova <khab@altlinux.org>

ExclusiveArch: %ix86 x86_64

Requires: libqt4
Requires: pcsc-lite-rutokens
Requires: fsprot-control

%description
vipnetcsp4-preinstall setup required packages and set compatibility layer
between VipNet CSP for Linux and ALT desktop distribution.It is needed for
setup VipNet CSP 4.x.

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
* Fri Apr 09 2021 Anna Khrustova <khab@altlinux.org> 0.1.0-alt1
- Initial build.

