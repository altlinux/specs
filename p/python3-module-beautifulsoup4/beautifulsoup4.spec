%define _unpackaged_files_terminate_build 1
%define pypi_name beautifulsoup4
%define mod_name bs4

%def_with check

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%%pyproject_runtimedeps_metadata_extra %1 \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

Name: python3-module-%pypi_name
Version: 4.15.0
Release: alt1
Summary: Screen-scraping library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/beautifulsoup4/
Vcs: https://git.launchpad.net/beautifulsoup
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
Provides: python3-module-BeautifulSoup4 = %EVR
Obsoletes: python3-module-BeautifulSoup4
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Beautiful Soup is a Python library designed for quick turnaround projects like
screen-scraping. Three features make it powerful:
- Beautiful Soup provides a few simple methods and Pythonic idioms for
  navigating, searching, and modifying a parse tree: a toolkit for dissecting a
  document and extracting what you need. It doesn't take much code to write an
  application
- Beautiful Soup automatically converts incoming documents to Unicode and
  outgoing documents to UTF-8. You don't have to think about encodings, unless
  the document doesn't specify an encoding and Beautiful Soup can't detect one.
  Then you just have to specify the original encoding.
- Beautiful Soup sits on top of popular Python parsers like lxml and html5lib,
  allowing you to try out different parsing strategies or trade speed for
  flexibility.

%add_python_extra lxml
%add_python_extra html5lib

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jun 08 2026 Stanislav Levin <slev@altlinux.org> 4.15.0-alt1
- 4.14.3 -> 4.15.0

* Mon Dec 08 2025 Stanislav Levin <slev@altlinux.org> 4.14.3-alt1
- 4.14.2 -> 4.14.3.

* Tue Oct 21 2025 Stanislav Levin <slev@altlinux.org> 4.14.2-alt1
- 4.13.5 -> 4.14.2.

* Mon Sep 01 2025 Stanislav Levin <slev@altlinux.org> 4.13.5-alt1
- 4.13.4 -> 4.13.5.

* Wed Apr 16 2025 Stanislav Levin <slev@altlinux.org> 4.13.4-alt1
- 4.13.3 -> 4.13.4.

* Wed Feb 05 2025 Stanislav Levin <slev@altlinux.org> 4.13.3-alt1
- 4.13.1 -> 4.13.3.

* Tue Feb 04 2025 Stanislav Levin <slev@altlinux.org> 4.13.1-alt1
- 4.12.3 -> 4.13.1.

* Mon Oct 07 2024 Stanislav Levin <slev@altlinux.org> 4.12.3-alt2
- fixed ftbfs (lxml 5.3.0).

* Mon Jan 29 2024 Grigory Ustinov <grenka@altlinux.org> 4.12.3-alt1
- Build new version.

* Sun Mar 12 2023 Vitaly Lipatov <lav@altlinux.ru> 4.11.2-alt1
- new version 4.11.2 (with rpmrb script)

* Sat Aug 27 2022 Vitaly Lipatov <lav@altlinux.ru> 4.11.1-alt1
- new version 4.11.1 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 4.11.0-alt1
- new version 4.11.0 (with rpmrb script)

* Fri Sep 17 2021 Stanislav Levin <slev@altlinux.org> 4.10.0-alt1
- 4.9.3 -> 4.10.0.

* Sat Nov 07 2020 Vitaly Lipatov <lav@altlinux.ru> 4.9.3-alt1
- new version 4.9.3 (with rpmrb script)

* Sat Nov 07 2020 Vitaly Lipatov <lav@altlinux.ru> 4.9.0-alt2
- build python3 package separately, cleanup spec

* Fri Sep 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 4.6.3-alt1
- update version to 4.6.3 from src

* Mon Jul 02 2018 Ivan Zakharyaschev <imz@altlinux.org> 4.5.3-alt2
- (.spec) use standard Python build/install macros
- (.spec) re-arrange Python/Python3 BuildRequires

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.5.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 4.4.0-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.0-alt1
- Version 4.4.0

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt1
- Version 4.3.2

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.1-alt1
- Version 4.3.1

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Wed Mar 06 2013 Aleksey Avdeev <solo@altlinux.ru> 4.1.3-alt1.1
- Added module for Python 3

* Fri Sep 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1
- Version 4.1.3

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt2
- Extracted tests into separate package

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.8.1-alt1.1
- Rebuild with Python-2.7

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8.1-alt1
- Version 3.0.8.1

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.6-alt1.1
- Rebuilt with python 2.6

* Mon Jun 09 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.6-alt1
- new version 3.0.6 (with rpmrb script) - fix bug #14975

* Sun Jul 22 2007 Vitaly Lipatov <lav@altlinux.ru> 3.0.4-alt1
- change buildarch to noarch

* Sat May 26 2007 Vitaly Lipatov <lav@altlinux.ru> 3.0.4-alt0.1
- initial build for ALT Linux Sisyphus

