Name: iaito
Version: 5.9.4
Release: alt1

Summary: GUI for radare2
License: GPLv3
Group: Development/Other
Url: https://github.com/radareorg/iaito

Source: %name-%version-%release.tar

BuildRequires: acr gcc-c++ radare2-devel
BuildRequires: qt6-base-devel qt6-svg-devel qt6-tools-devel

%description
iaito is the official graphical interface for radare2, a libre
reverse engineering framework.

%prep
%setup
sed -ri -e '/^QMAKE_CXXFLAGS/ s,$, %optflags,' -e '/QMAKE_LFLAGS.+rpath/d' src/Iaito.pro
sed -ri -e '/^(iaito|install)/ s,translations,build,' Makefile

%build
export QMAKE=/usr/bin/qmake-qt6
export LRELEASE=/usr/bin/lrelease-qt6
%configure
%make_build

%install
install -pm0755 -D build/iaito %buildroot%_bindir/iaito
install -pm0644 -D src/org.radare.iaito.appdata.xml %buildroot%_datadir/metainfo/org.radare.iaito.appdata.xml
install -pm0644 -D src/org.radare.iaito.desktop %buildroot%_desktopdir/org.radare.iaito.desktop
install -pm0644 -D src/img/iaito-o.svg %buildroot%_iconsdir/hicolor/scalable/apps/iaito.svg
install -pm0644 -D src/iaito.1 %buildroot%_man1dir/iaito.1

%files
%doc COPYING README*
%_bindir/iaito
%_desktopdir/*.desktop
%_iconsdir/*/*/apps/iaito.*
%_datadir/metainfo/*.appdata.xml
%_man1dir/iaito.1*

%changelog
* Fri Aug 30 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 5.9.4-alt1
- 5.9.4 released

* Mon May 27 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 5.9.2-alt1
- 5.9.2 released

* Mon Apr 01 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 5.9.0-alt1
- 5.9.0 released

* Wed Dec 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.8.8-alt1
- 5.8.8 released

* Thu Oct 27 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.7.8-alt1
- 5.7.8 released

* Thu Oct  6 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.7.6-alt1
- 5.7.6 released

* Mon Aug 22 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.7.2-alt1
- initial
