%add_findreq_skiplist *gdbmacros*

Name: qt-creator
Version: 2.5.0
Release: alt1
Summary: Lightweight and cross-platform IDE for Qt

Group: Development/Tools
License: LGPLv2 with exceptions
Url: http://qt.nokia.com/products/developer-tools
Packager: Anatoly Lyutin <vostok@altlinux.org>

#Source: http://download.qtsoftware.com/qtcreator/%name-%version-src.tar.gz
Source: %name-%version.tar
Source1: qtcreator.desktop

Patch: fix_linking_libhelp.patch

Requires: %name-data = %version-%release

BuildRequires: gcc-c++ 
BuildRequires: libqt4-devel >= 4.7.4
BuildRequires: libqt4-webkit >= 4.7.4

%description
Qt Creator (previously known as Project Greenhouse) is a new,
lightweight, cross-platform integrated  development environment (IDE)
designed to make development with the Qt application framework
even faster and easier.

%package doc
Summary: %name docs
Group: Documentation
BuildArch: noarch
Requires: %name
Requires: libqt4-sql-sqlite

%description doc
Documentation for %name

%package data
Summary: Data files for %name
Group: Development/Tools
BuildArch: noarch
Requires: %name

%description data
Data files for %name

%prep
%setup
subst 's,tools\/qdoc3,bin,' doc/doc.pri
subst 's,share\/doc\/qtcreator,share\/qtcreator\/doc,' doc/doc.pri src/plugins/help/helpplugin.cpp
%patch0 -p1

%build
export QTDIR=%_qt4dir
qmake-qt4 IDE_LIBRARY_BASENAME=%_lib
%make_build
%make_build docs

%install
%makeinstall_std INSTALL_ROOT=%buildroot%_prefix
mkdir -p %buildroot%_desktopdir
install %SOURCE1 %buildroot%_desktopdir

mkdir -p %buildroot%_datadir/qtcreator/translations
cp share/qtcreator/translations/*.qm %buildroot%_datadir/qtcreator/translations

for i in 16 24 32 48 64 128 256 512; do
    install -pD -m644 src/plugins/coreplugin/images/logo/${i}/qtcreator.png \
                      %buildroot%_iconsdir/hicolor/${i}x${i}/apps/qtcreator.png
#    mkdir -p %buildroot%_iconsdir/hicolor/${i}x${i}/apps
#    ln -s %_pixmapsdir/qtcreator_logo_${i}.png \
#          %buildroot%_iconsdir/hicolor/${i}x${i}/apps/%name.png
done
%make_install INSTALL_ROOT=%buildroot%_prefix install_docs

%files
%doc README LICENSE.LGPL LGPL_EXCEPTION.TXT
%_bindir/*
%_libdir/qtcreator
%_iconsdir/hicolor/*/apps/qtcreator.png
%_desktopdir/qtcreator.desktop

%files doc
%_datadir/qtcreator/doc

%files data
%dir %_datadir/qtcreator/translations
%dir %_datadir/qtcreator
%_datadir/qtcreator/*
%exclude %_datadir/qtcreator/doc

%changelog
* Fri May 11 2012 Anatoly Lyutin <vostok@altlinux.org> 2.5.0-alt1
- new version

* Mon Jan 09 2012 Anatoly Lyutin <vostok@altlinux.org> 2.4.0-alt1
- new version

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.0-alt1.1
- Rebuild with Python-2.7

* Thu Sep 22 2011 Anatoly Lyutin <vostok@altlinux.org> 2.3.0-alt1
- new version (closes #26219)

* Fri Aug 05 2011 Anatoly Lyutin <vostok@altlinux.org> 2.2.1-alt1
- new version

* Mon Jun 06 2011 Anatoly Lyutin <vostok@altlinux.org> 2.2.0-alt1
- update to 2.2.0

* Fri Mar 04 2011 Anatoly Lyutin <vostok@altlinux.org> 2.1.0-alt1
- update to 2.1.0

* Wed Jul 28 2010 Anatoly Lyutin <vostok@altlinux.org> 2.0.0-alt1
- update to 2.0.0

* Mon Mar 01 2010 Boris Savelev <boris@altlinux.org> 1.3.1-alt1
- new version

* Tue Dec 15 2009 Boris Savelev <boris@altlinux.org> 1.3.0-alt1
- new version (closes: #22547)

* Sun Aug 30 2009 Boris Savelev <boris@altlinux.org> 1.2.1-alt3.g26a3a3e
- build from upstream git

* Wed Aug 05 2009 Boris Savelev <boris@altlinux.org> 1.2.1-alt2.g0dbe82f
- new version

* Thu Jul 16 2009 Boris Savelev <boris@altlinux.org> 1.2.1-alt1.gba2a5a6
- new version

* Tue Jun 30 2009 Boris Savelev <boris@altlinux.org> 1.2.0-alt2.g6315f14
- build from upstream git
- add translations (closes:#20605)

* Fri Jun 26 2009 Boris Savelev <boris@altlinux.org> 1.2.0-alt1.g934ee44
- version up

* Mon May 25 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt6.gcf7cd73
- add %_bindir/qtcreator_process_stub (fix #20171)

* Mon May 11 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt5.gcf7cd73
- build from upstream git

* Sun May 03 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt4.ga1dc8f5
- build from upstream git

* Tue Apr 28 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt3.git.124.g092d8ca
- build from upstream git

* Tue Apr 28 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt2
- build doc (fix #19799)

* Thu Apr 23 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt1
- initial build for Sisyphus from Fedora

* Tue Mar 20 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.0.0-4
- fix lib's loading in 64 bit machines

* Tue Mar 18 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.0.0-3
- Changed License to LGPLv2 with exceptions and BR to qt4-devel >= 4.5.0

* Tue Mar 17 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.0.0-2
- Improved Version to make it more compatible with fedora guidelines

* Sun Mar 15 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.0.0-1
- initial RPM release
