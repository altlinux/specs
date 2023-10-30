%define pypi_name abseil-py

%def_with check

Name:    python3-module-%pypi_name
Version: 2.0.0
Release: alt1

Summary: Abseil Common Libraries
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/abseil/abseil-py

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

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
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 smoke_tests/sample_app.py --echo smoke 2>&1 |grep 'echo is smoke.'
python3 smoke_tests/sample_test.py 2>&1 | grep 'msg_for_test'

%files
%doc *.md
%python3_sitelibdir/absl/
%python3_sitelibdir/%{pyproject_distinfo absl_py}

%changelog
* Tue Oct 03 2023 Alexander Burmatov <thatman@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus.
