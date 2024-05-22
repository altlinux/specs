%define _unpackaged_files_terminate_build 1
%define oname ZopeUndo

%def_with check

Name: python3-module-%oname
Version: 6.0
Release: alt1

Summary: ZODB undo support for Zope2
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/ZopeUndo
Vcs: https://github.com/zopefoundation/ZopeUndo
BuildArch: noarch

Source: %name-%version.tar

# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %oname} = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-zope.testrunner
%endif

%description
This package is used to support the Prefix object that Zope 2 uses for
the undo log. It is a separate package only to aid configuration
management.

This package is included in Zope 2. It can be used in a ZEO server to
allow it to support Zope 2's undo log , without pulling in all of Zope
2.

%package tests
Summary: Tests for ZopeUndo
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package is used to support the Prefix object that Zope 2 uses for
the undo log. It is a separate package only to aid configuration
management.

This package contains tests for ZopeUndo.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -vv

%files
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Wed May 22 2024 Anton Vyatkin <toni@altlinux.org> 6.0-alt1
- New version 6.0.

* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt1.dev.git20130313.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev.git20130313
- Version 4.0.1dev
- Enabled testing

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt2
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1
- Version 4.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.12.0-alt1.1
- Rebuild with Python-2.7

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.0-alt1
- Initial build for Sisyphus

