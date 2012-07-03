%define oname SimpleParse
Name: python-module-simpleparse
Version: 2.1.0a1
Release: alt2.1.1.1

Summary: A Parser Generator for Python (w/mxTextTools derivative)

Group: Development/Python
License: BSD-like
Url: http://simpleparse.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://downloads.sourceforge.net/simpleparse/%oname-%version.tar.gz
Patch0: %name-2.1.0a1-alt-python2.6.patch

%setup_python_module %oname

%description
Provides a moderately fast parser generator for use with Python,
includes a forked version of the mxTextTools text-processing library
modified to eliminate recursive operation and fix a number of
undesirable behaviours.

Converts EBNF grammars directly to single-pass parsers for many
largely deterministic grammars.

%prep
%setup -n %oname-%version
%patch0 -p1

%build
%python_build

%install
%python_install

%files
%doc license.txt
%python_sitelibdir/simpleparse/
%python_sitelibdir/*.egg-info

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.0a1-alt2.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.0a1-alt2.1.1
- Rebuild with Python-2.7

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0a1-alt2.1
- Rebuilt with python 2.6

* Fri Nov 06 2009 Vitaly Lipatov <lav@altlinux.ru> 2.1.0a1-alt2
- cleanup spec, pack egg info file

* Mon Jul 27 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.1.0a1-alt2
- fix incompatibility with python2.6

* Mon Dec 01 2008 Vitaly Lipatov <lav@altlinux.ru> 2.1.0a1-alt1
- initial build for ALT Linux Sisyphus
