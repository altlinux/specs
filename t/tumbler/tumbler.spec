%def_enable ffmpeg
%def_disable gstreamer

Name: tumbler
Version: 0.1.26
Release: alt1
Summary: A thumbnail D-Bus service
License: %gpl2plus, %lgpl2plus
Group: Graphical desktop/XFce
Url: http://git.xfce.org/xfce/tumbler/
Packager: XFCE Team <xfce@packages.altlinux.org>

Requires: lib%name = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: gtk-doc intltool libdbus-glib-devel libfreetype-devel libgio-devel libgtk+2-devel libjpeg-devel libpng-devel
BuildRequires: libpoppler-glib-devel libgsf-devel libopenraw-gnome-devel
%{?_enable_ffmpeg:BuildRequires: libffmpegthumbnailer-devel}
%{?_enable_gstreamer:BuildRequires: gstreamer1.0-devel}

%description
Tumbler is a D-Bus service for applications to request
thumbnails for various URI schemes and MIME types.
It is an implementation of the thumbnail management D-Bus
specification

%package -n lib%name
Summary: A D-bus thumbnailing framweork
Group: System/Libraries
License: %lgpl2plus

%description -n lib%name
Tumbler is a D-Bus service for applications to request
thumbnails for various URI schemes and MIME types

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
License: %lgpl2plus

%description -n lib%name-devel
Development files and headers for %name

%prep
%setup -q
%patch -p1

%build
%xfce4reconf
%configure \
	--libexecdir=%_prefix/libexec \
	%{?_disable_ffmpeg:--disable-ffmpeg-thumbnailer} \
	%{?_disable_gstreamer:--disable-gstreamer-thumbnailer} \
	--disable-static
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS TODO
%_prefix/libexec/%name-1
%_libdir/%name-1
%_datadir/dbus-1/services/*.service

%exclude %_libdir/%name-1/plugins/*.la

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/%name-1
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Tue Dec 11 2012 Mikhail Efremov <sem@altlinux.org> 0.1.26-alt1
- Fix URL.
- FIx License.
- Build ODF and RAW thumbnailer plugins.
- Use %%xfce4reconf.
- Updated to 0.1.26 (closes: #28211).

* Wed Mar 09 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.1.21-alt1
- 0.1.21
- fixed path to tumblerd in dbus service files (closes: #25206)

* Mon Nov 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Thu Nov 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Tue Jan 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.1-alt1
- initial release

