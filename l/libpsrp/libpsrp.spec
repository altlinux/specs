%define post -28
# nuget psrp module
Name: 	  libpsrp
Version:  1.4.1
Release:  alt1

Summary:  PowerShell WS-Man PSRP Client for Linux
License:  MIT
Group:    Other
Url:      https://github.com/PowerShell/psl-omi-provider

Packager: Vitaly Lipatov <lav@altlinux.ru>

# NSource-git: https://github.com/PowerShell/psl-omi-provider.git
# Source-url: https://github.com/PowerShell/psl-omi-provider/archive/v%version%post.tar.gz
Source:  %name-%version.tar
Source1: .gear/CMakeLists.txt

BuildRequires: cmake rpm-macros-cmake gcc-c++
BuildRequires: libssl-devel libpam0-devel libomi-devel libomi-internal-devel

%description
PSRP communication is tunneled through the Open Management Infrastructure (OMI) using this OMI provider.

%prep
%setup

%build
cp %SOURCE1 src/
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
* Wed Dec 20 2017 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- new version 1.4.1 (with rpmrb script)

* Fri Jun 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Sisyphus
