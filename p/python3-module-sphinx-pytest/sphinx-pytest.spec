%define  oname sphinx-pytest

Name:    python3-module-%oname
Version: 0.1.1
Release: alt1

Summary: Helpful pytest fixtures for sphinx extensions

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/sphinx_pytest

# https://github.com/chrisjsewell/sphinx-pytest
Source:  %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-flit

BuildRequires: python3-module-sphinx

BuildArch: noarch

%description
Helpful pytest fixtures for sphinx extensions.

Sphinx is annoying, because the modularity is not great, meaning that there is no
real way just to convert single documents in isolation, etc.

This extension mainly provides some pytest fixtures to "simulate" converting
some source text to docutils AST at different stages; before transforms,
after transforms, etc.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/sphinx_pytest
%python3_sitelibdir/*.dist-info

%changelog
* Sun Jun 11 2023 Grigory Ustinov <grenka@altlinux.org> 0.1.1-alt1
- Automatically updated to 0.1.1.

* Tue Oct 18 2022 Grigory Ustinov <grenka@altlinux.org> 0.0.5-alt1
- Initial build for Sisyphus.
