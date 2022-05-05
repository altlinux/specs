%global pypi_name pendulum

Name: python3-module-%pypi_name
Version: 2.1.2
Release: alt1
Summary: Python datetimes made easy
Packager: Ilya Mashkin <oddity@altlinux.ru>
License: MIT
Url: https://pendulum.eustace.io
Source0: %pypi_name-%version.tar.gz
Group: Development/Python3

BuildArch: noarch

BuildRequires: rpm-build-python3 python3-module-setuptools rpm-macros-python3 pyproject-build  python3-module-build
BuildRequires: gcc

%description
Unlike other datetime libraries for Python, Pendulum is a drop-in replacement
for the standard datetime class (it inherits from it), so, basically, you can
replace all your datetime instances by DateTime instances in you code.

It also removes the notion of naive datetimes: each Pendulum instance is
timezone-aware and by default in UTC for ease of use.


%prep
%setup -n %pypi_name-%version
# https://bugzilla.altlinux.org/show_bug.cgi?id=39907
[ -e setup.py ] && rm -f ./setup.py
echo 'import setuptools; setuptools.setup()' > setup.py
%build
%python3_build

%install
%python3_install



%files
%doc README.rst
%python3_sitelibdir/%pypi_name-0.0.0-py?.??.egg-info
%python3_sitelibdir/pendulum

%changelog
* Wed May 03 2022 Ilya Mashkin <oddity@altlinux.ru> 2.1.2-alt1
- Build for Sisyphus

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.2-4
- Rebuilt for Python 3.10

* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.2-2
- Update build workflow

* Sun Aug 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.2-1
- Update to new upstream release 2.1.2 (#1876673)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.5-4
- Rebuilt for Python 3.9

* Tue Jan 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.5-2
- Fix description (rhbz#1790074)

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.5-1
- Initial package for Fedora
