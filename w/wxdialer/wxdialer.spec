Name: wxdialer
Version: 0.2.1
Release: alt6.1.qa2.1

Summary: A phone dialer written in wxPython
Summary(ru_RU.KOI8-R): Программа набора номера, написанная на wxPython

License: GPL
Group: Communications
Url: http://wxdialer.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: wxDialer-%version.tar.bz2
Source1: %name.png
Patch: wxDialer-%version-etersoft.patch
Patch1: %name-gettext.patch

%define installdir %_libdir/python%__python_version/tools
BuildRequires: desktop-file-utils

%description
wxDialer is a simple and easy to use dialer program, roughly based on the win9x
program 'dialer.exe' - all it does is allow you to make and receive calls on
your modem. A microphone is required, and it is suggested that you also have
headphones instead of using your speakers to prevent any nasty feedback. A
telephone headset, naturally, is best for this.

%description -l ru_RU.KOI8-R
wxDialer - это простая программа для набора номера через модем. Всё, что она
делает - позволяет вам делать и принимать звонки через модем. Вам потребуется
микрофон, и так же предполагается, что вы используете наушники вместо колонок,
чтобы избежать возникновения эффекта обратной связи. Телефонная гарнитура - лучший
вариант для этого.

%prep
%setup -n wxDialer-%version
%patch -p1
%patch1

%build
%make

%install
%makeinstall
install -d  %buildroot%_bindir
install -D -m0755 wxDialer.py %buildroot%installdir/%name.py
ln -s %installdir/%name.py %buildroot%_bindir/%name

install -D -m644 %SOURCE1 %buildroot%_niconsdir/%name.png

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Phone dialer
Comment=A phone dialer written in wxPython
Exec=%_bindir/%name
Icon=%name.png
Terminal=false
Type=Application
Categories=Internet;
EOF

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Internet \
	--add-category=Network \
	--add-category=Dialup \
	%buildroot%_desktopdir/wxdialer.desktop

%files -f %name.lang
%doc README TODO
%_bindir/%name
%_desktopdir/%name.desktop
%_niconsdir/*
%installdir/%name.py

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt6.1.qa2.1
- Rebuild with Python-2.7

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.1-alt6.1.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for wxdialer

* Sun Dec 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.1-alt6.1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for wxdialer
  * postclean-05-filetriggers for spec file

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt6.1
- Rebuilt with python 2.6

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt6
- replace menu with desktop file
- cleanup spec

* Sun May 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt5
- improve gettext using (fix bug #9596)

* Fri Mar 25 2005 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt4
- rebuild with python 2.4 and wxPython 2.5.4

* Thu Jul 15 2004 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt3
- add missed main module

* Tue Jun 29 2004 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt2
- fix required python version, group, Url
- move program to python dir

* Sat Jun 26 2004 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- first build for Sisyphus

