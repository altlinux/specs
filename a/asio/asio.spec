# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ perl(Date/Format.pm)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

%global commit 28d9b8d6df708024af5227c551673fdb2519f5bf
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           asio
Version:        1.10.8
Release:        alt1_6
Summary:        A cross-platform C++ library for network programming

Group:          Development/C++
License:        Boost Software License
URL:            https://think-async.com
Source0:        https://github.com/chriskohlhoff/%{name}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libssl-devel
BuildRequires:  boost-devel boost-devel-headers boost-python-headers
Source44: import.info

%description
The asio package contains a cross-platform C++ library for network programming
that provides developers with a consistent asynchronous I/O model using a
modern C++ approach.

%package devel
Summary:        Header files for asio
Group:          Development/Other

%description devel
Header files you can use to develop applications with asio.

The asio package contains a cross-platform C++ library for network programming
that provides developers with a consistent asynchronous I/O model using a
modern C++ approach.

%prep
%setup -q -n %{name}-%{commit}/%{name}

%build
./autogen.sh
%configure
%make_build

%install
make install DESTDIR=%{buildroot}

%files devel
%doc src/doc/*
%doc LICENSE_1_0.txt
%dir %{_includedir}/asio
%{_includedir}/asio/*
%{_includedir}/asio.hpp

%changelog
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

