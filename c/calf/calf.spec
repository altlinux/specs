# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libexpat-devel pkgconfig(cairo) pkgconfig(gtk+-2.0) pkgconfig(libglade-2.0) pkgconfig(lv2core)
# END SourceDeps(oneline)
Name:		calf
Version:	0.0.18.6
Release:	alt1_8
Summary:	Audio plugins pack
Group:		Sound
# The jackhost code is GPLv2+ 
# The GUI code is LGPLv2+
# ladspa plugin is LGPLv2+
# lv2 plugin is GPLv2+ and LGPLv2+ and Public Domain
# dssi plugin is LGPLv2+
License:	GPLv2+ and LGPLv2+
URL:		http://calf.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}-dssi.desktop
# LV2: use correct LADSPA URIs
# http://repo.or.cz/w/calf.git/commit/fb526c311c4ab401986b7d559d32732d6acd7cde
Patch0:		%{name}.git-fb526c311c4ab401986b7d559d32732d6acd7cde.patch
# Fix gcc-4.7 compilation error. Sent upstream via email
Patch1:		calf-gcc47.patch

BuildRequires:	desktop-file-utils
BuildRequires:	dssi-devel
BuildRequires:	expat-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk2-devel
BuildRequires:	libjack-devel
BuildRequires:	ladspa_sdk
BuildRequires:	liblash-devel
BuildRequires:	libglade2-devel
BuildRequires:	lv2core-devel

%global common_desc \
The Calf project aims at providing a set of high quality open source audio\
plugins for musicians. All the included plugins are designed to be used with\
multitrack software, as software replacement for instruments and guitar stomp\
boxes.
Source44: import.info

%description
%common_desc

The plugins are available in LV2, DSSI, Standalone JACK and LADSPA formats.
This package contains the common files and the Standalone JACK plugin.

%package -n ladspa-%{name}-plugins
Summary:	Calf plugins in LADSPA format
Group:		Sound
License:	LGPLv2+
Requires:	%{name} = %{version}-%{release}
Requires:	ladspa_sdk

%description -n ladspa-%{name}-plugins
%common_desc

This package contains only LADSPA effect plugins (no GUI), with LRDF.

%package -n lv2-%{name}-plugins
Summary:	Calf plugins in LV2 format
Group:		Sound
License:	GPLv2+ and LGPLv2+ and Public Domain
Requires:	%{name} = %{version}-%{release}
Requires:	lv2core

%description -n lv2-%{name}-plugins
%common_desc

This package contains LV2 synthesizers and effects, MIDI I/O and GUI
extensions.

%package -n dssi-%{name}-plugins
Summary:	Calf plugins in DSSI format
Group:		Sound
License:	LGPLv2+
Requires:	%{name} = %{version}-%{release}
Requires:	dssi

%description -n dssi-%{name}-plugins
%common_desc

This package contains DSSI synthesizers and effects, also GUI extensions.

%prep
%setup -q
%patch0 -p1 -b .ladspa_uri
%patch1 -p1 -b .gcc47

# Make sure that optflags are not overriden.
sed -i 's|-O3||' configure

%build
# Add GenericName to the .desktop file
echo "GenericName= Audio Effects" >> %{name}.desktop.in
%configure \
	--with-ladspa-dir=%{_libdir}/ladspa/ \
	--with-dssi-dir=%{_libdir}/dssi/ \
	--with-lv2-dir=%{_libdir}/lv2 

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# The Jack host
desktop-file-install \
	--remove-category="Application" \
	--add-category="X-Synthesis" \
	--dir=$RPM_BUILD_ROOT%{_datadir}/applications \
	$RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

# The DSSI host
ln -s jack-dssi-host $RPM_BUILD_ROOT%{_bindir}/%{name}
desktop-file-install \
	--dir=$RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}

# We don't need this file:
rm -f $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/icon-theme.cache

%files
%doc AUTHORS ChangeLog COPYING* README TODO
%{_bindir}/%{name}jackhost
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}*
%{_mandir}/man7/%{name}*

%files -n ladspa-%{name}-plugins
%{_libdir}/ladspa/%{name}.so
%{_datadir}/ladspa/rdf/%{name}.rdf

%files -n lv2-%{name}-plugins
%{_libdir}/lv2/%{name}.lv2/

%files -n dssi-%{name}-plugins
%{_bindir}/%{name}
%{_datadir}/applications/%{name}-dssi.desktop
%{_libdir}/dssi/%{name}/
%{_libdir}/dssi/%{name}.so

%changelog
* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.18.6-alt1_8
- import

