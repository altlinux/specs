%define pypi_name rapidfuzz

%def_enable check

Name: python3-module-%pypi_name
Version: 3.9.4
Release: alt1

Summary: Fast string Python 3 matching library for Python and C++
Group: Development/Python3
License: MIT
Url: http://pypi.python.org/pypi/%pypi_name

Vcs: https://github.com/maxbachmann/RapidFuzz.git
Source: https://pypi.io/packages/source/r/%pypi_name/%pypi_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-wheel
BuildRequires: python3-module-setuptools python3(skbuild)
%{?_enable_check:BuildRequires: /proc python3(pytest) python3(mypy) python3(pylint)
BuildRequires: python3(hypothesis) python3(pandas.testing)}
#BuildRequires: python3(pandas)

%add_python3_req_skip PyInstaller

%description
RapidFuzz is a fast string matching library for Python and C++, which is
using the string similarity calculations from FuzzyWuzzy.


%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README.md


%changelog
* Wed Jul 03 2024 Yuri N. Sedunov <aris@altlinux.org> 3.9.4-alt1
- 3.9.4

* Wed Jun 19 2024 Yuri N. Sedunov <aris@altlinux.org> 3.9.3-alt1
- 3.9.3

* Mon May 20 2024 Yuri N. Sedunov <aris@altlinux.org> 3.9.1-alt1
- 3.9.1

* Tue May 14 2024 Yuri N. Sedunov <aris@altlinux.org> 3.9.0-alt1
- 3.9.0

* Mon Apr 08 2024 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Sun Apr 07 2024 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Mar 25 2024 Yuri N. Sedunov <aris@altlinux.org> 3.7.0-alt1
- 3.7.0

* Wed Mar 06 2024 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Thu Jan 11 2024 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Sun Nov 12 2023 Yuri N. Sedunov <aris@altlinux.org> 3.5.2-alt1
- 3.5.2

* Fri Jul 21 2023 Yuri N. Sedunov <aris@altlinux.org> 3.1.2-alt1
- 3.1.2

* Wed Jun 07 2023 Yuri N. Sedunov <aris@altlinux.org> 3.1.1-alt1
- 3.1.1

* Mon Jun 05 2023 Yuri N. Sedunov <aris@altlinux.org> 3.1.0-alt1
- 3.1.0

* Mon Apr 17 2023 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Apr 11 2023 Yuri N. Sedunov <aris@altlinux.org> 2.15.1-alt1
- 2.15.1

* Sun Dec 04 2022 Yuri N. Sedunov <aris@altlinux.org> 2.13.3-alt1
- 2.13.3

* Wed Nov 23 2022 Yuri N. Sedunov <aris@altlinux.org> 2.13.2-alt1
- first build for Sisyphus


