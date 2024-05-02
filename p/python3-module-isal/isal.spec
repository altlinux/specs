Name: python3-module-isal
Version: 1.6.1
Release: alt1

Summary: Python bindings for the ISA-L library
License: PSF-2.0
Group: Development/Python
Url: https://github.com/pycompression/python-isal

Source0: %name-%version-%release.tar

BuildRequires: libisal-devel
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(cython)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_timeout)
BuildRequires: python3(test)

%description
%summary

%prep
%setup

%build
export PYTHON_ISAL_LINK_DYNAMIC=1
%pyproject_build

%install
%pyproject_install

%check
%ifarch aarch64 x86_64 ppc64le
%pyproject_run_pytest tests
%endif

%files
%python3_sitelibdir/isal
%python3_sitelibdir/isal-%version.dist-info

%changelog
* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.6.1-alt1
- 1.6.1 released
