%define _unpackaged_files_terminate_build 1
%define pypi_name cssselect

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.0
Release: alt1

Summary: Parses CSS3 Selectors and translates them to XPath 1.0
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.org/project/cssselect/
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(lxml)
%endif

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

Source: %name-%version.tar

%description
Cssselect parses CSS3 Selectors and translates them to XPath 1.0
expressions.  Such expressions can be used in lxml or another XPath
engine to find the matching elements in an XML or HTML document.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc AUTHORS docs README.rst CHANGES LICENSE
%python3_sitelibdir/cssselect/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Apr 03 2023 Anton Vyatkin <toni@altlinux.org> 1.2.0-alt1
- (NMU) New version 1.2.0.

* Tue Aug 09 2022 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 0.9.1 -> 1.1.0.

* Mon Apr 26 2021 Stanislav Levin <slev@altlinux.org> 0.9.1-alt3
- Built Python3 package from its ows src.

* Wed Feb 19 2020 Stanislav Levin <slev@altlinux.org> 0.9.1-alt2
- Fixed FTBS.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.9.1-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1
- Version 0.9.1 (ALT #30204)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.1
- Added module for Python 3

* Tue May 21 2013 Dmitry V. Levin <ldv@altlinux.org> 0.8-alt1
- Initial revision.
