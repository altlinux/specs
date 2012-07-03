%define major 1

Name: libparsifal
Version: 1.1.0
Release: alt4
Summary: Parsifal is a validating XML 1.0 parser based on SAX2
License: Public
Group: System/Libraries
Url: http://www.saunalahti.fi/~samiuus/toni/xmlproc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.saunalahti.fi/~samiuus/toni/xmlproc/libparsifal-1.1.0.tar.gz

%description
Parsifal can be used for parsing XML based messages (such as REST and RSS) and
for application specific data processing e.g. config files, data files etc.
Parsifal can also be used for document-oriented processing (e.g. XHTML
xhtml1-transitional.dtd) and for parsing modular documents because it is
conforming XML 1.0 parser and it supports features like internal and external
general entities, DTD parameter entities and default attributes etc. Parsifal is
ideal for processing large data files and streams since it's SAX based and
consumes very little memory not to mention it is fast enough for most purposes
'cos it's written in C.

Using Parsifal in place of large XML processing libraries (e.g. libxml, xerces)
or even in the place of small Expat (which doesn't support DTD validation) can
be justified for limited memory environments and in applications requiring
bundled parser; because of its modular design parsifal can be easily compiled to
support DTD validation or to perform only non-validating parsing etc. If you
need higher level tools, for example dom/xpath processing, you should look for
other libs of course.

%package devel
Summary: Development files for Parsifal XML parser
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for Parsifal XML parser.

%package devel-static
Summary: Static development files for Parsifal XML parser
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static development files for Parsifal XML parser.

%package doc
Summary: Documentation for Parsifal XML parser
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation for Parsifal XML parser.

%prep
%setup

%build
%autoreconf
%configure --with-gnu-ld
%make_build

%install
%makeinstall_std

install -d %buildroot%_docdir/%name
cp -fR doc/* %buildroot%_docdir/%name/ 

%files
%doc AUTHORS BUGS ChangeLog NEWS TODO COPYING
%_libdir/%name-%version.so

%files devel
%doc APIChanges
%_libdir/%name.so
%_includedir/*

%files devel-static
%_libdir/*.a

%files doc
%_docdir/%name

%changelog
* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt4
- Rebuilt for debuginfo

* Mon Oct 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt3
- Rebuilt without rpm-build-compat

* Fri Apr 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Remove dependence on libiconv

* Mon Apr 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
