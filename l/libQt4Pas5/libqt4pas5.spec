Name:           libQt4Pas5
Version:        2.5
Release:        alt1.1
License:        LGPLv2+
Source0:        http://users.telenet.be/Jan.Van.hijfte/qtforfpc/V%{version}/splitbuild-qt4pas-V%{version}_Qt4.5.3.tar.gz
Group: 		System/Libraries
Url:		http://users.telenet.be/Jan.Van.hijfte/qtforfpc/fpcqt4.html
Summary:        Qt4 interface bindings for Pascal

BuildRequires: gcc-c++ libqt4-devel

%description
Provides interface for Pascal applications
to the Qt4 C++ libraries.
This binding does not cover the whole Qt4 framework, it
just contains all classes needed to use Qt as a widgetset.

%package devel
Summary:        Qt4 interface bindings - development files
Group: 		Development/C++
Requires:       %name = %version-%release

%description devel
Provides interface for Pascal applications
to the Qt4 C++ libraries.
This binding does not cover the whole Qt4 framework, it
just contains all classes needed to use Qt as a widgetset.

This package contains the development files.

%prep
%setup -c

%build
cd ./splitbuild-qt4pas-V%{version}_Qt4.5.3

qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags"

%make_build

%install
cd ./splitbuild-qt4pas-V%{version}_Qt4.5.3

%__make install INSTALL_ROOT=%buildroot
mkdir -p %buildroot/%_datadir/pascal/qt4
cp qt4.pas %buildroot/%_datadir/pascal/qt4


%files
%_libdir/libQt4Pas.so.*

%files devel
%_libdir/libQt4Pas.so
%_datadir/pascal/qt4/

%changelog
* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1.1
- NMU: added URL

* Fri May 01 2015 Motsyo Gennadi <drool@altlinux.ru> 2.5-alt1
- build for ALT Linux (thx to Anatoly Chernov for draft)
