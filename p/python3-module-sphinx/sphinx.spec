%define _unpackaged_files_terminate_build 1
%define pypi_name Sphinx
%define oname sphinx

%def_enable docs
%def_enable check

%define sphinx3_dir %python3_sitelibdir_noarch/%oname

# should be synced to Requires-Dist
%define dependencies \\\
python3(sphinxcontrib.applehelp) \\\
python3(sphinxcontrib.devhelp) \\\
python3(sphinxcontrib.jsmath) \\\
python3(sphinxcontrib.htmlhelp) \\\
python3(sphinxcontrib.serializinghtml) \\\
python3(sphinxcontrib.qthelp) \\\
python3(jinja2) \\\
python3(Pygments) \\\
python3(docutils) \\\
python3(snowballstemmer) \\\
python3(babel) \\\
python3(alabaster) \\\
python3(imagesize) \\\
python3(requests) \\\
python3(packaging) \\\
%nil

Name: python3-module-%oname
Epoch: 1
Version: 5.0.1
Release: alt2

Summary: Tool for producing documentation for Python projects
License: BSD
Group: Development/Python3
Url: http://sphinx-doc.org
VCS: https://github.com/sphinx-doc/sphinx

BuildArch: noarch

# Source0-url: https://github.com/sphinx-doc/sphinx/archive/refs/tags/v%version.tar.gz
Source0: sphinx-%version.tar.gz
Source1: conf.py.template
Source2: macro3
Source3: refcounting.py

Patch1: %oname-alt-tests-offline.patch
Patch2: Fix-tests-for-Pygments-2.14.patch

Requires: %(echo "%dependencies")
Provides: python3-module-objects.inv
Obsoletes: python3-module-objects.inv

BuildRequires(pre): rpm-build-python3
BuildRequires: python-sphinx-objects.inv
BuildRequires: /usr/bin/convert

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_enabled docs
# synced to .[docs]
BuildRequires: %(echo "%dependencies")
BuildRequires: python3(sphinxcontrib.websupport)
%endif

%if_enabled check
# synced to .[test]
BuildRequires: %(echo "%dependencies")
BuildRequires: python3(pytest)
BuildRequires: python3(html5lib)
BuildRequires: python3(cython)
%endif

%add_python3_self_prov_path %buildroot%python3_sitelibdir/sphinx/tests/roots/

%description
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

%package devel
Summary: Development package for Sphinx
Group: Development/Python3
Requires: python3-module-%oname = %EVR
Requires: rpm-macros-sphinx3 = %EVR

%description devel
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This package destinated for development of Python modules.

%package tests
Summary: Tests for Sphinx
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip compiler
%add_python3_req_skip missing_module missing_package1 missing_package2
%add_python3_req_skip missing_package3
%add_python3_req_skip dummy missing_package1.missing_module1 missing_package3.missing_module3
%add_python3_req_skip mod_resource mod_something sphinx.missing_module4 unknown

%description tests
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This packages contains tests for Sphinx.

%if_enabled docs
%package doc
Summary: Documentation for Sphinx
Group: Development/Python3
%add_findreq_skiplist %sphinx3_dir/pickle/_downloads/example_google.py
%add_findreq_skiplist %sphinx3_dir/pickle/_downloads/example_numpy.py

%description doc
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This package contains documentation for Sphinx itself.

%package pickles
Summary: Pickles for Sphinx
Group: Development/Python3

%description pickles
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This packages contains pickles for Sphinx.
%endif

%package -n rpm-macros-sphinx3
Summary: RPM macros for build with Sphinx (Python 3)
Group: Development/Python3

# W.r.t. to the content of the macros (see the substitution in %%install):
#Requires: %sphinx3_dir
# ...but -- see the comment for rpm-macros-sphinx.

%description -n rpm-macros-sphinx3
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This packages contains RPM macros for build with Sphinx.

%prep
%setup -n sphinx-%version
%autopatch -p1

# ship the stable releases
sed -i '/^tag_build =.*/d;/^tag_date =.*/d' setup.cfg
sed -i 's/docutils>=0.14,<0.18/docutils>=0.14,<0.19/' setup.py

install -pm644 %SOURCE1 .

ln -s %_datadir/python-sphinx/objects.inv doc/
ln -s %_datadir/python-sphinx/objects.inv tests/

cp %SOURCE3 sphinx/ext/
install -pm644 %SOURCE2 .

%build
%pyproject_build

%if_enabled docs
# docs
export PYTHONPATH=`pwd`/build/lib
%make_build -C doc html
%make_build -C doc man
%make_build -C doc pickle
%endif

%install
%pyproject_install

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

pushd %buildroot%_bindir
for i in $(ls); do
    mv $i py3_$i
    ln -s py3_$i $i-3
    ln -s py3_$i $i-%__python3_version
done
popd

%if_enabled docs
# docs
install -d %buildroot%_docdir/%name
install -d %buildroot%_man1dir
cp -R doc/_build/html %buildroot%_docdir/%name/
install -p -m644 AUTHORS CHANGES* EXAMPLES LICENSE README.rst \
	%buildroot%_docdir/%name
%endif

# macros
install -d %buildroot%_rpmmacrosdir
sed -e 's:@SPHINX3_DIR@:%sphinx3_dir:g' < macro3 > %buildroot%_rpmmacrosdir/sphinx3

