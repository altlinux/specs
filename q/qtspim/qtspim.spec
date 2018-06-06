Name: qtspim
Version: 9.1.20
Release: alt1.r715
License: BSD
Summary: MIPS32 Simulator
Url: http://spimsimulator.sourceforge.net/
Group: Emulators

Source0: %name-%version.tar.bz2
Source1: %name.desktop

# Automatically added by buildreq on Sun Jun 03 2018
# optimized out: fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libGL-devel libqt5-core libqt5-gui libqt5-help libqt5-printsupport libqt5-sql libqt5-widgets libstdc++-devel python-base python-modules qt5-base-devel qt5-declarative-devel qt5-tools
BuildRequires: flex qt5-location-devel qt5-multimedia-devel qt5-script-devel qt5-serialport-devel qt5-tools-devel


Requires: qt5-assistant

%description
SPIM is a simulator that runs programs written for MIPS32 computers.
SPIM can read and immediately execute assembly language files.
SPIM is a self-contained system for running these programs and contains
a debugger and interface to a few operating system services.

%prep
%setup


mkdir build
pushd build
cp -r ../QtSpim/help .
cp -r ../QtSpim/windows_images .
sed -i 's/TARGET = QtSpim/TARGET = qtspim/g' ../QtSpim/QtSpim.pro
sed -i 's/QString("\/usr\/lib\/qtspim\/help\/qtspim.qhc")/QString("\/usr\/share\/qtspim\/help\/qtspim.qhc")/g' ../QtSpim/menu.cpp
sed -i 's/"\/usr\/lib\/qtspim\/bin\/assistant"/"\/usr\/bin\/assistant-qt5"/g' ../QtSpim/menu.cpp
qmake-qt5 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" ../QtSpim/QtSpim.pro
popd
cp -f %SOURCE1 .

%build
pushd build
make
popd

%install
pushd build
install -D       qtspim %buildroot%_bindir/%name
install -Dm 644  help/qtspim.qhc %buildroot%_datadir/%name/help/qtspim.qhc
install -m  644  help/qtspim.qch %buildroot%_datadir/%name/help
popd

install -D       %name.desktop %buildroot%_datadir/applications/%name.desktop
install -Dm 644  Setup/NewIcon48x48.png %buildroot%_liconsdir/%name.png
install -Dm 644  Documentation/qtspim.man %buildroot%_mandir/man1/qtspim.1
install -Dm 644  README  %buildroot%_docdir/%name/README
install -m  644  ChangeLog  Setup/qtspim_debian_deployment/copyright %buildroot%_docdir/%name


%files
%_bindir/%name
%_datadir/applications/%name.desktop
%_liconsdir/%name.png
%_datadir/%name/*
%_mandir/man1/*
%_docdir/%name/* 




%changelog
* Wed Jun 06 2018 Mikhail E. Rudachenko (ali) <ali@altlinux.org> 9.1.20-alt1.r715
- new version
- specfile cleanup
- desktop file fix


* Tue Apr 17 2012 Mikhail E. Rudachenko (ali) <ali@altlinux.org> 9.1.7-alt1.r598
- Initial build from scratch.



