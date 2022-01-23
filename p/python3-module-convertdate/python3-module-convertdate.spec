%define modname convertdate
# https://bugzilla.altlinux.org/show_bug.cgi?id=39164
%def_enable check

Name: python3-module-%modname
Version: 2.4.0
Release: alt1

Summary: Utils for converting between date formats and calculating holidays
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/convertdate/
BuildArch: noarch

Vcs: https://github.com/fitnr/convertdate.git
Source: https://github.com/fitnr/%modname/archive/v%version/%modname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
%{?_enable_check:BuildRequires: python3-module-pytest python3-module-pymeeus python3-module-pytz}

%py3_provides %modname
%py3_requires pytz pymeeus

%description
Converts between Gregorian dates and other calendar systems. Calendars
included: Baha'i, French Republican, Hebrew, Indian Civil, Islamic,
Julian, Mayan and Persian.

%prep
%setup -n %modname-%version

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir
py.test-3 tests

%files
%_bindir/censusgeocode
%python3_sitelibdir/*
%doc *.rst *.md

%changelog
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

