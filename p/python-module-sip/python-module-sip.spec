%define oname sip

%def_with python3

Name: python-module-%oname
Version: 4.13.2
Release: alt3
Summary: Python bindings generator for C++ class libraries
License: PSF
Group: Development/Python

%setup_python_module sip

Source0: %modulename.tar

URL: http://www.riverbankcomputing.com/software/sip/
Packager: Python Development Team <python@packages.altlinux.org>

Provides: %modulename = %version-%release
Obsoletes: %modulename <= 4.1-alt2.1

BuildPreReq: gcc-c++
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
Generates Python bindings for C++ class libraries from a set of class
specification files.  Also includes a Python extension module needed by all
generated bindings.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 bindings generator for C++ class libraries
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Generates Python bindings for C++ class libraries from a set of class
specification files.  Also includes a Python extension module needed by all
generated bindings.

%package -n python3-module-%oname-devel
Requires: python3-module-%oname = %version-%release
Summary: Header files for sip (Python 3)
Group: Development/Python3
BuildArch: noarch
Requires: python3-devel

%description -n python3-module-%oname-devel
Header files for sip
%endif

%package devel
Requires: %name = %version-%release
Summary: Header files for sip
Group: Development/Python
BuildArch: noarch
Provides: %modulename-devel = %version-%release
%py_package_provides %modulename-devel = %version-%release
Obsoletes: %modulename-devel
Requires: python-devel

%description devel
Header files for sip

%prep
%setup -n %modulename
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
python configure.py --debug -d %python_sitelibdir
sed -i 's|^\(CPPFLAGS.*\)|\1 -g -I%python_includedir|' */Makefile
%make

%if_with python3
pushd ../python3
python3 configure.py --debug -d %python3_sitelibdir
sed -i \
	's|^\(CPPFLAGS.*\)|\1 -g -I%{python3_includedir}mu|' \
	*/Makefile
sed -i \
	's|lpython%_python3_version|lpython%{_python3_version}mu|' \
	siplib/Makefile
%make
popd
%endif

%install
%if_with python3
pushd ../python3
%makeinstall_std
popd
mv %buildroot%_bindir/sip %buildroot%_bindir/sip3
sed -i 's|%_datadir/sip|%_datadir/sip3|' \
	%buildroot%python3_sitelibdir/sipconfig.py
sed -i 's|%_bindir/sip|%_bindir/sip3|' \
	%buildroot%python3_sitelibdir/sipconfig.py
%endif
%makeinstall_std

