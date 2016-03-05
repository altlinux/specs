%define oname sphinx

%def_with python3

%define sphinx_dir %python_sitelibdir_noarch/%oname
%if_with python3
%define sphinx3_dir %python3_sitelibdir_noarch/%oname
%endif

Name: python-module-%oname
Version: 1.4
Release: alt5.a0.git20150813
Epoch: 1

Summary: Tool for producing documentation for Python projects
License: BSD
Group: Development/Python
Url: http://sphinx.pocoo.org/
Packager: Python Development Team <python@packages.altlinux.org>

# https://github.com/sphinx-doc/sphinx.git
Source0: %name-%version.tar
Source1: conf.py.template
Source2: macro
Source3: macro3
Source4: refcounting.py

BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires: python-sphinx-objects.inv
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-pytz python3-module-setuptools python3-module-snowballstemmer
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-nose time

#BuildRequires: python-devel python-module-setuptools python-module-simplejson
# for docs
#BuildRequires: texlive-latex-extra 
#BuildRequires: python-module-Pygments
#BuildRequires: python-module-docutils python-module-jinja2 texlive-latex-base
# for tests
#BuildRequires:  python-module-nose python-modules-json
#BuildRequires: python-module-snowballstemmer python-module-babel
#BuildRequires: python-module-alabaster python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-nose
#BuildRequires: python3-devel python3-module-distribute
#BuildRequires: python3-module-Pygments python3-module-docutils
#BuildRequires: python3-module-jinja2 python3-module-nose
#BuildRequires: python-tools-2to3 python3-module-jinja2-tests
#BuildRequires: python3-module-snowballstemmer python3-module-babel
#BuildRequires: python3-module-alabaster python3-module-sphinx_rtd_theme
%endif

%py_requires simplejson

Provides: python-module-objects.inv
Obsoletes: python-module-objects.inv

%description
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

%if_with python3
%package -n python3-module-%oname
Summary: Tool for producing documentation for Python 3 projects
Group: Development/Python3
%add_python3_req_skip xapian
Provides: python3-module-objects.inv
Obsoletes: python3-module-objects.inv

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
Requires: rpm-macros-sphinx3 = %epoch:%version-%release
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

%package -n rpm-macros-sphinx3
Summary: RPM macros for build with Sphinx (Python 3)
Group: Development/Python3
#Requires: rpm-build-python3
#Requires: python3-module-%oname = %epoch:%version-%release

# W.r.t. to the content of the macros (see the substitution in %%install):
#Requires: %sphinx3_dir
# ...but -- see the comment for rpm-macros-sphinx.

%description -n rpm-macros-sphinx3
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
Requires: rpm-macros-sphinx = %epoch:%version-%release

%description devel
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This package destinated for development of Python modules.

%package -n rpm-macros-sphinx
Summary: RPM macros for build with Sphinx
Group: Development/Python
#Requires: rpm-build-python

# W.r.t. to the content of the macros (see the substitution in %%install):
#Requires: %sphinx_dir
# ...but we do not add such a formal dependency,
# because it is not needed at all
# given the intended usage of rpm-macros-* packages.
# The guarantee that a macro doesn't refer to a path other
# than the current valid %%sphinx_dir
# is given by the strict dep of the main pkg (on EVR of the macros pkg).

%description -n rpm-macros-sphinx
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
%add_findreq_skiplist %sphinx_dir/tests/typing_test_data.py

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
install -pm644 %_sourcedir/conf.py.template .

ln -s %_datadir/python-sphinx/objects.inv doc/
ln -s %_datadir/python-sphinx/objects.inv tests/

cp %SOURCE4 sphinx/ext/

%if_with python3
rm -rf ../python3
cp -a . ../python3
install -pm644 %_sourcedir/macro3 ../python3/
%endif

install -pm644 %_sourcedir/macro .

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

#cp -R tests %oname/
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

cp -R tests %buildroot%sphinx3_dir/
for i in $(find %buildroot%sphinx3_dir/tests -type d)
do
	touch $i/__init__.py
done

ln -rs %buildroot%_datadir/python-sphinx/objects.inv \
	%buildroot%sphinx3_dir/
# There is some objects.inv there already; probably, we want to update it:
ln -frs %buildroot%_datadir/python-sphinx/objects.inv \
	%buildroot%sphinx3_dir/tests/

popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i py3_$i
done
popd
%endif

%python_install

# tests

cp -R tests %buildroot%sphinx_dir/
for i in $(find %buildroot%sphinx_dir/tests -type d)
do
	touch $i/__init__.py
done

ln -rs %buildroot%_datadir/python-sphinx/objects.inv \
	%buildroot%sphinx_dir/
# There is some objects.inv there already; probably, we want to update it:
ln -frs %buildroot%_datadir/python-sphinx/objects.inv \
	%buildroot%sphinx_dir/tests/

# docs

install -d %buildroot%_docdir/%name
#install -d %buildroot%_docdir/%name/pdf
install -d %buildroot%_man1dir

cp -R doc/_build/html %buildroot%_docdir/%name/
#install -p -m644 doc/_build/latex/*.pdf %buildroot%_docdir/%name/pdf
install -p -m644 AUTHORS CHANGES* EXAMPLES LICENSE README.rst \
	%buildroot%_docdir/%name
