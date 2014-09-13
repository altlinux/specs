Name: vamp-simple-cepstrum
Version: 1
Release: alt1.hg20140620
Summary: A simple Vamp plugin to calculate and return cepstrum values from DFT binst
License: BSD
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/vamp-simple-cepstrum
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/vamp-simple-cepstrum
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildPreReq: gcc-c++ libvamp-devel

%description
A simple Vamp plugin to calculate and return cepstrum values from DFT
bins. Useful as a preliminary tool for looking at cepstral data for
simple pitch or envelope methods.

%prep
%setup

%build
%make_build_ext -f Makefile.linux64

%install
install -d %buildroot%_libdir/vamp
install -m644 simple-cepstrum.* %buildroot%_libdir/vamp/

%files
%_libdir/vamp

%changelog
* Sat Sep 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1-alt1.hg20140620
- Initial build for Sisyphus

