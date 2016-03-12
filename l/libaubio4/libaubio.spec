%define origname aubio
%define sover 4
%def_enable python

Name: libaubio%sover
Version: 0.4.1
Release: alt2.git20140312
Summary: Aubio is a library for real time audio labelling
Url: http://www.aubio.org/
License: GPL
Group: System/Libraries

# git://git.aubio.org/git/aubio/
Source: %origname-%version.tar

# Automatically added by buildreq on Thu Nov 06 2008
BuildRequires: docbook-to-man jackit-devel libfftw3-devel libsamplerate-devel libsndfile-devel

BuildPreReq: python-modules waf libavcodec-devel libavformat-devel
BuildPreReq: libavresample-devel txt2man doxygen python-devel
BuildPreReq: libnumpy-devel

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
Conflicts: lib%origname-devel

%description devel
Aubio is a library for real time audio labelling. Its features include
segmenting a sound file before each of its attacks, performing pitch detection,
tapping the beat and producing midi streams from live audio.

This package contains the C headers and documentation required for
building programs based on %name.

%package examples
Group: Sound
Summary: Examples of %name
Conflicts: lib%origname-examples

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

%package devel-docs
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description devel-docs
Aubio is a library for real time audio labelling. Its features include
segmenting a sound file before each of its attacks, performing pitch detection,
tapping the beat and producing midi streams from live audio.

This package contains documentation for %name.

%prep
%setup -n %origname-%version

rm -fR waflib

%build
waf configure --prefix=%prefix --libdir=%_libdir
waf build -vv

%if_enabled python
pushd python
%add_optflags -fno-strict-aliasing
%python_build_debug
popd
%endif

%install
waf install --destdir=%buildroot

%if_enabled python
pushd python
%python_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

%files
%doc AUTHORS ChangeLog README.md doc/*
%_libdir/*.so.*

%if_enabled python
%files -n python-module-%origname
%doc python/README python/demos
%python_sitelibdir/*
%endif

%files devel
%_includedir/%origname
%_libdir/*.so
%_pkgconfigdir/%origname.pc

%files examples
%_bindir/*
#_datadir/sounds/%origname
%_man1dir/*

%files devel-docs
%_docdir/lib%origname-doc

%changelog
* Sat Mar 12 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt2.git20140312
- rebuilt with recent libav

* Sat Sep 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20140312
- Version 0.4.1

* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.2
- Fixed build

* Thu Jan 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1.1
- rebuild for set:provides by request of mithraen

* Thu Nov 06 2008 Ildar Mulyukov <ildar@altlinux.ru> 0.3.2-alt1
- 1st version for Sisyphus
- Python bindings are OFF
- build without Lash and PureData
