Name: sysdig
Version: 0.1.89
Release: alt1

Summary: A system exploration and troubleshooting tool

Group: File tools
License: GPLv2
Url: https://github.com/draios/sysdig

# Source-url: https://github.com/draios/sysdig/archive/%version.tar.gz
Source: %name-%version.tar

# manually removed: python3 ruby ruby-stdlibs 
# Automatically added by buildreq on Mon Sep 29 2014
# optimized out: cmake cmake-modules libcloog-isl4 libstdc++-devel python3-base
BuildRequires: ccmake gcc-c++ jsoncpp-devel libdb4-devel libluajit-devel zlib-devel

%description
An open source system-level exploration and troubleshooting tool.

%prep
%setup
%__subst "s|add_subdirectory(driver)||g" CMakeLists.txt

%build
%cmake -DUSE_BUNDLED_LUAJIT:BOOL=off \
       -DUSE_BUNDLED_JSONCPP:BOOL=off \
       -DUSE_BUNDLED_ZLIB:BOOL=off
%cmake_build

%install
%cmakeinstall_std


%files
%_bindir/%name
%_man8dir/*
%_datadir/%name/

%changelog
* Sun Sep 28 2014 Vitaly Lipatov <lav@altlinux.ru> 0.1.89-alt1
- initial build for ALT Linux Sisyphus
