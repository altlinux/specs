Name: vamp-onsetsds-plugin
Version: 0.2
Release: alt1.hg20140801
Summary: Vamp plugin of the OnsetsDS note onset detection library
License: GPLv2
Group: Sound
Url: http://sourceforge.net/p/vamp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libonsetsds-devel libvamp-devel gcc-c++

%description
This is a Vamp plugin of the OnsetsDS note onset detection library.

%prep
%setup

rm -fR onsetsds

%build
%make_build

%install
install -d %buildroot%_libdir/vamp
install -m644 vamp-onsetsds.* %buildroot%_libdir/vamp/

%files
%doc AUTHORS README
%_libdir/vamp

%changelog
* Sat Sep 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.hg20140801
- Initial build for Sisyphus

