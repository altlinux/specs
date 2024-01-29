%define        _unpackaged_files_terminate_build 1
%define        mname sphinx_tabs
%define        pypiname sphinx-tabs
%def_disable   check

Name:          python3-module-%{pypiname}
Version:       3.4.5
Release:       alt1
Summary:       Tabbed views for Sphinx
License:       MIT
Group:         Development/Python3
Url:           https://sphinx-tabs.readthedocs.io
Vcs:           https://github.com/executablebooks/sphinx-tabs.git

BuildArch:     noarch
Source:        %name-%version.tar
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_enabled check
BuildRequires: python3-module-tox
%endif


%description
Create tabbed content in Sphinx documentation when building HTML.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject -- -vra

%files
%doc README* docs/*.rst
%python3_sitelibdir_noarch/%{mname}*

%changelog
* Fri Jan 26 2024 Pavel Skrylev <majioa@altlinux.org> 3.4.5-alt1
- Initial build v3.4.5 for Sisyphus
