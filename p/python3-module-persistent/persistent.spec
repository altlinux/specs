%define _unpackaged_files_terminate_build 1
%define oname persistent

%def_with check
%def_with docs

Name: python3-module-%oname
Version: 6.0
Release: alt1

Summary: Translucent persistent objects
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/persistent/
Vcs: https://github.com/zopefoundation/persistent.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with docs
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-objects.inv
BuildRequires: python3-module-repoze.sphinx.autointerface
BuildRequires: python3-module-sphinx_rtd_theme
%endif
%if_with check
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-manuel
BuildRequires: python3-module-manuel-tests
BuildRequires: python3-module-cffi
BuildRequires: python3-module-zope.deferredimport
%endif

%py3_provides persistent.TimeStamp

%description
This package contains a generic persistence implementation for Python.
It forms the core protocol for making objects interact "transparently"
with a database such as the ZODB.

%package docs
Summary: Documentation for translucent persistent objects
Group: Development/Documentation
BuildArch: noarch

%description docs
This package contains documentation for persistence implementation for
Python. It forms the core protocol for making objects interact
"transparently" with a database such as the ZODB.

%package tests
Summary: Tests for translucent persistent objects
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains a generic tests persistence implementation for
Python. It forms the core protocol for making objects interact
"transparently" with a database such as the ZODB.

%package devel
Summary: Development files for translucent persistent objects
Group: Development/Python3
Requires: %name = %EVR
Requires: python3-dev

%description devel
This package contains the files needed for binding the persistent C module.

%prep
%setup

%if_with docs
sed -i 's|sphinx-build|py3_sphinx-build|' docs/Makefile
%prepare_sphinx3 .
ln -s ../objects.inv3 docs/
%endif

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install
install -p -m644 src/persistent/_compat.h \
	%buildroot%_includedir/python%_python3_version%_python3_abiflags/

# Don't bother with development files
rm %buildroot%python3_sitelibdir/%oname/*.c

%if_with docs
# Build documentation
export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html
rm -f docs/_build/html/.buildinfo
%endif

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc *.txt README.rst CHANGES.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}
%exclude %python3_sitelibdir/%oname/test*
%exclude %python3_sitelibdir/%oname/*.h

%if_with docs
%files docs
%doc docs/_build/html/*
%endif

%files tests
%python3_sitelibdir/%oname/test*

%files devel
%_includedir/python%_python3_version%_python3_abiflags
%python3_sitelibdir/%oname/*.h

%changelog
* Mon Jun 03 2024 Anton Vyatkin <toni@altlinux.org> 6.0-alt1
- New version 6.0.

* Tue Feb 20 2024 Anton Vyatkin <toni@altlinux.org> 5.2-alt1
- New version 5.2.

* Fri Oct 06 2023 Anton Vyatkin <toni@altlinux.org> 5.1-alt1
- New version 5.1.

* Sun Jun 04 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt2
- Package split, create devel package (Closes: #46375).

* Fri Apr 14 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Mon May 10 2021 Grigory Ustinov <grenka@altlinux.org> 4.7.0-alt1
- Automatically updated to 4.7.0.

* Wed Mar 03 2021 Grigory Ustinov <grenka@altlinux.org> 4.6.4-alt3
- Enabled check.

* Mon Nov 23 2020 Grigory Ustinov <grenka@altlinux.org> 4.6.4-alt2
- Bootstrap for python3.9.

* Fri Jul 31 2020 Grigory Ustinov <grenka@altlinux.org> 4.6.4-alt1
- Automatically updated to 4.6.4.

* Wed Mar 18 2020 Grigory Ustinov <grenka@altlinux.org> 4.5.1-alt3
- Build with check.

* Sun Jan 19 2020 Grigory Ustinov <grenka@altlinux.org> 4.5.1-alt2
- Bootstrap for python3.8.

* Tue Jan 14 2020 Nikolai Kostrigin <nickel@altlinux.org> 4.5.1-alt1
- NMU: 4.2.4.2 -> 4.5.1
- Remove python2 module build
- Rearrange unittests execution
- Fix license

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 4.2.4.2-alt1.1.1.qa1
- NMU: applied repocop patch

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.4.2-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.4.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.4.2-alt1
- Updated to upstream version 4.2.4.2.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt2.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.1.1-alt2.1
- NMU: Use buildreq for BR.

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt2
- Really version 4.1.1

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt2
- Avoid conflict with ZODB3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt1
- Version 4.0.8

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.6-alt1.1
- Fixed build

* Wed Mar 13 2013 Aleksey Avdeev <solo@altlinux.ru> 4.0.6-alt1
- Initial build for ALT Linux Sisyphus
