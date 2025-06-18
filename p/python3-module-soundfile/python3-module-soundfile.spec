%define oname soundfile

%def_with check

Name:    python3-module-%oname
Version: 0.13.1
Release: alt1

Summary: An audio library based on libsndfile, CFFI and NumPy.
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/bastibe/SoundFile

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-cffi

%if_with check
BuildRequires: libsndfile-devel
BuildRequires: python3-module-numpy
%endif

Requires: libsndfile
Requires: python3-module-cffi

BuildArch: noarch

Source:  %oname-%version.tar.gz

%description
%summary

%prep
%setup -n %oname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/*.py
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/%oname-%version.dist-info
%doc *.rst LICENSE PKG-INFO

%changelog
* Wed Jun 18 2025 Grigory Ustinov <grenka@altlinux.org> 0.13.1-alt1
- Build new version (Closes: #54835).
- Build with check.

* Mon Oct 31 2022 Grigory Ustinov <grenka@altlinux.org> 0.11.0-alt1
- Build new version.

* Sun Oct 04 2020 Grigory Ustinov <grenka@altlinux.org> 0.10.3.post1-alt1
- Initial build for Sisyphus.
