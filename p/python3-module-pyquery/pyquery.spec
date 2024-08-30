%define _unpackaged_files_terminate_build 1
%define pypi_name pyquery

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.1
Release: alt1

Summary: A jQuery-like library for python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/pyquery/
Vcs: https://github.com/gawel/pyquery

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-cssselect
BuildRequires: python3-module-lxml
BuildRequires: python3-module-webtest
BuildRequires: python3-module-pytest
%endif

%description
%name allows you to make jQuery queries on XML documents.  The API is as much
as possible the similar to jQuery.  %name uses lxml for fast XML and HTML
manipulation.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v \
	--deselect=tests/test_pyquery.py::TestWebScrappingEncoding::test_get

%files
%doc *.rst *.txt
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Fri Aug 30 2024 Anton Vyatkin <toni@altlinux.org> 2.0.1-alt1
- New version 2.0.1.

* Tue Jan 23 2024 Anton Vyatkin <toni@altlinux.org> 2.0.0-alt3
- Fix FTBFS.

* Thu Apr 27 2023 Anton Vyatkin <toni@altlinux.org> 2.0.0-alt2
- Fix FTBFS

* Mon Apr 03 2023 Anton Vyatkin <toni@altlinux.org> 2.0.0-alt1
- New version 2.0.0.

* Wed Feb 02 2022 Stanislav Levin <slev@altlinux.org> 1.4.3-alt1
- 1.4.1 -> 1.4.3.

* Sun Aug 16 2020 Dmitry V. Levin <ldv@altlinux.org> 1.4.1.0.5.49eb-alt1
- Packaged pyquery-1.4.1-5-g49ebccf.
