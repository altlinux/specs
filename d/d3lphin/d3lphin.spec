%def_disable debug
%def_disable profile
%def_enable final
%def_enable threading
%def_disable rpath
#def_with arts
%def_disable arts

%define Name D3lphin
Name: d3lphin
Version: 0.9.2
Release: alt4
Summary: A file manager for KDE focusing on usability
License: %gpl2plus
Group: File tools
URL: https://marrat.homelinux.org/%Name
Source: %{url}?action=AttachFile&do=get&target=/%name-%version.tar
Patch: %name-%version-alt.patch
Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Oct 07 2007
BuildRequires: gcc-c++ kdelibs-devel libXext-devel libjpeg-devel libtqt-devel
BuildRequires: xml-utils xorg-cf-files

%description
%Name is a fork of dolphin, since the latter is unmaintained for
KDE 3.
%Name focuses on being only a file manager. This approach allows to
optimize the user interface for the task of file management.


%prep
%setup
%patch -p1


%build
%set_automake_version 1.9
#set_autoconf_version 2.5

%make_build -f Makefile.cvs
%configure \
    %{subst_enable debug} \
    %{subst_enable profile} \
    %{subst_enable final} \
    %{subst_enable threading} \
    %{subst_enable rpath} \
    --without-arts \
    --enable-new-ldflags
%make_build CXXFLAGS="-I%_includedir/tqtinterface"
bzip2 --best --keep --force ChangeLog


%install
%make_install DESTDIR=%buildroot install
rm -rf %buildroot%_datadir/locale/%name
%find_lang --with-kde %name


%files -f %name.lang
%doc AUTHORS ChangeLog.* TODO
%_bindir/*
%_datadir/apps/%name
%_iconsdir/hicolor/*/apps/*
%_desktopdir/kde/*


%changelog
* Tue Apr 19 2011 Ilya Mashkin <oddity@altlinux.ru> 0.9.2-alt4
- build without arts

* Sun Jul 19 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.2-alt3.1
- fixed build

* Mon Nov 03 2008 Led <led@altlinux.ru> 0.9.2-alt3
- fixed *.desktop

* Sat Aug 09 2008 Led <led@altlinux.ru> 0.9.2-alt2
- fixed *.desktop

* Sun Oct 07 2007 Led <led@altlinux.ru> 0.9.2-alt1
- updated BuildRequires

* Mon Sep 03 2007 Led <led@altlinux.ru> 0.9.2-alt0.3
- added uk.po
- cleaned up spec

* Mon Sep 03 2007 Led <led@altlinux.ru> 0.9.2-alt0.2
- cleaned up spec
- fixed License
- fixed %name.desktop

* Sun Sep 02 2007 Nick S. Grechukh <gns@altlinux.org> 0.9.2-alt0.1
- Initial packaging for ALT Linux 4.0

* Thu Aug 23 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.2-2
- New upstream version

* Wed Jul 18 2007 0.9.1-1
- Adopted dolphin-0.8.2 specfile for d3lphin-0.9.1

* Sun Apr 22 2007 Johan Cwiklinski <johan@x-tnd.be> 0.8.2-2
- Added gettext to BR so locales are correctly handled while building

* Sun Mar 18 2007 Johan Cwiklinski <johan.cwiklinski@fedoraproject.org> 0.8.2-1
- Upgrading to new version

* Sun Jan 14 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.8.1-1
- Initial package for Fedora Extras.
