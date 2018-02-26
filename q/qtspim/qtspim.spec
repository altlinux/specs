Name: qtspim
Version: 9.1.7
Release: alt1.r598
License: BSD
Summary: MIPS32 Simulator
Url: http://spimsimulator.sourceforge.net/
Group: Emulators
# from https://spimsimulator.svn.sourceforge.net/svnroot/spimsimulator
# svn info  https://spimsimulator.svn.sourceforge.net/svnroot/spimsimulator

# svn --depth empty co https://spimsimulator.svn.sourceforge.net/svnroot/spimsimulator/ --config-dir ./ -r 598 .
# svn up README
# svn up ChangeLog
# svn up QtSpim
# svn up CPU
# svn --depth empty co https://spimsimulator.svn.sourceforge.net/svnroot/spimsimulator/Documentation --config-dir ./ -r 598 Documentation
# cd Documentation/
# svn up qtspim.man 
# cd ..
# svn --depth empty co https://spimsimulator.svn.sourceforge.net/svnroot/spimsimulator/Setup --config-dir ./ -r 598 Setup
# cd Setup
# svn up NewIcon48x48.png
# cd ..
# svn --depth empty co https://spimsimulator.svn.sourceforge.net/svnroot/spimsimulator/Setup/qtspim_debian_deployment --config-dir ./ -r 598 Setup/qtspim_debian_deployment
# cd Setup/qtspim_debian_deployment
# svn up copyright
# cd ../..

Source0: %name-%version.tar.bz2
Source1: %name.desktop

# Automatically added by buildreq on Sun Feb 26 2012
# optimized out: fontconfig libqt4-clucene libqt4-core libqt4-devel libqt4-gui libqt4-help libqt4-network libqt4-sql libqt4-sql-sqlite libstdc++-devel
BuildRequires: flex gcc-c++ phonon-devel


Requires: qt4-assistant

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
sed -i  s':help/qtspim.qhp:../build/help/qtspim.qhp:g' ../QtSpim/QtSpim.pro
sed -i  s':help/qtspim.qhcp:../build/help/qtspim.qhcp:g' ../QtSpim/QtSpim.pro
sed -i 's/qhelpgenerator/qhelpgenerator-qt4/g' ../QtSpim/QtSpim.pro
sed -i 's/qcollectiongenerator/qcollectiongenerator-qt4/g' ../QtSpim/QtSpim.pro
sed -i 's/start(QLatin1String("assistant")/start(QLatin1String("assistant-qt4")/g' ../QtSpim/menu.cpp
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" ../QtSpim/QtSpim.pro
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
* Tue Apr 17 2012 Mikhail E. Rudachenko (ali) <ali@altlinux.org> 9.1.7-alt1.r598
- Initial build from scratch.



