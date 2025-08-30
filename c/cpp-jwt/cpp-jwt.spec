Name: cpp-jwt
Version: 1.5.1
Release: alt1

Summary: A C++14 library for JSON Web Tokens(JWT)
License: MIT
Group: Development/C++

Url: https://github.com/arun11299/%name
Vcs: https://github.com/arun11299/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/arun11299/%name/archive/refs/tags/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: libgtest-devel
BuildRequires: libssl-devel
BuildRequires: nlohmann-json-devel

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
%cmake -DCPP_JWT_USE_VENDORED_NLOHMANN_JSON:BOOL=OFF
%cmake_build

%install
%cmake_install
%__mkdir_p %buildroot%_cmakedir
%__mv %buildroot%_datadir/cmake/%name %buildroot%_cmakedir/%name

%check
%ctest

%files -n lib%name-devel
%doc LICENSE README.md
%_includedir/jwt
%_cmakedir/%name

%changelog
* Sat Aug 30 2025 Nazarov Denis <nenderus@altlinux.org> 1.5.1-alt1
- New version 1.5.1.

* Tue May 27 2025 Nazarov Denis <nenderus@altlinux.org> 1.5-alt1
- New version 1.5.

* Tue May 30 2023 Nazarov Denis <nenderus@altlinux.org> 1.4-alt1
- Initial build for ALT Linux
