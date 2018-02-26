Name:		TheButterflyEffect
# sed -n '/APPRELEASE/s/.*"\(.*\)".*/\1/p' src/tbe_global.h
Version:	8.2
Release:	alt1
License:	GPL
Group:		Games/Puzzles
Summary:	Combine mechanical elements to achieve a simple goal in the most complex way
Source:		http://dl.sourceforge.net/project/tbe/Milestone%%20%version/%name-m%version.src.tgz
Patch:		%name-qt4.patch
URL:		http://sourceforge.net/apps/trac/tbe/wiki/WikiStart

# Automatically added by buildreq on Fri Jul 02 2010
BuildRequires: gcc-c++ libqt4-devel unzip

%description
A game that uses realistic physics simulations to combine lots of simple mechanical elements to achieve a simple goal in the most complex way possible.

%prep
%setup -n %name-m%version
%patch

%build
./configure --datadir=%_gamesdatadir/%name
echo "QQQ"
#( cd 3rdParty; #make_build )
#qmake-qt4
%make_build
cat > %name <<@@@
#!/bin/sh
cd %_gamesdatadir/%name
%_gamesbindir/tbe
@@@

%install
mkdir -p %buildroot%_gamesdatadir/%name
cp -a images i18n levels %buildroot%_gamesdatadir/%name
install -D tbe %buildroot%_gamesbindir/tbe
install -D -m755 %name %buildroot%_gamesbindir/%name

%files
%doc README
%_gamesbindir/*
%_gamesdatadir/%name

%changelog
* Mon Dec 06 2010 Fr. Br. George <george@altlinux.ru> 8.2-alt1
- Version up
- Milestone based versioning used

* Fri Jul 02 2010 Fr. Br. George <george@altlinux.ru> 0.0.3-alt1
- Initial build for ALT

