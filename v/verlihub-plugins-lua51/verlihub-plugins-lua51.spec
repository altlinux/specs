# TODO: move lua plugins to special dir
# Pay attention:
# Please install the Lua socket extension library (luasocket)
# before trying to compile lua plugin. You can download it from the Lua
# website http://www.cs.princeton.edu/~diego/professional/luasocket/

%define oname lua
Name: verlihub-plugins-lua51
Version: 1.8.1
Release: alt1

Summary: Lua 5.1 plugin for verlihub

Url: http://www.verlihub-project.org
License: GPL
Group: Development/C

# Uwaga! there is three versions of lua 1.6 on the site
# use cvs -d :pserver:anonymous@verlihub.cvs.sourceforge.net:/cvsroot/verlihub co lua
Source: http://downloads.sourceforge.net/verlihub/%{oname}_%version.tar.bz2
Packager: Vitaly Lipatov <lav@altlinux.ru>

Requires: verlihub

# Automatically added by buildreq on Wed Jun 25 2008
BuildRequires: gcc-c++ libGeoIP-devel libMySQL-devel liblua5-devel libpcre-devel libverlihub-devel zlib-devel

%description
Lua 5.1 plugin for verlihub

%prep
%setup -n %oname

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_datadir/verlihub/*
%_libdir/*.so*

%changelog
* Thu Aug 20 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.8.1-alt1
- 1.8.1

* Tue Jul 14 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.7-alt1.rc1
- 1.7 rc1

* Wed Jul 09 2008 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt1cvs20080709
- build from CVS 20080709

* Wed Jun 25 2008 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt1
- initial build for ALT Linux Sisyphus (fix bug #16144)
- build with out luasocket
