%define  oname jupyter_kernel_test

%def_with check

Name:    python3-module-%oname
Version: 0.5.0
Release: alt1

Summary: A tool for testing Jupyter kernels

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/jupyter/jupyter_kernel_test

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-flit
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-jupyter_client
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-nest-asyncio
BuildRequires: python3-module-ipykernel
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
jupyter_kernel_test is a tool for testing Jupyter kernels. It tests kernels for
successful code execution and conformance with the Jupyter Messaging Protocol.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%__python3 test_ipykernel.py

%files
%doc *.md *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Wed Feb 08 2023 Grigory Ustinov <grenka@altlinux.org> 0.5.0-alt1
- Automatically updated to 0.5.0.

* Mon Sep 12 2022 Grigory Ustinov <grenka@altlinux.org> 0.4.5-alt1
- Automatically updated to 0.4.5.

* Sun Aug 21 2022 Grigory Ustinov <grenka@altlinux.org> 0.4.4-alt1
- Automatically updated to 0.4.4.

* Thu Aug 04 2022 Grigory Ustinov <grenka@altlinux.org> 0.4.3-alt1.1
- Fixed check section.

* Thu Aug 04 2022 Grigory Ustinov <grenka@altlinux.org> 0.4.3-alt1
- Initial build for Sisyphus.
