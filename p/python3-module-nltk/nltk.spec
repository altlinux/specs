%define _unpackaged_files_terminate_build 1
%define pypi_name nltk
%define mod_name %pypi_name

%def_enable check

Name: python3-module-%pypi_name
Version: 3.9.1
Release: alt3
Summary: Python modules for Natural Language Processing (NLP)
License: Apache-2.0
Group: Development/Python3
Url: http://www.nltk.org
Vcs: https://github.com/nltk/nltk.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# apply only for tests on RPM build
Patch0: skip_nltk_data_tests.patch
Patch1: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# optional deps, not packaged yet
%filter_from_requires /python3\(\.[[:digit:]]\)\?(twython\(\..*\)\?)/d
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_enabled check
# not packaged yet
%add_pyproject_deps_check_filter 'gensim$'
%add_pyproject_deps_check_filter 'mdit-plain$'
%add_pyproject_deps_check_filter 'twython$'
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-modules-sqlite3
%endif

%description
NLTK -- the Natural Language Toolkit -- is a suite of open source Python
modules, data sets, and tutorials supporting research and development in
Natural Language Processing.

%prep
%setup
%patch1 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_enabled check
%pyproject_deps_resync_check_pipreqfile requirements-ci.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

# don't package tests
rm -r %buildroot%python3_sitelibdir/*/test

%check
patch -p1 < %PATCH0
%pyproject_run_pytest -vra nltk --ignore nltk/test/unit/test_downloader.py

%files
%_bindir/nltk
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 21 2024 Stanislav Levin <slev@altlinux.org> 3.9.1-alt3
- Added missing tests dependency on sqlite3.

* Fri Nov 15 2024 Stanislav Levin <slev@altlinux.org> 3.9.1-alt2
- Backported fix for WordNetLemmatizer (closes: #51985).

* Fri Nov 01 2024 Pavel Skrylev <majioa@altlinux.org> 3.9.1-alt1
- ^ 3.8.1 -> 3.9.1
- ! CVE-2024-39705 (closes ALT #51738)

* Tue Feb 06 2024 Pavel Skrylev <majioa@altlinux.org> 3.8.1-alt1.1
- ! FTBFS: tests disabled

* Tue Feb 07 2023 Stanislav Levin <slev@altlinux.org> 3.8.1-alt1
- 3.6.1 -> 3.8.1.

* Thu Apr 15 2021 Stanislav Levin <slev@altlinux.org> 3.6.1-alt1
- 3.2.1 -> 3.6.1.

* Mon Dec 19 2016 Kirill Maslinsky <kirill@altlinux.org> 3.2.1-alt1
- Update to 3.2.1
- Drop nltk_contrib from this package

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 3.0.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1
- Version 3.0.1

* Thu May 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt3
- Moved tests into tests subpackage

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt2
- Fixed build

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1
- Version 2.0.4

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt2.beta7.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2.beta7
- Rebuilt with python 2.6

* Thu Nov 12 2009 Kirill Maslinsky <kirill@altlinux.org> 2.0-alt1.beta7
- 2.0 beta7
- nltk and nltk_contrib packaged together

* Tue Sep 15 2009 Kirill Maslinsky <kirill@altlinux.org> 2.0-alt1.beta5
- 2.0 beta5
- nltk and nltk_contrib now are separate packages
- correct License tag: Apache license
- do not build java interface
- spec cleanup (use proper macros for python build and install)

* Sun May 24 2009 Kirill Maslinsky <kirill@altlinux.org> 0.9.9-alt1
- 0.9.9

* Mon Mar 02 2009 Kirill Maslinsky <kirill@altlinux.org> 0.9.8-alt1.1
- fixed packaging
    - build as noarch
    - fix pythonic pseudo-unmets
    - do not package copy of PyYAML
    - use description from PKG-INFO

* Mon Mar 02 2009 Kirill Maslinsky <kirill@altlinux.org> 0.9.8-alt1
- Initial build for Sisyphus

