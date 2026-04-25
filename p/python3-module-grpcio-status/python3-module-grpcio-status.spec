%define _unpackaged_files_terminate_build 1
%define pypi_name grpcio-status
%define mod_name grpc_status

Name: python3-module-%pypi_name
Version: 1.80.0
Release: alt1

Summary: Status proto mapping for gRPC

License: Apache-2.0
URL: https://pypi.org/project/grpcio-status
Group: Development/Python3

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Apr 21 2026 Alexander Burmatov <thatman@altlinux.org> 1.80.0-alt1
- Initial build for Sisyphus.
