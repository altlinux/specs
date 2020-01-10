%define  modulename testfixtures
%def_with docs
%def_with check

Name:    python3-module-%modulename
Version: 6.10.0
Release: alt2

Summary: A collection of helpers and mock objects for unit tests and doc tests
License: MIT
Group:   Development/Python3
URL:     http://www.simplistix.co.uk/software/python/testfixtures

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-distribute
BuildRequires: python3-module-twisted-logger
BuildRequires: python3-module-twisted-core-test
BuildRequires: python3-module-service-identity

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-sybil
BuildRequires: python3-module-django
BuildRequires: python3-module-zope.component
%endif

%if_with docs
BuildRequires: python3-module-sphinx-devel
BuildRequires: python3-module-sybil
BuildRequires: python3-module-django
BuildRequires: python3-module-zope.component
%endif

Source:  %modulename-%version.tar
#VCS:    https://github.com/Simplistix/testfixtures

%description
TestFixtures is a collection of helpers and mock objects that are useful
when writing unit tests or doc tests.

%prep
%setup -n %modulename-%version

%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv docs/
%endif

%build
%python3_build

%install
%python3_install

%if_with docs
PYTHONPATH=$(pwd) %make -C docs html SPHINXBUILD=sphinx-build-3
mv docs/_build/html ./
rm -rf docs/_build
%endif

%check
rm -rf build
rm -f testfixtures/tests/test_django/test_compare.py
PYTHONPATH=$(pwd) py.test3 testfixtures/tests

%files
%doc README.rst docs
%if_with docs
%doc html
%endif
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Fri Jan 10 2020 Grigory Ustinov <grenka@altlinux.org> 6.10.0-alt2
- Build without python2.
- Build with docs.

* Wed Jun 19 2019 Andrey Cherepanov <cas@altlinux.org> 6.10.0-alt1
- New version.

* Thu Jun 13 2019 Andrey Cherepanov <cas@altlinux.org> 6.9.0-alt1
- New version.

* Sun May 05 2019 Andrey Cherepanov <cas@altlinux.org> 6.8.2-alt1
- New version.

* Sat May 04 2019 Andrey Cherepanov <cas@altlinux.org> 6.8.1-alt1
- New version.

* Tue Apr 30 2019 Andrey Cherepanov <cas@altlinux.org> 6.7.1-alt1
- New version.

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 6.7.0-alt1
- New version.

* Sat Mar 23 2019 Andrey Cherepanov <cas@altlinux.org> 6.6.2-alt1
- New version.

* Mon Mar 18 2019 Andrey Cherepanov <cas@altlinux.org> 6.6.1-alt1
- New version.

* Sat Feb 23 2019 Andrey Cherepanov <cas@altlinux.org> 6.6.0-alt1
- New version.

* Fri Jan 11 2019 Andrey Cherepanov <cas@altlinux.org> 6.4.3-alt1
- New version.

* Wed Jan 09 2019 Andrey Cherepanov <cas@altlinux.org> 6.4.2-alt1
- New version.

* Mon Dec 24 2018 Andrey Cherepanov <cas@altlinux.org> 6.4.1-alt1
- New version.

* Fri Dec 21 2018 Andrey Cherepanov <cas@altlinux.org> 6.4.0-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 6.3.0-alt1
- New version.

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 6.2.0-alt1
- New version.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 6.1.0-alt1
- New version.

* Wed May 02 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.2-alt1
- New version.

* Wed Apr 18 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.1-alt1
- New version.

* Wed Mar 28 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1
- New version.
- Build without HTML documentation.

* Fri Jan 26 2018 Andrey Cherepanov <cas@altlinux.org> 5.4.0-alt1
- New version.

* Wed Nov 22 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.1-alt1
- New version.

* Sat Oct 28 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1
- New version

* Mon Sep 04 2017 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.1-alt2
- Enabled python-3 build.
- Enabled tests.
- Built and packaged docs.

* Fri Jun 09 2017 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt1
- New version

* Mon Jun 05 2017 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version

* Tue May 16 2017 Andrey Cherepanov <cas@altlinux.org> 4.14.3-alt1
- New version

* Wed Mar 01 2017 Andrey Cherepanov <cas@altlinux.org> 4.13.5-alt1
- New version

* Tue Feb 07 2017 Andrey Cherepanov <cas@altlinux.org> 4.13.4-alt1
- new version 4.13.4

* Fri Dec 16 2016 Andrey Cherepanov <cas@altlinux.org> 4.13.3-alt1
- new version 4.13.3

* Sat Nov 05 2016 Andrey Cherepanov <cas@altlinux.org> 4.13.1-alt1
- new version 4.13.1

* Thu Oct 20 2016 Andrey Cherepanov <cas@altlinux.org> 4.12.0-alt1
- new version 4.12.0

* Fri Oct 14 2016 Andrey Cherepanov <cas@altlinux.org> 4.11.0-alt1
- new version 4.11.0

* Wed Sep 07 2016 Andrey Cherepanov <cas@altlinux.org> 4.10.1-alt1
- new version 4.10.1

* Thu Jun 09 2016 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt1
- new version 4.10.0

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1
- Version 4.1.2

* Fri Mar 28 2014 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- Initial build for ALT Linux
