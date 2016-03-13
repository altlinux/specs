%define oname xhtml2pdf

%def_with python3

Name: python-module-%oname
Version: 0.0.6
Release: alt1.git20140628.1
Summary: HTML/CSS to PDF converter based on Python
License: ASLv2.0
Group: Development/Python
Url: http://www.xhtml2pdf.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/chrisglass/xhtml2pdf.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

Conflicts: python-module-pisa
Requires: python-module-PyPDF2

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
Requires: %name = %EVR

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

%if_with python3
cp -fR . ../python3
mv ../python3/test/witherror.py ../python3/test/witherror.bak
#find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
for i in $(find ../python3 -type f -name '*.py'); do
	echo file: $i
	2to3 -w -n $i
done
mv ../python3/test/witherror.bak ../python3/test/witherror.py
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%files
%doc *.txt *.rst doc/*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%files demos
%doc demo/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst doc/*
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.6-alt1.git20140628.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20140628
- Initial build for Sisyphus

