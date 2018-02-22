Group: Graphical desktop/MATE
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize libgio-devel pkgconfig(dbus-1) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname caja-extensions
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name caja-extensions
%define version 1.20.0
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.20

# Settings used for build from snapshots.
%{!?rel_build:%global commit 298c7255b82986eeba72fff06f59479deae0b9d0}
%{!?rel_build:%global commit_date 20131201}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{oldname}-%{version}-%{git_ver}.tar.xz}

Name:           mate-file-manager-extensions
Summary:        Set of extensions for caja file manager
Version:        %{branch}.0
%if 0%{?rel_build}
Release:        alt1_1
%else
Release:        alt1_1
%endif
License:        GPLv2+
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R caja.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%%{oldname}-%%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{oldname}/snapshot/%{oldname}-%{commit}.tar.xz#/%{git_tar}}

Source1:        caja-share-setup-instructions
Source2:        caja-share-smb.conf.example

Patch0:         caja-extensions_use-beesu-command-for-gksu.patch

BuildRequires:  mate-common
BuildRequires:  mate-file-manager-devel
BuildRequires:  mate-desktop-devel
BuildRequires:  libdbus-glib-devel
BuildRequires:  gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel
BuildRequires:  libgupnp libgupnp-devel libgupnp-gir-devel
BuildRequires:  libdbus-glib-devel
BuildRequires:  gajim
Source44: import.info


%description
Extensions for the caja file-browser, open-terminal,
image-converter, sendto and share

%package common
Group: Graphical desktop/MATE
Summary:    Common files for %{oldname}
BuildArch:  noarch

%description common
%{summary}.

%package -n mate-file-manager-image-converter
Group: Graphical desktop/MATE
Summary:    MATE file manager image converter extension
Requires:   %{name}-common = %{version}-%{release}

%description -n mate-file-manager-image-converter
The caja-image-converter extension allows you to
re-size/rotate images from Caja.

%package -n mate-file-manager-open-terminal
Group: Graphical desktop/MATE
Summary:    Mate-file-manager extension for an open terminal shortcut
Requires:   %{name}-common = %{version}-%{release}

%description -n mate-file-manager-open-terminal
The caja-open-terminal extension provides a right-click "Open
Terminal" option for mate-file-manager users who prefer that option.

%package -n mate-file-manager-sendto
Group: Graphical desktop/MATE
Summary:    MATE file manager sendto
Requires:   %{name}-common = %{version}-%{release}

%description -n mate-file-manager-sendto
The caja-sendto extension provides 'send to' functionality
to the MATE Desktop file-manager, Caja.

%package -n mate-file-manager-sendto-devel
Group: Graphical desktop/MATE
Summary:    Development libraries and headers for caja-sendto
Requires:   %{name}-common = %{version}-%{release}
Requires:   mate-file-manager-sendto = %{version}-%{release}

%description -n mate-file-manager-sendto-devel
Development libraries and headers for caja-sendto

%package -n mate-file-manager-share
Group: Graphical desktop/MATE
Summary:    Easy sharing folder via Samba (CIFS protocol)
Requires:   %{name}-common = %{version}-%{release}
Requires:   samba

%description -n mate-file-manager-share
Caja extension designed for easier folders 
sharing via Samba (CIFS protocol) in *NIX systems.

%package -n mate-file-manager-beesu
Group: Graphical desktop/MATE
Summary:    MATE file manager beesu
Requires:   %{name}-common = %{version}-%{release}
Requires:   beesu

%description -n mate-file-manager-beesu
Caja beesu extension for open files as superuser

%package -n mate-file-manager-wallpaper
Group: Graphical desktop/MATE
Summary:    MATE file manager wallpaper
Requires:   %{name}-common = %{version}-%{release}

%description -n mate-file-manager-wallpaper
Caja wallpaper extension, allows to quickly set wallpaper.

%package -n caja-xattr-tags
Group: Graphical desktop/MATE
Summary:    MATE file manager xattr-tags
Requires:   %{name}-common = %{version}-%{release}

%description -n caja-xattr-tags
Caja xattr-tags extension, allows to quickly set xattr-tags.


