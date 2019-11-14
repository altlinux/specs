%define oname PyDSTool

Name: python3-module-%oname
Version: 0.88.121202
Release: alt4

Summary: Integrated simulation, modeling and analysis package for dynamical systems
License: BSD
Group: Development/Python3
Url: http://www.ni.gsu.edu/~rclewley/PyDSTool/FrontPage.html
# http://jay.cam.cornell.edu/svn/PyDSTool

Source: %oname-%version.tar.gz
Source1: %oname.pth

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%add_python3_req_skip matplotlib scipy pylab


%description
PyDSTool is an integrated simulation, modeling and analysis package for
dynamical systems, written in Python.

%install
install -d %buildroot%python3_sitelibdir
pushd %buildroot%python3_sitelibdir
tar -xzf %SOURCE0
rm -fR .gear

## py2 -> py3
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

find -type f -name '*.py' -exec 2to3 -w -n '{}' +
##

install -p -m644 %SOURCE1 .
popd

find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%files
%python3_sitelibdir/*


%changelog
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

