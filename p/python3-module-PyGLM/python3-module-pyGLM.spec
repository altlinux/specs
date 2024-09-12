%define pypi_name glm
%define distname pyglm
%define modname PyGLM

%def_disable check

Name: python3-module-%modname
Version: 2.7.2
Release: alt1

Summary: OpenGL Mathematics (GLM) library for Python
Group: Development/Python3
License: Zlib or Libpng
Url: http://pypi.python.org/pypi/%modname

Vcs: https://github.com/Zuzu-Typ/PyGLM.git
Source: https://pypi.io/packages/source/p/%distname/%distname-%version.tar.gz

Provides: python3(%pypi_name) = %EVR
Provides: python3(%modname) = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3(wheel) python3(setuptools)
BuildRequires: gcc-c++

%description
%summary

%prep
%setup -n %distname-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%{pypi_name}.*.so
%python3_sitelibdir/%pypi_name-stubs/
%python3_sitelibdir/%modname-%version.dist-info
%doc README* LICENSE


%changelog
* Thu Sep 12 2024 Yuri N. Sedunov <aris@altlinux.org> 2.7.2-alt1
- 2.7.2

* Mon Nov 27 2023 Yuri N. Sedunov <aris@altlinux.org> 2.7.1-alt1
- first build for Sisyphus


