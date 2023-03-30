%define _unpackaged_files_terminate_build 1
%define oname flexmock

%def_with check

Name: python3-module-%oname
Version: 0.11.3
Release: alt1

Summary: Mock/Stub/Spy library for Python
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/flexmock/
Vcs: https://github.com/flexmock/flexmock

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core
%if_with check
BuildRequires: python3-module-twisted-core-tests
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-testtools
BuildRequires: python3-module-subunit
%endif

%description
flexmock is a testing library for Python that makes it easy to create
mocks, stubs and fakes.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
sed -i '/python tests\/test_teamcity.py/d' tox.ini
%tox_check_pyproject

%files
%doc *.md LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Thu Mar 30 2023 Anton Vyatkin <toni@altlinux.org> 0.11.3-alt1
- New version 0.11.3.

* Thu Apr 09 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.10.4-alt2
- Build for python2 disabled.

* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 0.10.4-alt1
- 0.10.2 -> 0.10.4.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.7-alt1.git20140924.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.7-alt1.git20140924.1
- NMU: Use buildreq for BR.

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.git20140924
- Initial build for Sisyphus

