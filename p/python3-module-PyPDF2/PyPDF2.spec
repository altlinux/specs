%define _unpackaged_files_terminate_build 1
%define oname PyPDF2

Name: python3-module-%oname
Version: 1.26.0
Release: alt2
Summary: A utility to read and write PDFs with Python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/PyPDF2/

# https://github.com/mstamy2/PyPDF2.git
Source0: https://pypi.python.org/packages/b4/01/68fcc0d43daf4c6bdbc6b33cc3f77bda531c86b174cac56ef0ffdb96faab/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
Requires: python3-module-Reportlab

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
%setup -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%files
%doc CHANGELOG *.md
%python3_sitelibdir/*

%changelog
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

