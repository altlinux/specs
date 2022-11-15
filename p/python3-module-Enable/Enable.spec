%define _unpackaged_files_terminate_build 1

%def_with docs

%define oname Enable
Name: python3-module-%oname
Version: 5.3.1
Release: alt1.1

Summary: Drawing and interaction packages

Group: Development/Python3
License: BSD and GPLv2
URL: https://github.com/enthought/enable

Source: %name-%version.tar

Patch: use_system_freetype.patch

BuildRequires: gcc-c++ swig
BuildRequires: libX11-devel libGL-devel libGLU-devel
BuildRequires: libfreetype-devel
BuildRequires: libopenblas-devel liblapack-devel
BuildRequires(pre): rpm-build-python3
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-Cython

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-traits
BuildRequires: python3-module-sphinx-copybutton
%endif

%add_python3_req_skip macport mac_context hypothesis
%add_python3_req_skip wx.aui wx.glcanvas wx.grid wx.py.shell

%add_python3_self_prov_path %buildroot%python3_sitelibdir/kiva

%description
The Enable project provides two related multi-platform packages for
drawing GUI objects. The Enable package is a multi-platform object
drawing library built on top of Kiva. The core of Enable is a
container/component model for drawing and event notification. Kiva is a
multi-platform DisplayPDF vector drawing engine that supports multiple
output backends, including Windows, GTK, and Macintosh native windowing
systems, a variety of raster image formats, PDF, and Postscript.

%if_with docs
%package doc
Summary: Documentation for Enable project
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %EVR

%description doc
The Enable project provides two related multi-platform packages for
drawing GUI objects. The Enable package is a multi-platform object
drawing library built on top of Kiva. The core of Enable is a
container/component model for drawing and event notification. Kiva is a
multi-platform DisplayPDF vector drawing engine that supports multiple
output backends, including Windows, GTK, and Macintosh native windowing
systems, a variety of raster image formats, PDF, and Postscript.

This package contains development documentation for Enable project.

%package pickles
Summary: Pickles for Enable project
Group: Development/Python3

%description pickles
The Enable project provides two related multi-platform packages for
drawing GUI objects. The Enable package is a multi-platform object
drawing library built on top of Kiva. The core of Enable is a
container/component model for drawing and event notification. Kiva is a
multi-platform DisplayPDF vector drawing engine that supports multiple
output backends, including Windows, GTK, and Macintosh native windowing
systems, a variety of raster image formats, PDF, and Postscript.

This package contains pickles for Enable project.
%endif

%prep
%setup
%patch -p1

#remove bundled freetype2 library
rm -rf kiva/agg/freetype2

%build
%add_optflags -fno-strict-aliasing

%python3_build

%if_with docs
# generate html docs
sphinx-build-3 docs/source html
sphinx-build-3 docs/source pickles
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%python3_install

rm -fR %buildroot%python3_sitelibdir/enthought/kiva/mac
rm -f $(find %buildroot%python3_sitelibdir -name '*mac*.py*')

# remove shebangs from files
find %buildroot%python3_sitelibdir -type f -name '*.py' -exec \
    sed -i -e '1!b' -e '/^\#\!\/usr\/bin\/env python$/d' '{}' +

%if_with docs
cp -fR pickles %buildroot%python3_sitelibdir/enable/
%endif

%check
# tests need display

%files
%doc image_LICENSE*.txt LICENSE.txt
%doc *.rst CHANGES.txt
%python3_sitelibdir/*
%if_with docs
%exclude %python3_sitelibdir/enable/pickles

%files doc
%doc docs

%files pickles
%dir %python3_sitelibdir/enable
%python3_sitelibdir/enable/pickles
%endif

%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 5.3.1-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Thu Sep 15 2022 Grigory Ustinov <grenka@altlinux.org> 5.3.1-alt1
- Automatically updated to 5.3.1.

* Fri May 20 2022 Grigory Ustinov <grenka@altlinux.org> 5.3.0-alt1
- Automatically updated to 5.3.0.
- Build with system freetype.
- Build with docs.

* Thu Jan 13 2022 Grigory Ustinov <grenka@altlinux.org> 5.2.1-alt1
- Build new version.
- Build with bundled freetype (temporary for python3.10).

* Thu Jun 03 2021 Grigory Ustinov <grenka@altlinux.org> 4.8.1-alt3
- Drop python2 support.

* Wed Aug 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.8.1-alt2
- Updated build dependencies.

* Wed Feb 26 2020 Grigory Ustinov <grenka@altlinux.org> 4.8.1-alt1
- Build new version for python3.8.

* Sun Feb 02 2020 Vitaly Lipatov <lav@altlinux.ru> 4.8.0-alt3
- NMU: build without python2 modules

* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 4.8.0-alt2
- Build with system freetype (Closes: #36385).

* Fri Jul 19 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 4.8.0-alt1
- Updated to upstream version 4.8.0.
- Built modules for python-3.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 4.6.1-alt1
- automated PyPI update

* Tue Feb 09 2016 Sergey Alembekov <rt@altlinux.ru> 4.6.0-alt3.git20151207
- skip hypothesys requirement for -tests subpackage

* Mon Dec 07 2015 Sergey Alembekov <rt@altlinux.ru> 4.6.0-alt2.git20151207
- update to current upstream branch

* Sun May 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.0-alt1.git20150423
- Version 4.6.0

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20141003
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt1.git20140501
- Version 4.5.0

* Sun Oct 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20131017
- New snapshot

* Mon Jun 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.git20130328
- Rebuilt with updated NumPy

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.git20130328
- Version 4.3.0

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20130108
- New snapshot

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20120920
- Version 4.2.1

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120504
- New snapshot

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.1-alt1.git20120117.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.git20120117
- Version 4.1.1

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20111114
- Version 4.0.1

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt1.svn20110127.2
- Rebuild with Python-2.7

* Mon Oct 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20110127.1
- Rebuilt with updated NumPy

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.svn20110127
- Version 3.4.1

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20101113.2
- Rebuilt with python-module-sphinx-devel

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20101113.1
- Rebuilt for debuginfo

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.3-alt1.svn20101113
- Version 3.3.3

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.2-alt1.svn20100722
- Version 3.3.2

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1.svn20100225
- Version 3.3.1
- Extracted tests into separate package
- Added pickles package

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901.5
- Extracted tests into separated package
- Rebuilt with reformed NumPy

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901.4
- Rebuilt with reformed NumPy

* Sat Jan 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901.3
- Rebuilt without python-module-Numeric

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901.2
- Rebuilt with python 2.6

* Mon Oct 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901.1
- Extracted documentation into separate package

* Wed Oct 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20090901
- Initial build for Sisyphus

