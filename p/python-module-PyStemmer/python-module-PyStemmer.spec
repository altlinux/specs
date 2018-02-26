%define version 1.0.1
%define release alt1.2
%setup_python_module PyStemmer

Name: %packagename
Version:%version
Release: %release.1

Summary: Stemmer functionality in python

License: BSD
Group: Development/Python
Url: http://sourceforge.net/projects/pystemmer
Packager: Denis Klimov <zver@altlinux.org>

Source: %modulename-%version.tar

Provides: python-module-ruledispatch = %version-%release
Obsoletes: python-module-ruledispatch <= 0.5a0-alt0.1.1

%description
PyStemmer provides stemmer functionality in Python for English,
German, Norwegian, Italian, Dutch, Portuguese, French, Swedish.
PyStemmer is based on the Snowball stemmer (snowball.sourceforge.net) 

%prep
%setup -n %modulename-%version

%build
%python_build_debug

%install
%python_install

%files
%python_sitelibdir/Stemmer.so
%python_sitelibdir/%modulename-*.egg-info

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt1.2.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.2
- Rebuilt for debuginfo

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.1
- Rebuilt with python 2.6

* Fri Apr 17 2009 Denis Klimov <zver@altlinux.org> 1.0.1-alt1
- Initial build for ALT Linux

