%global pypi_name netaddr
%def_enable check
%def_without docs

Name:  python3-module-%{pypi_name}
Version: 1.3.0
Release: alt1
Summary: A pure Python network address representation and manipulation library

Group:  Development/Python3
License: BSD-3-Clause
URL:  https://pypi.org/project/netaddr
VCS:  https://github.com/drkjam/netaddr
Source0: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx-issues
%endif

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

%prep
%setup
# Make rpmlint happy, rip out python shebang lines from most python
# modules
find netaddr -name "*.py" | \
  xargs sed -i -e '1 {/^#!\//d}'

%build
%pyproject_build

%if_with docs
pushd docs
PYTHONPATH='../' sphinx-build-3 -b html -d build/doctrees source html
popd
%endif

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.rst
%_bindir/netaddr
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Fri Jul 26 2024 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Build new version.

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
