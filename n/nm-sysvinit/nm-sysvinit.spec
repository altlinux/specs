Name: nm-sysvinit
Version: 0.2
Release: alt1

Summary: Create the _nmconnect system group and add the user with UID=500 to the _nmconnect group
License: public domain
Group: System/Configuration/Hardware

Url: http://altlinux.org/sysvinit
Source: nm-group
BuildArch: noarch

Requires: polkit-sysvinit

%description
%summary
on SysVinit-based systems.

%install
mkdir -p %buildroot%_initdir
install -pm755 %SOURCE0 %buildroot%_initdir

%files
%_initdir/nm-group

%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig nm-group on
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/chkconfig nm-group off
fi

%changelog
* Tue Jun 06 2017 Anton Midyukov <antohami@altlinux.org> 0.2-alt1
- Initial build for ALT Linux Sisyphus (Thanks Yury Pakin and Daniil Golovanov).
