Name: vamp-pyin-plugin
Version: 1.0
Release: alt1.hg20140806
Summary: YIN algorithm for fundamental frequency (F0) estimation in monophonic audio
License: GPLv2
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/pyin
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/pyin
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildPreReq: gcc-c++ libvamp-devel boost-devel

%description
pYIN is a modification of the well-loved YIN algorithm for fundamental
frequency (F0) estimation in monophonic audio.

This project provides implementations of pYIN as well as the original
YIN method as part of the pYIN Vamp plugin. The plugin is written in C++
and can be used by any Vamp host such as Sonic Visualiser and Sonic
Annotator. The melody annotation program Tony uses the pYIN plugin.

%prep
%setup

%build
%make_build_ext -f Makefile.linux64

%install
install -d %buildroot%_libdir/vamp
install -m644 pyin.* %buildroot%_libdir/vamp/

%files
%doc README
%_libdir/vamp

%changelog
* Sun Sep 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20140806
- Initial build for Sisyphus

