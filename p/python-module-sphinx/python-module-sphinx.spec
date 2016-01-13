%define oname sphinx

%def_with python3

Name: python-module-%oname
Version: 1.4
Release: alt2.a0.git20150813
Epoch: 1

Summary: Tool for producing documentation for Python projects
License: BSD
Group: Development/Python
Url: http://sphinx.pocoo.org/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sphinx-doc/sphinx.git
Source0: %name-%version.tar
Source1: conf.py.template
Source2: macro
Source3: macro3
Source4: refcounting.py

BuildArch: noarch

BuildRequires(pre): rpm-build-python python-module-objects.inv
BuildRequires: python-devel python-module-setuptools python-module-simplejson
# for docs
#BuildRequires: texlive-latex-extra 
BuildRequires: python-module-Pygments
BuildRequires: python-module-docutils python-module-jinja2 texlive-latex-base
# for tests
BuildRequires:  python-module-nose python-modules-json
BuildRequires: python-module-snowballstemmer python-module-babel
BuildRequires: python-module-alabaster python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3 python3-module-objects.inv
BuildRequires: python3-devel python3-module-distribute
BuildRequires: python3-module-Pygments python3-module-docutils
BuildRequires: python3-module-jinja2 python3-module-nose
BuildRequires: python-tools-2to3 python3-module-jinja2-tests
BuildRequires: python3-module-snowballstemmer python3-module-babel
BuildRequires: python3-module-alabaster python3-module-sphinx_rtd_theme
%endif

%py_requires simplejson

%description
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

%if_with python3
%package -n python3-module-%oname
Summary: Tool for producing documentation for Python 3 projects
Group: Development/Python3
%add_python3_req_skip xapian

%description -n python3-module-%oname
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

