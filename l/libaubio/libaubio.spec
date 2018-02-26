%define origname aubio

Name: libaubio
Version: 0.3.2
Release: alt1.2
Summary: Aubio is a library for real time audio labelling
Url: http://www.aubio.org/
License: GPL
Group: System/Libraries
Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: http://www.aubio.org/pub/%origname-%version.tar
#.gz
Patch: libaubio-0.3.2-alt-DSO.patch

# Automatically added by buildreq on Thu Nov 06 2008
BuildRequires: docbook-to-man jackit-devel libfftw3-devel libsamplerate-devel libsndfile-devel

%description
Aubio is a library for real time audio labelling. Its features include
segmenting a sound file before each of its attacks, performing pitch detection,
tapping the beat and producing midi streams from live audio.

A few examples of applications are provided in examples/ and python/:
 - aubioonset output the onset detected,
 - aubionotes emits midi-like notes,
 - aubiocut is a python script that takes an input sound and creates one new
   sample at each detected onset or beat,
 - aubiopitch is a python script to extract pitch tracks from sound files.

%if_enabled python
%package -n python-module-%origname
Group: Development/Python
Summary: Python bindings to %name
Requires: %name = %version-%release

%description -n python-module-%origname
Aubio is a library for real time audio labelling. Its features include
segmenting a sound file before each of its attacks, performing pitch detection,
tapping the beat and producing midi streams from live audio.

This package contains the Python bindings required for
building Python programs based on %name.
%endif

%package devel
Group: Development/C
Summary: Development files of %name
Requires: %name = %version-%release

%description devel
Aubio is a library for real time audio labelling. Its features include
segmenting a sound file before each of its attacks, performing pitch detection,
tapping the beat and producing midi streams from live audio.

This package contains the C headers and documentation required for
building programs based on %name.

%package examples
Group: Sound
Summary: Examples of %name

%description examples
Aubio is a library for real time audio labelling. Its features include
segmenting a sound file before each of its attacks, performing pitch detection,
tapping the beat and producing midi streams from live audio.

This package contains
A few examples of applications are provided in examples/ and python/:
 - aubioonset output the onset detected,
 - aubionotes emits midi-like notes,
 - aubiocut is a python script that takes an input sound and creates one new
   sample at each detected onset or beat,
 - aubiopitch is a python script to extract pitch tracks from sound files.

aubioonset and aubionotes can work either off-line or online, outputting the
results on the console or playing a wood-block sound at each detected onset.
Both Python scripts can plot the results with Gnuplot.

%prep
%setup -q -n %origname-%version
%patch -p2

%build
%autoreconf
%configure
%make

%install
%makeinstall

%files
%doc AUTHORS ChangeLog README THANKS TODO VERSION
%_libdir/*.so.*

%if_enabled python
%files -n python-module-%origname
/usr/lib/python2.5/site-packages/%origname
%endif

%files devel
%_includedir/%origname
%_libdir/*.so
%_pkgconfigdir/%origname.pc

%files examples
%_bindir/*
%_datadir/sounds/%origname
%_man1dir/*

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.2
- Fixed build

* Thu Jan 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1.1
- rebuild for set:provides by request of mithraen

* Thu Nov 06 2008 Ildar Mulyukov <ildar@altlinux.ru> 0.3.2-alt1
- 1st version for Sisyphus
- Python bindings are OFF
- build without Lash and PureData
