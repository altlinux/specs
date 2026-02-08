%define pypi_name convertdate
# https://bugzilla.altlinux.org/show_bug.cgi?id=39164
%def_enable check

Name: python3-module-%pypi_name
Version: 2.4.1
Release: alt1

Summary: Utils for converting between date formats and calculating holidays
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/convertdate/

Vcs: https://github.com/fitnr/convertdate.git

Source: https://github.com/fitnr/%pypi_name/archive/v%version/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: python3(pytest) python3(pymeeus)}

%py3_provides %pypi_name
%py3_requires pymeeus

%description
Converts between Gregorian dates and other calendar systems. Calendars
included: Baha'i, French Republican, Hebrew, Indian Civil, Islamic,
Julian, Mayan and Persian.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc *.rst *.md

%changelog
* Sun Feb 08 2026 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Sun Jan 23 2022 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Wed Apr 14 2021 Yuri N. Sedunov <aris@altlinux.org> 2.3.2-alt1
- 2.3.2

* Thu Feb 18 2021 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1
- enabled %check

* Fri Nov 27 2020 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sat Sep 26 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Thu Jun 11 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.3.1-alt3
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.0.3.1-alt2.git20141125.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.3.1-alt2.git20141125.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.3.1-alt2.git20141125.1
- NMU: Use buildreq for BR.

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 2.0.3.1-alt2.git20141125
- Rebuild with "def_disable check"

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3.1-alt1.git20141125
- Initial build for Sisyphus

