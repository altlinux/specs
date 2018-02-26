# -*- mode: rpm-spec; coding: utf-8 -*-
%define version 0.9.9
%define release    alt1.1
%define source_version 0.9.9
%define source_name Pyrex
%setup_python_module Pyrex

%add_python_req_skip Pyrex

Summary: A language for writing Python extension modules
Name: python-module-Pyrex
Version: %version
Release: %release
Source: %source_name-%source_version.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
License: Freeware
Group: Development/Python
Prefix: %_prefix
Url: http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/
BuildPreReq: rpm-build-python
BuildArch: noarch

Requires: %name-pickles = %version-%release

%description
Pyrex  is  a  language  specially designed for writing Python extension
modules.  It's designed to bridge the gap between the nice, high-level,
easy-to-use world of Python and the messy, low-level world of C.

%package pickles
Summary: Pickle file for Pyrex
Group: Development/Python
BuildArch: noarch

%description pickles
Pyrex  is  a  language  specially designed for writing Python extension
modules.  It's designed to bridge the gap between the nice, high-level,
easy-to-use world of Python and the messy, low-level world of C.

This package contains pickle file for Pyrex.

%prep
%setup -q -n %source_name-%source_version

%build
%python_build

%install
CFLAGS="%optflags" python setup.py \
	install --optimize=2 \
		--root=%buildroot \
		--record=INSTALLED_FILES

# fool the ALT building system a little to avoid dependency on 
# python-strict :-)
subst 's/^#!.*\/python\([ 	].*\)\?$/#!\/usr\/bin\/env python%_python_version\1/' \
	%buildroot%_bindir/*

# Remove Mac-specific stuff
subst '/\/Mac\//d' INSTALLED_FILES
# Remove test file
subst '/\/Plex\/test/d' INSTALLED_FILES

%files -f INSTALLED_FILES
%doc README.txt ToDo.txt USAGE.txt CHANGES.txt Doc Demos
%dir %python_sitelibdir/Pyrex
%dir %python_sitelibdir/Pyrex/Compiler
%exclude %python_sitelibdir/Pyrex/Compiler/*.pickle
%dir %python_sitelibdir/Pyrex/Distutils
%dir %python_sitelibdir/Pyrex/DistutilsOld
%dir %python_sitelibdir/Pyrex/Plex
%dir %python_sitelibdir/Pyrex/Unix

%files pickles
%python_sitelibdir/Pyrex/Compiler/*.pickle

%changelog
* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt1.1
- Rebuild with Python-2.7

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1
- Version 0.9.9

* Tue Mar 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.6-alt1
- Version 0.9.8.6

* Thu Feb 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.5-alt6
- Moved pickle into separate package

* Tue Feb 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.5-alt5
- Fixed message format in LinuxSystem.py

* Fri Jan 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.5-alt4
- Fixed noarch build for x86_64 without hacking spec

* Fri Nov 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.5-alt3
- Rebuilt with python 2.6

* Thu Sep 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.5-alt2
- Rebuild as noarch package

* Wed Nov 26 2008 Anton Farygin <rider@altlinux.ru> 0.9.8.5-alt1
- new version

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.9.4.1-alt1.1.1.1
- Rebuilt with python-2.5.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.9.4.1-alt1.1.1
- Rebuilt using rpm-build-python-0.29-alt4.

* Fri May 19 2006 Anton Farygin <rider@altlinux.ru> 0.9.4.1-alt1.1
- new version

* Tue Mar 29 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.9.3-alt2.1
- Rebuilt with python-2.4.

* Fri Jan 21 2005 Alexey Morozov <morozov@altlinux.org> 0.9.3-alt2
- Rebuild against current rpm-build-python (0.20-alt1)
- Fixed python script binding to a version of python used to build the package

* Tue Sep  7 2004 Alexey Morozov <morozov@altlinux.org> 0.9.3-alt1
- Initial build for ALT Linux
