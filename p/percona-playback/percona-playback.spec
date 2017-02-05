# TODO: enable/fix checks
%def_disable check

Name: percona-playback
Version: 0.6
Release: alt2
Summary: A tool for replaying captured database server load

License: GPL2
Url: http://www.percona.com/
Source: percona-playback-%version.tar.gz
Patch0: percona-playback-0.6-ac_prog_mkdir.patch
Group: Databases
Packager: Evgenii Terechkov <evg@altlinux.org>

BuildRequires: libdrizzle-devel gettext-tools libpcap-devel
BuildRequires: libtbb-devel libmysqlclient-devel intltool
BuildRequires: boost-program_options-devel pkg-config python-modules
BuildRequires: gcc5-c++

%description
Percona Playback is a tool for replaying the captured load of one database
server against another in the most realistic way possible. Captured load can
come in the form of MySQL slow query logs or tcpdump capture.
It's multithreaded, modular and configurable to allow for flexibility and
future extension.

See http://www.percona.com/doc/percona-playback/ for on-line documentation.

%package devel
Summary: Development files for %name
Group: Databases
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
aclocal
autoheader
autoconf
libtoolize --copy --force
automake -afc
%configure --disable-static
%make_build

%install
%makeinstall_std
find %buildroot -name '*.la' -exec rm -f {} ';'

%check
make check

%files
%_bindir/%name
%_libdir/*.so.*
%doc AUTHORS README

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Mon Feb  6 2017 Terechkov Evgenii <evg@altlinux.org> 0.6-alt2
- Fix build by hardcoding gcc5-c++ compiler

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6-alt1.1.qa1
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.6-alt1.1
- rebuild with boost 1.57.0

* Tue Oct 29 2013 Terechkov Evgenii <evg@altlinux.org> 0.6-alt1
- Initial build for ALT Linux Sisyphus
