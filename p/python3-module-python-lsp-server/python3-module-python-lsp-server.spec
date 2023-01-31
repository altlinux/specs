%define _unpackaged_files_terminate_build 1
%define pypi_name python-lsp-server

%def_with check

Name: python3-module-%pypi_name
Version: 1.7.1
Release: alt1

Summary: Fork of the python-language-server project, maintained by the Spyder IDE team and the community
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/python-lsp-server/
Vcs: https://github.com/python-lsp/python-lsp-server

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(setuptools_scm)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(flaky)
BuildRequires: python3(pycodestyle)
BuildRequires: python3(pydocstyle)
BuildRequires: python3(jedi)
BuildRequires: python3(rope)
BuildRequires: python3(mccabe)
BuildRequires: python3(pyflakes)
BuildRequires: python3(pylint)
BuildRequires: python3(yapf)
BuildRequires: python3(autopep8)
BuildRequires: python3(flake8)
BuildRequires: python3(ujson)
BuildRequires: python3(whatthepatch)
BuildRequires: python3(python-lsp-jsonrpc)
BuildRequires: python3(PyQt5)
BuildRequires: python3(numpy)
BuildRequires: python3(matplotlib)
BuildRequires: python3(pandas)
BuildRequires: python3(docstring_to_markdown)
%endif

BuildArch: noarch

%py3_provides %pypi_name

%description
A Python 3.7+ implementation of the Language Server Protocol.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%_bindir/pylsp
%python3_sitelibdir/pylsp/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jan 31 2023 Ivan A. Melnikov <iv@altlinux.org> 1.7.1-alt1
- 1.7.1

* Thu Jan 05 2023 Ivan A. Melnikov <iv@altlinux.org> 1.7.0-alt1
- 1.7.0

* Sat Dec 10 2022 Ivan A. Melnikov <iv@altlinux.org> 1.6.0-alt1
- 1.6.0

* Thu Oct 06 2022 Anton Zhukharev <ancieg@altlinux.org> 1.5.0-alt1
- initial build for Sisyphus
