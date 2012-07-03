Name: qwebcam
Version: 0.0.3
Release: alt1

Summary: webcam viewer built on Qt4/C++
Group: Development/Tools
License: GPLv2+
Url: http://slist.lilotux.net/linux/%{name}/index_en.html

Source: %name-%version.tar
Source1: %name.watch

BuildRequires: gcc-c++ libqt4-devel >= 4.3 pkgconfig(opencv)

%description
Your webcam in QT.

%prep
%setup
#sed -i 's,debug_and_release,release,' qgit.pro
#sed -i '/QMAKE_CXXFLAGS_RELEASE/s,-O2 ,%optflags ,g' src/src.pro

%build
qmake-qt4 %name.pro
%make_build

%install
install -pD -m755 %name %buildroot%_bindir/%name

%files
#doc README
%_bindir/%name

%changelog
* Tue Jan 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt1
- Built for Sisyphus
