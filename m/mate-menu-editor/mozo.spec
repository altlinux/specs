# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname mozo
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           mate-menu-editor
Version:        1.4.0
Release:        alt2_1.1
Summary:        Menu editor for the MATE desktop

Group:          File tools
License:        LGPLv2+
URL:            http://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.4/%{oldname}-%{version}.tar.xz

Patch1:         mate-menu-editor-move-and_rename_directorys.patch

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-pygtk-devel
BuildRequires:  mate-menus-devel >= 1.1.1
BuildRequires:  intltool
BuildRequires:  mate-common
Requires:       pygtk2 python-module-mate-mateconf
Requires:       mate-menus >= 1.1.1

Obsoletes:		mate-menu-editor
Provides:		mozo
Patch33: alacarte-0.13.2-alt-xfce.patch
Source44: import.info

%description
mozo is a graphical menu editor that lets you edit, add, and delete
menu entries. It follows the freedesktop.org menu specification and
should work with any desktop environment that uses this specification.

%prep
%setup -q -n %{oldname}-%{version}
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1

%build

%configure

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT


%find_lang mozo

%files -f mozo.lang
%{python_sitelibdir_noarch}/Mozo
%{_bindir}/mozo
%{_datadir}/applications/mozo.desktop
%{_datadir}/mozo/mozo.ui
%{_datadir}/icons/hicolor/16x16/apps/mozo.png
%{_datadir}/icons/hicolor/22x22/apps/mozo.png
%{_datadir}/icons/hicolor/24x24/apps/mozo.png
%{_datadir}/icons/hicolor/32x32/apps/mozo.png
%{_datadir}/icons/hicolor/48x48/apps/mozo.png
%{_datadir}/icons/hicolor/256x256/apps/mozo.png

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- new release

