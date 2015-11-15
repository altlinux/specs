Name: autobahn-cpp
Version: 0.1.0
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
BuildRequires: libmsgpack-devel >= 1.1.0

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
* Sun Nov 15 2015 Vitaly Lipatov <lav@altlinux.ru> 0.1.0-alt1
- initial build for ALT Linux Sisyphus