%package -n python3-module-%oname-devel
Summary: Development package for Sphinx (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %epoch:%version-%release
#Requires: python3-module-%oname-pickles = %epoch:%version-%release
Requires: python3-module-%oname-tests
Requires: rpm-macros-%{oname}3 >= %epoch:%version-%release
Requires: python3-module-objects.inv
Requires: python3-module-jinja2-tests

%description -n python3-module-%oname-devel
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This package destinated for development of Python modules.

%package -n python3-module-%oname-pickles
Summary: Pickles for Sphinx (Python 3)
Group: Development/Python3

%description -n python3-module-%oname-pickles
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This packages contains pickles for Sphinx.

%package -n python3-module-%oname-tests
Summary: Tests for Sphinx (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %epoch:%version-%release
%py3_requires nose
%add_python3_req_skip compiler
%add_python3_req_skip missing_module missing_package1 missing_package2
%add_python3_req_skip missing_package3 typing

%description -n python3-module-%oname-tests
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This packages contains tests for Sphinx.

%package -n rpm-macros-%{oname}3
Summary: RPM macros for build with Sphinx (Python 3)
Group: Development/Python3
#Requires: rpm-build-python3 python3-module-objects.inv
#Requires: python3-module-%oname = %epoch:%version-%release

%description -n rpm-macros-%{oname}3
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This packages contains RPM macros for build with Sphinx.
%endif

%package devel
Summary: Development package for Sphinx
Group: Development/Python
Requires: %name = %epoch:%version-%release
Requires: %name-pickles = %epoch:%version-%release
Requires: rpm-macros-%oname >= %epoch:%version-%release
Requires: python-module-objects.inv

%description devel
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This package destinated for development of Python modules.

%package -n rpm-macros-%oname
Summary: RPM macros for build with Sphinx
Group: Development/Python
#Requires: rpm-build-python python-module-objects.inv
#Requires: %name = %epoch:%version-%release

%description -n rpm-macros-%oname
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This packages contains RPM macros for build with Sphinx.

%package tests
Summary: Tests for Sphinx
Group: Development/Python
Requires: %name = %epoch:%version-%release
%py_requires nose
%add_python_req_skip compiler
%add_python_req_skip missing_module missing_package1 missing_package2
%add_python_req_skip missing_package3
%add_findreq_skiplist %python_sitelibdir/%oname/tests/typing_test_data.py

%description tests
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This packages contains tests for Sphinx.

%package doc
Summary: Documentation for Sphinx
Group: Development/Python

%description doc
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This package contains documentation for Sphinx itself.

%package pickles
Summary: Pickles for Sphinx
Group: Development/Python

%description pickles
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This packages contains pickles for Sphinx.

%prep
%setup

cp %SOURCE4 sphinx/ext/

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

install -p -m644 %SOURCE1 %SOURCE2 .
install -p -m644 %SOURCE1 %SOURCE3 ../python3

install -p -m644 %python_sitelibdir/%oname/objects.inv doc
install -p -m644 %python_sitelibdir/%oname/objects.inv tests

%if_with python3
install -p -m644 %python3_sitelibdir/%oname/objects.inv ../python3/doc
install -p -m644 %python3_sitelibdir/%oname/objects.inv ../python3/tests
%endif

%build
%python_build

%if_with python3
pushd ../python3

find -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|python|python3|' doc/Makefile
sed -i 's|mimetools|email|g' tests/etree13/HTMLTreeBuilder.py
sed -i 's|%_bindir/python|%_bindir/python3|' tests/coverage.py
sed -i 's|%_bindir/env python|%_bindir/env python3|' \
	tests/path.py tests/run.py

#cp -fR tests %oname/
#for i in $(find %oname/tests -type d)
#do
#	touch $i/__init__.py
#done

%python3_build

popd
%endif

# docs

%make_build -C doc html
%make_build -C doc man

%install
%if_with python3
pushd ../python3
%python3_install

cp -fR tests %buildroot%python3_sitelibdir/%oname/
for i in $(find %buildroot%python3_sitelibdir/%oname/tests -type d)
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

# tests

cp -fR tests %buildroot%python_sitelibdir/%oname/
for i in $(find %buildroot%python_sitelibdir/%oname/tests -type d)
do
	touch $i/__init__.py
done

# docs

install -d %buildroot%_docdir/%name
#install -d %buildroot%_docdir/%name/pdf
install -d %buildroot%_man1dir

cp -fR doc/_build/html %buildroot%_docdir/%name/
#install -p -m644 doc/_build/latex/*.pdf %buildroot%_docdir/%name/pdf
install -p -m644 AUTHORS CHANGES* EXAMPLES LICENSE README.rst \
	%buildroot%_docdir/%name
#install -p -m644 doc/_build/man/*.1 %buildroot%_man1dir

# macros

install -d %buildroot%_rpmmacrosdir
install -p -m644 macro %buildroot%_rpmmacrosdir/%oname
install -p -m644 ../python3/macro3 %buildroot%_rpmmacrosdir/%{oname}3

#install -p -m644 %oname/directives/desc.py \
#	%buildroot%python_sitelibdir/%oname/directives/

#if_with python3
#install -p -m644 %oname/directives/desc.py \
#	%buildroot%python3_sitelibdir/%oname/directives/
#endif

# add pickle files

%make_build -C doc pickle

install -d %buildroot%python_sitelibdir/%oname/doctrees
install -p -m644 doc/_build/doctrees/*.pickle \
	%buildroot%python_sitelibdir/%oname/doctrees/
install -p -m644 %oname/pycode/*.pickle \
	%buildroot%python_sitelibdir/%oname/pycode/
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/
install -p -m644 conf.py.template \
	%buildroot%python_sitelibdir/%oname/

%ifarch x86_64
LIBSUF=64
%endif

#if_with python3
#pushd ../python3
#export PYTHONPATH=%buildroot%python3_sitelibdir
#export PATH=$PATH:%buildroot%_bindir
#sed -i 's|^SPHINXBUILD.*|SPHINXBUILD = py3_sphinx-build|' doc/Makefile
#make_build -C doc pickle
#install -d %buildroot%python3_sitelibdir/%oname/doctrees
#install -p -m644 doc/_build/doctrees/*.pickle \
#	%buildroot%python3_sitelibdir/%oname/doctrees/
#cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/
install -p -m644 conf.py.template \
	%buildroot%python3_sitelibdir/%oname/
#popd
#endif

#check
# test_autosummary work only with installed Sphinx
#rm -f tests/test_autosummary.py
#make test

%files
%_bindir/*
%exclude %_bindir/py3_*
%python_sitelibdir/%oname/
%exclude %python_sitelibdir/%oname/tests
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/%oname/doctrees
%python_sitelibdir/*.egg-info
#_man1dir/*

%files devel

%files pickles
%python_sitelibdir/%oname/pickle
%python_sitelibdir/%oname/doctrees

%files tests
%python_sitelibdir/%oname/tests
%python_sitelibdir/%oname/tests

%files doc
%doc %_docdir/%name

%files -n rpm-macros-%oname
%_rpmmacrosdir/%oname

%if_with python3
%files -n python3-module-%oname
%_bindir/py3_*
%python3_sitelibdir/%oname/
%exclude %python3_sitelibdir/%oname/tests
#exclude %python3_sitelibdir/%oname/pickle
#exclude %python3_sitelibdir/%oname/doctrees
%python3_sitelibdir/*.egg-info

%files -n python3-module-%oname-devel

#files -n python3-module-%oname-pickles
#python3_sitelibdir/%oname/pickle
#python3_sitelibdir/%oname/doctrees

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests

%files -n rpm-macros-%{oname}3
%_rpmmacrosdir/%{oname}3
%endif

%changelog
* Wed Jan 13 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.4-alt2.a0.git20150813
- spec cleanup: *PreReq -> Requires, dropped rpm-macros-* deps.

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.4-alt1.a0.git20150813
- New snapshot

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.4-alt1.a0.git20150727
- Version 1.4a0

* Thu Jun 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3-alt7.a0
- Avoid download objects.inv

* Tue Jun 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3-alt6.a0
- Restored %python3_sitelibdir/%oname/conf.py.template

* Tue Jun 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3-alt5.a0
- New snapshot

* Tue Jan 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3-alt4.a0
- Restored original sphinx/highlighting.py

* Wed Jan 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3-alt3.a0
- Removed sphinx.ext from sys.path

* Wed Jan 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3-alt2.a0
- Enabled devel subpackage

* Wed Jan 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3-alt1.a0
- Version 1.3a0

* Tue Jan 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.2-alt2
- Added sphinx/ext/refcounting.py from old source

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.2-alt1
- Version 1.2

* Thu Oct 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.3-alt6
- Fixed build manpages (ALT #29450)

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.3-alt5
- Use 'find... -exec...' instead of 'for ... $(find...'

* Thu Mar 21 2013 Aleksey Avdeev <solo@altlinux.ru> 1:1.1.3-alt4.1
- Rebuild with Python-3.3

* Sun Jan 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.3-alt4
- Disabled generating of man pages (broken)

* Mon Sep 10 2012 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.3-alt3
- Fixed rpm-macros-sphinx* interpackage requirements.

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.3-alt2
- Added python3-module-jinja2-tests in requirements for
  python3-module-sphinx-devel

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.3-alt1
- Version 1.1.3
- Added module for Python 3

* Thu Feb 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.2-alt4
- Added necessary requirements for rpm-macros-sphinx (ALT #26915)

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.2-alt3
- Fixed intersphinx.py

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.2-alt2
- Fixed doctest.py

* Sun Nov 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.2-alt1
- Version 1.1.2

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.7-alt3
- Built with docs (except pdf)

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.0.7-alt2.1
- Rebuild with Python-2.7 (bootstrap without docs)

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.7-alt2
- Find objects.inv into local machine

* Sat Apr 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.7-alt1
- Version 1.0.7

* Thu Mar 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.5-alt2
- Moved development requirements devel subpackage (inspired by damir@)
- Fixed requirements with %%epoch

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.5-alt1
- Version 1.0.5

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.1-alt2
- Restored sphinx.directives.desc
- Added requirement on simplejson

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.1-alt1
- Version 1.0.1

* Wed Jun 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6.7-alt2
- Version 0.6.7 (version down from 1.0b2)

* Sat Feb 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt11
- Avoided rewrite conf.py

* Sat Feb 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt10
- Use objects.inv instead of Grammar file for build docs
- Macro %%prepare_sphinx need directory for copying files as parameter

* Tue Feb 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt9
- Added runtime requirement on %name-pickles

* Tue Feb 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt8
- Fixed syntax error in %%generate_pickles

* Tue Feb 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt7
- Macros: %%generate_pickles: added 3rd parameter for module name

* Mon Feb 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt6
- Macros %%generate_pickles: extended set of 1st parameter

* Wed Feb 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt5
- Added macros %%generate_pickles() for generating pickles in packages,
  that haven't this functions
- Add conf.py.template for work of Sphinx, when it copy into current
  docs directory (macros %%generate_pickles())

* Mon Feb 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt4
- Added macros %%sphinx_Grammar_file

* Mon Feb 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt3
- Added build time pickle files. E.g., files environment.pickle,
  searchindex.pickle and globalcontext.pickle may using as sources pickle
  files when build documentation

* Sun Jan 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt2
- Added:
  + pickles file (need by documentation process for some packages)
  + docs in PDF
  + manpages
  + tests package (fixed error in tests)
  + package with macros, need by build with python-module-%oname
- Enabled `make test' when build packages

* Thu Jan 21 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.4-alt1
- 0.6.4 (closes: #22808)

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3-alt1.1
- Rebuilt with python 2.6

* Thu Sep 17 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Mon May 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.1-alt2
- build HTML docs and package them as -doc subpackage

* Mon May 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.1-alt1
- initial build
