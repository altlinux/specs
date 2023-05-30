Name: cpp-jwt
Version: 1.4
Release: alt1

Summary: A C++14 library for JSON Web Tokens(JWT)
License: MIT
Group: Development/C++

Url: https://github.com/arun11299/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/arun11299/%name/archive/refs/tags/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgtest-devel
BuildRequires: libssl-devel

%description
For the uninitiated, JSON Web Token(JWT) is a JSON based standard (RFC-7519) for creating assertions or access tokens that consists of some claims (encoded within the assertion). This assertion can be used in some kind of bearer authentication mechanism that the server will provide to clients, and the clients can make use of the provided assertion for accessing resources.

%package -n lib%name-devel
Summary: A C++14 library for JSON Web Tokens(JWT)
Group: Development/C++

%description -n lib%name-devel
For the uninitiated, JSON Web Token(JWT) is a JSON based standard (RFC-7519) for creating assertions or access tokens that consists of some claims (encoded within the assertion). This assertion can be used in some kind of bearer authentication mechanism that the server will provide to clients, and the clients can make use of the provided assertion for accessing resources.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n lib%name-devel
%doc LICENSE README.md
%_includedir/jwt
%_libdir/cmake/%name

%changelog
* Tue May 30 2023 Nazarov Denis <nenderus@altlinux.org> 1.4-alt1
- Initial build for ALT Linux
