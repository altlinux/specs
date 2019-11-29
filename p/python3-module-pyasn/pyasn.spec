%define oname pyasn

Name: python3-module-%oname
Version: 1.5.0
Release: alt2

Summary: Offline IP address to Autonomous System Number lookup module
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyasn/

# https://github.com/hadiasghari/pyasn.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires ipaddress

BuildRequires: python3-module-coverage python3-module-nose


%description
pyasn is a Python extension module that enables very fast IP address to
Autonomous System Number lookups. Current state and Historical lookups
can be done, based on the BGP / MRT file used as input.

pyasn is different from other ASN lookup tools in that it providers
offline and historical lookups. It provides utility scripts for users to
build their own lookup databases based on any BGP/MRT dump file. This
makes pyasn much faster than online dig/whois/json lookups.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.md *.txt
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.5.0-alt2
- python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.0-alt1.b6.git20141105.1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1.b6.git20141105.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.0-alt1.b6.git20141105.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt1.b6.git20141105.1
- NMU: Use buildreq for BR.

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.b6.git20141105
- Initial build for Sisyphus

