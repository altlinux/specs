%define _unpackaged_files_terminate_build 1
%define oname pyvista

Name: python3-module-%oname
Version: 0.42.3
Release: alt1
Summary: 3D plotting and mesh analysis through a streamlined interface for the Visualization Toolkit (VTK)
License: MIT
Group: Development/Python3
Url: https://docs.pyvista.org/version/stable/index.html
VCS: https://github.com/pyvista/pyvista.git

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-vtk
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-pooch
BuildRequires: python3-module-scooby
BuildRequires: python3-module-matplotlib
# Optional requirement for jupyter web integration
%filter_from_requires /python3(trame\(\..*\)\?)/d
%filter_from_requires /python3(trame_vtk\(\..*\)\?)/d

%description
PyVista is a helper module for the Visualization Toolkit (VTK) that
wraps the VTK library through NumPy and direct array access through a
variety of methods and classes.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Thu Oct 19 2023 Elizaveta Morozova <morozovaes@altlinux.org> 0.42.3-alt1
- Initial build for ALT.


