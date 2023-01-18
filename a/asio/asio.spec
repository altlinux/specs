# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ perl(Date/Format.pm)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var

%global commit 28d9b8d6df708024af5227c551673fdb2519f5bf
%global shortcommit %(c=%commit; echo ${c:0:7})

Name: asio
Version: 1.26.0
Release: alt2

Summary: A cross-platform C++ library for network programming
License: Boost Software License
Group: Development/C++

Url: https://think-async.com
Source: %name-%version.tar.bz2
Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libssl-devel gcc gcc-c++
BuildRequires: boost-devel boost-devel-headers boost-python-headers
%ifnarch %e2k
BuildRequires: boost-coroutine-devel
%endif
Source44: import.info

%description
The asio package contains a cross-platform C++ library for network programming
that provides developers with a consistent asynchronous I/O model using a
modern C++ approach.

%package devel
Summary: Header files for asio
Group: Development/Other

%description devel
Header files you can use to develop applications with asio.

The asio package contains a cross-platform C++ library for network programming
that provides developers with a consistent asynchronous I/O model using a
modern C++ approach.

%prep
%setup

%ifarch %e2k
%add_optflags -Wno-unused-variable
# lcc 1.25's EDG frontend can't handle such C++ code
echo "int main() {}" > src/examples/cpp14/executors/pipeline.cpp
%endif

%build
#./autogen.sh
%configure
%make_build

%install
%makeinstall_std

%files devel
%doc doc/*
%doc LICENSE*
%dir %_includedir/asio
%_includedir/asio/*
%_includedir/asio.hpp
%_libdir/pkgconfig/asio.pc

%changelog
* Wed Jan 18 2023 Ilya Mashkin <oddity@altlinux.ru> 1.26.0-alt2
- Fixed build for Elbrus

* Mon Jan 16 2023 Ilya Mashkin <oddity@altlinux.ru> 1.26.0-alt1
- 1.26.0

* Sun Aug 14 2022 Ilya Mashkin <oddity@altlinux.ru> 1.24.0-alt1
- 1.24.0

* Sat Aug 06 2022 Ilya Mashkin <oddity@altlinux.ru> 1.23.0-alt1
- 1.23.0

* Thu Jan 20 2022 Michael Shigorin <mike@altlinux.org> 1.21.0-alt2
- E2K: ftbfs workaround (ilyakurdyukov@)

* Sun Nov 07 2021 Ilya Mashkin <oddity@altlinux.ru> 1.21.0-alt1
- 1.21.0

* Wed Oct 20 2021 Ilya Mashkin <oddity@altlinux.ru> 1.20.0-alt1
- 1.20.0

* Fri Jun 04 2021 Ilya Mashkin <oddity@altlinux.ru> 1.18.2-alt1
- 1.18.2

* Sat May 15 2021 Ilya Mashkin <oddity@altlinux.ru> 1.18.1-alt1
- 1.18.1

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.10.8-alt1_6
- NMU: update to new version by fcimport
- requiest by oddity@

* Tue Mar 04 2014 Ilya Mashkin <oddity@altlinux.ru> 1.10.1-alt1
- 1.10.1

* Sun Jan 09 2011 Ilya Mashkin <oddity@altlinux.ru> 1.4.7-alt1
- 1.4.7

* Tue Jun 01 2010 Ilya Mashkin <oddity@altlinux.ru> 1.4.5-alt1
- 1.4.5

* Tue Aug 11 2009 Ilya Mashkin <oddity@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Thu Jan 08 2009 Ilya Mashkin <oddity@altlinux.ru> 1.2.0-alt1
- New stable version 1.2.0

* Sun Apr 20 2008 Igor Zubkov <icesik@altlinux.org> 1.0.0-alt1
- 0.3.9 -> 1.0.0

* Thu Apr 03 2008 Igor Zubkov <icesik@altlinux.org> 0.3.9-alt1
- 0.3.7 -> 0.3.9
- buildreq

* Sat May 12 2007 Igor Zubkov <icesik@altlinux.org> 0.3.7-alt1
- build for Sisyphus

