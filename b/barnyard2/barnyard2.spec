Name: barnyard2
Version: 2.1.13
Release: alt4

Summary: Snort Log Backend
License: GPLv2
Group: Networking/Other

Url: https://github.com/firnsy/barnyard2

Source0: %name-%version.tar
Source1: barnyard2.init

Patch1: barnyard2-1.11-alt-confpath.patch
Patch2: barnyard2-1.11-alt-default_output.patch
# in upstream, remove on next version
Patch3: barnyard2-1.13-alt-sguild-padding.patch

BuildRequires: libpcap-devel
BuildRequires: tcl-devel

%description
Barnyard2 has 3 modes of operation:
One-shot, continual, continual w/ checkpoint.  In one-shot mode,
barnyard will process the specified file and exit.  In continual mode,
barnyard will start with the specified file and continue to process
new data (and new spool files) as it appears.  Continual mode w/
checkpointing will also use a checkpoint file (or waldo file in the
snort world) to track where it is.  In the event the barnyard process
ends while a waldo file is in use, barnyard will resume processing at
the last entry as listed in the waldo file.

%package mysql
Summary: barnyard2 with MySQL support
Group: Networking/Other
BuildArch: noarch
Requires: %name = %version-%release
Requires: mysql
BuildRequires: mysql-devel libmysqlclient-devel libmysqlclient18 libmysqlclient16
%description mysql
barnyard2 binary compiled with mysql support.

%prep
%setup

%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%autoreconf
./autogen.sh
%configure 					\
	--with-mysql				\
	--with-mysql-libraries=%_libdir 	\
    --with-tcl=%_libdir \
	--with-mysql-includes=%_includedir/mysql
%make_build

%install
%makeinstall_std

mkdir -p %buildroot/{%_sysconfdir/%name,%_logdir/%name,%_datadir/%name,%_logdir/%name}
mv %buildroot%_sysconfdir/barnyard2.conf %buildroot%_sysconfdir/%name/barnyard2.conf
install -Dpm 644 rpm/barnyard2.config %buildroot%_sysconfdir/sysconfig/barnyard2
install -Dpm 744 %SOURCE1 %buildroot%_initdir/barnyard2

# mysql
install -Dpm 644 schemas/create_mysql %buildroot%_datadir/%name/schemas/create_mysql

%files
%_bindir/*
%config(noreplace) %dir %_sysconfdir/%name
%config(noreplace) %_initdir/barnyard2
%config(noreplace) %_sysconfdir/%name/barnyard2.conf
%config(noreplace) %_sysconfdir/sysconfig/barnyard2
%attr(1770,root,root) %dir %_logdir/%name
%doc LICENSE doc/INSTALL doc/README.*

%files mysql
%dir %_datadir/%name
%dir %_datadir/%name/schemas
%_datadir/%name/schemas/create_mysql

%changelog
* Fri Jan 23 2015 Andriy Stepanov <stanv@altlinux.ru> 2.1.13-alt4
- Upstream commit ce3c0228, fixed: incorrect padding in sguild for
events without packets

* Wed Sep 03 2014 Mikhail Efremov <sem@altlinux.org> 2.1.13-alt3
- init script: Simplify print_all_ifaces() function.
- init script: Create log directories if needed.
- Fix init scripts priorities.

* Wed Jun 04 2014 Timur Aitov <timonbl4@altlinux.org> 2.1.13-alt2
- remove 'fix-create-pidfile' patch
- mod init script

* Wed May 07 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 2.1.13-alt1
- New version

* Mon Feb 18 2013 Timur Aitov <timonbl4@altlinux.org> 1.11-alt3
- set output database by default
- fix barnayrd2 init script
- fix create pidfile

* Fri Jan 25 2013 Timur Aitov <timonbl4@altlinux.org> 1.11-alt2
- barnyard2-mysql - noarch now

* Thu Jan 24 2013 Timur Aitov <timonbl4@altlinux.org> 1.11-alt1
- [1.11]

