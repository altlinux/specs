Name: autobahn-cpp
Version: 17.5.1
Release: alt1

Summary: WAMP for C++ 11 on Boost/Asio

License: ASL 2.0
Group: Development/C++
Url: https://github.com/crossbario/autobahn-cpp

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/crossbario/autobahn-cpp.git
Source: %name-%version.tar

BuildRequires: gcc-c++ >= 4.8
BuildRequires: boost-asio-devel >= 1.56
BuildRequires: boost-program_options-devel
# builds only with 1.4.2
BuildRequires: libmsgpack1-devel = 1.4.2
BuildRequires: websocketpp-devel >= 0.7.0
BuildRequires: libssl-devel

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake

%description
Autobahn|Cpp is a subproject of Autobahn which implements
the Web Application Messaging Protocol (WAMP) in C++
supporting the following application roles
* Caller
* Callee
* Publisher
* Subscriber

The API and implementation make use of modern C++ 11
and new asynchronous idioms using (upcoming) features
of the standard C++ library, in particular Futures,
Continuations and Lambdas.

%package devel
Summary: Development files
Group: Development/C++
#Requires: %name = %version-%release

%description devel
Autobahn|Cpp is a subproject of Autobahn which implements
the Web Application Messaging Protocol (WAMP) in C++
supporting the following application roles
* Caller
* Callee
* Publisher
* Subscriber

The API and implementation make use of modern C++ 11
and new asynchronous idioms using (upcoming) features
of the standard C++ library, in particular Futures,
Continuations and Lambdas.


%prep
%setup

%build
%cmake_insource

%install
%makeinstall_std

%files devel
%_includedir/autobahn/

%changelog
* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 17.5.1-alt1
- new version 17.5.1 (with rpmrb script)

* Thu Aug 11 2016 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- new version

* Sun Nov 15 2015 Vitaly Lipatov <lav@altlinux.ru> 0.1.0-alt1
- initial build for ALT Linux Sisyphus
