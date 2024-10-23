%define pypi_name markdown-checklist
%define mod_name markdown_checklist

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.4
Release: alt2

Summary: Python Markdown extension for task lists with checkboxes

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/markdown-checklist/

BuildArch: noarch

# https://github.com/FND/markdown-checklist.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3-module-setuptools
%if_with check
BuildRequires: python3-module-markdown
BuildRequires: python3-module-pytest
%endif

%py3_provides markdown_checklist
%py3_requires markdown

%description
Python Markdown extension for lists of tasks with checkboxes.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Oct 23 2024 Stanislav Levin <slev@altlinux.org> 0.4.4-alt2
- Migrated from removed setuptools' test command (see #50996).

* Thu Aug 04 2022 Grigory Ustinov <grenka@altlinux.org> 0.4.4-alt1
- Build new version.

* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1.git20150127.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20150127.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150127
- Initial build for Sisyphus

