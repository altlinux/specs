Name: buzztrax
Version: 0.8.0
Release: alt1.git20140805
Summary: Modular music composer for Linux
License: LGPLv2.1
Group: Sound
Url: http://buzztrax.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Buzztrax/buzztrax.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ libbml-devel gst-buzztrax-devel buzzmachines
BuildPreReq: intltool gtk-doc libclutter-gtk3-devel glib2-devel
BuildPreReq: gst-plugins1.0-devel gst-plugins-bad1.0-devel
BuildPreReq: libgsf-devel libxml2-devel libcheck-devel libgudev-devel
BuildPreReq: gtk-doc-mkpdf librarian desktop-file-utils
BuildPreReq: gstreamer1.0-utils

Requires: lib%name = %EVR %name-data = %EVR
Requires: gst-buzztrax buzzmachines gst-plugins-base1.0
Requires: gst-plugins-good1.0 gst-plugins-bad1.0 gstreamer1.0-utils

%description
Buzztrax is a music composer similar to tracker applications. It is
roughly modelled after the windows only, closed source application
called Buzz.

%package data
Summary: Data files of %name
Group: Sound
Requires: %name = %EVR
BuildArch: noarch

%description data
Buzztrax is a music composer similar to tracker applications. It is
roughly modelled after the windows only, closed source application
called Buzz.

This package contains data files of %name.

%package -n lib%name
Summary: Shared libraries of %name
Group: System/Libraries

%description -n lib%name
Buzztrax is a music composer similar to tracker applications. It is
roughly modelled after the windows only, closed source application
called Buzz.

This package contains shared libraries of %name.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Buzztrax is a music composer similar to tracker applications. It is
roughly modelled after the windows only, closed source application
called Buzz.

This package contains development files of %name.

%prep
%setup

%build
./autogen.sh \
	--noconfigure \
	--debug \
	--prefix=%prefix
%configure \
	--enable-gtk-doc \
	--enable-gtk-doc-html \
	--enable-static=no \
	--enable-debug \
	--enable-man \
	--with-html-dir=%_docdir
%make_build V=1

%install
%makeinstall_std

find %buildroot -type f -name '*.la' -exec rm -f '{}' +

for i in ChangeLog*; do
	gzip $i
done

install -d %buildroot%_docdir/%name-%version
install -p -m644 AUTHORS ChangeLog* NEWS* *.md TODO \
	%buildroot%_docdir/%name-%version/

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_man1dir/*
%_libexecdir/%name-songio
%_libdir/gstreamer-1.0/*

%files data
%_xdgmimedir/audio
%_xdgmimedir/packages
%_datadir/omf/*
%_iconsdir/hicolor/*/apps/*
%_iconsdir/gnome/*/apps/*
%_datadir/glib-2.0/schemas/*
%_datadir/%name
%_desktopdir/*
%_datadir/GConf/gsettings/*
%_datadir/appdata/*
%doc %_datadir/gnome/help/*
%doc %_docdir/%name-*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Sun Sep 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20140805
- Initial build for Sisyphus

