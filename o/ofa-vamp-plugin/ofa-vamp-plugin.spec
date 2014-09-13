Name: ofa-vamp-plugin
Version: 20140619
Release: alt1
Summary: Vamp plugin for MusicIP fingerprinting and audio lookup using libofa
License: BSD
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/ofa-vamp-plugin
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/ofa-vamp-plugin
Source: %name-%version.tar

BuildPreReq: gcc-c++ libvamp-devel libofa-devel libcurl-devel
BuildPreReq: libexpat-devel

%description
This Vamp audio analysis plugin uses the OFA audio fingerprinting
library from MusicIP (http://www.musicip.com/) to calculate a
fingerprint from its audio input, and attempt to identify it as a
known track in the MusicDNS database.

%prep
%setup

%build
%make_build

%install
install -d %buildroot%_libdir/vamp
install -m644 ofa-vamp-plugin.* %buildroot%_libdir/vamp/

%files
%doc README
%_libdir/vamp

%changelog
* Sat Sep 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140619-alt1
- Initial build for Sisyphus

