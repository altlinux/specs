%define src_ver 111-2
%define pkg_ver %(echo %src_ver | sed -e 's,-,.,g')
%define simutrans_ver 0.%pkg_ver

Summary: A complete Simutrans game data package with 64x64 tiles
Summary(ru_RU.UTF-8): Полный пакет данных для игры Simutrans с ячейками 64x64 точки
Name: simutrans-pak64
Version: %pkg_ver
Release: alt1
License: Distributable
Group: Games/Strategy
URL: http://www.simutrans.com
BuildArch: noarch

# https://downloads.sourceforge.net/project/simutrans/pak64/%src_ver/simupak64-%src_ver.zip
Source0: simupak64-%src_ver.tar
#Source10: simutrans_pak.alternatives

Provides: simutrans-pak = %simutrans_ver
Conflicts: simutrans < %simutrans_ver

#BuildPreReq: rpm-macros-alternatives
#BuildRequires: unzip

%description
This is a complete data package of version %src_ver for Simutrans transport game
with 64x64 tiles. pak64 can be deemed an official Simutrans pak.

%description -l ru_RU.UTF-8
Этот пакет содержит данные версии %src_ver для транспортной игры Simutrans с ячейками
размером 64x64 точки. pak64 может считаться официальным набором для Simutrans.

%prep
%setup -q -c %name-%version

%install
mkdir -p %buildroot%_libexecdir/simutrans
cp -pr simutrans/pak %buildroot%_libexecdir/simutrans/pak64

#install -pD -m0644 %SOURCE10 %buildroot%_altdir/%name

#sed -i '
#s|%%_libexecdir|%_libexecdir|g
#' %buildroot%_altdir/%name

%files
%_libexecdir/simutrans/*
#%_altdir/%name

%changelog
* Sun Mar 25 2012 Aleksey Avdeev <solo@altlinux.ru> 111.2-alt1
- New version
- Rename %%_libexecdir/simutrans/pak to %%_libexecdir/simutrans/pak64

* Sun Jun 19 2011 Aleksey Avdeev <solo@altlinux.ru> 110.0.1-alt1
- New version
- Removed Packager:

* Tue Jan 08 2008 Michael Shigorin <mike@altlinux.org> 99.17-alt1
- built for Sisyphus
- added Packager:

* Sun Jan  6 2008 Alexey Morozov <morozov@altlinux.org> 99.17-alt1
- Initial build for ALT Linux
