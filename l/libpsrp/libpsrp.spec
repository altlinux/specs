# nuget psrp module
Name: 	  libpsrp
Version:  1.1.0
Release:  alt1

Summary:  PowerShell WS-Man PSRP Client for Linux
License:  MIT
Group:    Other
Url:      https://github.com/PowerShell/psl-omi-provider

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/PowerShell/psl-omi-provider.git
Source:   %name-%version.tar

BuildRequires: cmake rpm-macros-cmake gcc-c++
BuildRequires: libssl-devel libpam0-devel libomi-devel libomi-internal-devel

%description
PSRP communication is tunneled through the Open Management Infrastructure (OMI) using this OMI provider.

%prep
%setup

%build
cp .gear/CMakeLists.txt src/
cd src
%cmake_insource -DULINUX_SSL=0
%make_build
#cd pal/build/; ./configure --enable-system-build
#cd installbuilder/; make

%install
cd src
mkdir -p %buildroot%_libdir/
cp libpsrpclient.so %buildroot%_libdir/

%files
%_libdir/libpsrpclient.so

%changelog
* Fri Jun 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Sisyphus
