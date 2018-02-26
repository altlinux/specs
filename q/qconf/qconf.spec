%define qtdir   %_libdir/qt4

Name: qconf
Version: 1.4
Release: alt1

Summary: Allows you to have a nice configure script for your qmake-based project
Group: Development/KDE and QT
License: GPL

Url: http://delta.affinix.com/qconf/
Source: %name-%version.tar.bz2
Packager: Anton A. Vinogradov <arc@altlinux.org>

# Automatically added by buildreq on Tue Dec 15 2009
BuildRequires: gcc-c++ libqt4-devel

%description
QConf allows you to have a nice configure script for your
qmake-based project. It is intended for developers who don't need
(or want) to use the more complex GNU autotools. With qconf/qmake,
it is easy to maintain a cross-platform project that uses a
familiar configuration interface on unix.

%prep
%setup -q

%build
./configure --prefix=%prefix \
            --bindir=%_bindir \
            --datadir=%_datadir \
            --qtdir=%_qt4dir

%install
%make INSTALL_ROOT=%buildroot install

%files
%doc COPYING README TODO
%_bindir/%name
%_datadir/%name




%changelog
* Mon Mar 22 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4-alt1
- release bump only

* Wed Jan 27 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4-alt0.1
- initial build for ALT Linux

