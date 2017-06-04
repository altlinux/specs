Name: vamp-aubio-plugins
Version: 0.5.1
Release: alt1
Summary: A set of Vamp plugins
License: GPLv2
Group: Sound
Url: https://aubio.org/vamp-aubio-plugins/ 
# git git://git.aubio.org/git/vamp-aubio-plugins 
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-make 
BuildPreReq: libvamp-devel libaubio4-devel gcc-c++ waf >= 1.9.12

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
%patch0 -p1

%build
waf configure --prefix=%prefix --libdir=%_libdir
waf build -vv

%install
waf install --destdir=%buildroot

%files
%doc README.md
%_libdir/vamp

%changelog
* Sun Jun 04 2017 Anton Farygin <rider@altlinux.ru> 0.5.1-alt1
- new version

* Sat Sep 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.hg20131231
- Snapshot from mercurial

* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus

