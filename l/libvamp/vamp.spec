%def_disable static

Name: libvamp
Version: 2.5
Release: alt2.hg20140905

Summary: plugin system for plugins that extract descriptive information from audio data
License: %bsdstyle
Group: System/Libraries
Url: http://www.vamp-plugins.org/

Source0: %name-%version.tar

BuildPreReq: rpm-build-licenses

BuildRequires: gcc-c++ libsndfile-devel

%description
Vamp is an API for C and C++ plugins that process sampled audio data
to produce descriptive output (measurements or semantic observations).

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name
%endif

%package -n vamp-tools
Summary: Tools for use with VAMP
Group: Development/Other

%description -n vamp-tools
This package contains VAMP RDF template generator and a command-line host for
VAMP audio analysis plugins.

%package -n vamp-example-plugins
Summary: Example plugins for Vamp
Group: Sound

%description -n vamp-example-plugins
Example plugins implemented using the C++ classes.

These plugins are intended to be useful examples you can draw code
from in order to provide the basic shape and structure of a Vamp
plugin.  They are also intended to be correct and useful, if simple.

- ZeroCrossing calculates the positions and density of zero-crossing
points in an audio waveform.
- SpectralCentroid calculates the centre of gravity of the frequency
domain representation of each block of audio.
- PowerSpectrum calculates a power spectrum from the input audio.
- AmplitudeFollower is a simple implementation of SuperCollider's
amplitude-follower algorithm.
- PercussionOnsetDetector estimates the locations of percussive
onsets.
- FixedTempoEstimator calculates a single beats-per-minute value
which is an estimate of the tempo of a piece of music that is assumed
to be of fixed tempo, using autocorrelation of a frequency domain
energy rise metric.


%prep
%setup

%build
%autoreconf
%configure %{subst_enable static}
%make_build LIBS=-ldl

%install
%makeinstall_std libdir=%_libdir

%files
%_libdir/*.so.*
%doc CHANGELOG README README.compat

%files devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%dir %_includedir/vamp
%dir %_includedir/vamp-sdk
%dir %_includedir/vamp-hostsdk
%_includedir/*/*.h
%if_enabled static
%else
%exclude %_libdir/*.a
%endif

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%files -n vamp-tools
%_bindir/*

%files -n vamp-example-plugins
%_libdir/vamp/vamp-example-plugins*

%changelog
* Sun Sep 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt2.hg20140905
- Added path to plugins for x86_64

* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.hg20140905
- Version 2.5

* Tue Oct 16 2012 Paul Wolneykien <manowar@altlinux.ru> 2.4-alt1
- New version 2.4.

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2.1
- Rebuilt for soname set-versions

* Sat Aug 08 2009 Timur Batyrshin <erthad@altlinux.org> 2.0-alt2
- moved *.pc to devel

* Fri Aug 07 2009 Timur Batyrshin <erthad@altlinux.org> 2.0-alt1
- Initial build for sisyphus

