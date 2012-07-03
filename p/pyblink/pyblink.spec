Name: pyblink
Version: 0.4.3
Release: alt2.qa3.1

Summary: Makes it easier to use Pybliographer in connection with eg. Open Office

License: GPL
Group: Text tools
Url: http://www.sonnet.dk/pyblink/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.sonnet.dk/%name/%name-%version.tar.bz2

BuildArchitectures: noarch

# manually removed: eric
# Automatically added by buildreq on Wed Nov 22 2006
BuildRequires: python-module-pygtk-libglade python-modules-encodings

%description
Pyblink uses the Cite-facility created for Lyx. It means that the
Lyx-pipe must exist, and pybliographic must be configurated to use that
lyx-pipe. The default lyx pipe is in ~/.lyx and is called lyxpipe.in
and lyxpipe.out

%prep
%setup -q

%build
export Python="/usr/bin/env python"
%configure
%make

%install
%makeinstall

install -d -m 0755 %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Pyblink
Comment=Pybibliorapher connector
Icon=%name
Exec=%name
Terminal=false
Categories=Office;Publishing;
EOF

%files
%_bindir/*
%_datadir/%name
%_desktopdir/%name.desktop

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.3-alt2.qa3.1
- Rebuild with Python-2.7

* Sat Apr 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.3-alt2.qa3
- NMU: converted menu to desktop file

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt2.1.1
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.4.3-alt2.1
- Rebuilt with python-2.5.

* Wed Nov 22 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.3-alt2
- fix build

* Tue Dec 06 2005 Vitaly Lipatov <lav@altlinux.ru> 0.4.3-alt1
- rebuild with new pycairo

* Sun Sep 11 2005 Vitaly Lipatov <lav@altlinux.ru> 0.4.3-alt0.1
- first build for ALT Linux Sisyphus

