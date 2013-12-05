%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec
%def_enable wayland
%def_enable fb
%def_enable multisense
%def_disable tslib

Name: efl
Version: 1.8.1
Release: alt1

Summary: Enlightenment Foundation Libraries
License: BSD/LGPLv2.1+
Group: System/Libraries
Url: http://www.enlightenment.org/

Source: http://download.enlightenment.org/rel/libs/%name/%name-%version.tar.bz2

%{?_enable_static:BuildPreReq: glibc-devel-static}
BuildRequires: gcc-c++ glibc-kernheaders glib2-devel libcheck-devel lcov doxygen
BuildRequires: libpng-devel libjpeg-devel libopenjpeg-devel libtiff-devel libgif-devel libwebp-devel
BuildRequires: fontconfig-devel libfreetype-devel libfribidi-devel libharfbuzz-devel
BuildRequires: libpulseaudio-devel libsndfile-devel libbullet-devel gst-plugins-devel zlib-devel
BuildRequires: liblua5-devel libssl-devel libcurl-devel libdbus-devel
BuildRequires: libmount-devel libblkid-devel
BuildRequires: libudev-devel systemd-devel libsystemd-journal-devel libsystemd-daemon-devel
BuildRequires: libX11-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXext-devel
BuildRequires: libXfixes-devel libXinerama-devel libXrandr-devel libXrender-devel libXScrnSaver-devel
BuildRequires: libXtst-devel libXcursor-devel libXp-devel libXi-devel
BuildRequires: libGL-devel
%{?_enable_tslib:BuildRequires: libts-devel}
%{?_enable_wayland:BuildRequires: libwayland-client-devel >= 1.3.0 libwayland-cursor-devel libxkbcommon-devel libwayland-egl-devel}

%description
EFL is a collection of libraries for handling many common tasks a
developer may have such as data structures, communication, rendering,
widgets and more.

There are many components inside EFL. They also build various things
like shared libraries, loadable plug-in modules and also binary
executables.

For more doumentation please see:

http://www.enlightenment.org/p.php?p=docs

%package -n %name-libs
Summary: Enlightenment Foundation Libraries
Group: System/Libraries
Conflicts: libeina < %version
#Obsoletes: libeina < %version
Provides: libeina = %version-%release
Conflicts: libeet < %version
#Obsoletes: libeet < %version
Provides: libeet = %version-%release
Conflicts: libevas < %version
#Obsoletes: libevas < %version
Provides: libevas = %version-%release
Conflicts: libecore < %version
#Obsoletes: libecore < %version
Provides: libecore = %version-%release
Conflicts:  libembryo < %version
#Obsoletes: libembryo < %version
Provides: libembryo = %version-%release
Conflicts:  libeio < %version
#Obsoletes: libeio < %version
Provides: libeio = %version-%release
Conflicts:  libefreet < %version
#Obsoletes: libefreet < %version
Provides: libefreet = %version-%release
Conflicts:  libethumb < %version
#Obsoletes: libethumb < %version
Provides: libethumb = %version-%release
Conflicts:  libemotion < %version
#Obsoletes: libemotion < %version
Provides: libemotion = %version-%release

Provides: libeo = %version-%release
Provides: libephysics = %version-%release

%description -n %name-libs
This package contains shared EFL libraries.

%package -n %name-libs-devel
Summary: Enlightenment Foundation Libraries development files
Group: Development/C
Requires: %name-libs = %version-%release
Conflicts: libeina-devel < %version
#Obsoletes: libeina-devel < %version
Provides: libeina-devel = %version-%release
Conflicts: libeet-devel < %version
#Obsoletes: libeet-devel < %version
Provides: libeet-devel = %version-%release
Conflicts: libevas-devel < %version
#Obsoletes: libevas-devel < %version
Provides: libevas-devel = %version-%release
Conflicts:  ibecore-devel < %version
#Obsoletes: libecore-devel < %version
Provides: libecore-devel = %version-%release
Conflicts: libembryo-devel < %version
#Obsoletes: libembryo-devel < %version
Provides: libembryo-devel = %version-%release
Conflicts: libeio-devel < %version
#Obsoletes: libeio-devel < %version
Provides: libeio-devel = %version-%release
Conflicts:  libefreet-devel < %version
#Obsoletes: libefreet-devel < %version
Provides: libefreet-devel = %version-%release
Conflicts:  libethumb-devel < %version
#Obsoletes: libethumb-devel < %version
Provides: libethumb-devel = %version-%release
Conflicts:  libemotion-devel < %version
#Obsoletes: libemotion-devel < %version
Provides: libemotion-devel = %version-%release

Provides: libeo-devel = %version-%release
Provides: libephysics-devel = %version-%release

