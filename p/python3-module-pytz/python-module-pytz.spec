%define _unpackaged_files_terminate_build 1
%define pypi_name pytz
%define mod_name %pypi_name

Name: python3-module-%pypi_name
Version: 2026.2
Release: alt1
Epoch: 1
Summary: World timezone definitions, modern and historical
License: MIT
Group: Development/Python
Url: https://pypi.org/project/pytz
VCS: https://github.com/stub42/pytz
BuildArch: noarch
Source0: %pypi_name-%version.tar
Source1: %pyproject_deps_config_name
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
pytz brings the Olson tz database into Python. This library allows accurate and
cross platform timezone calculations using Python 2.4 or higher. It also solves
the issue of ambiguous times at the end of daylight saving time, which you can
read more about in the Python Library Reference (datetime.tzinfo).

%prep
%setup -n %pypi_name-%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# sync to .github/workflows/main.yml
%pyproject_run -- bash -s <<-'ENDTESTS'
set -eux
python %mod_name/tests/test_lazy.py -vv
python %mod_name/tests/test_tzinfo.py -vv
python %mod_name/tests/test_docs.py -vv
ENDTESTS

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu May 14 2026 Stanislav Levin <slev@altlinux.org> 1:2026.2-alt1
- 2026.1.post1 -> 2026.2.

* Tue Mar 03 2026 Stanislav Levin <slev@altlinux.org> 1:2026.1.post1-alt1
- 2025.2 -> 2026.1.post1.

* Tue Mar 25 2025 Stanislav Levin <slev@altlinux.org> 1:2025.2-alt1
- 2025.1 -> 2025.2.

* Mon Feb 03 2025 Stanislav Levin <slev@altlinux.org> 1:2025.1-alt1
- 2024.1 -> 2025.1.

* Fri Jul 26 2024 Grigory Ustinov <grenka@altlinux.org> 1:2024.1-alt1
- Build new version.

* Sat Nov 25 2023 Grigory Ustinov <grenka@altlinux.org> 1:2023.3.post1-alt1
- Build new version for python3.12.

* Thu Dec 08 2022 Stanislav Levin <slev@altlinux.org> 1:2022.6-alt1
- 2021.1 -> 2022.6.

* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2021.1-alt1
- 2021.1 released

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2020.5-alt1
- 2020.5 released

* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2020.1-alt1
- 2020.1 released

* Fri Nov 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2019.3-alt1
- 2019.3 released

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1:2016.10-alt1
- automated PyPI update

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:2015.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:2015.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2015.4-alt1
- Version 2015.4

* Thu Dec 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2014.10-alt2
- Added %%oname-zoneinfo

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2014.10-alt1
- Version 2014.10

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2014.9-alt1
- Version 2014.9

* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2014.7-alt1
- Version 2014.7

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2014.4-alt1
- Version 2014.4

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2013.9-alt1
- Version 2013.9

* Mon Sep 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013d-alt1
- Version 2013d

* Thu Feb 21 2013 Aleksey Avdeev <solo@altlinux.ru> 2012j-alt1
- Version 2012j

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012c-alt1
- Version 2012c
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2010o-alt1.1
- Rebuild with Python-2.7

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010o-alt1
- Version 2010o

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010k-alt1
- Version 2010k
- Added tests

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2009j-alt4.1
- Rebuilt with python 2.6

* Tue Jul 14 2009 Ivan Fedorov <ns@altlinux.org> 2009j-alt4
- fix unowned directories

* Tue Jul 14 2009 Ivan Fedorov <ns@altlinux.org> 2009j-alt3
- fix building

* Tue Jul 14 2009 Ivan Fedorov <ns@altlinux.org> 2009j-alt2
- fix building

* Mon Jul 13 2009 Ivan Fedorov <ns@altlinux.org> 2009j-alt1
- 2009j

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2006p-alt1.1
- Rebuilt with python-2.5.

* Sun Feb 18 2007 Ivan Fedorov <ns@altlinux.ru> 2006p-alt1
- 2006p

* Thu Feb 02 2006 Ivan Fedorov <ns@altlinux.ru> 2005r-alt1
- 2005r

* Tue Oct 04 2005 Ivan Fedorov <ns@altlinux.ru> 2005m-alt1
- Initial build for ALT Linux.
