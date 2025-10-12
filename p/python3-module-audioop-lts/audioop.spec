%define srcname audioop-lts

%def_with check

Name:    python3-module-%srcname
Version: 0.2.2
Release: alt1

Summary: LTS Port of Python audioop

License: PSF-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/audioop-lts
VCS:     https://github.com/AbstractUmbra/audioop

Source: %name-%version.tar

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-test
BuildRequires: python3-module-pytest
%endif

%description
An LTS port of the Python builtin module audioop which was deprecated
since version 3.11 and removed in 3.13.

This project exists to maintain this module for future versions.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run pytest tests/test_audioop.py

%files
%doc *.md
%python3_sitelibdir/audioop
%python3_sitelibdir/audioop_lts-%version.dist-info

%changelog
* Sun Oct 12 2025 Grigory Ustinov <grenka@altlinux.org> 0.2.2-alt1
- Automatically updated to 0.2.2.

* Tue Jul 29 2025 Grigory Ustinov <grenka@altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus.
