Name: gst-buzztrax
Version: 0.8.0
Release: alt1.git20140819
Summary: buzztrax extension for gstreamer
License: LGPLv2.1
Group: Sound
Url: http://buzztrax.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Buzztrax/gst-buzztrax.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ gstreamer1.0-devel libbml-devel buzzmachines
BuildPreReq: liborc-devel libfluidsynth-devel libcheck-devel
BuildPreReq: gst-plugins1.0-devel orc gtk-doc

%description
This module contains experimental code that extends gstreamer. The
library will never be ABI stable. if you are interested in any code
here, please help to mature it in order to get it into upstream. The
extensions are quite likely to be required to build a git version of
buzztrax.

%package devel
Summary: Development files of buzztrax extension for gstreamer
Group: Development/C++
Requires: %name = %EVR

%description devel
This module contains experimental code that extends gstreamer. The
library will never be ABI stable. if you are interested in any code
here, please help to mature it in order to get it into upstream. The
extensions are quite likely to be required to build a git version of
buzztrax.

This package contains development files of %name.

%package devel-docs
Summary: Documentation for buzztrax extension for gstreamer
Group: Development/Documentation
BuildArch: noarch

%description devel-docs
This module contains experimental code that extends gstreamer. The
library will never be ABI stable. if you are interested in any code
here, please help to mature it in order to get it into upstream. The
extensions are quite likely to be required to build a git version of
buzztrax.

This package contains development documentation for %name.

%prep
%setup

%build
./autogen.sh \
	--noconfigure \
	--debug \
	--prefix=%prefix
%configure \
	--enable-static=no \
	--enable-debug \
	--enable-orc \
	--enable-gtk-doc
%make_build

%install
%makeinstall_std

rm -f %buildroot%_libdir/gstreamer-1.0/*.la

%files
%doc AUTHORS ChangeLog NEWS *.md TODO
%_libdir/*.so.*
%_libdir/gstreamer-1.0/*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files devel-docs
%_datadir/gtk-doc

%changelog
* Sun Sep 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20140819
- Initial build for Sisyphus

