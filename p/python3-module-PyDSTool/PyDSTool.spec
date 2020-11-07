%define oname PyDSTool

Name: python3-module-%oname
Version: 0.91.0
Release: alt1

Summary: Integrated simulation, modeling and analysis package for dynamical systems

License: BSD
Group: Development/Python3
Url: http://www.ni.gsu.edu/~rclewley/PyDSTool/FrontPage.html

# Source-url: %__pypi_url %oname
Source: %name-%version.tar
Source1: %oname.pth

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%add_python3_req_skip matplotlib scipy pylab

%description
PyDSTool is an integrated simulation, modeling and analysis package for
dynamical systems, written in Python.

%prep
%setup
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install
%python3_prune

rm -rfv %buildroot%_prefix/{examples,tests}/

#install -p -m644 %SOURCE1 .

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-*.egg-info


%changelog
* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 0.91.0-alt1
- new version (0.91.0) with rpmgs script

* Sat Nov 07 2020 Vitaly Lipatov <lav@altlinux.ru> 0.88.121202-alt5
- switch to build from tarball, cleanup spec

* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.88.121202-alt4
- python2 disabled

* Mon Mar 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.88.121202-alt3.bzr20130716.1.1
- (NMU) Rebuilt with python-3.6.4.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.88.121202-alt3.bzr20130716.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.88.121202-alt3.bzr20130716
- Added module for Python 3

* Sun Dec 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.88.121202-alt2.bzr20130716
- Applied repocop patch

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.88.121202-alt1.bzr20130716
- Version 0.88.121202

* Sun Oct 30 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.88-alt1.svn20100720.2.1
- Rebuild with Python-2.7

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.88-alt1.svn20100720.2
- Requires GotoBLAS2 instead of ATLAS

* Tue Mar 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.88-alt1.svn20100720.1
- Removed requirement of libfftw3-devel

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.88-alt1.svn20100720
- Version 0.88

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.87-alt1.svn20090922.1
- Rebuilt with python 2.6

* Sat Oct 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.87-alt1.svn20090922
- Initial build for Sisyphus

