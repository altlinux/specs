%def_disable snapshot
%define modname feedparser
%def_without doc
# tests not ready for python3
%def_disable check

Name: python3-module-%modname
Version: 5.2.1
Release: alt1

Summary: Universal feed parser for Python
Group: Development/Python3
License: BSD-style
Url: https://github.com/kurtmckee/%modname

BuildArch: noarch

BuildRequires: rpm-build-python3 python3-module-setuptools
%{?_with_doc:BuildRequires: python3-module-sphinx python3-module-requests}

%if_disabled snapshot
Source: https://pypi.io/packages/source/f/%modname/%modname-%version.tar.gz
%else
Source: %modname-%version.tar
%endif
Patch: feedparser-5.1.3-fc-tests-py3.patch

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
%setup -n %modname-%version
%patch -p1

find -type f -print0 |
	xargs -r0 sed -i 's/\r//' --

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
# this test may fail, disable it
rm -f feedparser/tests/illformed/chardet/big5.xml

cd %modname
PYTHONPATH=%buildroot%python3_sitelibdir %__python3 feedparsertest.py

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
* Sat Feb 17 2018 Yuri N. Sedunov <aris@altlinux.org> 5.2.1-alt1
- first build for Sisyphus

