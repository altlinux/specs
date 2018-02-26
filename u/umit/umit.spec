Name: umit
Version: 1.0
Release: alt1.1

Summary: Umit is a network scanning frontend

Group: Monitoring
License: GPLv2
Url: http://sourceforge.net/projects/umit/

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Source: %name-%version.tar.bz2
Source1: %name.pamd
Source2: %name.security


BuildRequires: python-module-setuptools hd2u python-module-sphinx
Requires: nmap

%description
UMIT is the new nmap frontend, intended to be cross plataform, easy to use, fast and highly customizable.

%prep
%setup -q
dos2unix umit/core/Paths.py
sed -i "/BASE_DOCS_DIR/s/umit/umit-%version/g" install_scripts/common.py
mv share/doc/umit share/doc/umit-%version

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot --install-lib=%python_sitelibdir -P

#Menu and icons
%__mkdir_p %buildroot%_pixmapsdir
ln -s umit/umit-menu.xpm %buildroot%_pixmapsdir/%name-menu.xpm
#__install -p -m 644 share/pixmaps/umit/umit_48x48.png %buildroot%_pixmapsdir/%name.png

%__mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name-root.desktop  <<EOF
[Desktop Entry]
Name=Umit (as root)
Comment=%summary
Exec=umit-root
Icon=%name-menu
Type=Application
Terminal=false
Categories=Application;Network;Security;
EOF

cat > %buildroot%_desktopdir/%name.desktop  <<EOF
[Desktop Entry]
Name=Umit
Comment=%summary
Exec=umit
Icon=%name-menu
Type=Application
Terminal=false
Categories=Application;Network;Security;
EOF

ln -s $(relative %_libexecdir/consolehelper/helper %_bindir/) %buildroot%_bindir/umit-root
install -pD -m640 %_sourcedir/umit.pamd %buildroot%_sysconfdir/pam.d/umit-root
install -pD -m640 %_sourcedir/umit.security %buildroot%_sysconfdir/security/console.apps/umit-root

mv %buildroot%_datadir/doc/%name-%version/html .

%find_lang --with-gnome %name

%files -f %name.lang
%doc COPYING*
%doc html
%config(noreplace) %_sysconfdir/pam.d/umit-root
%config(noreplace) %_sysconfdir/security/console.apps/umit-root
%_bindir/umit*
%_datadir/%name
%_datadir/icons/umit
%_desktopdir/umit*.desktop
%_pixmapsdir/umit*
%python_sitelibdir/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1
- Rebuild with Python-2.7

* Mon Apr 04 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1
- initial build for ALT Linux
