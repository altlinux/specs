Name: qm-vamp-plugins
Version: 1.7
Release: alt1.hg20140806
Summary: QM Vamp Plugins
License: GPLv2
Group: Sound
Url: http://vamp-plugins.org/plugin-doc/qm-vamp-plugins.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/qm-vamp-plugins
Source: %name-%version.tar

BuildPreReq: gcc-c++ libvamp-devel libqm-dsp-devel liblapack-devel

%description
The QM Vamp Plugin set is a library of Vamp audio feature extraction
plugins developed at the Centre for Digital Music at Queen Mary,
University of London.

%prep
%setup

rm -fR build/linux/amd64

%build
%make_build -f build/linux/Makefile.linux64

%install
install -d %buildroot%_libdir/vamp
install -m644 qm-vamp-plugins.* %buildroot%_libdir/vamp/

%files
%doc README.txt
%_libdir/vamp

%changelog
* Mon Sep 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.hg20140806
- Initial build for Sisyphus

