#
# author: Enrique Martinez <enmaca@hotmail.com>
# license: GPL-3+
#
Name: clsync
Version: 0.4.2
Release: alt2

Summary: Live sync tool based on inotify
License: GPLv3+
Group: File tools

Url: https://github.com/xaionaro/clsync
Source0: %name-%version.tar
Source1: %name.init

# Automatically added by buildreq on Sat Oct 01 2016
# optimized out: glib2-devel perl pkg-config python-base python-modules
BuildRequires: libgio-devel

%description
live sync tool based on inotify, written in GNU C
Clsync recursively watches for source directory and executes external
program to sync the changes. Clsync is adapted to use together with rsync.
This utility is much more lightweight than competitors and supports such
features as separate queue for big files, regex file filter,
multi-threading.

%package devel
Summary: Development Files for clsync
Group: Development/C
Requires: clsync = %version-%release

%description devel
live sync tool based on inotify, written in GNU C
Clsync recursively watches for source directory and executes external
program to sync the changes. Clsync is adapted to use together with rsync.
This utility is much more lightweight than competitors and supports such
features as separate queue for big files, regex file filter,
multi-threading.

%prep
%setup

%build
%autoreconf
%configure
%make

%install
%makeinstall_std
install -pDm755 %SOURCE1 %buildroot%_initdir/%name
mkdir -p %buildroot%_sysconfdir/%name/rules
mkdir -p %buildroot%_localstatedir/%name/from
mkdir -p %buildroot%_localstatedir/%name/to

cat > %buildroot%_sysconfdir/%name/clsync.conf <<EOF
# This configuration is a simple test
[default]
watch-dir = %_localstatedir/%name/from
rules-file = %_sysconfdir/%name/rules/default
destination-dir = %_localstatedir/%name/to
mode = rsyncdirect
sync-handler = %_bindir/rsync
background = 1
syslog = 1
full-initialsync = 1
retries = 3
EOF

cat > %buildroot%_sysconfdir/%name/rules/default <<EOF
-d^[Dd]ont[Ss]ync\$
+*.*
EOF

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/*
%doc %_docdir/*
%_man1dir/%name.1*
%dir %_localstatedir/%name/from
%dir %_localstatedir/%name/to
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/rules
%config(noreplace) %_sysconfdir/%name/clsync.conf
%config %_sysconfdir/%name/rules/default
%_initdir/%name

%files devel
%_includedir/%name/

%changelog
* Sat Oct 01 2016 Michael Shigorin <mike@altlinux.org> 0.4.2-alt2
- improved initscript to actually stop the service
- added post/preun service scriptlets

* Sat Oct 01 2016 Michael Shigorin <mike@altlinux.org> 0.4.2-alt1
- built for sisyphus @ #ossdevconf

* Thu Sep 29 2016 Andrew A. Savchenko <bircoph@gmail.com> - 0.4.2-1
- Maintenance release, many bug fixes

* Thu Nov 6 2014 Dmitry Yu Okunev <dyokunev@ut.mephi.ru> - 0.4-1
- A lot of fixes

* Thu Jan 9 2014 Dmitry Yu Okunev <dyokunev@ut.mephi.ru> - 0.3-1
- Added support of control socket

* Thu Oct 24 2013 Barak A. Pearlmutter <bap@debian.org> - 0.2.1-1
- New upstream version

* Fri Oct 11 2013 Barak A. Pearlmutter <bap@debian.org> - 0.1-2
- Tweak debian/watch to ignore debian releases

* Sat Sep 07 2013 Barak A. Pearlmutter <bap@debian.org> - 0.1-1
- Initial release (Closes: #718769 )
