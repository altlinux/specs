%define _unpackaged_files_terminate_build 1
%define oname evelink

%def_without check

Name: python3-module-%oname
Version: 0.7.5
Release: alt3
Summary: Python Bindings for the EVE Online API
License: MIT
Group: Development/Python3
# Source-git: https://github.com/eve-val/evelink.git
Url: https://pypi.python.org/pypi/EVELink/

Source: %name-%version.tar
Patch0: evelink-async-fix.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-mock
BuildRequires: python3-module-nose
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-html5lib
%endif

%py3_provides %oname

%add_findreq_skiplist %python3_sitelibdir/%oname/appengine/*
%add_findprov_skiplist %python3_sitelibdir/%oname/appengine/*
%add_python3_req_skip evelink.thirdparty.six.moves six.moves.configparser

BuildArch: noarch

%description
EVELink provides a means to access the EVE XML API from Python.

%prep
%setup
%patch0 -p1

%build
%python3_build_debug

%install
%python3_install
rm -f %buildroot/usr/LICENSE
rm -f %buildroot/usr/README.md

%check
python3 setup.py build_ext -i
nosetests3 -v

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/*

%changelog
* Fri Oct 23 2020 Stanislav Levin <slev@altlinux.org> 0.7.5-alt3
- Dropped dependency on coveralls.

* Thu Sep 24 2020 Pavel Vasenkov <pav@altlinux.org> 0.7.5-alt2
- Drop python2 support.

* Thu Apr 30 2020 Pavel Vasenkov <pav@altlinux.org> 0.7.5-alt1.2
- (NMU) fixed:
  * rename variable with reserved name
  * set correct python2 executable in shebang and scripts

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.5-alt1
- Updated to upstream version 0.7.5.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt1.p2.git20141130.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1.p2.git20141130.1
- NMU: Use buildreq for BR.

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.p2.git20141130
- Initial build for Sisyphus

