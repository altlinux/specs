Name: vamp-chp-plugin
Version: 20140612
Release: alt1
Summary: Constrained Harmonic Peak plugin
License: MIT
Group: Sound
Url: https://code.soundsoftware.ac.uk/hg/chp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/chp
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildPreReq: gcc-c++ libvamp-devel

%description
This is a simple Vamp plugin that returns the peak frequency within a
given frequency range, from a harmonic product spectrum.

%prep
%setup

%build
%make_build_ext -f Makefile.linux

%install
install -d %buildroot%_libdir/vamp
install -m644 chp.so %buildroot%_libdir/vamp/

%files
%doc README
%_libdir/vamp

%changelog
* Sun Sep 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140612-alt1
- Initial build for Sisyphus

