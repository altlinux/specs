Version: 4.2.3
Release: alt3.svn20120223
%setup_python_module cx_Freeze
%define origname cx-freeze

%def_with python3

Name: python-module-%origname
Summary: Scripts and modules for freezing Python scripts into executables
License: PSF
URL: http://cx-freeze.sourceforge.net/
Provides: cx_Freeze
# https://cx-freeze.svn.sourceforge.net/svnroot/cx-freeze/trunk
Source: %origname-%version.tar.bz2
Group: Development/Python
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python-tools-2to3
%endif
AutoReq: yes, nopython

%py_provides cx_Freeze
#py_requires elementtree.ElementTree datetime decimal cairo gio
#py_requires pangocairo_git pango_git atk_git
#py_requires numpy wx PyQt4 sip
#py_requires _strptime xml.etree.ElementTree os
#py_requires zlib

%description
cx_Freeze is a set of scripts and modules for freezing Python scripts into
executables in much the same way that py2exe and py2app do. It requires Python
2.3 or higher since it makes use of the zip import facility which was introduced
in that version.

There are three different ways to use cx_Freeze. The first is to use the
included freeze script which works well for simple scripts. The second is to
create a distutils setup script which can be used for more complicated
configuration or to retain the configuration for future use. The third method
involves working directly with the classes and modules used internally by
cx_Freeze and should be reserved for complicated scripts or extending or
embedding.

There are three different options for producing executables as well. The first
option is the only one that was available in earlier versions of cx_Freeze, that
is appending the zip file to the executable itself. The second option is
creating a private zip file with the same name as the executable but with the
extension .zip. The final option is the default which is to create a zip file
called library.zip and place all modules in this zip file. The final two options
are necessary when creating an RPM since the RPM builder automatically strips
executables.

%if_with python3
%package -n python3-module-%origname
Summary: Scripts and modules for freezing Python 3 scripts into executables
Group: Development/Python
AutoReq: yes, nopython
%py_provides cx_Freeze

%description -n python3-module-%origname
cx_Freeze is a set of scripts and modules for freezing Python scripts into
executables in much the same way that py2exe and py2app do. It requires Python
2.3 or higher since it makes use of the zip import facility which was introduced
in that version.

There are three different ways to use cx_Freeze. The first is to use the
included freeze script which works well for simple scripts. The second is to
create a distutils setup script which can be used for more complicated
configuration or to retain the configuration for future use. The third method
involves working directly with the classes and modules used internally by
cx_Freeze and should be reserved for complicated scripts or extending or
embedding.

There are three different options for producing executables as well. The first
option is the only one that was available in earlier versions of cx_Freeze, that
is appending the zip file to the executable itself. The second option is
creating a private zip file with the same name as the executable but with the
extension .zip. The final option is the default which is to create a zip file
called library.zip and place all modules in this zip file. The final two options
are necessary when creating an RPM since the RPM builder automatically strips
executables.
%endif

%package samples
Summary: Samples for cx_Freeze
Group: Development/Documentation
BuildArch: noarch

%description samples
cx_Freeze is a set of scripts and modules for freezing Python scripts into
executables in much the same way that py2exe and py2app do. It requires Python
2.3 or higher since it makes use of the zip import facility which was introduced
in that version.

This package contains samples for cx_Freeze.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build_debug
%if_with python3
pushd ../python3
sed -i 's|\(libname =.*\)|\1 + "mu"|' setup.py
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install

for i in $(find %buildroot%python3_sitelibdir/cx_Freeze/ -type d)
do
	touch $i/__init__.py
done
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i py3_$i
done
popd
%endif

%python_install

for i in $(find %buildroot%python_sitelibdir/cx_Freeze/ -type d)
do
	touch $i/__init__.py
done

rm -f $(find %buildroot -name 'windist*')

%files
%doc *.txt doc/*.html
%_bindir/*
%if_with python3
%exclude %_bindir/py3_*
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/samples

%files samples
%doc samples

%if_with python3
%files -n python3-module-%origname
%doc *.txt doc/*.html
%_bindir/py3_*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/samples
%endif

%changelog
* Sat May 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.3-alt3.svn20120223
- New snapshot
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.2.3-alt2.svn20111130.1
- Rebuild to remove redundant libpython2.7 dependency

* Sun Dec 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.3-alt2.svn20111130
- New snapshot

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.3-alt2.svn20110414
- Fixed RPATH

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.2.3-alt1.svn20110414.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.3-alt1.svn20110414
- Version 4.2.3

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.2-alt1.svn20101121.2
- Rebuilt for debuginfo

* Wed Feb 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.2-alt1.svn20101121.1
- Minimized requirements

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.2-alt1.svn20101121
- Version 4.2.2

* Tue Jul 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1.svn20100723
- Version 4.2
- Requires pygtk_git modules

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt2.svn20090204.1
- Rebuilt with python 2.6

* Sun Jul 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt2.svn20090204
- Replaced build commands by macros

* Wed Feb 04 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 4.0.1-alt1.svn20090204
- Initial build for Sisyphus

