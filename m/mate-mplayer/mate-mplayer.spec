Group: Graphical desktop/MATE
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize gcc-c++ libgio-devel pkgconfig(dbus-1) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmlib) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(x11)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%bcond_without minimal

Name:           mate-mplayer
Version:        1.0.8
Release:        alt2_0
Summary:        An MPlayer GUI, a full-featured binary

License:        GPLv2+
URL:            https://github.com/NiceandGently/mate-mplayer
Source0:        https://github.com/downloads/NiceandGently/mate-mplayer/%{name}-%{version}.tar.xz

BuildRequires:  libalsa-devel
BuildRequires:  libdbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libgmtk-devel
BuildRequires:  libgtk+3-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgpod-devel
BuildRequires:  libmusicbrainz3-devel
BuildRequires:  libnotify-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  mate-file-manager-devel
BuildRequires:  libpulseaudio-devel
BuildRequires:  mate-common
#BuildRequires:  mate-conf-devel
BuildRequires:	desktop-file-utils

Requires:       mate-control-center
Requires:       fuse-gvfs
Requires:       mencoder
Requires:       mplayer
Requires:       %{name}-common = %{version}-%{release}

Provides:       %{name}-binary = %{version}-%{release}
Source44: import.info
Patch33: mate-mplayer-1.0.7-alt-no-mateconf.patch

%description
MATE MPlayer is a simple GUI for MPlayer. It is intended to be a nice tight
player and provide a simple and clean interface to MPlayer. MATE MPlayer has
a rich API that is exposed via DBus. Using DBus you can control a single or
multiple instances of MATE MPlayer from a single command.
This package provides a full-featured binary.


%package common
Group: Graphical desktop/MATE
Summary:        An MPlayer GUI, common files

%description common
MATE MPlayer is a simple GUI for MPlayer. It is intended to be a nice tight
player and provide a simple and clean interface to MPlayer. MATE MPlayer has
a rich API that is exposed via DBus. Using DBus you can control a single or
multiple instances of MATE MPlayer from a single command.
This package provides the common files.


%if %{with minimal}
%package minimal
Group: Graphical desktop/MATE
Summary:        An MPlayer GUI, a minimal version
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Provides:       %{name}-binary%{?_isa} = %{version}-%{release}

%description minimal
MATE MPlayer is a simple GUI for MPlayer. It is intended to be a nice tight
player and provide a simple and clean interface to MPlayer. MATE MPlayer has
a rich API that is exposed via DBus. Using DBus you can control a single or
multiple instances of MATE MPlayer from a single command.
This package provides a version with reduced requirements, targeted at users
who want browser plugin functionality only.
%endif


%package caja
Group: Graphical desktop/MATE
Summary:        An MPlayer GUI, caja extension
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description caja
MATE MPlayer is a simple GUI for MPlayer. It is intended to be a nice tight
player and provide a simple and clean interface to MPlayer. MATE MPlayer has
a rich API that is exposed via DBus. Using DBus you can control a single or
multiple instances of MATE MPlayer from a single command.
This package provides a caja extension, which shows properties of audio and
video files in the properties dialogue.


%prep
%setup -qcT
tar -xJf %{SOURCE0}
mv %{name}-%{version} generic
%if %{with minimal}
tar -xJf %{SOURCE0}
mv %{name}-%{version} minimal
%endif
pushd generic
%patch33 -p1
popd
pushd minimal
%patch33 -p1
popd

%build
pushd generic
#NOCONFIGURE=1 ./autogen.sh
%configure \
	--with-libnotify \
	--enable-gtk3 \
	--enable-caja \
	--with-dbus \
	--with-alsa \
	--with-pulseaudio \
	--with-libgpod \
	--with-libmusicbrainz3 \
	--with-gio \
	--disable-schemas-compile

make %{?_smp_mflags}
popd

%if %{with minimal}
pushd minimal
#NOCONFIGURE=1 ./autogen.sh
%configure --program-suffix=-minimal --without-gio --without-libnotify \
    --without-libgpod --without-libmusicbrainz3 --disable-caja --enable-gtk3 \
	--with-dbus --with-alsa --with-pulseaudio --disable-schemas-compile --without-libgda
make %{?_smp_mflags}
popd
%endif


%install
pushd generic
make install DESTDIR=$RPM_BUILD_ROOT
popd

%if %{with minimal}
pushd minimal
make install DESTDIR=$RPM_BUILD_ROOT
popd
%endif

%find_lang %{name}

#remove intrusive docs
rm -rf $RPM_BUILD_ROOT%{_docdir}/mate-mplayer

#kill the libtool archives
find $RPM_BUILD_ROOT -name *.la -exec rm -f {} \;

sed -i -e s,apps.gecko-mediaplayer.preferences,org.mate.gecko-mediaplayer.preferences, %buildroot%{_datadir}/glib-2.0/schemas/org.mate.gecko-mediaplayer.preferences.gschema.xml

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/mate-mplayer.desktop


%files
%{_bindir}/mate-mplayer
%{_datadir}/applications/mate-mplayer.desktop
%{_datadir}/mate-control-center/default-apps/mate-mplayer.xml


%files common -f %{name}.lang
%doc generic/COPYING generic/ChangeLog generic/README generic/DOCS/keyboard_shortcuts.txt generic/DOCS/tech/*
%{_datadir}/glib-2.0/schemas/org.mate.gecko-mediaplayer.preferences.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.mate-mplayer.preferences.*
%{_datadir}/icons/hicolor/*/apps/mate-mplayer.*
%{_mandir}/man1/mate-mplayer.1*


%if %{with minimal}
%files minimal
%{_bindir}/mate-mplayer-minimal
%endif


%files caja
%{_libdir}/caja/extensions-2.0/libmate-mplayer-properties-page.so*


%changelog
* Thu Mar 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_0
- quickfix for apps.gecko-mediaplayer.preferences
- TODO: proper fix

* Sat Mar 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_0
- new version (closes: 29887)

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt3_0101
- added mplayer dep (closes: 28929)

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt2_0101
dropped obsolete mate-conf BR:

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1_0101
- initial import

