Name: umask-control
Version: 0.2
Release: alt1

Summary: Facilities control for umask
License: GPL
Group: System/Servers
BuildArch: noarch
Url: http://git.etersoft.ru/people/kipruss/packages/umask-control.git
Packager: Konstantin Baev <kipruss@altlinux.org>

PreReq: control

Source0: %name-%version.tar

%description
This package contains control rules for umask.

%prep
%setup

%install
mkdir -p %buildroot%_sysconfdir/{profile.d,sysconfig}
mkdir -p %buildroot%_controldir
install -pD -m644 umask.conf %buildroot%_sysconfdir/sysconfig
install -pD -m755 umask.sh %buildroot%_sysconfdir/profile.d
install -pD -m755 umask.csh %buildroot%_sysconfdir/profile.d
install -pD -m755 umask.control %buildroot%_controldir/umask

%files
%config %_controldir/umask
%_sysconfdir/profile.d/umask.*
%config(noreplace) %_sysconfdir/sysconfig/umask.conf

%changelog
* Tue May 19 2009 Konstantin Baev <kipruss@altlinux.org> 0.2-alt1
- Move umask.conf from /etc to /etc/sysconfig

* Sat Apr 04 2009 Konstantin Baev <kipruss@altlinux.org> 0.1-alt3
- Minor bugfix in specfile

* Sat Apr 04 2009 Konstantin Baev <kipruss@altlinux.org> 0.1-alt2
- Add csh-script

* Fri Apr 03 2009 Konstantin Baev <kipruss@altlinux.org> 0.1-alt1
- Initial release.
