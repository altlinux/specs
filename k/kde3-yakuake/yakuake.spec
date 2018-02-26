%define qtdir %_qt3dir
%define kdedir %_K3prefix
%define _unpackaged_files_terminate_build 1
%define origname yakuake

Name: kde3-yakuake
Version: 2.8.1
Release: alt5

Summary: Very powerful Quake style Konsole
License: %gpl2plus
Group: Terminals

Url: http://extragear.kde.org/apps/yakuake/
Packager: Evgeny Sinelnikov <sin@altlinux.ru>

Source: http://download.berlios.de/yakuake/%origname-%version.tar.bz2
Patch0: yakuake-2.8-i18n.patch
Patch1: yakuake-2.8.1-automake-check.patch
Patch2: yakuake-alt-DSO.patch

%def_without arts

BuildPreReq: rpm-build-licenses

BuildPreReq: gcc4.5-c++ kdelibs-devel libtqt-devel
%if_with arts
BuildRequires:  libarts-devel
%endif 

%description
A KDE konsole which looks like those found in Quake.

%prep
%setup -n %origname-%version
%patch0 -p1
%patch1
%patch2

cp -Rp /usr/share/libtool/aclocal/libtool.m4 admin/libtool.m4.in
cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
make -f admin/Makefile.common cvs ||:

%build
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%kdedir

%add_optflags -I%_includedir/tqtinterface
export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

%K3configure \
	%{subst_with arts} \
	--enable-final

%make_build

%install
%K3install

%find_lang --with-kde %origname

%files -f %origname.lang
%doc AUTHORS ChangeLog README TODO
%_K3bindir/*
%_K3xdg_apps/*.desktop
%_K3cfg/*.kcfg
%_K3apps/%origname
%_kde3_iconsdir/hicolor/*/apps/*
%_K3i18n/*/*/*.mo

%changelog
* Sat Jun 04 2012 Roman Savochenko <rom_as@altlinux.ru> 2.8.1-alt5
- Build for TDE 3.5.13 release.

* Sun Mar 13 2011 Evgeny Sinelnikov <sin@altlinux.ru> 2.8.1-alt4
- Update for new compiler and environment restrictions:
+ Build with tqtinterface includes cxxflags
+ Build without arts 

* Sun Jun 28 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.8.1-alt3
- rebuild with patch for automake-1.11 using

* Mon Jun 15 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.8.1-alt2
- rename to kde3-yakuake due kde4-yakuake renamed to yakuake as mainstream
- remove obsolete macroses

* Sun Feb 10 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Tue Nov 20 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.8-alt2
- spec cleanup
- enable _unpackaged_files_terminate_build
- fix packaging of icons (#10173, php-coder@)

* Sat Oct 13 2007 Nick S. Grechukh <gns@altlinux.org> 2.8-alt1
- new version (wrar@ reminded ;)

* Thu May 04 2006 Nick S. Grechukh <gns@altlinux.org> 2.7.5-alt1
- new version. fixed Url and Source. i18n removed (fixed in upstream)

* Mon Feb 13 2006 Nick S. Grechukh <gns@altlinux.org> 2.7.3-alt5
- removed kdedesktop2mdkmenu

* Sun Nov 13 2005 Nick S. Grechukh <gns@altlinux.ru> 2.7.3-alt4
- new version with i18n patch from Albert Valiev

* Mon Oct 24 2005 Nick S. Grechukh <gns@altlinux.org> 2.7.2-alt1
- new version

* Thu Oct 13 2005 Nick S. Grechukh <gns@altlinux.org> 2.6-alt1
- initial build 
