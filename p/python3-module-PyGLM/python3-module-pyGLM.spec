%def_disable snapshot

%define _name glm
%define pypi_name py%_name
%define modname PyGLM

%def_disable check

Name: python3-module-%modname
Version: 2.8.3
Release: alt1

Summary: OpenGL Mathematics (GLM) library for Python
Group: Development/Python3
License: Zlib
Url: http://pypi.python.org/pypi/%modname

Vcs: https://github.com/Zuzu-Typ/PyGLM.git

%if_disabled snapshot
Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz
Source1: https://github.com/Zuzu-Typ/PyGLM/blob/master/test/PyGLM_test.py
#Source: https://github.com/Zuzu-Typ/PyGLM/archive/%version/%modname-%version.tar.gz
%else
Source: %modname-%version.tar
%endif

Provides: python3-module-%pypi_name = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3(wheel) python3(setuptools)
BuildRequires: gcc-c++
%{?_enable_check:BuildRequires: python3(pytest)}

%description
%summary

%prep
%setup -n %{?_disable_snapshot:%pypi_name}%{?_enable_snapshot:%modname}-%version
mkdir test
cp %SOURCE1 test/

%build
%pyproject_build

%install
%pyproject_install

%check
py.test-3 test/PyGLM_test.py -v

%files
%python3_sitelibdir/%_name/
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-stubs/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README* LICENSE


%changelog
* Wed Nov 26 2025 Yuri N. Sedunov <aris@altlinux.org> 2.8.3-alt1
- 2.8.3

* Thu Apr 17 2025 Yuri N. Sedunov <aris@altlinux.org> 2.8.2-alt1
- 2.8.2

* Wed Apr 02 2025 Yuri N. Sedunov <aris@altlinux.org> 2.8.1-alt1
- 2.8.1

* Fri Oct 11 2024 Yuri N. Sedunov <aris@altlinux.org> 2.7.3-alt1
- 2.7.3

* Thu Sep 12 2024 Yuri N. Sedunov <aris@altlinux.org> 2.7.2-alt1
- 2.7.2

* Mon Nov 27 2023 Yuri N. Sedunov <aris@altlinux.org> 2.7.1-alt1
- first build for Sisyphus


