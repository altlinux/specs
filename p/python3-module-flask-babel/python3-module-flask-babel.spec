%define _unpackaged_files_terminate_build 1
%define pypi_name flask-babel
%define mod_name flask_babel

%def_with check

Name: python3-module-%pypi_name
Version: 4.0.0
Release: alt1

Summary: i18n and l10n support for Flask based on Babel and pytz
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/flask-babel/
Vcs: https://github.com/python-babel/flask-babel

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-4.0.0-alt-fix-tests.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-flask
BuildRequires: python3-module-babel
BuildRequires: python3-module-pytz
%endif

%description
Implements i18n and l10n support for Flask.
This is based on the Python babel and pytz modules.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE CHANGELOG README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Dec 18 2023 Anton Zhukharev <ancieg@altlinux.org> 4.0.0-alt1
- Updated to 4.0.0.
- Built from upstream VCS.
- Updated summary and description.

* Sat May 20 2023 Vitaly Lipatov <lav@altlinux.ru> 3.0.1-alt2
- add BR: python3-module-pytz for check

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Build new version.

* Wed Jan 18 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Build new version.

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version 2.0.0 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.11.1-alt2
- build python3 package separately

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.11.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt2.git20130729.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 0.9-alt2.git20130729
- Rebuild with "def_disable check"
- Cleanup bildreq

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.git20130729
- Initial build for Sisyphus
