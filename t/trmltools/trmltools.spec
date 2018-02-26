Name: trmltools
Summary: Tools to convert rml to pdf and html
Version: 1.1
Release: alt9.16.1.1
Source: trml2pdf-%version.tar.bz2
License: BSD-like
Group: Development/Python
Url: http://www.openreport.org

BuildArch: noarch
BuildRequires: rpm-build-python >= 0.8
BuildRequires: python-devel

Packager: Ilya Mashkin <oddity@altlinux.ru>

%{!?python_sitelib: %define python_sitelib %(%__python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}


Requires: python-module-Reportlab python-module-imaging

%description
Tools to convert rml files to pdf and html und Schweinsbacken

%prep
%setup -q -n trml2pdf-%version

%build
%install

install -d %buildroot/%python_sitelibdir
cp -rf trml2pdf %buildroot/%python_sitelibdir/

install -d %buildroot/%_bindir
ln -s -f %python_sitelibdir/trml2pdf/trml2pdf.py %buildroot/%_bindir/trml2pdf
chmod 775 %buildroot/%python_sitelibdir/trml2pdf/trml2pdf.py

%files
%_bindir/trml2pdf
%python_sitelibdir/trml2pdf
%doc rmls

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt9.16.1.1
- Rebuild with Python-2.7

* Thu Nov 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt9.16.1
- Rebuilt with python 2.6

* Sat Nov 22 2008 Ilya Mashkin <oddity@altlinux.ru> 1.1-alt9.16
- Initial Build for ALT Linux
