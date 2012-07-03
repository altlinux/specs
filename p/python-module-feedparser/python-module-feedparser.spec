Name: python-module-feedparser
Version: 4.1
Release: alt1.1
Epoch: 1

%define sname feedparser

Summary: Universal feed parser for Python
Group: Development/Python
License: BSD-style
Url: http://feedparser.org/
BuildArch: noarch

%setup_python_module feedparser

# http://%sname.googlecode.com/files/%sname-%version.zip
Source: %sname-%version.tar

Patch1: feedparser-deb-utf8-decoding.patch
Patch2: feedparser-deb-title-override.patch
Patch3: feedparser-deb-contentType.patch
Patch4: feedparser-deb-auth-handlers.patch
Patch5: feedparser-deb-doc-css-path.patch
Patch6: feedparser-deb-etag.patch

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
Requires: %name = %version-%release

%description doc
This package contains documentation for the Universal feed parser.

%prep
%setup -n %sname-%version
find -type f -print0 |
	xargs -r0 sed -i 's/\r//' --
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%python_build

%install
%python_install

%define docdir %_docdir/%name
mkdir -p %buildroot/%docdir
install -pm644 LICENSE README %buildroot/%docdir/
cp -a docs %buildroot/%docdir/html
rm %buildroot/%docdir/html/examples/.ht*

%files
%python_sitelibdir/*
%dir %docdir
%docdir/[RL]*

%files doc
%dir %docdir
%docdir/html

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:4.1-alt1.1
- Rebuild with Python-2.7

* Mon Feb 01 2010 Dmitry V. Levin <ldv@altlinux.org> 1:4.1-alt1
- Initial revision.
