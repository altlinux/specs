%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define oname grpcio-tools

Name: python3-module-%oname
Version: 1.64.0
Release: alt1
Summary: HTTP/2-based RPC framework
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/grpcio-tools

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libprotobuf-devel
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(Cython) python3-module-protobuf
BuildRequires: python3-module-wheel

%description
HTTP/2-based RPC framework.

%prep
%setup -n %oname-%version

# remove bundled libraries
#rm -rf third_party/protobuf

%build
export GRPC_PYTHON_BUILD_WITH_CYTHON=1
%add_optflags %(getconf LFS_CFLAGS)
%pyproject_build

%install
export GRPC_PYTHON_BUILD_WITH_CYTHON=1
%pyproject_install

%check
export GRPC_PYTHON_BUILD_WITH_CYTHON=1
python3 setup.py test

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Wed May 29 2024 Andrey Cherepanov <cas@altlinux.org> 1.64.0-alt1
- New version.

* Tue Feb 15 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 1.43.0-alt1
- Updated to upstream version 1.43.0.

* Fri Aug 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.39.0-alt1
- Updated to upstream version 1.39.0.

* Thu Mar 18 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.36.1-alt1
- Updated to upstream version 1.36.1.

* Fri Jan 24 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.26.0-alt1
- Updated to upstream version 1.26.0.

* Tue Aug 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.22.0-alt1
- Updated to upstream version 1.22.0 (Closes: #37081).
- Disabled build for python-2.

* Fri Mar 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.19.0-alt1
- Updated to upstream version 1.19.0.

* Thu May 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.0-alt1
- Initial build for ALT.
