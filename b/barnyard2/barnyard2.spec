Name: barnyard2
Version: 1.11
Release: alt2

Summary: Snort Log Backend
License: GPLv2
Group: Networking/Other

Url: https://github.com/firnsy/barnyard2

Source0: %name-%version.tar
Source1: barnyard2

Patch1: barnyard2-1.11-alt-confpath.patch

BuildRequires: libpcap-devel

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
BuildRequires: mysql-devel
%description mysql
barnyard2 binary compiled with mysql support.

%prep
%setup

%patch1 -p1

%build
autoreconf --install
%configure 					\
	--with-mysql				\
	--with-mysql-libraries=/usr/%_lib
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
%config(noreplace) %_initdir/barnyard2
%config(noreplace) %_sysconfdir/%name/barnyard2.conf
%config(noreplace) %_sysconfdir/sysconfig/barnyard2
%attr(1770,root,root) %dir %_logdir/%name
%doc LICENSE doc/INSTALL doc/README.*

%files mysql
%_datadir/%name/schemas/create_mysql

%changelog
* Fri Jan 25 2013 Timur Aitov <timonbl4@altlinux.org> 1.11-alt2
- barnyard2-mysql - noarch now

* Thu Jan 24 2013 Timur Aitov <timonbl4@altlinux.org> 1.11-alt1
- [1.11]

