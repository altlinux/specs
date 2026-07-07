%define _unpackaged_files_terminate_build 1
%define pypi_name markdown2
%define mod_name %pypi_name

%def_without check

Name: python3-module-%pypi_name
Version: 2.5.5
Release: alt1

Summary: Another implementation of Markdown in Python
License: MIT and BSD-3-Clause and GPL-2.0-or-later and Python-2.0
Group: Development/Python3
Url: https://pypi.org/project/markdown2/
Vcs: https://github.com/trentm/python-markdown2.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
%pyproject_builddeps_build
BuildRequires: rpm-build-pyproject
%if_with check
%pyproject_builddeps_check
%endif

%description
This project provides a converter written in Python that closely matches
the behaviour of the original Perl-implemented Markdown.pl. There is
another Python markdown.py, but markdown2.py is faster and, to my
knowledge, more correct.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
rm -rf %buildroot%prefix/testing

%check
%pyproject_run_pytest -vca

%files
%doc LICENSE.txt README.md
%_bindir/markdown2
%python3_sitelibdir_noarch/%mod_name.py
%python3_sitelibdir_noarch/__pycache__/%mod_name.*.pyc
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jul 07 2026 Andrey Kuzma <kuzmaav@altlinux.org> 2.5.5-alt1
- Updated to 2.5.5.
- Switched to rpm-build-pyproject scheme.

* Tue May 20 2025 Alexander Danilov <admsasha@altlinux.org> 2.3.10-alt1
- Version 2.3.10 (Fixes: CVE-2018-5773, CVE-2020-11888).

* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.3.1-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.3.1-alt1.git20141222.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.1-alt1.git20141222.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 2.3.1-alt1.git20141222.1
- NMU: Use buildreq for BR.

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1.git20141222
- Version 2.3.1

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.git20140306
- Version 2.2.1

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.git20131127
- Version 2.1.1

* Sat Mar 02 2013 Aleksey Avdeev <solo@altlinux.ru> 2.1.0-alt1
- Version 2.1.0

* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt1.git20120427
- Version 1.4.3
- Added module for Python 3

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1.19-alt1.git20110718
- Version 1.0.1.19

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1.17-alt1.1
- Rebuild with Python-2.7

* Fri Jul 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1.17-alt1
- Initial build for Sisyphus