%files
%_bindir/*
%exclude %_bindir/sip3
%python_sitelibdir/*
%doc README NEWS LICENSE*

%files devel
%python_includedir/*
%doc doc/*

%if_with python3
%files -n python3-module-%oname
%doc README NEWS LICENSE*
%_bindir/sip3
%python3_sitelibdir/*

%files -n python3-module-%oname-devel
%{python3_includedir}mu/*
%doc doc/*
%endif

%changelog
* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.13.2-alt3
- Fixed config for python3-module-sip

* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.13.2-alt2
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.13.2-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.13.2-alt1
- Version 4.13.2

* Tue Jan 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.13.1-alt1
- Version 4.13.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.12.3-alt1.1
- Rebuild with Python-2.7

* Sun Jul 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.12.3-alt1
- Version 4.12.3

* Sun Mar 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.12.1-alt2
- Rebuilt for debuginfo

* Mon Jan 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.12.1-alt1
- Version 4.12.1 (ALT #24999)

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.11.2-alt1
- Version 4.11.2

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.5-alt2
- Set devel package as noarch

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.5-alt1
- Version 4.10.5

* Tue Jan 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10-alt1
- Version 4.10

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8.2-alt1.1
- Rebuilt with python 2.6

* Wed Aug 26 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.8.2-alt1
- Update to new release

* Mon Jul 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.8.1-alt1
- Update to new release

* Tue Nov 25 2008 Evgeny Sinelnikov <sin@altlinux.ru> 4.7.9-alt1
- New version

* Sun Aug 17 2008 Evgeny Sinelnikov <sin@altlinux.ru> 4.7.6-alt3
- Fixed rpath problem and libpython linking (#14655)

* Tue Aug 05 2008 Evgeny Sinelnikov <sin@altlinux.ru> 4.7.6-alt2
- Push rlz@ build to Sisyphus

* Sat Jun 07 2008 Dmitry M. Maslennikov <rlz at altlinux.org> 4.7.6-alt1
- New version

* Tue Jan 01 2008 Ivan Fedorov <ns@altlinux.org> 4.7.3-alt1
- 4.7.3

* Mon Aug 20 2007 Ivan Fedorov <ns@altlinux.org> 4.7-alt1
- 4.7

* Fri Jul 13 2007 Ivan Fedorov <ns@altlinux.org> 4.6-alt1
- 4.6
- Added support for wchar_t.
- The -g command line option releases the GIL whenever a call is made to
  the wrapped library.
- Added the /HoldGIL/ annotation to explicitly retain the GIL when
  calling a particular function in the wrapped library.
- Added sipFindClass() and sipFindNamedEnum() to the public API.
- /TransferThis/ may be specified more than once.
- Added support for __truediv__ and __itruediv__.
- The SIP code generator and module may be built as universal binaries
  under MacOS/X using the -n command line option to configure.py.

* Thu Dec 28 2006 Ivan Fedorov <ns@altlinux.ru> 4.5.2-alt1
- 4.5.2
- spec clean up (rewrite buildreqs)

* Thu Nov 09 2006 Ivan Fedorov <ns@altlinux.ru> 4.5-alt1
- 4.5

* Mon Jun 12 2006 Ivan Fedorov <ns@altlinux.ru> 4.4.5-alt1
- 4.4.5

* Sun May 28 2006 Ivan Fedorov <ns@altlinux.ru> 4.4.3-alt1
- 4.4.3
- fix #9616

* Sun Apr 09 2006 Ivan Fedorov <ns@altlinux.ru> 4.4.1-alt1
- 4.4.1

* Sun Apr 09 2006 Ivan Fedorov <ns@altlinux.ru> 4.4-alt1
- 4.4

* Mon Mar 06 2006 Alexey Morozov <almorozov@altlinux.org> 4.3.2-alt1.0.1
- NMU: fixed provides list for -devel subpackage
- changed XFree86-devel to xorg-x11-devel

* Wed Dec 07 2005 Ivan Fedorov <ns@altlinux.ru> 4.3.2-alt1
- 4.3.2

* Sat Nov 05 2005 Ivan Fedorov <ns@altlinux.ru> 4.3.1-alt1
- 4.3.1

* Sat Mar 12 2005 Ivan Fedorov <ns@altlinux.ru> 4.2.1-alt1
- 4.2.1
- rebuild with python 2.4

* Mon Feb 21 2005 Ivan Fedorov <ns@altlinux.ru> 4.2-alt1
- 4.2

* Thu Jan 27 2005 Ivan Fedorov <ns@altlinux.ru> 4.1.1-alt2
- updating obsoleting of sip

* Tue Jan 04 2005 Ivan Fedorov <ns@altlinux.ru> 4.1.1-alt0.M24.1
- Backport to Master 2.4

* Wed Dec 22 2004 Ivan Fedorov <ns@altlinux.ru> 4.1.1-alt1
- 4.1.1

* Sun Dec 12 2004 Ivan Fedorov <ns@altlinux.ru> 4.1-alt3
- fix spec to be compatible with python policy

* Tue Sep 28 2004 Eugene V. Horohorin <genix@altlinux.ru> 4.1-alt2
- license mistake fix
- spec clean up (using %%python_site_packages_dir instead of old method of %%python_site)

* Tue Sep 21 2004 Eugene V. Horohorin <genix@altlinux.org> 4.1-alt1
- new release

* Thu Sep 02 2004 Eugene V. Horohorin <genix@altlinux.ru> 4.0.1-alt1
- new release

* Wed May 19 2004 Serge V. Sergeev <ssv@altlinux.ru> 4.0-alt0.3
- new release

* Mon Feb 16 2004 Serge V. Sergeev <ssv@altlinux.ru> 3.10-alt1
- new release

* Wed Dec 24 2003 Serge V. Sergeev <ssv@altlinux.ru> 3.9-alt2
- add definitionn of QTDIR variable ( need for new build system )

* Thu Dec 11 2003 Serge V. Sergeev <ssv@altlinux.ru> 3.9-alt1
- new release

* Fri Aug 01 2003 Serge Sergeev <ssv@altlinux.ru> 3.7-alt2
- added _findprov_lib_path macro to temporary solve problem with dependencies

* Tue Jul 08 2003 Serge Sergeev <ssv@altlinux.ru> 3.7-alt1
- new release

* Mon Apr 28 2003 Serge Sergeev <ssv@altlinux.ru> 3.6-alt1
- new release

* Thu Apr 10 2003 Serge Sergeev <ssv@altlinux.ru> 3.6-alt0.1
- New build from snapshot

* Fri Dec 20 2002 Serge Sergeev <ssv@altlinux.ru> 3.5-alt2
- Increase release for upgrade

* Mon Dec 16 2002 Serge Sergeev <ssv@altlinux.ru> 3.5-alt1
- new release

* Mon Dec 16 2002 Serge Sergeev <ssv@altlinux.ru> 3.5-alt0.1.20021205
- new release
- correct version

* Fri Dec 06 2002 Serge Sergeev <ssv@altlinux.ru> 20021205-alt1
- build from snapshot
- some documentation added in separate package

* Tue Nov 05 2002 Serge Sergeev <ssv@altlinux.ru> 3.4-alt1
- new release

* Wed Sep 04 2002 Serge Sergeev <ssv@altlinux.ru> 3.3.2-alt1
- new release

* Fri Aug 02 2002 Serge Sergeev <sergeyssv@mail.ru> 3.3-alt1
- Clean up spec file

* Thu Jul 25  2002 <sergeyssv@mail.ru>
- some fixes

* Thu Jun 06  2002 <sergeyssv@mail.ru>
- Initial release
