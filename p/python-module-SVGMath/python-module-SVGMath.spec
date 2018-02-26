%define oname SVGMath
Name: python-module-%oname
Version: 0.3.3
Release: alt3.1

Summary: MathML to SVG Converter in Python

Group: Development/Python
License: MIT
Url: http://grigoriev.ru/svgmath/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: http://dl.sf.net/svgmath/%oname-%version.tar.bz2

%setup_python_module %oname

%description
SVGMath formats MathML 2.0 expressions as SVG 1.1 images.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%doc README.txt LICENSE.txt
%python_sitelibdir/svgmath/

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.3-alt3.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt3
- Rebuilt with python 2.6

* Mon Feb 23 2009 Vitaly Lipatov <lav@altlinux.ru> 0.3.3-alt2
- cleanup spec, build as noarch (thanks to Dmitry Levin)

* Wed Apr 23 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3.3-alt1
- new version 0.3.3 (with rpmrb script)

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt1
- initial build for ALT Linux Sisyphus
