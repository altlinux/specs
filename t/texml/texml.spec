%define version 2.0.2
%define release alt2

%setup_python_module texml

Summary: TeXML: an XML syntax for TeX (LaTeX, ConTeXt)
Name: texml
Version: %version
Release: %release
Source: %modulename-%version.tar
License: MIT
Group: Publishing
BuildArch: noarch
Url: http://getfo.org/texml/

BuildRequires: python-devel python-modules-compiler
BuildRequires: python-modules-encodings python-modules-xml

%description
TeXML is an XML syntax for TeX. The processor transforms the TeXML
markup into the TeX markup, escaping special and out-of-encoding
characters. The intended audience is developers who automatically
generate [La]TeX or ConTeXt files.

%prep
%setup

%build
%python_build_debug
               
%install
%python_build_install --optimize=2 \
                          --record=INSTALLED_FILES
# texml.1 may be compressed, INSTALLED_FILES becomes incorrect
sed -i 's/texml.1/texml.1*/' INSTALLED_FILES

%files -f INSTALLED_FILES
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/texml-%version

%changelog
* Tue Oct 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.2-alt2
- Updated spec to allow any man page compression.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.2-alt1.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.2
- Rebuilt with python 2.6

* Thu Nov 19 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.0.1-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for texml
  * postclean-05-filetriggers for spec file

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 2.0.1-alt1.1
- Rebuilt with python-2.5.

* Thu Jul 20 2006 Oleg Parashchenko <olpa@altlinux.ru> 2.0.1-alt1
- New TeXML version.

* Tue Jul 11 2006 Oleg Parashchenko <olpa@altlinux.ru> 2.0.0-alt2
- Field "Packager" is added to spec-file.

* Mon Jul 10 2006 Oleg Parashchenko <olpa@altlinux.ru> 2.0.0-alt1
- Initial build.
