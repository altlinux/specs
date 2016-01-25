Name: python3-module-feedparser
Version: 5.2.0
Release: alt2.git20150416

%define sname feedparser
%def_without doc
%def_disable check

Summary: Universal feed parser for Python
Group: Development/Python3
License: BSD-style
Url: http://feedparser.org/
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python-tools-2to3
%{?_with_doc:BuildRequires: python3-module-sphinx}

# https://github.com/kurtmckee/feedparser.git
# branch: develop
Source: %sname-%version.tar

%description
Universal feed parser is a Python module for downloading and parsing
syndicated feeds.  It can handle RSS 0.90, Netscape RSS 0.91,
Userland RSS 0.91, RSS 0.92, RSS 0.93, RSS 0.94, RSS 1.0, RSS 2.0,
Atom 0.3, Atom 1.0, and CDF feeds.  It also parses several popular
extension modules, including Dublin Core and Apple's iTunes extensions.
It provides the same API to all formats, and sanitizes URIs and HTML.

%package doc
Summary: Documentation for the Universal feed parser for Python
Group: Development/Python
Requires: %name = %EVR

%description doc
This package contains documentation for the Universal feed parser.

%prep
%setup -n %sname-%version
find -type f -print0 |
	xargs -r0 sed -i 's/\r//' --
mv feedparser/sgmllib3.py feedparser/sgmllib3.py.bak
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
mv feedparser/sgmllib3.py.bak feedparser/sgmllib3.py

%build
%python3_build
%{?_with_doc:py3_sphinx-build -b html docs html}

%install
%python3_install

%define docdir %_docdir/%name
mkdir -p %buildroot%docdir
install -pm644 LICENSE NEWS README.rst %buildroot%docdir/
%{?_with_doc:cp -a html %buildroot%docdir/}

%check
cd %sname
PYTHONPATH=%buildroot%python3_sitelibdir python3 feedparsertest.py -v

%files
%python3_sitelibdir/*
%dir %docdir
%docdir/[LNR]*

%if_with doc
%files doc
%dir %docdir
%docdir/html
%endif

%changelog
* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 5.2.0-alt2.git20150416
- build without tests and docs

* Thu Apr 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2.0-alt1.git20150416
- Initial build for Sisyphus

