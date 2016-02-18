%global pypi_name netaddr
%def_with python3
%def_disable check

Name:		python-module-%{pypi_name}
Version:	0.7.13
Release:	alt1.1
Summary:	A pure Python network address representation and manipulation library

Group:		Development/Python
License:	BSD
URL:		http://github.com/drkjam/netaddr
Source0:	%{name}-%{version}.tar

BuildArch:	noarch
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-Pygments python3-module-alabaster python3-module-babel python3-module-cssselect python3-module-docutils python3-module-jinja2 python3-module-markupsafe python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx_rtd_theme xz
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python3-module-html5lib python3-module-jinja2-tests python3-module-sphinx rpm-build-python3 time

#BuildRequires:	python-devel >= 2.4
#BuildRequires:  python-module-sphinx

%description
A pure Python network address representation and manipulation library.

netaddr provides a Pythonic way of working with :-

- IPv4 and IPv6 addresses and subnets
- MAC addresses, OUI and IAB identifiers, IEEE EUI-64 identifiers
- arbitrary (non-aligned) IP address ranges and IP address sets
- various non-CIDR IP range formats such as nmap and glob-style formats

Included are routines for :-

- generating, sorting and summarizing IP addresses and networks
- performing easy conversions between address notations and formats
- detecting, parsing and formatting network address representations
- performing set-based operations on groups of IP addresses and subnets
- working with arbitrary IP address ranges and formats
- accessing OUI and IAB organisational information published by IEEE
- accessing IP address and block information published by IANA

For details on the latest updates and changes, see :-

    http://github.com/drkjam/netaddr/blob/rel-0.7.x/CHANGELOG

API documentation for the latest release is available here :-

    http://packages.python.org/netaddr/

%if_with python3
%package -n python3-module-%{pypi_name}
Summary:        A pure Python network address representation and manipulation library
Group:		Development/Python
BuildArch:      noarch
#BuildRequires:  rpm-build-python3
#BuildRequires:  python3-module-sphinx

%description -n python3-module-%{pypi_name}
A pure Python network address representation and manipulation library.

netaddr provides a Pythonic way of working with :-

- IPv4 and IPv6 addresses and subnets
- MAC addresses, OUI and IAB identifiers, IEEE EUI-64 identifiers
- arbitrary (non-aligned) IP address ranges and IP address sets
- various non-CIDR IP range formats such as nmap and glob-style formats

Included are routines for :-

- generating, sorting and summarizing IP addresses and networks
- performing easy conversions between address notations and formats
- detecting, parsing and formatting network address representations
- performing set-based operations on groups of IP addresses and subnets
- working with arbitrary IP address ranges and formats
- accessing OUI and IAB organisational information published by IEEE
- accessing IP address and block information published by IANA

For details on the latest updates and changes, see :-

    http://github.com/drkjam/netaddr/blob/rel-0.7.x/CHANGELOG

API documentation for the latest release is available here :-

    http://packages.python.org/netaddr/

%endif

%prep
%setup

# Make rpmlint happy, get rid of DOS line endings
%{__sed} -i 's/\r//' netaddr/*.py
%{__sed} -i 's/\r//' netaddr/ip/*.py
%{__sed} -i 's/\r//' netaddr/eui/*.idx

# Make rpmlint happy, rip out python shebang lines from most python
# modules
find netaddr -name "*.py" | \
  xargs %{__perl} -ni -e 'print unless /usr\/bin\/python|env\s+python/'

# Make rpmlint happy, fix permissions on documentation files
chmod 0644 README AUTHORS CHANGELOG COPYRIGHT INSTALL LICENSE REFERENCES THANKS

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

#docs
pushd docs
PYTHONPATH='../' sphinx-build -b html -d build/doctrees source html
PYTHONPATH='../' py3_sphinx-build -b html -d build/doctrees source python3/html
popd

%install
%if_with python3
pushd ../python3
%python3_install
mv %{buildroot}%{_bindir}/netaddr %{buildroot}%{_bindir}/netaddr3
popd
%endif

%python_install

%check
%{__python} netaddr/tests/__init__.py
LANG=en_US.UTF-8 %{__python3} netaddr/tests/__init__.py

%files
%doc AUTHORS CHANGELOG COPYRIGHT INSTALL LICENSE REFERENCES THANKS
%doc README docs/html
%{python_sitelibdir}/*
%{_bindir}/netaddr

%if_with python3
%files -n python3-module-%{pypi_name}
%doc AUTHORS CHANGELOG COPYRIGHT INSTALL LICENSE REFERENCES THANKS
%doc README docs/python3/html
%{python3_sitelibdir}/*
%{_bindir}/netaddr3
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.13-alt1.1
- NMU: Use buildreq for BR.

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.13-alt1
- Version 0.7.13

* Fri Aug 29 2014 Lenar Shakirov <snejok@altlinux.ru> 0.7.12-alt1
- 0.7.12

* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 0.7.5-alt1
- Initial release for Sisyphus (based on Fedora)
