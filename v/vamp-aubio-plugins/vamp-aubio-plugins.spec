Name: vamp-aubio-plugins
Version: 0.4.0
Release: alt1
Summary: A set of Vamp plugins
License: GPLv2
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/vamp-aubio-plugins/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
#BuildPreReq: libvamp-devel libaubio-devel gcc-c++
BuildPreReq: libvamp-devel gcc-c++

%description
A set of Vamp plugins (http://www.sonicvisualiser.org/vamp.html) for
audio feature extraction using Paul Brossier's aubio
(http://aubio.piem.org/).

This set includes five plugins: Onset for onset detection, Pitch for
pitch tracking, Notes for combined onset and pitch, Tempo to estimate
and track beats based on onset locations, and Silence to find sections
of audio that are quieter than a given RMS signal level.  These
plugins compile into a single plugin library called vamp-aubio.so (the
file extension may vary depending on your platform).

%prep
%setup

%build
#add_optflags -I%_includedir/aubio
%make_build_ext

%install
install -d %buildroot%_libdir/vamp
install -m644 vamp-aubio.* vamp-plugin.* \
	%buildroot%_libdir/vamp/

%files
%doc README
%_libdir/vamp

%changelog
* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus

