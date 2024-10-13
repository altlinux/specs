%define _unpackaged_files_terminate_build 1
%define pypi_name numpydoc
%define mod_name %pypi_name

# tests requires an access to the Internet
%def_without check

Name: python3-module-%pypi_name
Version: 1.8.0
Release: alt1
Epoch: 1

Summary: Numpy's Sphinx extensions
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/numpydoc/
Vcs: https://github.com/numpy/numpydoc

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
BuildRequires: python3-module-pytest-cov
%endif

%description
This package provides the numpydoc Sphinx extension for handling
docstrings formatted according to the NumPy documentation format.
The extension also adds the code description directives np:function,
np-c:function, etc.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
rm -r %buildroot%python3_sitelibdir/%mod_name/tests

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE.txt README.rst
%_bindir/%pypi_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Oct 13 2024 Anton Zhukharev <ancieg@altlinux.org> 1:1.8.0-alt1
- Updated to 1.8.0.

* Tue Apr 02 2024 Anton Zhukharev <ancieg@altlinux.org> 1:1.7.0-alt1
- Updated to 1.7.0.

* Sat Oct 21 2023 Anton Zhukharev <ancieg@altlinux.org> 1:1.6.0-alt1
- Built for ALT Sisyphus.

