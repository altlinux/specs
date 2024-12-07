%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: bwm-ng
Version: 0.6.3.0.14.5782
Release: alt1

Summary: Bandwidth Monitor NG is a small and simple console-based live bandwidth monitor.
License: GPLv2+
Group: Monitoring
Url: http://www.gropp.org/
Vcs: https://github.com/vgropp/bwm-ng.git

Source0: %name-%version.tar

BuildRequires: libncurses-devel libtinfo-devel pkg-config
BuildRequires: libstatgrab-devel net-tools

%description
Bandwidth Monitor NG is a small and simple console-based live network and disk
io bandwidth monitor for Linux, BSD, Solaris, Mac OS X and others.

Short list of features:
- supports /proc/net/dev, netstat, getifaddr, sysctl, kstat, /proc/diskstats
  /proc/partitions, IOKit, devstat and libstatgrab
- unlimited number of interfaces/devices supported
- interfaces/devices are added or removed dynamically from list
- white-/blacklist of interfaces/devices
- output of KB/s, Kb/s, packets, errors, average, max and total sum
- output in curses, plain console, CSV or HTML
- configfile

%prep
%setup
%autoreconf

%build
%configure --prefix=%buildroot --enable-64bit \
			--enable-netstatbyte \
			--enable-netstatlink \
			--with-ncurses \
			--with-time	\
			--with-getopt_long \
			--with-getifaddrs \
			--with-procnetdev \
			--with-partitions \
			--with-libstatgrab \
			--with-netstatlinuxnew \
			--without-strip
%make_build

%install
%makeinstall_std
install -D -m644 .gear/bwm-ng.conf %buildroot%_sysconfdir/bwm-ng.conf

%files
%_bindir/bwm-ng
%_man1dir/*
%config(noreplace) %_sysconfdir/bwm-ng.conf
%doc AUTHORS ChangeLog NEWS README THANKS bwm-ng.conf-example bwm-ng.css

%changelog
* Sat Dec 07 2024 Andrew Savchenko <bircoph@altlinux.org> 0.6.3.0.14.5782-alt1
- Version bump
- Add new input methods

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Sep 30 2007 Ilya Mashkin <oddity at altlinux.ru> 0.6-alt1
- new version 0.6

* Sat Mar 18 2006 Dmitry Marochko <mothlike@altlinux.ru> 0.5-alt1.1
- as-needed fix

* Mon Mar 13 2006 Dmitry Marochko <mothlike@altlinux.ru> 0.5-alt1
- Initial build for Sisyphus
