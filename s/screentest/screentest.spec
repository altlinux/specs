Name: screentest
Version: 2.0
Release: alt2.1

Summary: The CRT screen quality testing utility
Summary(ru_RU.KOI8-R): Утилита для тестирования качества ЭЛТ-монитора
Group: System/Configuration/Hardware
License: GPL
Url: http://www.fi.muni.cz/~kas/screentest/

Source0: ftp://ftp.fi.muni.cz/pub/linux/people/jan_kasprzak/screentest/%name-%version.tar.gz
Patch0: screentest-2.0-alt-DSO.patch

BuildRequires: libgtk+2-devel libglade-devel glib2-devel

%description
Screentest is a simple program which displays various patterns
(colors, circles, grids, text) on your screen in order to allow you to
evaluate the quality of your CRT monitor (sharpness, linearity, etc).

%description -l ru_RU.KOI8-R
Screentest - простая программа, которая отображает различные образцы
(цвета, окружности, сетки, текст) на экране с целью оценки качества
ЭЛТ-монитора (чёткости, линейности и т.д.).

%prep
%setup -q
%patch0 -p2

%build
%configure
%make

%install
%makeinstall

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Screentest
GenericName=CRT screen test
Comment=The CRT screen quality testing utility
Icon=%{name}
Exec=%name
Terminal=false
Categories=Settings;HardwareSettings;X-ALTLinux-VideoSettings;
StartupNotify=false
EOF

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog NEWS NEW_TESTS README
%_bindir/*
%_datadir/%name
%_desktopdir/%{name}.desktop

%changelog
* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2.1
- Fixed build

* Tue Mar 29 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2
- .desktop comment clean-up

* Mon Mar 28 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1
- new version;
- picked up from orphaned

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2.1
- NMU (by repocop): the following fixes applied:
  * update_menus for screentest

* Mon Jan 29 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.0-alt2
- Fixed BuildRequires.
- Added Packager: field.

* Thu Mar 25 2004 Andrei Bulava <abulava@altlinux.ru> 1.0-alt1
- initial build for ALT Linux

