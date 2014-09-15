Name: vamp-nnls-chroma
Version: 0.2.1
Release: alt1.hg2010806
Summary: Chordino and NNLS Chroma
License: GPLv2
Group: Sound
Url: http://www.isophonics.net/nnls-chroma
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/nnls-chroma
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildPreReq: gcc-c++ libvamp-devel boost-devel

%description
NNLS Chroma analyses a single channel of audio using frame-wise spectral
input from the Vamp host. The plugin was originally developed to extract
treble and bass chromagrams for subsequent use in chord extraction
methods. The spectrum is transformed to a log-frequency spectrum
(constant-Q) with three bins per semitone.

%package src
Summary: Sources of %name
Group: Development/C++
BuildArch: noarch

%description src
NNLS Chroma analyses a single channel of audio using frame-wise spectral
input from the Vamp host. The plugin was originally developed to extract
treble and bass chromagrams for subsequent use in chord extraction
methods. The spectrum is transformed to a log-frequency spectrum
(constant-Q) with three bins per semitone.

This package contains sources of %name.

%prep
%setup

mkdir -p ../src
cp * ../src/

%build
%make_build_ext -f Makefile.linux

%install
install -d %buildroot%_libdir/vamp
install -m644 nnls-chroma.* %buildroot%_libdir/vamp/

install -d %buildroot%_datadir/nnls-chroma
install -p -m644 ../src/* %buildroot%_datadir/nnls-chroma/

%files
%doc README *.txt
%_libdir/vamp

%files src
%_datadir/nnls-chroma

%changelog
* Mon Sep 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.hg2010806
- Snapshot from mercurial
- Added src subpackage

* Sat Sep 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

