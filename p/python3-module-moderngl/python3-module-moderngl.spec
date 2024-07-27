%define oname moderngl

Name: python3-module-moderngl
Version: 5.10.0
Release: alt1

Summary: Modern OpenGL binding for Python

Url: https://github.com/moderngl/moderngl
License: MIT
Group: Development/Python3

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: gcc-c++

%description
ModernGL is a Python wrapper over OpenGL Core.
ModernGL simplifies the creation of graphics applications like scientific simulations, games or user interfaces.
Usually, acquiring in-depth knowledge of OpenGL requires a steep learning curve. In contrast,
ModernGL is easy to learn and use. ModernGL is capable of rendering with high performance and quality, with less code written.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/*

%changelog
* Fri Jul 26 2024 Ivan Mazhukin <vanomj@altlinux.org> 5.10.0-alt1
- Initial build for ALT Sisyphus

