%define modname StrEnum
%define pypi_name strenum

Name: python3-module-%pypi_name
Version: 0.4.15
Release: alt1

Summary: A Python Enum that inherits from str
Group: Development/Python3
License: MIT
Url: https://pypi.python.org/pypi/%modname

Vcs: https://github.com/irgeek/StrEnum.git

Source: https://pypi.io/packages/source/S/%modname/%modname-%version.tar.gz
# https://github.com/irgeek/StrEnum/pull/34
Patch: StrEnum-0.4.15-up-python-3.12.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)

%description
StrEnum is a Python 'enum.Enum' that inherits from 'str' to complement
'enum.IntEnum' in the standard library.

%prep
%setup -n %modname-%version
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%modname-%version.dist-info
%doc README*


%changelog
* Fri Sep 20 2024 Yuri N. Sedunov <aris@altlinux.org> 0.4.15-alt1
- first build for Sisyphus


