%define _unpackaged_files_terminate_build 1
%define pypi_name pytz

Name: python3-module-%pypi_name
Epoch: 1
Version: 2022.6
Release: alt1

Summary: World timezone definitions, modern and historical
Source0: %pypi_name-%version.tar
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.org/project/pytz
VCS: https://github.com/stub42/pytz

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
pytz brings the Olson tz database into Python. This library allows accurate and
cross platform timezone calculations using Python 2.4 or higher. It also solves
the issue of ambiguous times at the end of daylight saving time, which you can
read more about in the Python Library Reference (datetime.tzinfo).

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
# sync to .github/workflows/main.yml
cat > tox.ini <<'EOF'
[testenv]
commands =
    python pytz/tests/test_lazy.py -vv
    python pytz/tests/test_tzinfo.py -vv
EOF
%tox_check_pyproject

%files
%python3_sitelibdir/pytz/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
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
