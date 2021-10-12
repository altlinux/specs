%define oname python-subunit

Name: python3-module-subunit
Version: 1.4.0
Release: alt1

Summary: Python implementation of subunit test streaming protocol

License: Apache or BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/python-subunit/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildArch: noarch

BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-testscenarios
BuildRequires: python3(hypothesis) python3(fixtures)
BuildRequires: python3-module-testtools >= 0.9.34

%description
Subunit is a streaming protocol for test results. The protocol is human
readable and easily generated and parsed. By design all the components
of the protocol conceptually fit into the xUnit TestCase->TestResult
interaction.

Subunit comes with command line filters to process a subunit stream and
language bindings for python, C, C++ and shell. Bindings are easy to
write for other languages.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%check
#python3 setup.py test

%files
%doc NEWS README.rst
%_bindir/*
%python3_sitelibdir/*


%changelog
* Tue Oct 12 2021 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt3
- build python3 module separately

* Fri Oct 16 2020 Stanislav Levin <slev@altlinux.org> 1.3.0-alt2
- Dropped dependency on tests packages(Python2).

* Tue Dec 11 2018 Alexey Shabalin <shaba@altlinux.org> 1.3.0-alt1
- 1.3.0

* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt4
- rebuild with python3.6

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.0-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.0-alt3
- Updated build dependencies.

* Mon Jun 05 2017 Lenar Shakirov <snejok@altlinux.ru> 1.2.0-alt2
- Fix test_results packaging

* Tue May 23 2017 Lenar Shakirov <snejok@altlinux.ru> 1.2.0-alt1
- Version 1.2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Aug 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.18-alt3
- Added necessary obsoletes

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.18-alt2
- Renamed python-module-python-subunit -> python-module-subunit

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.18-alt1
- Version 0.0.18

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.15-alt1
- Version 0.0.15

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.10-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.10-alt1
- Version 0.0.10

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.0.7-alt2.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.7-alt1.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1
- Initial build for Sisyphus

