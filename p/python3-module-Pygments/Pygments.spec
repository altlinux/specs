%define _unpackaged_files_terminate_build 1
%define pypi_name Pygments

%def_with check

Name: python3-module-Pygments
Version: 2.14.0
Release: alt1

Summary: Pygments is a syntax highlighting package written in Python

License: BSD-2-Clause
Group: Development/Python3
Url: https://pygments.org/
VCS: https://github.com/pygments/pygments.git

BuildArch: noarch

Source: %name-%version.tar
Source1: autobuild.watch
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

# PEP503 normalized name
Provides: python3-module-pygments = %EVR
# PyPI well known name
%py3_provides %pypi_name

%description
It is a generic syntax highlighter for general use in all kinds of
software such as forum systems, wikis or other applications that need
to prettify source code. Highlights are:
 * a wide range of common languages and markup formats is supported
 * special attention is paid to details, increasing quality by a fair amount
 * support for new languages and formats are added easily
 * a number of output formats, presently HTML, LaTeX, RTF, SVG and ANSI sequences
 * it is usable as a command-line tool and as a library

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install
mv %buildroot%_bindir/pygmentize %buildroot%_bindir/pygmentize3
ln -s pygmentize3 %buildroot%_bindir/pygmentize.py3

# only for build pygments doc
rm -fv %buildroot%python3_sitelibdir/pygments/sphinxext.py

%check
%pyproject_run_pytest -vra

%files
%_bindir/pygmentize3
%_bindir/pygmentize.py3
%python3_sitelibdir/pygments/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Tue Jan 24 2023 Stanislav Levin <slev@altlinux.org> 2.14.0-alt1
- 2.13.0 -> 2.14.0.

* Tue Oct 11 2022 Stanislav Levin <slev@altlinux.org> 2.13.0-alt1
- 2.12.0 -> 2.13.0.

* Tue Jun 21 2022 Fr. Br. George <george@altlinux.org> 2.12.0-alt1
- 2.11.2 -> 2.12.0

* Fri Feb 25 2022 Stanislav Levin <slev@altlinux.org> 2.11.2-alt1
- 2.10.0 -> 2.11.2.

* Wed Sep 08 2021 Stanislav Levin <slev@altlinux.org> 2.10.0-alt1
- 2.8.1 -> 2.10.0.

* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 2.8.1-alt3
- really drop extra deps on sphinx

* Tue Apr 27 2021 Vitaly Lipatov <lav@altlinux.ru> 2.8.1-alt2
- drop extra deps on sphinx

* Thu Apr 15 2021 Stanislav Levin <slev@altlinux.org> 2.8.1-alt1
- 2.6.1 -> 2.8.1.

* Mon Dec 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.1-alt2
- Fixed documentation generation on p9.

* Wed May 06 2020 Stanislav Levin <slev@altlinux.org> 2.6.1-alt1
- 2.4.2 -> 2.6.1.
- Enabled testing.

* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.4.2-alt2
- Fixed build requires.

* Sat Jun 29 2019 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt1
- new version 2.4.2

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt2
- rebuild with python3.6

* Tue Jun 06 2017 Fr. Br. George <george@altlinux.ru> 2.2.0-alt1
- Autobuild version bump to 2.2.0
- Move "testing" lexer back to main package
- Introduce Python3 doc and pickle

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- new version 2.1.3 (with rpmrb script)

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.2-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 2.0.2-alt1.1
- NMU: Use buildreq for BR.

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1
- Version 2.0.1

* Wed Mar 20 2013 Aleksey Avdeev <solo@altlinux.ru> 1.6-alt1.1
- Rebuild with Python-3.3

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- VErsion 1.6

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt2
- Moved %%_bindir/pygmentize for Python 3 into python3-module-%%oname

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1
- Version 1.5
- Added module for Python 3

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Version 1.4

* Fri Nov 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt3
- Enabled docs

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.1-alt2.1
- Rebuild with Python-2.7

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt2
- Rebuilt with python-module-sphinx-devel

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Tue Mar 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4
- Rebuilt with updated macro %%prepare_sphinx

* Wed Feb 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Added pickles package

* Tue Feb 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added documentation and tests

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Rebuilt with python 2.6

* Thu Dec 11 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- new version 1.0 (with rpmrb script)

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- initial build for ALT Linux Sisyphus
