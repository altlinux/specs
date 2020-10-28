%def_disable snapshot

%define modname cairo
%define oname py%modname
%define ver_major 1.18

Name: python-module-%oname
Version: %ver_major.2
Release: alt3

Summary: Pycairo is a set of Python bindings for the cairo vector graphics library
Group: Development/Python
License: LGPL-2.1 and MPL-1.1
Url: https://github.com/pygobject/pycairo

%if_disabled snapshot
Source: %url/releases/download/v%version/%oname-%version.tar.gz
%else
# VCS: https://github.com/pygobject/pycairo.git
Source: %oname-%version.tar
%def_with bootstrap
%endif

%setup_python_module %modname

BuildRequires(pre): rpm-build-python
BuildRequires: libcairo-devel >= 1.13.1
BuildRequires: python-devel
%{?_with_bootstrap:BuildRequires: python-module-Pygments}

%description
The Pycairo bindings are designed to match the cairo C API as closely as
possible, and to deviate only in cases which are clearly better implemented in
a more 'Pythonic' way.

%package devel
Summary: Development files for pycairo
Group: Development/Python
Requires: %name = %EVR
Obsoletes: python-module-pycairo-common-devel
Provides: python-module-pycairo-common-devel = %EVR

%description devel
Development files for pycairo.

%package docs
Summary: Documentation for pycairo
Group: Development/Documentation
BuildArch: noarch

%description docs
Documentation for pycairo.

%prep
%setup -n %oname-%version

# fix pc-file install
subst 's|\"lib\"|"%_lib"|' setup.py

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename
%doc NEWS README*

%files devel
%dir %_includedir/%oname
%_includedir/%oname/pycairo.h
%_pkgconfigdir/%oname.pc


%changelog
* Wed Oct 28 2020 Yuri N. Sedunov <aris@altlinux.org> 1.18.2-alt3
- devel: obsoletes/provides common-devel

* Thu Feb 06 2020 Yuri N. Sedunov <aris@altlinux.org> 1.18.2-alt2
- removed python3 support (the last version supporting Python 2.7 is 1.18.x)
- removed common-devel subpackage

* Sat Oct 26 2019 Yuri N. Sedunov <aris@altlinux.org> 1.18.2-alt1
- 1.18.2
- made python2 build optional

* Sat Apr 20 2019 Yuri N. Sedunov <aris@altlinux.org> 1.18.1-alt1
- 1.18.1

* Sat Nov 24 2018 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- 1.18.0

* Thu Oct 25 2018 Yuri N. Sedunov <aris@altlinux.org> 1.17.1-alt1
- 1.17.1

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.16.3-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Mar 02 2018 Yuri N. Sedunov <aris@altlinux.org> 1.16.3-alt1
- 1.16.3

* Mon Sep 04 2017 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt1
- 1.15.2

* Fri Jun 09 2017 Yuri N. Sedunov <aris@altlinux.org> 1.13.3-alt1
- 1.13.3

* Thu Jun 01 2017 Yuri N. Sedunov <aris@altlinux.org> 1.13.2-alt1
- 1.13.2

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 1.13.1-alt1
- 1.13.1

* Sat Apr 22 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Sat Apr 22 2017 Yuri N. Sedunov <aris@altlinux.org> 1.11.0-alt1
- 1.11.0 (new upstream), built 2 & 3 modules from one source

* Thu Jan 12 2017 Michael Shigorin <mike@altlinux.org> 1.10.1-alt2.git20120522.1
- BOOTSTRAP: added doc knob (on by default)

* Thu Oct 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt2.git20120522
- New snapshot

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt2.git20110619
- Enabled docs (except pdf) and pickles

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.10.1-alt1.git20110619.1
- Rebuild with Python-2.7
- bootstrap without docs and pickles

* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt1.git20110619
- New snapshot
- Fixed updating (ALT #26118)

* Mon May 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt1.git20110502
- Version 1.10.1

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.11-alt1.git20110328.1
- Rebuilt with python-module-sphinx-devel

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.11-alt1.git20110328
- Some fixes from upstream

* Sun Mar 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.11-alt1.git20110123
- Version 1.8.11
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.10-alt1.git20100922.1
- Rebuilt for soname set-versions

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.10-alt1.git20100922
- Version 1.8.10 (ALT #24355)

* Fri Feb 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.9-alt1.git20100114
- Version 1.8.9
- Added docs, tests, examples and pickles packages

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.6-alt1.1
- Rebuilt with python 2.6

* Wed Jul 01 2009 Alexey Shabalin <shaba@altlinux.ru> 1.8.6-alt1
- new version 1.8.6 (with rpmrb script)
- update buildreq
- add patch for build with python-2.5 (upstream requires 2.6)

* Tue Sep 30 2008 Alexey Shabalin <shaba@altlinux.ru> 1.4.12-alt1
- new version 1.4.12 (with rpmrb script)

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.4.0-alt1.1
- Rebuilt with python-2.5.

* Sun Jun 24 2007 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.6-alt1
- new version 1.2.6 (with rpmrb script)

* Sat Sep 02 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt0.1
- new version 1.2.2 (with rpmrb script)

* Sun Apr 30 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt3
- rebuild with new cairo

* Thu Feb 09 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- update build requires

* Tue Nov 22 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- fix build/install sections (#7930)
- split devel package

* Tue Oct 04 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt0.1
- new version
- add pycairo.pc to install

* Mon Sep 12 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- enable build cairo.gtk

* Fri Sep 02 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version

* Sun Aug 28 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt0.1
- first build for ALT Linux Sisyphus
