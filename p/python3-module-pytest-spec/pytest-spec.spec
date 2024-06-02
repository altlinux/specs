%define oname pytest-spec

%def_with check

Name: python3-module-%oname
Version: 3.2.0
Release: alt1

Summary: pytest plugin to display test execution output like a SPECIFICATION

License: GPLv2+
Group: Development/Python3
URL: https://pypi.org/project/pytest-spec
VCS: https://github.com/pchomik/pytest-spec

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-mock
BuildRequires: python3-module-six
%endif

%py3_provides pytest_spec


%description
pytest plugin to display test execution output like a SPECIFICATION.

Available features:

* Format output to look like specification.
* Group tests by classes.
* Failed, passed and skipped are marked and colored.
* Remove test_ and underscores for every test.
* Method under test may be highlighted (method) like in example.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# remove extra pytest dependencies
sed -i '/addopts/d' setup.cfg
%pyproject_run_pytest

%files
%doc *.md *txt
%python3_sitelibdir/pytest_spec
%python3_sitelibdir/pytest_spec-%version.dist-info

%changelog
* Sun Jun 02 2024 Grigory Ustinov <grenka@altlinux.org> 3.2.0-alt1
- Build new version.
- Build with check.

* Mon May 30 2022 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt3
- Fixed BuildRequires.

* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt2
- python2 disabled

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.24-alt2.git20150202.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.2.24-alt2.git20150202
- Rebuild with "def_disable check"
- Cleanup buildreq

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.24-alt1.git20150202
- Initial build for Sisyphus

