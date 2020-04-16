%define _unpackaged_files_terminate_build 1

%define oname pytest-isort

Name: python3-module-%oname
Version: 0.1.0
Release: alt2

Summary: pytest plugin to perform isort checks (import ordering)
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-isort

BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3

%description
pytest plugin to perform isort checks (import ordering)

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Thu Apr 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.0-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.0-alt1
- Initial build for ALT.
