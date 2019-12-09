%define _unpackaged_files_terminate_build 1
%define oname doxx

Name: python3-module-%oname
Version: 0.9.4
Release: alt2

Summary: Simple, flexible text file templating engine
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/doxx/
BuildArch: noarch

# https://github.com/chrissimpkins/doxx.git
Source0: https://pypi.python.org/packages/79/67/8ced67baf183fd8c8beb03983aff4d17a757fc748cab69a907b41a0a66f8/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Naked python3-module-yieldfrom.urllib3

%py3_provides %oname
%py3_requires Naked


%description
Simple, flexible text file templating engine.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc docs/* PKG-INFO
%_bindir/*
%python3_sitelibdir/*


%changelog
* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.4-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20150112.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1.git20150112.1
- NMU: Use buildreq for BR.

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20150112
- Initial build for Sisyphus

