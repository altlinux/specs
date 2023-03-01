%define Name QXmlEdit
Name: qxmledit
Version: 0.9.18
Release: alt1

Summary: Simple XML editor and XSD viewer

Group: Editors
License: GPLv2+
URL: https://github.com/lbellonda/%name

# Source-url: https://github.com/lbellonda/qxmledit/archive/%version.tar.gz
Source: %name-%version.tar
Source10: QXmlEdit_ru.ts
Patch1: alt-desktop-l10n.patch

Provides: %Name = %version-%release

BuildRequires: gcc-c++ qt5-base-devel qt5-scxml-devel qt5-xmlpatterns-devel qt5-svg-devel rpm-macros-qt5 qt5-tools

# ../include/qwt3d_openglhelper.h
BuildRequires: libGLU-devel

%description
%Name is a simple XML editor written in Qt 5. Its main features are unusual
data visualization modes, nice XML manipulation and presentation. It can split
very big XML files into fragments, and compare XML files. It is one of the few
graphical Open Source XSD viewers.
Main features:
  - Hierarchical customizable view of XML elements.
  - Fast XML hierarchy navigation.
  - Split of big XML files.
  - Search supporting XPath expressions.
  - Base 64 data handling.
  - Custom visualization styles.
  - XML Schema (XSD) viewer.
  - Columnar view.
  - Sessions handling.
  - Graphical XML file view.
  - Map view of a XML document.
  - Split and fragment extraction of big XML files.
  - Visual compare of XML Schema files.
  - Visual compare of XML files.
  - XML Snippets.
  - XSL specialized mode.


%prep
%setup
%patch1 -p1

cat %SOURCE10 >src/languages_app/QXmlEdit_ru.ts

%build
lrelease-qt5 src/QXmlEdit.pro
lrelease-qt5 src/QXmlEditWidget.pro
lrelease-qt5 src/sessions/QXmlEditSessions.pro

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%qmake_qt5 "CONFIG+=release staticlib" %Name.pro
# DISABLE_COMPILE_WARNINGS disables -Werror, not warnings
%make_build \
%ifarch %e2k
	QXMLEDIT_INST_AVOID_PRECOMP_HEADERS=yes \
	QXMLEDIT_INST_DISABLE_COMPILE_WARNINGS=yes \
%endif
	QXMLEDIT_INST_DATA_DIR=%_datadir/%name \
	QXMLEDIT_INST_DIR=%_bindir \
	QXMLEDIT_INST_DOC_DIR=%_docdir/%name-%version \
	QXMLEDIT_INST_LIB_DIR=%_libdir \
	QXMLEDIT_INST_INCLUDE_DIR=%_includedir/%name


%install
%make_install INSTALL_ROOT=%buildroot install
install -m 0644 AUTHORS NEWS README ROADMAP TODO %buildroot%_docdir/%name-%version/

install -pD -m 0644 src/images/icon.png %buildroot%_niconsdir/%name.png
install -pD -m 0644 ./src/images/icon.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

install -d -m 0755 %buildroot%_desktopdir
#mv %buildroot%_datadir/%name/%Name.desktop %buildroot%_desktopdir/%Name.desktop
install -D -m 0644 install_scripts/environment/desktop/QXmlEdit.desktop %buildroot/%_desktopdir/


%files
%doc %_docdir/%name-%version
%_bindir/*
%_datadir/%name
%_desktopdir/*
%_niconsdir/*
%_iconsdir/hicolor/scalable/apps/*
%exclude %_includedir
%exclude %_libdir


%changelog
* Wed Mar 01 2023 Sergey V Turchin <zerg@altlinux.org> 0.9.18-alt1
- new version
- update russian translation

* Mon Nov 14 2022 Sergey V Turchin <zerg@altlinux.org> 0.9.17-alt1
- new version

* Tue Sep 14 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.9.16-alt2
- fixed build for Elbrus
- fixed -flto

* Thu Oct 01 2020 Sergey V Turchin <zerg@altlinux.org> 0.9.16-alt1
- new version

* Tue Oct 28 2019 Konstantin Kondratyuk <kondratyuk@altlinux.org> 0.9.13-alt3
- add russian translations

* Wed Oct 17 2019 Konstantin Kondratyuk <kondratyuk@altlinux.org> 0.9.13-alt2
- build translations

* Wed Oct 16 2019 Konstantin Kondratyuk <kondratyuk@altlinux.org> 0.9.13-alt1
- new version 0.9.13 (with rpmrb script)

* Fri Mar 01 2019 Vitaly Lipatov <lav@altlinux.ru> 0.9.12-alt1
- new version (0.9.12) with rpmgs script
- move source code to the subdir
- build with Qt 5

* Mon Jul 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.7.1-alt1
- Update to upstream version 0.9.7-1

* Sun Mar 30 2014 Led <led@altlinux.ru> 0.8.10-alt1
- initial build
