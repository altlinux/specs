Name: pystopwatch
Version: 2.0
Release: alt1.1.1

Summary: A stopwatch written in python with a timer and two countdown functions that can minimize to the tray

Group: Office
License: GPL2
Url: http://xyne.archlinux.ca/info/pystopwatch

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://xyne.archlinux.ca/src/%name-%version.tar.bz2

BuildArch: noarch

%description
A stopwatch written in python with a timer and two countdown functions that can minimize to the tray.

%prep
%setup -n %name

%install
install -D %name %buildroot%_bindir/%name

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Stopwatch
Comment=A stopwatch with a timer and two countdown functions
Exec=%_bindir/%name
Icon=%name.png
Terminal=false
Type=Application
Categories=Office;
EOF

%files
%_bindir/%name
%_desktopdir/*.desktop

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.1
- Rebuilt with python 2.6

* Thu May 21 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- initial build for ALT Linux Sisyphus
