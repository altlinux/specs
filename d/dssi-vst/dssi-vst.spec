Name: dssi-vst
Version: 0.9
Release: alt1.git20140805
Summary: DSSI plugin wrapper for VST plugins
License: GPLv2
Group: Sound
Url: http://breakfastquay.com/dssi-vst/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/falkTX/dssi-vst.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ dssi-devel libjack-devel libwine-devel
BuildPreReq: liblo-devel dssi ladspa_sdk libalsa-devel zlib-devel

%description
Originally developed at Breakfast Quay but now grown up and moved away,
dssi-vst is an adapter that allows users of Linux audio software to take
VST and VSTi audio effects and instrument plugins compiled for Windows,
and load them into native LADSPA or DSSI plugin hosts.

%package -n ladspa-%name
Summary: LADSPA plugin wrapper for VST plugins
Group: Sound

%description -n ladspa-%name
Originally developed at Breakfast Quay but now grown up and moved away,
dssi-vst is an adapter that allows users of Linux audio software to take
VST and VSTi audio effects and instrument plugins compiled for Windows,
and load them into native LADSPA or DSSI plugin hosts.

This package contains LADSPA plugin wrapper for VST plugins.

%prep
%setup

%build
%make_build \
	PREFIX=%prefix \
	_LADSPA_DIR=%_ladspa_path \
	_DSSI_DIR=%_libdir/dssi

%install
%makeinstall_std \
	PREFIX=%prefix \
	_LADSPA_DIR=%_ladspa_path \
	_DSSI_DIR=%_libdir/dssi

%files
%doc COPYING README
%_bindir/*
%_libdir/dssi/*

%files -n ladspa-%name
%_ladspa_path/*

%changelog
* Wed Sep 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.git20140805
- Initial build for Sisyphus

