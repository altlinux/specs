Summary: Edward Loper's API Documentation Generation Tool
Version: 3.0.1
Release: alt2.1
Epoch: 1
%setup_python_module epydoc
Source0: http://downloads.sourceforge.net/epydoc/%modulename-%version.tar.gz
Name: %packagename
License: MIT
Group: Development/Python
BuildArch: noarch
Url: http://epydoc.sourceforge.net
Packager: Fr. Br. George <george@altlinux.ru>

Patch0: epydoc-docutils-0.6.patch
Patch1: epydoc-python-2.6.patch

%description
Epydoc is a tool for generating API documentation for Python modules, based on their docstrings. For an example of epydoc's output, see the API documentation for epydoc itself (html, pdf). A lightweight markup language called epytext can be used to format docstrings, and to add information about specific fields, such as parameters and instance variables. Epydoc also understands docstrings written in ReStructuredText, Javadoc, and plaintext.

%prep
%setup -q -n %modulename-%version
%patch0 -p1
%patch1 -p1

%build
python setup.py build

%install
python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
mkdir -p %buildroot/%_man1dir
install man/*.1 %buildroot/%_man1dir/

%files -f INSTALLED_FILES
%doc doc
%_man1dir/*

%changelog
* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:3.0.1-alt2.1
- Rebuild with Python-2.7

* Sat Mar 06 2010 Evgeny Sinelnikov <sin@altlinux.ru> 1:3.0.1-alt2
- Add fixes from Gentoo (#287546, #288273)

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.1-alt1.qa1.1
- Rebuilt with python 2.6

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1:3.0.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for python-module-epydoc
  * postclean-05-filetriggers for spec file

* Sat Jan 10 2009 Fr. Br. George <george@altlinux.ru> 1:3.0.1-alt1
- Version up
- Previous version was ALPHA, too bad

* Sat Jul 29 2006 Fr. Br. George <george@altlinux.ru> 3.0alpha2-alt1
- Initial ALT build

