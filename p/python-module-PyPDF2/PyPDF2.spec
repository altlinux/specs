%define _unpackaged_files_terminate_build 1
%define oname PyPDF2

%def_with python3

Name: python-module-%oname
Version: 1.26.0
Release: alt1
Summary: A utility to read and write PDFs with Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/PyPDF2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mstamy2/PyPDF2.git
Source0: https://pypi.python.org/packages/b4/01/68fcc0d43daf4c6bdbc6b33cc3f77bda531c86b174cac56ef0ffdb96faab/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

Requires: python-module-Reportlab

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel rpm-build-python3

%description
A Pure-Python library built as a PDF toolkit. It is capable of:

* extracting document information (title, author, ...)
* splitting documents page by page
* merging documents page by page
* cropping pages
* merging multiple pages into a single page
* encrypting and decrypting PDF files
* and more!

%package -n python3-module-%oname
Summary: A utility to read and write PDFs with Python
Group: Development/Python3
Requires: python3-module-Reportlab

%description -n python3-module-%oname
A Pure-Python library built as a PDF toolkit. It is capable of:

* extracting document information (title, author, ...)
* splitting documents page by page
* merging documents page by page
* cropping pages
* merging multiple pages into a single page
* encrypting and decrypting PDF files
* and more!

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc CHANGELOG *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.md
%python3_sitelibdir/*
%endif

%changelog
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