%prep
%if 0%{?rel_build}
%setup -n %{oldname}-%{version} -q
%patch0 -p1
%else
%setup -q -n %{oldname}-%{commit}
%patch0 -p1
%endif

cp %{SOURCE1} SETUP

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# for snapshots
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}

%build
%configure \
     --disable-schemas-compile \
     --enable-image-converter  \
     --enable-open-terminal    \
     --enable-sendto           \
     --with-sendto-plugins=all \
     --enable-share            \
     --enable-gksu             \
     --enable-wallpaper        \
     --disable-static

%make_build V=1

%install
%{makeinstall_std}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

mkdir -p %{buildroot}/%{_sysconfdir}/samba/
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/samba/

%find_lang %{oldname} --with-gnome --all-name


%files common -f %{oldname}.lang
%doc AUTHORS COPYING README SETUP
%dir %{_datadir}/caja-extensions

%files -n mate-file-manager-image-converter
%{_libdir}/caja/extensions-2.0/libcaja-image-converter.so
%{_datadir}/caja-extensions/caja-image-resize.ui
%{_datadir}/caja-extensions/caja-image-rotate.ui
%{_datadir}/caja/extensions/libcaja-image-converter.caja-extension

%files -n mate-file-manager-open-terminal
%{_libdir}/caja/extensions-2.0/libcaja-open-terminal.so
%{_datadir}/glib-2.0/schemas/org.mate.caja-open-terminal.gschema.xml
%{_datadir}/caja/extensions/libcaja-open-terminal.caja-extension

%files -n mate-file-manager-sendto
%{_bindir}/caja-sendto
%dir %{_libdir}/caja-sendto
%dir %{_libdir}/caja-sendto/plugins
%{_libdir}/caja-sendto/plugins/libnstburn.so
%{_libdir}/caja-sendto/plugins/libnstemailclient.so
%{_libdir}/caja-sendto/plugins/libnstpidgin.so
%{_libdir}/caja-sendto/plugins/libnstremovable_devices.so
%{_libdir}/caja-sendto/plugins/libnstupnp.so
%{_libdir}/caja-sendto/plugins/libnstgajim.so
%{_libdir}/caja/extensions-2.0/libcaja-sendto.so
%{_datadir}/glib-2.0/schemas/org.mate.Caja.Sendto.gschema.xml
%{_datadir}/caja-extensions/caja-sendto.ui
%{_datadir}/caja/extensions/libcaja-sendto.caja-extension
%dir %{_datadir}/gtk-doc/html/caja-sendto
%{_datadir}/gtk-doc/html/caja-sendto/*
%{_mandir}/man1/caja-sendto.1*

%files -n mate-file-manager-sendto-devel
%dir %{_includedir}/caja-sendto
%{_includedir}/caja-sendto/caja-sendto-plugin.h
%{_libdir}/pkgconfig/caja-sendto.pc

%files -n mate-file-manager-share
%config %{_sysconfdir}/samba/caja-share-smb.conf.example
%{_libdir}/caja/extensions-2.0/libcaja-share.so
%{_datadir}/caja-extensions/share-dialog.ui
%{_datadir}/caja/extensions/libcaja-share.caja-extension

%files -n mate-file-manager-beesu
%{_libdir}/caja/extensions-2.0/libcaja-gksu.so
%{_datadir}/caja/extensions/libcaja-gksu.caja-extension

%files -n mate-file-manager-wallpaper
%{_libdir}/caja/extensions-2.0/libcaja-wallpaper.so
%{_datadir}/caja/extensions/libcaja-wallpaper.caja-extension

%files -n caja-xattr-tags
%{_libdir}/caja/extensions-2.0/libcaja-xattr-tags.so
%{_datadir}/caja/extensions/libcaja-xattr-tags.caja-extension


%changelog
* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

* Mon Oct 16 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.0-alt1_1
- new fc release

* Wed Sep 06 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.18.1-alt1_4
- new fc release

* Wed Oct 12 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.16.0-alt1_1
- update to mate 1.16

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.0-alt1_1
- new version

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.1-alt2_1
- fixed dependencies

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.1-alt1_1
- new version

* Wed Nov 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_1
- fixed requires ImageMagick -> /usr/bin/convert (closes: #30444)

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Sat Mar 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_0
- new fc release