%description -n %name-libs-devel
This package contains headers, development libraries, test programs and
documentation for EFL.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	--enable-xinput22 \
	--enable-systemd \
	--enable-image-loader-webp \
	--enable-harfbuzz \
	%{subst_enable multisense} \
	%{subst_enable tslib} \
	%{subst_enable wayland} \
	%{subst_enable fb}

%make_build
#%make doc

%install
%makeinstall_std
find %buildroot%_libdir -name "*.la" -delete

%find_lang %name

%files -n %name-libs -f %name.lang
%_bindir/edje_cc
%_bindir/edje_codegen
%_bindir/edje_decc
%_bindir/edje_external_inspector
%_bindir/edje_inspector
%_bindir/edje_pick
%_bindir/edje_player
%_bindir/edje_recc
%_bindir/edje_watch
%_bindir/eet
%_bindir/eeze_disk_ls
%_bindir/eeze_mount
%_bindir/eeze_scanner
%_bindir/eeze_umount
%_bindir/efreetd
%_bindir/eina-bench-cmp
%_bindir/ethumb
%_bindir/ethumbd
%_bindir/ethumbd_client
%_bindir/evas_cserve2_client
%_bindir/evas_cserve2_usage
%_libdir/*.so.*
%_libdir/ecore/
%_libdir/ecore_evas/
%_libdir/ecore_imf/
%_libdir/edje/
%_libdir/eeze/
%_libdir/efreet/
%_libdir/emotion/
%_libdir/ethumb/
%_libdir/ethumb_client/
%_libdir/evas/
%_datadir/dbus-1/services/org.enlightenment.Efreet.service
%_datadir/dbus-1/services/org.enlightenment.Ethumb.service
%_datadir/ecore/
%_datadir/ecore_imf/
%_datadir/edje/
%_datadir/eeze/
%_datadir/efreet/
%_datadir/embryo/
%_datadir/emotion/
%_datadir/eo/
%exclude %_datadir/eo/gdb/eo_gdb.py
%exclude %_datadir/eo/gdb/eo_gdb.py
%_datadir/ethumb/
%_datadir/ethumb_client/
%_datadir/evas/
%_datadir/mime/packages/edje.xml
%doc AUTHORS README NEWS COMPLIANCE

%files -n %name-libs-devel
%_bindir/eldbus-codegen
%_bindir/evas_cserve2_debug
%_bindir/evas_cserve2_shm_debug
%_bindir/embryo_cc
%_includedir/*
%_libdir/cmake/*
%_libdir/*.so
%_libdir/pkgconfig/ecore-audio.pc
%_libdir/pkgconfig/ecore-con.pc
%_libdir/pkgconfig/ecore-evas.pc
%_libdir/pkgconfig/ecore-fb.pc
%_libdir/pkgconfig/ecore-file.pc
%_libdir/pkgconfig/ecore-imf-evas.pc
%_libdir/pkgconfig/ecore-imf.pc
%_libdir/pkgconfig/ecore-input-evas.pc
%_libdir/pkgconfig/ecore-input.pc
%_libdir/pkgconfig/ecore-ipc.pc
%_libdir/pkgconfig/ecore-wayland.pc
%_libdir/pkgconfig/ecore-x.pc
%_libdir/pkgconfig/ecore.pc
%_libdir/pkgconfig/edje.pc
%_libdir/pkgconfig/eet.pc
%_libdir/pkgconfig/eeze.pc
%_libdir/pkgconfig/efreet-mime.pc
%_libdir/pkgconfig/efreet-trash.pc
%_libdir/pkgconfig/efreet.pc
%_libdir/pkgconfig/eina.pc
%_libdir/pkgconfig/eio.pc
%_libdir/pkgconfig/eldbus.pc
%_libdir/pkgconfig/embryo.pc
%_libdir/pkgconfig/emotion.pc
%_libdir/pkgconfig/eo.pc
%_libdir/pkgconfig/ephysics.pc
%_libdir/pkgconfig/ethumb.pc
%_libdir/pkgconfig/ethumb_client.pc
%_libdir/pkgconfig/evas-fb.pc
%_libdir/pkgconfig/evas-opengl-x11.pc
%_libdir/pkgconfig/evas-software-buffer.pc
%_libdir/pkgconfig/evas-software-x11.pc
%_libdir/pkgconfig/evas-wayland-shm.pc
%_libdir/pkgconfig/evas.pc
%_datadir/gdb/
%exclude %_datadir/gdb/auto-load/*/*/libeo.so.*-gdb.py
%exclude %_datadir/eo/gdb/eo_gdb.py


%changelog
* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- first build for Sisyphus

