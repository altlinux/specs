%def_with check

# mklove configure script can't process it
%define _configure_gettext %nil

# lto breaks crc32 detection in configure script
# See https://github.com/edenhill/librdkafka/issues/2426
%ifnarch x86_64
%define optflags_lto %nil
%endif

Name: librdkafka
Version: 2.0.2
Release: alt1

Summary: the Apache Kafka C/C++ client library

License: BSD-2-Clause
Group: Development/C++
Url: https://github.com/edenhill/librdkafka

Packager: Pavel Vainerman <pv@altlinux.ru>

# Source-url: https://github.com/edenhill/librdkafka/archive/v%{version}.tar.gz
Source: %name-%version.tar
Source1: rdkafka.pc

BuildRequires: cmake gcc-c++ libssl-devel liblz4-devel libxxhash-devel libsasl2-devel

%if_with check
BuildRequires: ctest
%endif

%description
librdkafka is a C library implementation of the Apache Kafka protocol, containing
both Producer and Consumer support. It was designed with message delivery
reliability and high performance in mind, current figures exceed 1 million
msgs/second for the producer and 3 million msgs/second for the consumer.

%package devel
Group: Development/C++
Summary: the Apache Kafka C/C++ client library
Requires: %name = %version-%release

%description devel
librdkafka is a C library implementation of the Apache Kafka protocol, containing
both Producer and Consumer support. It was designed with message delivery
reliability and high performance in mind, current figures exceed 1 million
msgs/second for the producer and 3 million msgs/second for the consumer.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_libdir/pkgconfig
cp %SOURCE1 %buildroot%_libdir/pkgconfig/
%__subst 's|@VERSION@|%{version}|g' %buildroot%_libdir/pkgconfig/*.pc

rm -f %buildroot%_libdir/*.a
rm -f %buildroot%_datadir/licenses/librdkafka/LICENSES.txt

%check
%make_build check

%files
%doc LICENSE README.md
%_docdir/%name
%_libdir/*.so.*

%files devel
%_libdir/*.so
%dir %_includedir/%name
%_includedir/%name/*.h
%_libdir/pkgconfig/*.pc

%changelog
* Sun Feb 12 2023 Grigory Ustinov <grenka@altlinux.org> 2.0.2-alt1
- Automatically updated to 2.0.2.

* Thu Aug 18 2022 Grigory Ustinov <grenka@altlinux.org> 1.9.2-alt1
- Automatically updated to 1.9.2.
- Build with check.

* Fri Jul 15 2022 Grigory Ustinov <grenka@altlinux.org> 1.9.1-alt1
- Automatically updated to 1.9.1.

* Mon Jun 27 2022 Grigory Ustinov <grenka@altlinux.org> 1.9.0-alt1
- Build new version for python3-module-confluent-kafka from git.

* Thu May 26 2022 Grigory Ustinov <grenka@altlinux.org> 1.6.2-alt1
- Build new version for python3-module-confluent-kafka.

* Sun Jan 24 2021 Pavel Vainerman <pv@altlinux.ru> 1.5.3-alt1
- new version (1.5.3) with rpmgs script

* Sat Jun 20 2020 Grigory Ustinov <grenka@altlinux.org> 1.4.4-alt1
- Build new version for python3-module-confluent-kafka.

* Wed Mar 27 2019 Pavel Vainerman <pv@altlinux.ru> 0.11.6-alt2
- added patch for use system libxxhash (altbug #36399)

* Tue Mar 26 2019 Pavel Vainerman <pv@altlinux.ru> 0.11.6-alt1
- added patch for use external(system) lz4 (closed altbug #36399)

* Fri Nov 09 2018 Pavel Vainerman <pv@altlinux.ru> 0.11.6-alt0.3
- minor fixes in spec

* Fri Nov 09 2018 Pavel Vainerman <pv@altlinux.ru> 0.11.6-alt0.2
- added pc-file

* Fri Nov 09 2018 Pavel Vainerman <pv@altlinux.ru> 0.11.6-alt0.1
- new version (0.11.6) with rpmgs script

