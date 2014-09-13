Name: cepstral-pitchtracker
Version: 1.0
Release: alt1.hg20140620
Summary: A straightforward cepstral pitch- and note-tracker Vamp plugin
License: MIT
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/cepstral-pitchtracker/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildPreReq: gcc-c++ libvamp-devel boost-devel

%description
A straightforward cepstral pitch- and note-tracker Vamp plugin, probably
most suited to tracking singing pitch.

%prep
%setup

%build
%make_build_ext -f Makefile.linux64

%install
install -d %buildroot%_libdir/vamp
install -m644 cepstral-pitchtracker.* %buildroot%_libdir/vamp/

%files
%doc README
%_libdir/vamp

%changelog
* Sat Sep 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20140620
- Snapshot from mercurial

* Sat Sep 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

