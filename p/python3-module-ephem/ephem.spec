%define pypi_name ephem

%def_with check

Name: python3-module-%pypi_name
Version: 4.1.5
Release: alt2

Summary: Compute positions of the planets and stars
License: MIT
Group: Development/Python
URL: https://pypi.org/project/ephem
VCS: https://github.com/brandon-rhodes/pyephem

Source: %name-%version-%release.tar

BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

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
# remove shebangs in test files
sed -i '1{/env python/d}' ephem/tests/test_*.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest %buildroot%python3_sitelibdir/%pypi_name/tests -k 'not JPLTest'

%files
%doc *.rst ephem/doc/*.rst issues
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version.dist-info
%exclude %python3_sitelibdir/%pypi_name/doc
%exclude %python3_sitelibdir/%pypi_name/tests

%changelog
* Thu Aug 01 2024 Grigory Ustinov <grenka@altlinux.org> 4.1.5-alt2
- fixed license (Closes: #51018)
- built with check

* Tue Jan 09 2024 Grigory Ustinov <grenka@altlinux.org> 4.1.5-alt1
- 4.1.5 released

* Tue Jan 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.4-alt1
- 4.1.4 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.3-alt1
- 4.1.3 released

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
