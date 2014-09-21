Name: vamp-tempogram-plugin
Version: 0.0
Release: alt1.hg20140912
Summary: A Vamp plugin implementation of the tempogram and cyclic tempogram features
License: GPLv2
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/vamp-tempogram
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/vamp-tempogram
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildPreReq: libvamp-devel gcc-c++

%description
A Vamp plugin implementation of the tempogram and cyclic tempogram
features described in Grosche, Muller, and Kurth 2010, providing a
robust mid-level representation that encodes local tempo information.

%prep
%setup

%build
%make_build_ext -f Makefile.linux

%install
install -d %buildroot%_libdir/vamp
install -m644 tempogram.* %buildroot%_libdir/vamp/

%files
%doc CITATION README
%_libdir/vamp

%changelog
* Sun Sep 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0-alt1.hg20140912
- Initial build for Sisyphus

