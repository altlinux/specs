%define _unpackaged_files_terminate_build 1
%define oname requests-cache

%def_disable check

Name: python3-module-%oname
Version: 0.4.13
Release: alt2

Summary: Persistent cache for requests library
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/requests-cache/
BuildArch: noarch

# https://github.com/reclosedev/requests-cache.git
Source0: https://pypi.python.org/packages/1a/cf/12349c7113b252d9a0b26d497d3349baeb6c8f293b440e55a00e7fa6e4a4/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-chardet python3-module-pytest
BuildRequires: python3-module-unittest2 python3-module-urllib3
BuildRequires: python3-module-sphinx

%py3_provides requests_cache
%py3_requires sqlite3


%description
Requests-cache is a transparent persistent cache for requests
(version >= 1.1.0) library.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Requests-cache is a transparent persistent cache for requests
(version >= 1.1.0) library.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Requests-cache is a transparent persistent cache for requests
(version >= 1.1.0) library.

This package contains documentation for %oname.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%make -C docs pickle
%make -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test

%files
%doc *.rst sandbox.py example.py PKG-INFO docs
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.13-alt2
- python2 disabled

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.13-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.9-alt1.git20150117.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.9-alt1.git20150117.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.9-alt1.git20150117
- Version 0.4.9

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt1.git20141219
- Initial build for Sisyphus

