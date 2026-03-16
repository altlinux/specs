%define oname sphinx_rtd_dark_mode
%def_with check

Name: python3-module-%oname
Version: 1.3.0
Release: alt2

Summary: ReadTheDocs.org dark mode for Sphinx.
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/sphinx-rtd-dark-mode/
VCS: https://github.com/MrDogeBro/sphinx_rtd_dark_mode.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-pytest
BuildRequires: python3-module-sphinx_rtd_theme
%endif

%description
This Sphinx extension adds a toggleable dark mode to the Read the Docs theme.
A little icon is added in the bottom right hand corner which allows
the user to switch between light or dark mode.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests/build.py

%files
%doc LICENSE *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon Mar 16 2026 Danila Skachedubov <skachedubov@altlinux.org> 1.3.0-alt2
- Changed the source links.

* Mon Mar 16 2026 Danila Skachedubov <skachedubov@altlinux.org> 1.3.0-alt1
- first build for ALT.
