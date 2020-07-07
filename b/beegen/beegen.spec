Name: beegen
Version: 0.2
Release: alt1

Summary: Automatic hasher bee generator
License: GPLv2+
Group: System/Base
BuildArch: noarch

Source: %name-%version.tar

%description
This is an automatic hasher bee generator.  It generates both personal
accounts for ssh keys found in /etc/openssh/authorized_keys/ and
multiple bee accounts for ssh key templates found in the same directory.

%prep
%setup

%install
install -pDm755 mkbee %buildroot%_sbindir/mkbee
install -pDm755 %name %buildroot%_sbindir/%name
install -pDm755 %name.init %buildroot%_initdir/%name

%post
if [ $1 -eq 1 ]; then
        /sbin/chkconfig --add %name
fi

%preun
if [ $1 -eq 0 ]; then
	/sbin/chkconfig --del %name
fi

%files
%_sbindir/mkbee
%_sbindir/%name
%_initdir/%name

%changelog
* Mon Jul 06 2020 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Added mkbee.

* Mon Jun 04 2012 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
