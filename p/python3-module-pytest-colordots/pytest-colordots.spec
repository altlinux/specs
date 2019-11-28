%define oname pytest-colordots

Name: python3-module-%oname
Version: 1.1
Release: alt2

Summary: Colorizes the progress indicators
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-colordots
BuildArch: noarch

# https://github.com/svenstaro/pytest-colordots.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(colorama) python3(pytest)

%py3_provides pytest_colordots


%description
Colorizes the progress indicators

This is an adoption of pytest-greendots which sadly does not have an
upstream repository.

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
%doc *.md
%python3_sitelibdir/*


%changelog
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Oct 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1-alt1
- Updated to upstream version 1.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20141120.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20141120.1
- NMU: Use buildreq for BR.

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141120
- Initial build for Sisyphus

