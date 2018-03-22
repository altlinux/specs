%def_with python3

Name: aimc
Version: r313
Release: alt1.svn20130718.2.1
Summary: A C++ Implementation of the Auditory Image Model
License: ASL v2.0
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/aimc
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://aimc.googlecode.com/svn/trunk/
Source: %name-%version.tar

BuildPreReq: gcc-c++ scons doxygen graphviz libcarfac-devel
BuildPreReq: libsndfile-devel libcairo-devel python-devel swig
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%description
The Auditory Image Model in C++. AIM-C is a real time version of the
auditory image model written in C that is suitable for batch processing
of sound databases.

%package -n python-module-%name
Summary: Python module of the Auditory Image Model
Group: Development/Python

%description -n python-module-%name
The Auditory Image Model in C++. AIM-C is a real time version of the
auditory image model written in C that is suitable for batch processing
of sound databases.

This package contains Python module of the Auditory Image Model.

%package -n python3-module-%name
Summary: Python module of the Auditory Image Model
Group: Development/Python3

%description -n python3-module-%name
The Auditory Image Model in C++. AIM-C is a real time version of the
auditory image model written in C that is suitable for batch processing
of sound databases.

This package contains Python module of the Auditory Image Model.

%prep
%setup

%if_with python3
cp -fR swig swig3
%endif

%build
scons -j %__nprocs
pushd swig
%python_build_debug
popd

%if_with python3
pushd swig3
%python3_build_debug
popd
%endif

#doxygen doc/Doxyfile

%install
install -d %buildroot%_bindir
install -m755 build/posix-release/AIMCopy %buildroot%_bindir/

pushd swig
%python_install
popd

%if_with python3
pushd swig3
%python3_install
popd
%endif

%files
%_bindir/*

%files -n python-module-%name
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%name
%python3_sitelibdir/*
%endif

#doc build/doxygen-html/*

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> r313-alt1.svn20130718.2.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> r313-alt1.svn20130718.2
- Fixed build with new toolchain

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> r313-alt1.svn20130718.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Sep 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r313-alt1.svn20130718
- Initial build for Sisyphus

