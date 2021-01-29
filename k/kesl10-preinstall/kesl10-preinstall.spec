Name: kesl10-preinstall
Version: 0.1.0
Release: alt1

Summary: Requires set for install  KESL 10
License: GPLv3
Group: System/X11

Url: http://www.altlinux.org/Kaspersky_Endpoint_Security
Source: %name-%version.tar
Packager: Anna Khrustova <khab@altlinux.org>

ExclusiveArch: %ix86 x86_64

Requires: libxcbutil-keysyms
Requires: libxcb-render-util
Requires: libxcbutil-icccm
Requires: libxcbutil-image

%description
Pre-install required packages and set compatibility layer between
Kaspersky Endpoint Security 10 for Linux and ALT 8SP Workstation.
This is needded for setup KESL 10 GUI and work with the antivirus
as regular user.

%post
if  grep -sE '^[^#]' /etc/fstab |
	grep -E '\s/home\s' |
   	grep -qw noexec
then
	if [ -f /_NEW_SYSTEM_ ]; then
		echo "Don't forget remove 'noexec' from" >&2
		echo "/home mount options in /etc/fstab!" >&2
        else
	     from="$(grep -sE '^[^#]' /etc/fstab |grep -E '\s/home\s' |tail -n1)"
	     to="$(echo "$from" |sed -E 's/(\,noexec|noexec\,?)//')"
	     [ "$from" = "$to" ] || sed -i "s|$from|$to|" /etc/fstab
	fi
fi

%files

%changelog
* Thu Jan 28 2021 Anna Khrustova <khab@altlinux.org> 0.1.0-alt1
- Initial build.

