%define oname xhtml2pdf

Name: python-module-%oname
Version: 0.2.2
Release: alt1
Summary: HTML/CSS to PDF converter based on Python
License: ASLv2.0
Group: Development/Python
Url: http://www.xhtml2pdf.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/chrisglass/xhtml2pdf.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose

Conflicts: python-module-pisa

%description
xhtml2pdf is a html2pdf converter using the ReportLab Toolkit, the
HTML5lib and pyPdf. It supports HTML 5 and CSS 2.1 (and some of CSS 3).
It is completely written in pure Python so it is platform independent.

The main benefit of this tool that a user with Web skills like HTML and
CSS is able to generate PDF templates very quickly without learning new
technologies.

%package demos
Summary: Demos for %oname
Group: Development/Documentation
Requires: python3-module-%oname = %EVR

%description demos
xhtml2pdf is a html2pdf converter using the ReportLab Toolkit, the
HTML5lib and pyPdf. It supports HTML 5 and CSS 2.1 (and some of CSS 3).
It is completely written in pure Python so it is platform independent.

The main benefit of this tool that a user with Web skills like HTML and
CSS is able to generate PDF templates very quickly without learning new
technologies.

This package contains demos for %oname.

%package -n python3-module-%oname
Summary: HTML/CSS to PDF converter based on Python
Group: Development/Python3
Requires: python3-module-PyPDF2

%description -n python3-module-%oname
xhtml2pdf is a html2pdf converter using the ReportLab Toolkit, the
HTML5lib and pyPdf. It supports HTML 5 and CSS 2.1 (and some of CSS 3).
It is completely written in pure Python so it is platform independent.

The main benefit of this tool that a user with Web skills like HTML and
CSS is able to generate PDF templates very quickly without learning new
technologies.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files -n python3-module-%oname
%doc *.txt *.rst doc/*
%_bindir/*
%python3_sitelibdir/*

%files demos
%doc demo/*

%changelog
* Mon Sep 23 2019 Anton Farygin <rider@altlinux.ru> 0.2.2-alt1
- up to 0.2.2
- removed python-2.7 support 

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.6-alt1.git20140628.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.6-alt1.git20140628.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20140628
- Initial build for Sisyphus

