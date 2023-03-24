%global pypi_name netaddr
%def_enable check

Name:		python3-module-%{pypi_name}
Version:	0.8.0
Release:	alt1
Summary:	A pure Python network address representation and manipulation library

Group:		Development/Python3
License:	BSD
URL:		http://github.com/drkjam/netaddr
# Source0-url: https://github.com/drkjam/netaddr/archive/netaddr-%version.tar.gz
Source0:	%name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-sphinx
%{?_enable_check:BuildRequires: python3-module-pytest python3-module-pytest-cov}

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


%prep
%setup

# Make rpmlint happy, get rid of DOS line endings
%{__sed} -i 's/\r//' netaddr/*.py
%{__sed} -i 's/\r//' netaddr/ip/*.py
%{__sed} -i 's/\r//' netaddr/eui/*.idx

# Make rpmlint happy, rip out python shebang lines from most python
# modules
find netaddr -name "*.py" | \
  xargs sed -i -e '1 {/^#!\//d}'

# Make rpmlint happy, fix permissions on documentation files
chmod 0644 AUTHORS CHANGELOG COPYRIGHT INSTALL LICENSE REFERENCES THANKS

%build
%python3_build


#docs
pushd docs
PYTHONPATH='../' sphinx-build-3 -b html -d build/doctrees source html
popd

%install
%python3_install

%check
py.test3

%files
%doc AUTHORS CHANGELOG COPYRIGHT LICENSE REFERENCES THANKS
%doc README.rst docs/html
%python3_sitelibdir/*
%_bindir/netaddr

%changelog
* Fri Mar 24 2023 Alexey Shabalin <shaba@altlinux.org> 0.8.0-alt1
- 0.8.0

* Mon Mar 23 2020 Alexey Shabalin <shaba@altlinux.org> 0.7.19-alt2
- build as new python3 package
- backported patch from upstream
- enable check
- build as noarch

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 0.7.19-alt1
- new version 0.7.19 (with rpmrb script)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.13-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.13-alt1.1
- NMU: Use buildreq for BR.

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.13-alt1
- Version 0.7.13

* Fri Aug 29 2014 Lenar Shakirov <snejok@altlinux.ru> 0.7.12-alt1
- 0.7.12

* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 0.7.5-alt1
- Initial release for Sisyphus (based on Fedora)
