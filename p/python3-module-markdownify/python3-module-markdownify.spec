%define _unpackaged_files_terminate_build 1

%define pypi_name markdownify

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.3
Release: alt1

Summary: Convert HTML to Markdown
License: MIT
Group: Development/Python3
URL: https://github.com/matthewwithanm/python-markdownify

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-beautifulsoup4
BuildRequires: python3-module-six
BuildRequires: pytest3
BuildRequires: python3-module-flake8
BuildRequires: python3-module-restructuredtext_lint
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.rst
%_bindir/markdownify
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jul 01 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.3-alt1
- New version 1.2.3.

* Sat Jan 24 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus
