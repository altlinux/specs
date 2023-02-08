%define oname xhtml2pdf

%def_with check

Name: python3-module-%oname
Version: 0.2.9
Release: alt1

Summary: HTML/CSS to PDF converter based on Python

License: Apache-2.0
Group: Development/Python3
Url: http://www.xhtml2pdf.com/

# https://github.com/chrisglass/xhtml2pdf.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-html5lib
Buildrequires: python3-module-Reportlab
Buildrequires: python3-module-asn1crypto
BuildRequires: python3-module-arabic-reshaper
BuildRequires: python3-module-bidi
BuildRequires: python3-module-pypdf
BuildRequires: python3-module-pyHanko
BuildRequires: python3-module-Pillow
%endif

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

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v

%files
%doc *.txt *.rst
%_bindir/pisa
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%files demos
%doc demo/*

%changelog
* Tue Jan 31 2023 Grigory Ustinov <grenka@altlinux.org> 0.2.9-alt1
- Automatically updated to 0.2.9.

* Mon Jun 27 2022 Grigory Ustinov <grenka@altlinux.org> 0.2.8-alt1
- Build new version.

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.2.2-alt2
- Rename package.

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

