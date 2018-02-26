%def_disable xine

Name: emotion
Version: 1.0.1
Release: alt1

Summary: Widget set based on the Enlightenment Foundation Libraries
Group: Graphical desktop/Enlightenment
License: LGPLv2+
Url: http://www.enlightenment.org

Source: http://download.enlightenment.org/releases/%name-%version.tar.bz2
Patch: emotion-1.0.0-link.patch

BuildRequires: doxygen edje libecore-devel libedje-devel
BuildRequires: libeet-devel >= 1.6.0 libeeze-devel libeio-devel
BuildRequires: libvlc-devel gst-plugins-devel
%{?_enable_xine:BuildRequires: libxine-devel}
BuildRequires: chrpath

%description
Emotion is a library to easily integrate media playback into EFL
applications, it will take care of using Ecore's main loop and video
display is done using Evas.

%package -n lib%name
Summary: Emotion Library
Group: System/Libraries

%description -n lib%name
Emotion is a library to easily integrate media playback into EFL
applications, it will take care of using Ecore's main loop and video
display is done using Evas.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use Emotion library.

%prep
%setup
%patch -b .link

%build
%autoreconf
%configure --disable-static \
	%{subst_enable xine}

%make_build

%install
%makeinstall_std

%files -n lib%name
%_libdir/lib%name.so.*
%_libdir/edje/modules/%name/*/*.so
%dir %_libdir/%name
%_libdir/%name/em_generic.so
%_libdir/%name/gstreamer.so
%dir %_libdir/%name/utils
%_libdir/%name/utils/em_generic_vlc
%{?_enable_xine:%_libdir/%name/modules/xine.so}
%exclude %_libdir/%name/*.la
%exclude %_libdir/edje/modules/%name/*/*.la
%_datadir/%name/
%doc COPYING*

%files -n lib%name-devel
%_bindir/%{name}_test
%_includedir/%{name}*/
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Mon Jun 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon May 21 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt2
- fixed build

* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.0.65643-alt2
- used %%autoreconf to fix RPATH problem

* Tue Dec 06 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.0.65643-alt1
- first build for Sisyphus

