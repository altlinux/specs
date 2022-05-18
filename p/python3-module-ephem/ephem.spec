Name: python3-module-ephem
Version: 4.1.2
Release: alt1

Summary: Compute positions of the planets and stars
License: LGPL-3
Group: Development/Python
Url: https://pypi.python.org/pypi/ephem/

Source: %name-%version-%release.tar

BuildRequires: rpm-build-python3 python3-module-setuptools

%description
PyEphem provides an ephem Python package for performing high-precision
astronomy computations. The underlying numeric routines are coded in C
and are the same ones that drive the popular XEphem astronomy
application, whose author, Elwood Charles Downey, generously gave
permission for their use in PyEphem. The name ephem is short for the
word ephemeris, which is the traditional term for a table giving the
position of a planet, asteroid, or comet for a series of dates.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.rst ephem/doc/*.rst TODO issues
%python3_sitelibdir/ephem
%python3_sitelibdir/ephem-%version-*-info
%exclude %python3_sitelibdir/ephem/doc
%exclude %python3_sitelibdir/ephem/tests

%changelog
* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.2-alt1
- 4.1.2 released

* Thu Sep 24 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.7.1-alt1
- 3.7.7.1 released

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.7.6.0-alt1.git20141124.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.7.6.0-alt1.git20141124.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.7.6.0-alt1.git20141124.1
- NMU: Use buildreq for BR.

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.6.0-alt1.git20141124
- Initial build for Sisyphus
