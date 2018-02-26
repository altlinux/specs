%define oname xappy
Name: python-module-%oname
Version: 0.6.0
Release: alt1.svn20110316
Summary: Easy-to-use interface to the Xapian search engine
License: GPL
Group: Development/Python
Url: http://pypi.python.org/pypi/xappy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://xappy.googlecode.com/svn/trunk/
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
The "xappy" python module is an easy-to-use interface to the Xapian
search engine. Xapian provides a low level interface, dealing with terms
and documents, but not really worrying about where terms come from, or
how to build searches to match the way in which data has been indexed.
In contrast, "xappy" allows you to design a field structure, specifying
what kind of information is held in particular fields, and then uses
this field structure to index data appropriately, and to build and
perform searches.

%package docs
Summary: Documentation for xappy
Group: Development/Documentation

%description docs
The "xappy" python module is an easy-to-use interface to the Xapian
search engine. Xapian provides a low level interface, dealing with terms
and documents, but not really worrying about where terms come from, or
how to build searches to match the way in which data has been indexed.
In contrast, "xappy" allows you to design a field structure, specifying
what kind of information is held in particular fields, and then uses
this field structure to index data appropriately, and to build and
perform searches.

This package contains documentation for xappy.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc AUTHORS ChangeLog README
%python_sitelibdir/*

%files docs
%doc docs/* examples

%changelog
* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.svn20110316
- Version 0.6.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.1
- Rebuild with Python-2.7

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus

