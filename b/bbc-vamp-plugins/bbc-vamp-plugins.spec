Name: bbc-vamp-plugins
Version: 1.1
Release: alt1.git20140618
Summary: A collection of audio feature extraction algorithms in the Vamp plugin format
License: ASLv2.0
Group: Sound
Url: http://www.vamp-plugins.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bbcrd/bbc-vamp-plugins.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildPreReq: libvamp-devel gcc-c++ doxygen

%description
This is a collection of audio feature extraction algorithms written in
the Vamp plugin format by BBC Research and Development.

%prep
%setup

%build
%make_build -f Makefile.linux

pushd src
doxygen ../bbc-vamp-plugins.doxyfile
popd

%install
install -d %buildroot%_libdir/vamp
install -m644 bbc-vamp-plugins.so bbc-vamp-plugins.cat \
	bbc-vamp-plugins.n3 %buildroot%_libdir/vamp/

%files
%doc AUTHORS README.md src/doc/html
%_libdir/vamp

%changelog
* Sat Sep 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20140618
- Initial build for Sisyphus

