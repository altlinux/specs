%define oname cx-freeze

Name: python3-module-%oname
Version: 6.1
Release: alt1

Summary: Scripts and modules for freezing Python scripts into executables
License: PSF
Group: Development/Python3
URL: http://cx-freeze.sourceforge.net/

Source: %oname-%version.tar.bz2

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx chrpath

Conflicts: python-module-%oname
Provides: cx_Freeze

%add_python3_req_skip BUILD_CONSTANTS


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

sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile

%build
%python3_build_debug

%make -C doc html

%install
%python3_install

rm -f $(find %buildroot -name 'windist*')

for i in $(find %buildroot%python3_sitelibdir/cx_Freeze/ -type d)
do
    touch $i/__init__.py
done

for i in %buildroot%python3_sitelibdir/cx_Freeze/bases/Console*
do
    chrpath -d $i
done

%files
%doc README.md doc/build/html/*
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/samples

%files samples
%doc cx_Freeze/samples


%changelog
* Mon Feb 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 6.1-alt1
- Version updated to 6.1
- build for python2 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0-alt1.hg20141226.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.0-alt1.hg20141226.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 5.0-alt1.hg20141226.1
- NMU: Use buildreq for BR.

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt1.hg20141226
- Version 5.0

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.3-alt1.hg20140508
- Version 4.3.3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt1.svn20131105
- Version 4.3.2

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.3-alt4.svn20120223
- Use 'find... -exec...' instead of 'for ... $(find...'

* Sat Mar 23 2013 Aleksey Avdeev <solo@altlinux.ru> 4.2.3-alt3.svn20120223.1
- Rebuild with Python-3.3

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

