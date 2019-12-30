%define oname xappy

Name: python3-module-%oname
Version: 0.6.0
Release: alt2

Summary: Easy-to-use interface to the Xapian search engine
License: GPL
Group: Development/Python3
Url: http://pypi.python.org/pypi/xappy/
BuildArch: noarch

# http://xappy.googlecode.com/svn/trunk/
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


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
%patch0 -p1

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python.*|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%doc AUTHORS ChangeLog README
%python3_sitelibdir/*

%files docs
%doc docs/* examples


%changelog
* Mon Dec 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6.0-alt2
- porting on python3

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.svn20110316
- Version 0.6.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.1
- Rebuild with Python-2.7

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus

