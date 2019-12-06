%define _unpackaged_files_terminate_build 1
%define oname rsttst

Name: python3-module-%oname
Version: 0.3.0
Release: alt2

Summary: rsttst makes your reStructuredText testable
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/rsttst/
BuildArch: noarch

# https://github.com/willemt/rsttst.git
Source0: https://pypi.python.org/packages/b5/d9/fed43b27554822d8dd227f290707ae06eabf223a79522a27a1e1469994f3/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Pygments python3-module-docutils

%py3_provides %oname
%py3_requires pygments docutils


%description
rsttst makes your reStructuredText documentation testable.

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
%doc *.rst
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Dec 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.5-alt1.git20150215.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20150215
- Initial build for Sisyphus

