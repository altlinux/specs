%def_disable snapshot
%define pypi_name hijridate

%def_enable check

Name: python3-module-%pypi_name
Version: 2.5.0
Release: alt1

Summary: Hijri to Gregorian dates converter
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%pypi_name

Vcs: https://github.com/dralshehri/hijridate.git

%if_disabled snapshot
Source: https://pypi.io/packages/source/h/%pypi_name/%pypi_name-%version.tar.gz
%else
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch
#Provides: python3(%pypi_name) = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(hatchling) python3(hatch-fancy-pypi-readme) python3(wheel)
%{?_enable_check:BuildRequires: python3(pytest_cov)}

%description
HijriDate is a Python package for converting between Hijri and Gregorian
dates using the Umm al-Qura calendar. The package has been thoroughly
verified and tested against original references to ensure its accuracy
and reliability. It has an intuitive design, allows rich comparison and
basic formatting of Hijri dates, and is optimized for performance.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test-3

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README* CHANGELOG*


%changelog
* Wed Feb 05 2025 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt1
- first build for Sisyphus


