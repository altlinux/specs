%define oname mf2py

Name: python3-module-%oname
Version: 1.0.5
Release: alt2

Summary: Python Microformats2 parser
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/mf2py/
# https://github.com/tommorris/mf2py.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-requests
BuildRequires: python3-module-BeautifulSoup4 python3-module-nose
BuildRequires: python3-module-mock python-tools-2to3

%py3_provides %oname
%py3_requires html5lib requests bs4 flask gunicorn


%description
Python parser for microformats 2. Full-featured and mostly stable.
Implements the full mf2 spec, including backward compatibility with
microformats1.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc AUTHORS *.md doc/source/*.rst
%python3_sitelibdir/*


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.5-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.5-alt1.git20170715.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.5-alt1.git20170715
- Updated to current upstream version.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt1.git20150205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1.git20150205.1
- NMU: Use buildreq for BR.

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20150205
- Initial build for Sisyphus

