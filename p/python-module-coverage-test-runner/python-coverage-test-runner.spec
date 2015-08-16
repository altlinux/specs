%define oldname python-coverage-test-runner
%global pkgname CoverageTestRunner
%global prjname coverage-test-runner

%def_without python3

Name: python-module-coverage-test-runner
Version: 1.10
Release: alt4.git20150418

Summary: Python module for enforcing code coverage completeness

License: GPLv3+
Group: Development/Python
Url: http://liw.fi/%prjname/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# git://git.liw.fi/coverage-test-runner
Source: %{oldname}_%version.orig.tar.gz

Source44: import.info

BuildArch: noarch

# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
# END SourceDeps(oneline)

BuildRequires: python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-coverage
%endif

%description
CoverageTestRunner is a Python module for running unit tests and
failing them if the unit test module does not exercise all statements
in the module it tests.

For example, unit tests in module foo_tests.py are supposed to test
everything in the foo.py module, and if they don't, it's a bug in the
test coverage. It does not matter if other tests happen to test the
missing parts. The unit tests for the module should test everything in
that module.

%if_with python3
%package -n python3-module-%prjname
Summary: Python module for enforcing code coverage completeness
Group: Development/Python3

%description -n python3-module-%prjname
CoverageTestRunner is a Python module for running unit tests and
failing them if the unit test module does not exercise all statements
in the module it tests.

For example, unit tests in module foo_tests.py are supposed to test
everything in the foo.py module, and if they don't, it's a bug in the
test coverage. It does not matter if other tests happen to test the
missing parts. The unit tests for the module should test everything in
that module.
%endif

%prep
%setup -n %pkgname-%version

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
make check
%if_with python3
pushd ../python3
sed -i 's|^python|python3|' testrun
make check
popd
%endif

%files
%doc COPYING NEWS README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%prjname
%doc COPYING NEWS README
%python3_sitelibdir/*
%endif

%changelog
* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt4.git20150418
- human build for ALT Linux Sisyphus (as request from lav@)

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_3
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_2
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_1
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_1
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_3
- update to new release by fcimport

* Sun Dec 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_2
- initial fc import

