%define modname convertdate

%def_disable check

Name: python-module-%modname
Version: 2.2.0
Release: alt1

Summary: Utils for converting between date formats and calculating holidays
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/convertdate/

# https://github.com/fitnr/convertdate.git
Source: https://github.com/fitnr/%modname/archive/v%version/%name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-pytest python-module-pytz

%py_provides %modname
%py_requires pytz

%description
Converts between Gregorian dates and other calendar systems. Calendars
included: Baha'i, French Republican, Hebrew, Indian Civil, Islamic,
Julian, Mayan and Persian.

%prep
%setup -n %modname-%version

%build
%python_build_debug

%install
%python_install

%check
%__python setup.py test
py.test-%_python_version tests/*.py

%files
%doc *.rst *.md
%python_sitelibdir/*


%changelog
* Wed Dec 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- first build for Sisyphus


