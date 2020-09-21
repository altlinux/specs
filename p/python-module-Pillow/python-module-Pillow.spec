%define __python2 %_bindir/python2
%define oname Pillow

%def_without python3
# bootstrap building docs (pillow is required by docutils, docutils are
#  required by sphinx; pillow build-requires sphinx)
%def_without docs
%def_enable check

%global py2_libbuilddir %(python -c 'import sys; import sysconfig; print("lib.{p}-{v[0]}.{v[1]}".format(p=sysconfig.get_platform(), v=sys.version_info))')
%global py3_libbuilddir %(python3 -c 'import sys; import sysconfig; print("lib.{p}-{v[0]}.{v[1]}".format(p=sysconfig.get_platform(), v=sys.version_info))')

Name: python-module-%oname
Version: 6.2.0
Release: alt2

Summary: Python image processing library

# License: see http://www.pythonware.com/products/pil/license.htm
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Pillow/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/python-pillow/Pillow.git
#Source-url: https://pypi.io/packages/source/P/%oname/%oname-%version.tar.gz
# Source-url: https://github.com/python-pillow/Pillow/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires: rpm-build-intro >= 2.1.4

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose python-module-html5lib python-module-pytest
BuildPreReq: python-modules-tkinter

BuildRequires: tk-devel zlib-devel libwebp-devel libopenjpeg2.0-devel
BuildRequires: libfreetype-devel libjpeg-devel liblcms2-devel libtiff-devel libwebp-devel libimagequant-devel

%if_with python3
BuildRequires(pre): rpm-build-python3 >= 0.1.9.2-alt1
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose python3-module-html5lib python3-module-jinja2-tests python3-module-pytest
BuildPreReq: python3-modules-tkinter
%endif

Conflicts: python-module-imaging < %EVR
Obsoletes: python-module-imaging < %EVR
Provides: python-module-imaging = %EVR


%if_with docs
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python-module-docutils python3-module-sphinx python3-module-sphinx-better-theme
BuildRequires: python3-module-sphinx_rtd_theme python3-module-olefile
%endif

%description
Python image processing library, fork of the Python Imaging Library (PIL)

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

%package devel
Summary: Development files for %oname
Group: Development/Python
BuildArch: noarch
Requires: %name = %EVR

%description devel
Python image processing library, fork of the Python Imaging Library (PIL)

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

This package contains development files for %oname.

%package -n python3-module-%oname-pickles
Summary: Pickles for %oname
Group: Development/Python3

%description -n python3-module-%oname-pickles
Python image processing library, fork of the Python Imaging Library (PIL)

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Python image processing library, fork of the Python Imaging Library (PIL)

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Python Imaging Library (Fork)
Group: Development/Python3

%description -n python3-module-%oname
Python image processing library, fork of the Python Imaging Library (PIL)

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

%package -n python3-module-%oname-devel
Summary: Development files for %oname
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-devel
Python image processing library, fork of the Python Imaging Library (PIL)

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

This package contains development files for %oname.

%prep
%setup
%python3_dirsetup

%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv docs/
%endif

%build
%python_build_debug

%python3_dirbuild_debug

%if_with docs
export LC_ALL=en_US.UTF-8
PYTHONPATH=$PWD/../python3/build/%py3_libbuilddir make -C docs pickle html BUILDDIR=_build_py3 SPHINXBUILD=%_bindir/py3_sphinx-build
rm -f docs/_build_py3/html/.buildinfo
%endif

%install
export LC_ALL=en_US.UTF-8
%if_with python3
pushd ../python3
%python3_install
install -d %buildroot%__python3_includedir
install -p -m644 src/libImaging/*.h \
	%buildroot%__python3_includedir
popd
%endif

%python_install
install -d %buildroot%python_includedir
install -p -m644 src/libImaging/*.h %buildroot%python_includedir/

install -d %buildroot%python3_sitelibdir/%oname/
%if_with python3
cp -fR docs/_build_py3/pickle %buildroot%python3_sitelibdir/PIL/pickle
%endif

%check
# Check Python 2 modules
#ln -s $PWD/Images $PWD/build/%py2_libbuilddir/Images
cp -R $PWD/Tests $PWD/build/%py2_libbuilddir/Tests
cp -R $PWD/selftest.py $PWD/build/%py2_libbuilddir/selftest.py
pushd build/%py2_libbuilddir
PYTHONPATH=$PWD %{__python2} selftest.py
popd

%if_with python3
# Check Python 3 modules
#ln -s $PWD/Images $PWD/build/%py3_libbuilddir/Images
cp -R $PWD/Tests $PWD/../python3/build/%py3_libbuilddir/Tests
cp -R $PWD/selftest.py $PWD/../python3/build/%py3_libbuilddir/selftest.py
pushd ../python3/build/%py3_libbuilddir
PYTHONPATH=$PWD %{__python3} selftest.py
popd
%endif

%files
%doc *.rst docs/COPYING LICENSE *.md
%python_sitelibdir/PIL/
%python_sitelibdir/%oname-*.egg-info/

%files devel
%python_includedir/*

%if_with docs
%files -n python3-module-%oname-pickles
%python3_sitelibdir/PIL/pickle/

%files docs
%doc docs/_build_py3/html/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/COPYING LICENSE *.md
%python3_sitelibdir/PIL/
%python3_sitelibdir/%oname-*.egg-info/
%if_with docs
%exclude %python3_sitelibdir/PIL/pickle/
%endif

%files -n python3-module-%oname-devel
# Here, we re-use the same path as in the build system
%__python3_includedir/*
%endif

%changelog
* Mon Sep 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.2.0-alt2
- rebuilt without python3

* Mon Oct 07 2019 Vitaly Lipatov <lav@altlinux.ru> 6.2.0-alt1
- new version 6.2.0 (with rpmrb script)

* Sun Jul 01 2018 Vitaly Lipatov <lav@altlinux.ru> 5.2.0-alt1
- new version 5.2.0 (with rpmrb script) with check enabled
- drop PIL.pth, it was an illusion to support import Image
- rewrite install, check and make docs (thanks, Fedora)
- add openjpeg support

* Wed Apr 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.0-alt2
- (NMU) Rebuilt with python-3.6.4.

* Tue Apr 24 2018 Vitaly Lipatov <lav@altlinux.ru> 5.1.0-alt1
- new version 5.1.0 (with rpmrb script)
- build with libeimagequant support

* Wed Oct 04 2017 Vitaly Lipatov <lav@altlinux.ru> 4.3.0-alt1
- switch to build from tarball
- new version (4.3.0) with rpmgs script

* Fri Mar 24 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.0-alt2.dev0.git20150806.1.qa1
- NMU: rebuilt against Tcl/Tk 8.6.

* Mon May 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.0-alt2.dev0.git20150806.1
- BR: sphinx_rtd_theme (the theme is optional since sphinx-1.4.1).

* Sat Apr  2 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.0-alt2.dev0.git20150806
- (.spec) use the new correct %%__python3_includedir.

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 3.0.0-alt1.dev0.git20150806.1
- NMU: Use buildreq for BR.

* Thu Aug 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.dev0.git20150806
- Version 3.0.0.dev0

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.git20150302
- New snapshot
- Added devel package

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.git20150225
- Snapshot from git

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1
- Version 2.7.0

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt3
- Added PIL.pth into python3-module-%oname

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt2
- Provides python-module-imaging

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1
- Initial build for Sisyphus