#install -p -m644 doc/_build/man/*.1 %buildroot%_man1dir

# macros

install -d %buildroot%_rpmmacrosdir
sed -e 's:@SPHINX_DIR@:%sphinx_dir:g' < macro > %buildroot%_rpmmacrosdir/sphinx
sed -e 's:@SPHINX3_DIR@:%sphinx3_dir:g' < ../python3/macro3 > %buildroot%_rpmmacrosdir/sphinx3

#install -p -m644 %oname/directives/desc.py \
#	%buildroot%sphinx_dir/directives/

#if_with python3
#install -p -m644 %oname/directives/desc.py \
#	%buildroot%sphinx3_dir/directives/
#endif

# add pickle files

%make_build -C doc pickle

install -d %buildroot%sphinx_dir/doctrees
install -p -m644 doc/_build/doctrees/*.pickle \
	%buildroot%sphinx_dir/doctrees/
install -p -m644 %oname/pycode/*.pickle \
	%buildroot%sphinx_dir/pycode/
cp -R doc/_build/pickle %buildroot%sphinx_dir/
install -p -m644 conf.py.template \
	%buildroot%sphinx_dir/

%ifarch x86_64
LIBSUF=64
%endif

#if_with python3
#pushd ../python3
#export PYTHONPATH=%buildroot%python3_sitelibdir
#export PATH=$PATH:%buildroot%_bindir
#sed -i 's|^SPHINXBUILD.*|SPHINXBUILD = py3_sphinx-build|' doc/Makefile
#make_build -C doc pickle
#install -d %buildroot%sphinx3_dir/doctrees
#install -p -m644 doc/_build/doctrees/*.pickle \
#	%buildroot%sphinx3_dir/doctrees/
#cp -R doc/_build/pickle %buildroot%sphinx3_dir/
install -p -m644 conf.py.template \
	%buildroot%sphinx3_dir/
#popd
#endif

#check
# test_autosummary work only with installed Sphinx
#rm tests/test_autosummary.py
#make test

mkdir -p %buildroot%_rpmlibdir
cat <<\EOF >%buildroot%_rpmlibdir/%name-files.req.list
# %name dirlist for %_rpmlibdir/files.req
%sphinx_dir	%name
EOF
%if_with python3
cat <<\EOF >%buildroot%_rpmlibdir/python3-module-%oname-files.req.list
# python3-module-%oname dirlist for %_rpmlibdir/files.req
%sphinx3_dir	python3-module-%oname
EOF
%endif

%files
%_bindir/*
%exclude %_bindir/py3_*
%sphinx_dir/
%exclude %sphinx_dir/tests
%exclude %sphinx_dir/pickle
%exclude %sphinx_dir/doctrees
%python_sitelibdir/*.egg-info
#_man1dir/*

%files devel

%files pickles
#dir %sphinx_dir/
%sphinx_dir/pickle
%sphinx_dir/doctrees

%files tests
#dir %sphinx_dir/
%sphinx_dir/tests
%sphinx_dir/tests

%files doc
%doc %_docdir/%name

%files -n rpm-macros-sphinx
%_rpmmacrosdir/sphinx
%_rpmlibdir/%name-files.req.list

%if_with python3
%files -n python3-module-%oname
%_bindir/py3_*
%sphinx3_dir/
%exclude %sphinx3_dir/tests
#exclude %sphinx3_dir/pickle
#exclude %sphinx3_dir/doctrees
%python3_sitelibdir/*.egg-info

%files -n python3-module-%oname-devel

#files -n python3-module-%oname-pickles
#dir %sphinx3_dir/
#%sphinx3_dir/pickle
#%sphinx3_dir/doctrees

%files -n python3-module-%oname-tests
#dir %sphinx3_dir/
%sphinx3_dir/tests

%files -n rpm-macros-sphinx3
%_rpmmacrosdir/sphinx3
%_rpmlibdir/python3-module-%oname-files.req.list
%endif

%changelog
* Sat Mar  5 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4-alt5.a0.git20150813
- rpm-macros-* shouldn't have a formal dep on the main pkg (via %%sphinx_dir);
  the guarantee of compatibility is given by other formal deps
  (of the main pkgs on EVR of the macros pkg; see RPM Macros Packaging Policy
  and https://lists.altlinux.org/pipermail/devel/2016-March/201042.html).
- Declare with a *-files.req.list that we own %%sphinx{,3}_dir
  (just in case other pkgs happen to need to do something inside it).
- (.spec) When the various subpkgs owned %%sphinx_dir, too,
  this caused unwanted installation of them by APT/hsh for %%sphinx_dir.

* Thu Mar 03 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4-alt4.a0.git20150813
- rpm-macros-sphinx{,3}: save the real path %%__sphinx{,3}_dir
  (when built) and require it (when used).

* Wed Mar 02 2016 Dmitry V. Levin <ldv@altlinux.org> 1:1.4-alt3.a0.git20150813
- Added Provides/Obsoletes for python*-module-objects.inv.
- Cleaned up %%sphinx* macros.

* Tue Mar 01 2016 Dmitry V. Levin <ldv@altlinux.org> 1:1.4-alt2.a0.git20150813.2
- NMU: replaced python*-module-objects.inv with python-sphinx-objects.inv.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:1.4-alt2.a0.git20150813.1
- NMU: Use buildreq for BR.

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
