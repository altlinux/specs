%def_enable snapshot

%define modname Wand
%define pypi_name wand
%ifarch %ix86 armh
%def_disable check
%else
%def_enable check
%endif

Name: python3-module-%pypi_name
Version: 0.6.13
Release: alt1

Summary: Ctypes-based simple MagickWand API binding for Python
Group: Development/Python3
License: MIT
Url: https://wand-py.org/

Vcs: https://github.com/emcconville/wand.git

%if_disabled snapshot
Source: https://pypi.io/packages/source/w/%pypi_name/%modname-%version.tar.gz
#Source: https://github.com/emcconville/wand/archive/%version/%modname-%version.tar.gz
%else
Source: %modname-%version.tar
%endif

BuildArch: noarch

Provides: python3(%pypi_name) = %EVR

Requires: ImageMagick-lib >= 7.1

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)
BuildRequires: libImageMagick-devel
%{?_enable_check:BuildRequires: python3(pytest)}

%description
Wand is a ctypes-based simple ImageMagick binding for Python, supporting
2.7, 3.3+, and PyPy. All functionalities of MagickWand API are
implemented in Wand.

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test3

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%modname-*dist-info
%doc README*

%changelog
* Wed Aug 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.6.13-alt1
- first build for Sisyphus




