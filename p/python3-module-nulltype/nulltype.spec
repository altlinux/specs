%define _unpackaged_files_terminate_build 1
%define oname nulltype

Name: python3-module-%oname
Version: 2.2.11
Release: alt2
Summary: Null values and sentinels like, but not, None
License: Apache-2.0
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/nulltype

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-tox python3-module-virtualenv
BuildRequires: python3-module-pytest

%description
Helps define "null" values and sentinels parallel to, but different
from, None.

None is a great sentinel value and a classic implementation of the null
object pattern.

But there are times that you need more than one nullish value to
represent different aspects of emptiness. "Nothing there" is logically
different from "undefined," "prohibited," "end of data" and other kinds
of null.

The core function of nulltype is representing emptiness and falsity in a
way that doesn't overload None (or False, 0, {}, [], "", or any of the
other possible "there's nothing here!" values). It helps create
designated identifiers with specific meanings such as Passthrough,
Prohibited, and Undefined.

%prep
%setup -n %oname-%version

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=$PWD
py.test3 --assert=plain -vv

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Wed Sep 09 2020 Stanislav Levin <slev@altlinux.org> 2.2.11-alt2
- Stopped Python2 package build.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.2.11-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.11-alt1
- Updated to upstream version 2.2.11.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.6-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.6-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.6-alt1
- Initial build for Sisyphus

