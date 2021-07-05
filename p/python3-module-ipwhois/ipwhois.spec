%define _unpackaged_files_terminate_build 1
%define oname ipwhois

%def_without check

Name: python3-module-%oname
Version: 1.2.0
Release: alt2

Summary: Retrieve and parse whois data for IPv4 and IPv6 addresses

License: BSD
Group: Development/Python3
Url: https://pypi.org/project/ipwhois/

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

Patch2: fix-alt.patch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(dns)
BuildRequires: python3(nose)
%endif

%description
ipwhois is a Python package focused on retrieving and parsing whois data
for IPv4 and IPv6 addresses.

Features:
* Parses a majority of whois fields in to a standard dictionary
* IPv4 and IPv6 support
* Referral whois support
* Supports REST queries (useful if whois is blocked from your network)
* Proxy support for REST queries
* Recursive network parsing for IPs with parent/children networks listed
* Python 2.6+ and 3.3+ supported
* Useful set of utilities
* BSD license

%prep
%setup
%patch2 -p1

%build
%python3_build

%install
%python3_install

%check
export NO_INTERNET=YES
nosetests3 -v -w ipwhois --exclude="(online|stress)"

%files
%doc *.rst
%_bindir/ipwhois_cli.py
%_bindir/ipwhois_utils_cli.py
%python3_sitelibdir/ipwhois/
%python3_sitelibdir/*.egg-info/

%changelog
* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt2
- switch to build from tarball
- disable tests (missed in pypi tarball)

* Fri May 07 2021 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.0 -> 1.2.0.

* Wed Apr 01 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt3
- Unique addresses test fixed.

* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt2
- Build for python2 disabled.

* Sat Feb 16 2019 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 0.15.1 -> 1.1.0.
- Dropped dependency on sphinxcontrib.napoleon.
- Enabled testing.

* Tue Jul 11 2017 Terechkov Evgenii <evg@altlinux.org> 0.15.1-alt1
- 0.15.1

* Mon May 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.3-alt1.git20150814.1.1.1
- BR: sphinx_rtd_theme (the theme is optional since sphinx-1.4.1).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.3-alt1.git20150814.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.3-alt1.git20150814.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.3-alt1.git20150814
- Initial build for Sisyphus

