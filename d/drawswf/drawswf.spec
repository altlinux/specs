Name: drawswf
Version: 1.2.9
Release: alt3.qa1

Summary: drawing application with a capability of export in flash animation
License: GPL
Group: Graphics

Url: http://drawswf.sf.net
Source: %name-%version.tar.bz2

#BuildArchitectures: i586

Requires: java-common, bash
Packager: Ilya Mashkin <oddity@altlinux.ru>


Summary(ru_RU.KOI8-R): графический редактор с возможностью создания флэш анимации 

%description
DrawSWF is a simple drawing application written in Java.
The drawing can be exported as an animated SWF file.
To write the flash file the JavaSWF2 is used
(see http://www.anotherbigidea.com/javaswf/index.html).


%description -l ru_RU.KOI8-R
DrawSWF - простой графический редактор написанный на Java.
Созданные в нем анимации можно экспортировать как анимированные SWF файлы.
Для создания флэш файлов используется JavaSWF2
(подробнее о JavaSWF2 на http://www.anotherbigidea.com/javaswf/index.html).

%prep
%setup -q

%build
%install
install -D -m755 %name-%version.jar $RPM_BUILD_ROOT%_libdir/%name/%name-%version.jar
install -D -m755 %name $RPM_BUILD_ROOT%_bindir/%name
install -D -m644 %name.png $RPM_BUILD_ROOT%_niconsdir/%name.png

#install menu
install -m755 -d %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=DrawSWF
GenericName=Flash Animation
Comment=creation of flash animation
Icon=%{name}
Exec=%{name}
Terminal=false
Categories=Graphics;2DGraphics;VectorGraphics;
EOF

%files
%_bindir/*
%attr(755,root,root) %_libdir/%name
%_desktopdir/%{name}.desktop
%_niconsdir/*
%doc README

%changelog
* Mon Apr 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.9-alt3.qa1
- NMU: converted menu to desktop file

* Sun Sep 06 2009 Ilya Mashkin <oddity@altlinux.ru> 1.2.9-alt3
- fix icons locations

* Fri Apr 10 2009 Ilya Mashkin <oddity@altlinux.ru> 1.2.9-alt2
- fix name of jar file in script
- remove deprecated macros

* Wed Oct 22 2008 Ilya Mashkin <oddity@altlinux.ru> 1.2.9-alt1
- 1.2.9

* Sun Oct 12 2003 Alexander Nekrasov <canis@altlinux.ru> 1.2.7-alt1
- first build
