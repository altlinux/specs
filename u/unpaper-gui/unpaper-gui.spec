Name: unpaper-gui
Version: 1.0
Release: alt1

Summary: GUI for unpaper

License: GPL
Group: Publishing
URL: http://wiki.ubuntuusers.de/Archiv/unpaper-GUI

Source: http://fleksem.klf.uw.edu.pl/~jsbien/sebu0708l/%name-%version.tar

# Automatically added by buildreq on Mon Sep 19 2011
# optimized out: fontconfig libgdk-pixbuf libstdc++-devel
BuildRequires: gcc-c++ libwxGTK-devel

%description
The aim of this program is to simplify using of unpaper by providing
graphical user interface.

%prep
%setup
cd src

%build
cd src
%make_build

%install
install -D src/unpap %buildroot%_bindir/unpap

%files
%doc README
%_bindir/unpap

%changelog
* Mon Sep 19 2011 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus


