%define _unpackaged_files_terminate_build 1
%define pypi_name rope

# unfortunately, 1 test is broken,
# see https://github.com/python-rope/rope/issues/478
%def_without check

Name: python3-module-%pypi_name
Version: 1.7.0
Release: alt1

Summary: A python refactoring library
License: LGPL-3.0+
Group: Development/Python3
Url: https://pypi.org/project/rope/
Vcs: https://github.com/python-rope/rope

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_timeout)
BuildRequires: python3(pytoolconfig)
BuildRequires: python3(build)
BuildRequires: python3(sqlite3)
%endif

BuildArch: noarch

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%__python3 -m pytest .

%files
%doc COPYING README.rst CHANGELOG.md docs
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jan 17 2023 Anton Zhukharev <ancieg@altlinux.org> 1.7.0-alt1
- 1.7.0

* Sun Jan 15 2023 Anton Zhukharev <ancieg@altlinux.org> 1.6.0-alt1
- 1.6.0

* Thu Oct 06 2022 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- 0.9.4.1 -> 1.3.0
- rewrite spec from a scratch
- do not pack tests

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.9.4.1-alt1.2
- (NMU) rebuild with python3.6

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.4.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4.1-alt1
- Version 0.9.4-1 (Python 3)

* Mon Sep 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1
- Version 0.9.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.3-alt1.1
- Rebuild with Python-2.7

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1
- Version 0.9.3

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1
- Version 0.9.2 (ALT #17977)

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.1
- Rebuilt with python 2.6

* Sat May 10 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.8.2-alt1
- Initial ALT build
