%define oname soundfile

Name:    python3-module-%oname
Version: 0.11.0
Release: alt1

Summary: An audio library based on libsndfile, CFFI and NumPy.
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/bastibe/SoundFile

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-cffi

Requires: libsndfile
Requires: python3-module-cffi

BuildArch: noarch

Source:  %oname-%version.tar.gz

%description
%summary

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*.py
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/*.egg-info
%doc *.rst LICENSE PKG-INFO

%changelog
* Mon Oct 31 2022 Grigory Ustinov <grenka@altlinux.org> 0.11.0-alt1
- Build new version.

* Sun Oct 04 2020 Grigory Ustinov <grenka@altlinux.org> 0.10.3.post1-alt1
- Initial build for Sisyphus.
