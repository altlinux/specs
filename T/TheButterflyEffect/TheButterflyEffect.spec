Name:		TheButterflyEffect
# sed -n '/APPRELEASE/s/.*"\(.*\)".*/\1/p' src/tbe_global.h
Version:	8.2
Release:	alt2
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
# gcc6 FIX 
sed -i 's/static const float/static constexpr float/' src/model/PolyObject.h

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
* Wed Jan 18 2017 Fr. Br. George <george@altlinux.ru> 8.2-alt2
- GCC6 fix

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 8.2-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Dec 06 2010 Fr. Br. George <george@altlinux.ru> 8.2-alt1
- Version up
- Milestone based versioning used

* Fri Jul 02 2010 Fr. Br. George <george@altlinux.ru> 0.0.3-alt1
- Initial build for ALT

