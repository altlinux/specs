Name: sysdig
Version: 0.1.101
Release: alt1

Summary: A system exploration and troubleshooting tool

Group: File tools
License: GPLv2
Url: https://github.com/draios/sysdig

# Source-url: https://github.com/draios/sysdig/archive/%version.tar.gz
Source: %name-%version.tar

# manually removed: python3 ruby ruby-stdlibs 
# Automatically added by buildreq on Sat Jul 18 2015
# optimized out: cmake cmake-modules libstdc++-devel libtinfo-devel python3-base zlib-devel
BuildRequires: ccmake gcc-c++ jsoncpp-devel libdb4-devel libluajit-devel libncurses-devel zlib-devel

%description
An open source system-level exploration and troubleshooting tool.

%prep
%setup
%__subst "s|add_subdirectory(driver)||g" CMakeLists.txt

%build
%cmake -DUSE_BUNDLED_LUAJIT:BOOL=off \
       -DUSE_BUNDLED_JSONCPP:BOOL=off \
       -DUSE_BUNDLED_ZLIB:BOOL=off \
       -DUSE_BUNDLED_NCURSES:BOOL=off
%cmake_build

%install
%cmakeinstall_std
rm -rf %buildroot/%_datadir/zsh/
rm -rf %buildroot/usr/etc/

%files
%_bindir/%name
%_bindir/c%name
%_bindir/sysdig-probe-loader
%_man8dir/*
%_datadir/%name/

%changelog
* Fri Jul 17 2015 Vitaly Lipatov <lav@altlinux.ru> 0.1.101-alt1
- new version 0.1.101 (with rpmrb script)

* Thu Jun 04 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1.89-alt2
- rebuild with c++11 ABI

* Sun Sep 28 2014 Vitaly Lipatov <lav@altlinux.ru> 0.1.89-alt1
- initial build for ALT Linux Sisyphus
