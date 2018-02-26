%define rname tagpy
Name: python-module-tagpy
Version: 0.94.8
Release: alt3.3

Summary: TagPy is a set of Python bindings for TagLib. 
License: GPL2+
Group: Development/Python
Url: http://mathema.tician.de/software/tagpy

Packager: Alexey Morsov <swi@altlinux.ru>
Source: %name-%version.tar

Buildrequires: python-devel boost-python-devel libtag-devel gcc-c++
Buildrequires: python-module-setuptools ctags

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

%prep
%setup
#subst 's|boost_python-gcc42-mt|boost_python-mt|g' setup.py

%build
export CC=g++
./configure \
	--taglib-inc-dir=%_includedir/taglib \
	--boost-python-libname=boost_python-mt
%make_build
#python setup.py build

%install
python setup.py install --root=%buildroot \
	--optimize=2 --record=INSTALLED_FILES


%files 
#-f INSTALLED_FILES
%python_sitelibdir/*


%changelog
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


