Name: python-module-CDDB
Version: 1.4
Release: alt1.2.1.1

Summary: Fetch information about audio cd's
License: GPL
Group: Sound
URL: http://cddb-py.sourceforge.net/

Source0: http://dl.sf.net/cddb-py/CDDB-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Wed May 28 2008 (-bi)
BuildRequires: python-devel

%description
This is a set of three modules to access the CDDB and FreeDB online
databases of audio CD track titles and information.

%prep
%setup -n CDDB-%version

%build
%python_build_debug

%install
%python_build_install --optimize=2 \
		--record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc CHANGES README

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4-alt1.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4-alt1.2.1
- Rebuild with Python-2.7

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.2
- Rebuilt for debuginfo

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.1
- Rebuilt with python 2.6

* Wed May 28 2008 Igor Zubkov <icesik@altlinux.org> 1.4-alt1
- build for Sisyphus

