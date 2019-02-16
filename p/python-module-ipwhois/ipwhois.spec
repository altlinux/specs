%define _unpackaged_files_terminate_build 1
%define oname ipwhois

%def_with check
%def_with docs

Name: python-module-%oname
Version: 1.1.0
Release: alt1
Summary: Retrieve and parse whois data for IPv4 and IPv6 addresses
License: BSD
Group: Development/Python
Url: https://pypi.org/project/ipwhois/

# https://github.com/secynic/ipwhois.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(dns)
BuildRequires: python2.7(ipaddr)
BuildRequires: python2.7(nose)
BuildRequires: python3(dns)
BuildRequires: python3(nose)
%endif

%py_requires ipaddr

%if_with docs
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python2.7(sphinx)
BuildRequires: python2.7(sphinx_rtd_theme)
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

%package -n python3-module-%oname
Summary: Retrieve and parse whois data for IPv4 and IPv6 addresses
Group: Development/Python3
%add_python3_path %_bindir/
%add_python3_compile_exclude %_bindir/

%description -n python3-module-%oname
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

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
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

This package contains pickles for %oname.
%endif

%prep
%setup
%patch -p1

cp -fR . ../python3

%if_with docs
%prepare_sphinx %oname/docs
ln -s ../objects.inv %oname/docs/source/
%endif

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%if_with docs
export PYTHONPATH=$PWD
%make -C %oname/docs pickle
%make -C %oname/docs html
cp -fR ipwhois-docs/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
nosetests -v -w ipwhois --exclude="(online|stress)"
pushd ../python3
nosetests3 -v -w ipwhois --exclude="(online|stress)"
popd

%files
%doc *.rst
%python_sitelibdir/ipwhois-%version-py%_python_version.egg-info/
%python_sitelibdir/ipwhois/
%if_with docs
%doc ipwhois-docs/html
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle
%endif

%files -n python3-module-%oname
%doc *.rst
%_bindir/ipwhois_cli.py
%_bindir/ipwhois_utils_cli.py
%python3_sitelibdir/ipwhois-%version-py%_python3_version.egg-info/
%python3_sitelibdir/ipwhois/

%changelog
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

