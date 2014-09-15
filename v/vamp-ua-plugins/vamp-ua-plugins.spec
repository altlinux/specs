Name: vamp-ua-plugins
Version: 1.0
Release: alt1
Summary: Vamp plugins developed in DRIMS project
License: GPL
Group: Sound
Url: http://grfia.dlsi.ua.es/cm/projects/drims/softwareVAMP.php
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-c++ libvamp-devel boost-devel libsndfile-devel
BuildPreReq: libfftw3-devel

%description
The UAPlugins set is a library of VAMP plugins developed in the DRIMS
project to perform onset detection and polyphonic transcription.

%prep
%setup

%build
%make_build -f Makefile.linux

%install
install -d %buildroot%_libdir/vamp
install -m644 ua-vamp-plugins.* %buildroot%_libdir/vamp/

%files
%doc *.txt
%_libdir/vamp

%changelog
* Mon Sep 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

