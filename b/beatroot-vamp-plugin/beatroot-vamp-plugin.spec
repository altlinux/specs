Name: beatroot-vamp-plugin
Version: 1.0
Release: alt1.hg20140625
Summary: BeatRoot Vamp Plugin
License: GPLv2
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/beatroot-vamp
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/beatroot-vamp
Source: %name-%version.tar

BuildPreReq: gcc-c++ libvamp-devel

%description
A Vamp Plugin implementation of the BeatRoot beat tracking system.

%prep
%setup

%build
%make_build -f Makefile.linux

%install
install -d %buildroot%_libdir/vamp
install -m644 beatroot-vamp.* %buildroot%_libdir/vamp/

%files
%doc CITATION README
%_libdir/vamp

%changelog
* Sat Sep 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20140625
- Initial build for Sisyphus

