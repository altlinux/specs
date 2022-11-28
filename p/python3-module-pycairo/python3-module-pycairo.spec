%def_disable snapshot
%def_with doc
%def_enable check

%define modname cairo
%define oname py%modname
%define ver_major 1.23

Name: python3-module-%oname
Version: %ver_major.0
Release: alt1

Summary: Pycairo is a set of Python bindings for the cairo vector graphics library
Group: Development/Python3
License: LGPL-2.1 and MPL-1.1
Url: https://github.com/pygobject/pycairo

%if_disabled snapshot
Source: %url/releases/download/v%version/%oname-%version.tar.gz
%else
Vcs: https://github.com/pygobject/pycairo.git
Source: %oname-%version.tar
%def_with bootstrap
%endif

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson libcairo-devel >= 1.15.10 python3-devel
%{?_with_bootstrap:BuildRequires: python3-module-Pygments}
%{?_with_doc:
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: texlive-latex-base python3-module-sphinx-devel python3-module-sphinx_rtd_theme}
%{?_enable_check:BuildRequires: python3-module-pytest}

%description
The Pycairo bindings are designed to match the cairo C API as closely as
possible, and to deviate only in cases which are clearly better implemented in
a more 'Pythonic' way.

%package devel
Summary: Development files for pycairo
Group: Development/Python3
Requires: %name = %EVR

%description devel
Development files for pycairo.

%package docs
Summary: Documentation for pycairo
Group: Development/Documentation
BuildArch: noarch

%description docs
Documentation for pycairo.

%package tests
Summary: Tests for pycairo
Group: Development/Python3
Requires: %name = %EVR

%description tests
Documentation for pycairo.

%package examples
Summary: Examples for pycairo
Group: Development/Python3
Requires: %name = %EVR
%add_python3_req_skip snippets

%description examples
Examples for pycairo.

%package pickles
Summary: Pickles for pycairo
Group: Development/Python3

%description pickles
Pickles for pycairo.

%prep
%setup -n %oname-%version
%{?_with_doc:%prepare_sphinx3 docs}

%build
%meson
%meson_build
%{?_with_doc:%make_build -C docs}

%install
%meson_install

# docs
install -d %buildroot%_docdir/%name-%version
install -p -m644 NEWS README* \
	%buildroot%_docdir/%name-%version

%if_with doc
cp -fR docs/_build/reference %buildroot%_docdir/%name-%version/

# pickles
install -d %buildroot%python3_sitelibdir/%oname/pickle
cp -fR docs/_build/.doctrees/* %buildroot%python3_sitelibdir/%oname/pickle/

# tests and examples
cp -fR examples tests %buildroot%python3_sitelibdir/%modname/
for i in $(find %buildroot%python3_sitelibdir/%modname/examples -type d)
do
	touch $i/__init__.py
done

%pre pickles
rm -fR %python3_sitelibdir/%oname/pickle
%endif # doc

%check
%__meson_test

%files
%python3_sitelibdir/%modname/
%python3_sitelibdir/%oname-%version.egg-info
%if_with doc
%exclude %python3_sitelibdir/%modname/tests
%exclude %python3_sitelibdir/%modname/examples
%endif
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/NEWS
%doc %_docdir/%name-%version/README*

%files devel
%exclude %python3_sitelibdir_noarch/%modname/include/py3cairo.h
%dir %_includedir/%oname
%_includedir/%oname/py3cairo.h
%_pkgconfigdir/py3cairo.pc

%if_with doc
%files docs
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version
%exclude %_docdir/%name-%version/NEWS
%exclude %_docdir/%name-%version/README*

%files tests
%python3_sitelibdir/%modname/tests

%files examples
%python3_sitelibdir/%modname/examples

%files pickles
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/%oname/pickle/
%endif

%changelog
* Mon Nov 28 2022 Yuri N. Sedunov <aris@altlinux.org> 1.23.0-alt1
- 1.23.0

* Sat Nov 19 2022 Yuri N. Sedunov <aris@altlinux.org> 1.22.0-alt1
- 1.22.0

* Thu May 12 2022 Yuri N. Sedunov <aris@altlinux.org> 1.21.0-alt1
- 1.21.0 (ported to Meson build system)

* Sat Feb 12 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.1-alt2
- NMU: Packed egg-info files, see
  https://lists.altlinux.org/pipermail/devel/2020-October/212260.html

* Mon Jun 07 2021 Yuri N. Sedunov <aris@altlinux.org> 1.20.1-alt1
- 1.20.1

* Wed Feb 24 2021 Yuri N. Sedunov <aris@altlinux.org> 1.20.0-alt3
- enabled %%check again

* Thu Dec 03 2020 Grigory Ustinov <grenka@altlinux.org> 1.20.0-alt2
- Bootstrap for python3.9.

* Wed Oct 28 2020 Yuri N. Sedunov <aris@altlinux.org> 1.20.0-alt1
- 1.20.0

* Thu Mar 19 2020 Yuri N. Sedunov <aris@altlinux.org> 1.19.1-alt1
- 1.19.1
- enabled %%check

* Thu Feb 06 2020 Yuri N. Sedunov <aris@altlinux.org> 1.19.0-alt1
- 1.19.0 (python3 only)
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
