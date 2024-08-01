%define oname glcontext

Name: python3-module-%oname
Version: 2.5.0
Release: alt1

Summary: glcontext is a library providing OpenGL implementation for ModernGL on multiple platforms

Url: https://github.com/moderngl/glcontext
License: MIT
Group: Development/Python3

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: gcc-c++ libX11-devel

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Thu Aug 01 2024 Ivan Mazhukin <vanomj@altlinux.org> 2.5.0-alt1
- Initial build for ALT Sisyphus

