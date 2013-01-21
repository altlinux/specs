%define _name webkit-efl
%define snapshot r127150

%set_verify_elf_method textrel=relaxed
%define _libexecdir %_prefix/libexec
%add_verify_elf_skiplist %_libexecdir/WebKitPluginProcess

# freetype/pango
%define font_backend freetype
# none/opengl/cairo/clutter
%define acceleration_backend opengl
%def_disable introspection
%def_enable geolocation
%def_disable web_audio
%def_disable media_stream
%def_enable spellcheck
%def_disable webkit2

%def_disable unstable_features

Name: lib%_name
Version: 1.9.90
Release: alt0.1

Summary: EFL Port of WebKit browser engine
License: %bsd %lgpl2plus
Group: System/Libraries
Url: http://trac.webkit.org/wiki/EFLWebKit

Source: http://packages.profusion.mobi/%_name/%_name-svn-%snapshot.tar.bz2
Patch: webkit-efl-alt-pkgconfig.patch

BuildPreReq: rpm-build-licenses

BuildRequires: libevas-devel libecore-devel libedje-devel libeeze-devel libefreet-devel libedbus-devel
BuildRequires: edje embryo_cc
BuildRequires: perl-Term-ANSIColor
BuildRequires: libharfbuzz-devel
BuildRequires: gstreamer-devel gst-plugins-devel

BuildRequires: cmake gcc-c++ libicu-devel bison perl-Switch zlib-devel
BuildRequires: flex >= 2.5.33
BuildRequires: gperf libjpeg-devel libpng-devel
BuildRequires: libxml2-devel >= 2.6
BuildRequires: libXt-devel
BuildRequires: libgtk+3-devel >= 3.4.0
BuildRequires: libgail3-devel >= 3.0
BuildRequires: libenchant-devel >= 0.22
BuildRequires: libsqlite3-devel >= 3.0
BuildRequires: libxslt-devel >= 1.1.7
#BuildRequires: gstreamer1.0-devel >= 0.11.90 gst-plugins1.0-devel >= 0.11.90
BuildRequires: librsvg-devel >= 2.2.0
BuildRequires: gtk-doc >= 1.10
BuildRequires: libsoup-devel >= 2.39.2
BuildRequires: libpango-devel >= 1.21.0 libcairo-devel >= 1.10 libcairo-gobject-devel
BuildRequires: libgio-devel >= 2.25.0
BuildRequires: python-modules-json
BuildRequires: ruby ruby-stdlibs

%if %font_backend == freetype
BuildRequires: fontconfig-devel >= 2.4 libfreetype-devel
%endif
%if %acceleration_backend == clutter
BuildRequires: libclutter-devel >= 1.8.2
BuildRequires: libclutter-gtk3-devel >= 1.0.2
%endif
%if %acceleration_backend == opengl
BuildRequires: libGL-devel libXcomposite-devel libXdamage-devel
%endif

%{?_enable_geolocation:BuildPreReq: libgeoclue-devel}
%{?_enable_spellcheck:BuildPreReq: libenchant-devel}
%{?_enable_media_stream:BuildPreReq: farstream0.2-devel}

%description
WebKit is an open source web browser engine.
The EFL port of WebKit is intended to provide a browser component
primarily for users of the portable EFL toolkit.

%package devel
Summary: Development files for WebKit EFL port
Group: Development/C++
Requires: %name = %version-%release

%description devel
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux. This package contains development headers.

%prep
%setup -n %_name-svn-%snapshot
%patch

%build
%ifarch %arm ppc
# Use linker flags to reduce memory consumption on low-mem architectures
%add_optflags -Wl,--no-keep-memory -Wl,--reduce-memory-overheads
%endif

# Build with -g1 on all platforms to avoid running into 4 GB ar format limit
# https://bugs.webkit.org/show_bug.cgi?id=91154
%define optflags_debug -g1

%cmake -DPORT=Efl
pushd BUILD
%make_build

%install
pushd BUILD
%makeinstall_std
popd

%find_lang ewebkit

%files -f ewebkit.lang
%_libdir/libewebkit.so.*
%_datadir/ewebkit-0/

%files devel
%_includedir/ewebkit-0/
%_libdir/libewebkit.so
%_pkgconfigdir/ewebkit.pc

%changelog
* Mon Jan 21 2013 Yuri N. Sedunov <aris@altlinux.org> 1.9.90-alt0.1
- first draft build for Sisyphus

