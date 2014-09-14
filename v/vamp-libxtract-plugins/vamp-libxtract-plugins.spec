Name: vamp-libxtract-plugins
Version: 0.6.6
Release: alt1.hg20140806
Summary: A Vamp plugin encapsulating many of the functions of LibXtract library
License: GPLv2
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/vamp-libxtract-plugins
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://code.soundsoftware.ac.uk/hg/vamp-libxtract-plugins
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildPreReq: gcc-c++ libxtract-devel libvamp-devel
BuildPreReq: libfftw3-devel

%description
A set of Vamp plugins (http://www.vamp-plugins.org/) for low-level
audio feature extraction using Jamie Bullock's libxtract
(http://sourceforge.net/projects/libxtract/).

%prep
%setup

%build
%make_build_ext

%install
install -d %buildroot%_libdir/vamp
install -m644 vamp-libxtract.* %buildroot%_libdir/vamp/

%files
%doc README STATUS
%_libdir/vamp

%changelog
* Sun Sep 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.6-alt1.hg20140806
- Initial build for Sisyphus

