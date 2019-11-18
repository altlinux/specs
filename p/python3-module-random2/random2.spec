%define oname random2

Name: python3-module-%oname
Version: 1.0.2
Release: alt2

Summary: Python 3 compatible Python 2 `random` Module
License: PSFL
Group: Development/Python3
Url: https://pypi.python.org/pypi/random2/
# https://github.com/strichter/random2.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
Python 3 compatible Python 2 `random` Module.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/*


%changelog
* Mon Nov 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt2
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.dev0.git20130315.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.dev0.git20130315.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.dev0.git20130315
- Initial build for Sisyphus

