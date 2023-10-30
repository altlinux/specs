%define pypi_name requests-wsgi-adapter

%def_with check

Name:    python3-module-%pypi_name
Version: 0.4.1
Release: alt1

Summary: WSGI Transport Adapter for Requests
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/seanbrant/requests-wsgi-adapter

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-requests
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
python3 runtests.py

%files
%doc *.rst
%python3_sitelibdir/wsgiadapter.py
%python3_sitelibdir/__pycache__/wsgiadapter*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Oct 26 2023 Alexander Burmatov <thatman@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus.
