%define  oname sphinx-pytest

%def_with check

Name:    python3-module-%oname
Version: 0.2.0
Release: alt1

Summary: Helpful pytest fixtures for sphinx extensions

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/sphinx_pytest
VCS:     https://github.com/chrisjsewell/sphinx-pytest

Source:  %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-flit
BuildRequires: python3-module-sphinx

%if_with check
BuildRequires: python3-module-sphinx-tests
BuildRequires: python3-module-pytest
%endif

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
%pyproject_run_pytest

%files
%doc LICENSE *.md
%python3_sitelibdir/sphinx_pytest
%python3_sitelibdir/*.dist-info

%changelog
* Tue Jan 23 2024 Grigory Ustinov <grenka@altlinux.org> 0.2.0-alt1
- Automatically updated to 0.2.0.
- Build with check.

* Sun Jun 11 2023 Grigory Ustinov <grenka@altlinux.org> 0.1.1-alt1
- Automatically updated to 0.1.1.

* Tue Oct 18 2022 Grigory Ustinov <grenka@altlinux.org> 0.0.5-alt1
- Initial build for Sisyphus.
