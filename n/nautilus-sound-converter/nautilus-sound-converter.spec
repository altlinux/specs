Name: nautilus-sound-converter
Version: 3.0.1
Release: alt1
Summary: Nautilus extension to convert audio files

Group: Graphical desktop/GNOME
License: %gpl2plus
Url: http://projects.gnome.org/nautilus-sound-converter/

Source: %name-%version.tar

BuildPreReq: rpm-build-licenses rpm-build-gnome gnome-common
BuildRequires: intltool >= 0.40.6
BuildRequires: GConf libGConf-devel
BuildRequires: libnautilus-devel >= 3.0.0
BuildRequires: libgio-devel >= 2.28.0
BuildRequires: libgtk+3-devel >= 3.0.0
BuildRequires: libgnome-media-profiles-devel >= 2.11.91
BuildRequires: gstreamer-devel >= 0.10.20


# The bare minimum plugins needed.
Requires: gst-plugins-good gst-plugins-base

%description
Adds a "Convert Sound File..." menu item to the context menu
of audio files. This opens a dialog where you can decide what audio
format you wish to convert the selected files to.

%prep
%setup

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static --disable-schemas-install
%make_build

%install
%makeinstall_std
%find_lang %name

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi


%files -f %name.lang
%doc COPYING README NEWS
%nautilus_extdir/*.so
%_datadir/%name/
%_sysconfdir/gconf/schemas/%name.schemas

%exclude %nautilus_extdir/*.la

%changelog
* Wed Mar 14 2012 Alexey Shabalin <shaba@altlinux.ru> 3.0.1-alt1
- Initial build.
