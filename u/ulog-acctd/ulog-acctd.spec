Name: ulog-acctd
Summary: ulog-acctd - A userspace network accounting daemon
Version: 0.4.3
Release: alt6.qa1
License: GPL
Group: System/Servers
Url: http://alioth.debian.org/projects/pkg-ulog-acctd
Packager: Eugene Prokopiev <enp@altlinux.ru>

Source0: %name-%version.tar
Source1: %name-%version-statup.tar
Source2: %name-%version-contrib-billing-example.tar
Patch0:  %name-%version-logfile-permissions.patch

%description
ulog-acctd is a userspace network accounting daemon which
generates log files of network traffic for accounting purposes.

%prep
%setup
%patch0 -p1

%build
pushd src
%make_build
popd
pushd doc
makeinfo --no-headers -o - ulog-acctd.texi > README
makeinfo --no-split ulog-acctd.texi
popd

%install
mkdir -p %buildroot/%_sysconfdir
mkdir -p %buildroot/%_sbindir
mkdir -p %buildroot/%_infodir
mkdir -p %buildroot/%_man8dir
mkdir -p %buildroot/%_logdir/%name
install doc/ulog-acctd.8 %buildroot/%_man8dir/ulog-acctd.8
install -m 644 doc/ulog-acctd.info %buildroot/%_infodir/ulog-acctd.info
install -m 755 src/ulog-acctd %buildroot/%_sbindir/ulog-acctd
install -m 644 src/ulog-acctd.conf %buildroot/%_sysconfdir/ulog-acctd.conf
tar -xf %SOURCE1
mkdir -p %buildroot/%_initdir
cp %name-%version-statup/%name.init %buildroot/%_initdir/%name
mkdir -p %buildroot/%_sysconfdir/logrotate.d/
cp %name-%version-statup/%name.logrotate %buildroot/%_sysconfdir/logrotate.d/%name
tar -xf %SOURCE2
cp -a %name-%version-contrib-billing-example contrib/billing-example

%post
%post_service ulog-acctd

%preun
%preun_service ulog-acctd

%files
%_sbindir/ulog-acctd
%config %_sysconfdir/ulog-acctd.conf
%_initdir/%name
%_sysconfdir/logrotate.d/%name
%_mandir/man8/*
%_infodir/*
%dir %_logdir/%name

%doc doc/README COPYING contrib

%changelog
* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.3-alt6.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for ulog-acctd
  * postclean-05-filetriggers for spec file

* Tue May 13 2008 Eugene Prokopiev <enp@altlinux.ru> 0.4.3-alt6
- add billing example

* Tue May 13 2008 Eugene Prokopiev <enp@altlinux.ru> 0.4.3-alt5
- add startup files

* Tue May 13 2008 Eugene Prokopiev <enp@altlinux.ru> 0.4.3-alt4
- add logfile-permissions.patch

* Tue May 13 2008 Eugene Prokopiev <enp@altlinux.ru> 0.4.3-alt3
- git repo refactoring

* Fri Nov 23 2007 Eugene Prokopiev <enp@altlinux.ru> 0.4.3-alt2
- move to git.alt
- update billing example

* Wed Sep 06 2006 Eugene Prokopiev <enp@altlinux.ru> 0.4.3-alt1
- First build for Sisyphus

* Tue Dec 20 2005 Eugene Prokopiev <enp@altlinux.ru> 0.4.3-alt0.M24.1
- First build for ALM 2.4 with billing example
  This work based on my previous build for ALM 2.2 with many changes
  Thanks to Pavel Usishev <usishev@yandex.ru>
