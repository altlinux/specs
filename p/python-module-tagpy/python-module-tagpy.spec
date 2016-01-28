%define rname tagpy

%def_with python3

Name: python-module-tagpy
Version: 2013.1
Release: alt2.git20130711.1.1.1

Summary: TagPy is a set of Python bindings for TagLib. 
License: GPL2+
Group: Development/Python
Url: http://mathema.tician.de/software/tagpy

# http://git.tiker.net/trees/tagpy.git
Source: %name-%version.tar

#Buildrequires: python-devel boost-python-devel libtag-devel gcc-c++
#Buildrequires: python-module-setuptools ctags
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel boost-python3-devel
#BuildPreReq: python3-module-setuptools
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: boost-python-headers elfutils libboost_python3-1.58.0 libstdc++-devel python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-dev
BuildRequires: boost-devel-headers boost-python-devel boost-python3-devel gcc-c++ libtag-devel python-module-setuptools python3-module-setuptools rpm-build-python3

%description
TagPy is a set of Python bindings for Scott Wheeler's TagLib.
It builds upon Boost.Python, a wrapper generation library which is part
of the Boost set of C++ libraries.

Just like TagLib, TagPy can:

  * read and write ID3 tags of version 1 and 2, with many supported
    frame types for version 2 (in MPEG Layer 2 and MPEG Layer 3, FLAC
    and MPC),
  * access Xiph Comments in Ogg Vorbis Files and Ogg Flac Files,
  * access APE tags in Musepack and MP3 files.

%package -n python3-module-%rname
Summary: TagPy is a set of Python bindings for TagLib
Group: Development/Python3

%description -n python3-module-%rname
TagPy is a set of Python bindings for Scott Wheeler's TagLib.
It builds upon Boost.Python, a wrapper generation library which is part
of the Boost set of C++ libraries.

Just like TagLib, TagPy can:

  * read and write ID3 tags of version 1 and 2, with many supported
    frame types for version 2 (in MPEG Layer 2 and MPEG Layer 3, FLAC
    and MPC),
  * access Xiph Comments in Ogg Vorbis Files and Ogg Flac Files,
  * access APE tags in Musepack and MP3 files.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fpermissive
export CC=g++
./configure.py \
	--taglib-inc-dir=%_includedir/taglib \
	--boost-python-libname=boost_python-mt
%python_build_debug

%if_with python3
pushd ../python3
python3 configure.py \
	--taglib-inc-dir=%_includedir/taglib \
	--boost-python-libname=boost_python3-mt
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files 
%doc README*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%rname
%doc README*
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2013.1-alt2.git20130711.1.1.1
- NMU: Use buildreq for BR.

* Wed May 20 2015 Sergey V Turchin <zerg@altlinux.org> 2013.1-alt2.git20130711.1.1
- rebuild with gcc5

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 2013.1-alt2.git20130711.1
- rebuild with boost 1.57.0

* Tue Aug 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1-alt2.git20130711
- Added module for Python 3

* Thu Sep 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1-alt1.git20130711
- Version 2013.1 (thnx iv@)

* Wed Sep 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.94.8-alt5.git20120103
- Fixed build

* Mon Feb 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.94.8-alt4.git20120103.1
- Rebuilt with Boost 1.53.0

* Sun Dec 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.94.8-alt4.git20120103
- New snapshot

* Fri Sep 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.94.8-alt3.4
- Rebuilt with Boost 1.51.0

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.94.8-alt3.3
- Rebuilt with Boost 1.49.0

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.94.8-alt3.2
- Rebuilt with Boost 1.48.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.94.8-alt3.1
- Rebuild with Python-2.7

* Mon Jul 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.94.8-alt3
- Rebuilt with Boost 1.47.0

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.94.8-alt2
- Rebuilt with Boost 1.46.1

* Tue Dec 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.94.8-alt1
- Version 0.94.8

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.94.7-alt2
- Rebuilt with python 2.6

* Tue Sep 08 2009 Alexey Morsov <swi@altlinux.ru> 0.94.7-alt1
- new version
- add python-module-setuptools into BuildRequires

* Mon May 11 2009 Alexey Morsov <swi@altlinux.ru> 0.94.5-alt2
- fix build with gcc4.4

* Tue Feb 26 2008 Alexey Morsov <swi@altlinux.ru> 0.94.5-alt1
- 0.95.5
- fix build with taglib 1.5

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 0.93-alt1.1
- Rebuilt with python-2.5.

* Thu Jan 17 2008 Alexey Morsov <swi@altlinux.ru> 0.93-alt1
- initial build for sisyphus