%if_enabled docs
install -d %buildroot%sphinx3_dir/doctrees
install -p -m644 doc/_build/doctrees/*.pickle \
	%buildroot%sphinx3_dir/doctrees/
cp -R doc/_build/pickle %buildroot%sphinx3_dir/
%endif

install -p -m644 conf.py.template \
	%buildroot%sphinx3_dir/

mkdir -p %buildroot%_rpmlibdir
cat <<\EOF >%buildroot%_rpmlibdir/python3-module-%oname-files.req.list
%sphinx3_dir	python3-module-%oname
EOF

%check
%pyproject_run_pytest --ignore tests/test_build_linkcheck.py

%files
%_bindir/*
%sphinx3_dir/
%exclude %sphinx3_dir/tests
%exclude %sphinx3_dir/testing
%if_enabled docs
%exclude %sphinx3_dir/pickle
%exclude %sphinx3_dir/doctrees
%endif
%python3_sitelibdir/%pypi_name-%version.dist-info/

%files devel
%files tests
%sphinx3_dir/tests
%sphinx3_dir/testing

%if_enabled docs
%files pickles
%sphinx3_dir/pickle
%sphinx3_dir/doctrees

%files doc
%doc %_docdir/%name
%endif

%files -n rpm-macros-sphinx3
%_rpmmacrosdir/sphinx3
%_rpmlibdir/python3-module-%oname-files.req.list

%changelog
* Wed Jan 25 2023 Stanislav Levin <slev@altlinux.org> 1:5.0.1-alt2
- Fixed FTBFS (Pygments 2.14.0).

* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 1:5.0.1-alt1
- Autobuild version bump to 5.0.1

* Sat Apr 16 2022 Fr. Br. George <george@altlinux.org> 1:4.5.0-alt1
- Autobuild version bump to 4.5.0

* Thu Feb 17 2022 Michael Shigorin <mike@altlinux.org> 1:4.3.1-alt3
- Fix build with --enable docs --disable check.

* Wed Feb 02 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.3.1-alt2
- Rebuilt with docs.

* Mon Dec 06 2021 Grigory Ustinov <grenka@altlinux.org> 1:4.3.1-alt1
- Build new version for python3.10.
- Bootstrap without docs.

* Thu Sep 09 2021 Stanislav Levin <slev@altlinux.org> 1:4.0.2-alt2
- Fixed FTBFS (new Pygments 2.10).

* Sat May 22 2021 Fr. Br. George <george@altlinux.ru> 1:4.0.2-alt1
- Autobuild version bump to 4.0.2

* Mon May 17 2021 Fr. Br. George <george@altlinux.ru> 1:4.0.1-alt4
- Stop creating a section directory on build manpage by default

* Sun May 16 2021 Fr. Br. George <george@altlinux.ru> 1:4.0.1-alt3
- Switch to tox check

* Sun May 16 2021 Fr. Br. George <george@altlinux.ru> 1:4.0.1-alt2
- Add popular sphinxcontribs to requirelents

* Sun May 16 2021 Fr. Br. George <george@altlinux.ru> 1:4.0.1-alt1
- Major version update

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 1:3.5.4-alt1
- NMU: new version 3.5.4 (with rpmrb script)

* Thu Jul 09 2020 Fr. Br. George <george@altlinux.ru> 1:2.4.4-alt1
- Version up

* Wed Jul 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.2.0-alt4
- Updated macros.

* Tue Oct 01 2019 Stanislav Levin <slev@altlinux.org> 1:2.2.0-alt3
- Dropped extra dep on testing/tests.

* Mon Sep 23 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.2.0-alt2
- Rebuilt with docs and tests.

* Mon Sep 23 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.2.0-alt1
- Updated to upstream version 2.2.0 (Closes: #37252).
- Disabled build for python-2.

* Sun Jun 09 2019 Stanislav Levin <slev@altlinux.org> 1:1.6.5-alt6
- Moved tests out to their own package.

* Sat Jun 01 2019 Stanislav Levin <slev@altlinux.org> 1:1.6.5-alt5
- Fixed Pytest4.x compatibility errors.

* Fri Apr 26 2019 Grigory Ustinov <grenka@altlinux.org> 1:1.6.5-alt4
- Fixed FTBFS (Closes: #36648).

* Tue Sep 18 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.6.5-alt3
- added sphinx-build-3 for compatibility with fedora

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:1.6.5-alt2
- rebuild with python3.6

* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.6.5-alt1
- Updated to upstream version 1.6.5.

* Thu Oct 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.6.4-alt1
- Updated to upstream version 1.6.4.

* Sat Apr 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4.1-alt2
- %%py_requires alabaster (in the new source code, alabaster looks
  like a conditional import--i.e., not top-level and hence not
  autodetected--but this doesn't make much sense since setuptools
  check the declared reqs when running the entry_point
  %_bindir/sphinx-build...)

* Thu Apr 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4.1-alt1
- 1.4.1 released

* Thu Apr 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4-alt8.a0.git20150813
- 2to3 not used, because sphinx is known to support Python3 natively.
  (This fixed one test that used to fail before.)
- Enabled %%check (for Python{2,3}).

* Thu Apr 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4-alt6.a0.git20150813
- (.spec) clarify: use the pure upstream sources & explicitly expose
  a single useful patch (sphinx-1.4b1-alt-avoid-download-objects.inv.patch).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4-alt5.a0.git20150813.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

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
