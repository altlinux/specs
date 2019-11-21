%define oname formats

Name: python3-module-%oname
Version: 0.1.1
Release: alt3

Summary: Support multiple formats with ease
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/formats/
# https://github.com/redodo/formats.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_provides %oname
%py3_requires json


%description
Formats will provide you with a consistent API to parse and compose
data.

You could of course use the register method to register your own parser,
but decorators are much more fun!

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
py.test3 -vv

%files
%doc *.md *.rst
%python3_sitelibdir/*


%changelog
* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.1-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.1-alt2.git20150211.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt2.git20150211
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20150211.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20150211
- Initial build for Sisyphus

