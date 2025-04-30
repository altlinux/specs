%define pypi_name txmongo

# need network
%def_without check

Name:    python3-module-%pypi_name
Version: 25.0.0
Release: alt1

Summary: asynchronous python driver for mongo
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/twisted/txmongo

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
TxMongo is an asynchronous Python/Twisted driver for MongoDB that implements
the wire protocol on non-blocking sockets. The API derives from the original
PyMongo.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Apr 28 2025 Alexander Burmatov <thatman@altlinux.org> 25.0.0-alt1
- Initial build for Sisyphus.
