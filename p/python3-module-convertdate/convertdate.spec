%define oname convertdate

%def_disable check

Name: python3-module-%oname
Version: 2.0.3.1
Release: alt3

Summary: Utils for converting between date formats and calculating holidays
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/convertdate/
BuildArch: noarch

# https://github.com/fitnr/convertdate.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_provides %oname
%py3_requires ephem pytz


%description
Converts between Gregorian dates and other calendar systems. Calendars
included: Baha'i, French Republican, Hebrew, Indian Civil, Islamic,
Julian, Mayan and Persian.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
py.test-%_python3_version tests/*.py

%files
%doc *.rst *.md
%python3_sitelibdir/*


%changelog
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

