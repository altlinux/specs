%define oname PyPDF2

%def_with check

Name: python3-module-%oname
Version: 1.27.9
Release: alt1

Summary: A utility to read and write PDFs with Python

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/PyPDF2

# https://github.com/mstamy2/PyPDF2.git
Source0: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
Requires: python3-module-Reportlab

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-Pillow
%endif

%description
A Pure-Python library built as a PDF toolkit. It is capable of:

* extracting document information (title, author, ...)
* splitting documents page by page
* merging documents page by page
* cropping pages
* merging multiple pages into a single page
* encrypting and decrypting PDF files
* and more!

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
py.test3

%files
%doc CHANGELOG *.md
%python3_sitelibdir/*

%changelog
* Wed Apr 27 2022 Grigory Ustinov <grenka@altlinux.org> 1.27.9-alt1
- Build new version.

* Thu Jul 22 2021 Grigory Ustinov <grenka@altlinux.org> 1.26.0-alt2
- Drop python2 support.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.26.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.24-alt1.git20141231.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.24-alt1.git20141231.1
- NMU: Use buildreq for BR.

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.24-alt1.git20141231
- Version 1.24

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.23-alt1.git20140815
- Initial build for Sisyphus

