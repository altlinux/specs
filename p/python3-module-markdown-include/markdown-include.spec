%define oname markdown-include

Name: python3-module-%oname
Version: 0.4.2
Release: alt2

Summary: Provides an "include" function, similar to that found in LaTeX
License: GPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/markdown-include/
BuildArch: noarch

# https://github.com/cmacmackin/markdown-include.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-markdown

%py3_provides markdown_include
%py3_requires markdown json


%description
This is an extension to Python-Markdown which provides an "include"
function, similar to that found in LaTeX (and also the C pre-processor
and Fortran).

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

ln -s README.md README.rst

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
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.2-alt1.git20150126.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.git20150126.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1.git20150126.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20150126
- Version 0.4.2

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20150120
- Initial build for Sisyphus

