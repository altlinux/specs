Name: nautilus-sound-converter
Version: 3.0.3
Release: alt0.1
Summary: Nautilus extension to convert audio files

Group: Graphical desktop/GNOME
License: %gpl2plus
Url: http://projects.gnome.org/nautilus-sound-converter/

Source: %name-%version.tar

BuildPreReq: rpm-build-licenses rpm-build-gnome gnome-common
BuildRequires: intltool >= 0.40.6
BuildRequires: libnautilus-devel >= 3.0.0
BuildRequires: libgio-devel >= 2.28.0
BuildRequires: libgtk+3-devel >= 3.0.0
BuildRequires: gstreamer1.0-devel >= 0.11.92 gst-plugins1.0-devel


# The bare minimum plugins needed.
Requires: gst-plugins-good1.0 gst-plugins-base1.0

%description
Adds a "Convert Sound File..." menu item to the context menu
of audio files. This opens a dialog where you can decide what audio
format you wish to convert the selected files to.

%prep
%setup

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static --enable-compile-warnings=no --enable-cxx-warnings=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc COPYING README NEWS
%nautilus_extdir/*.so
%_datadir/%name/
%_datadir/glib-2.0/schemas/*.xml
%_datadir/GConf/gsettings/*.convert

%exclude %nautilus_extdir/*.la

%changelog
* Tue Oct 01 2013 Alexey Shabalin <shaba@altlinux.ru> 3.0.3-alt0.1
- upstream snapshot of branch gst-1-0

* Mon Aug 06 2012 Alexey Shabalin <shaba@altlinux.ru> 3.0.2-alt1
- 3.0.2

* Wed Mar 14 2012 Alexey Shabalin <shaba@altlinux.ru> 3.0.1-alt1
- Initial build.
