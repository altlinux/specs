%define origname htmlgen

Name:           python-module-HTMLgen
Version:        2.2.2
Release:        alt2.1.1
Summary:        class library to create HTML documents from within Python
Group:          Development/Python
License:        BSD
URL:            http://starship.python.net/crew/friedrich/HTMLgen/html/main.html
Source0:        %origname-%version.tar.gz
Source1:	%origname.__init__.py
Patch0:		%origname.alt.patch
Packager:	Mikhail Pokidko <pma@altlinux.org>
BuildArch:      noarch

Requires:	python-module-imaging
Provides:       python-module-HTMLgen

# Automatically added by buildreq on Tue Mar 25 2008
BuildRequires: python-base python-modules-compiler

%description
HTMLgen is a class library for the generation of HTML documents with
Python scripts. It's used when you want to create HTML pages
containing information which changes from time to time. For example
you might want to have a page which provides an overall system summary
of data collected nightly. Or maybe you have a catalog of data and
images that you would like formed into a spiffy set of web pages for
the world to browse. Python is a great scripting language for these
tasks and with HTMLgen it's very straightforward to construct objects
which are rendered out into consistently structured web pages. Of
course, CGI scripts written in Python can take advantage of these
classes as well.

This software should work on both Unix and Macintosh and Win32
platforms running Python 1.3 or greater. (HTMLcalendar.py requires
1.4) If you are running 1.5 the new re and string module enhancements
are used for performance.

%prep
%setup -n %origname-%version.orig -q
%patch -p1

%build

%install
mkdir -p %buildroot%python_sitelibdir/HTMLgen
install -m 555 *.py %buildroot%python_sitelibdir/HTMLgen/
install -m 555 *.rc %buildroot%python_sitelibdir/HTMLgen/
install -m 644 %SOURCE1 %buildroot%python_sitelibdir/HTMLgen/__init__.py
python -c 'import compileall;compileall.compile_dir("%buildroot%python_sitelibdir/HTMLgen/")'
python -O -c 'import compileall;compileall.compile_dir("%buildroot%python_sitelibdir/HTMLgen/")'

%files
%doc data html image README ChangeLog HTML.rc HTMLgen.rc
%python_sitelibdir/HTMLgen/*
#python_sitelibdir/HTMLgen/*.pyo

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.2-alt2.1.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt2.1
- Rebuilt with python 2.6

* Tue Apr 08 2008 Mikhail Pokidko <pma@altlinux.org> 2.2.2-alt2
- "link stylesheet" patch changes

* Tue Mar 18 2008 Mikhail Pokidko <pma@altlinux.org> 2.2.2-alt1
- Initial ALT build
  + __init__.py : make HTMLgen importable
  + patch : make HTMLgen compatible with modern python


