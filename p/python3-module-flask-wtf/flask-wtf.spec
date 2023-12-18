%define _unpackaged_files_terminate_build 1
%define oname flask-wtf

%def_with check

Name: python3-module-%oname
Version: 1.2.1
Release: alt1

Summary: Simple integration of Flask and WTForms
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/Flask-WTF/
Vcs: https://github.com/wtforms/flask-wtf

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-flask
BuildRequires: python3-module-flask-babel
BuildRequires: python3-module-wtforms
%endif

%description
Simple integration of Flask and WTForms, including CSRF, file upload and
Recaptcha integration.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE.rst README.rst
%python3_sitelibdir/flask_wtf/
%python3_sitelibdir/flask_wtf-%version.dist-info/

%changelog
* Mon Dec 18 2023 Anton Zhukharev <ancieg@altlinux.org> 1.2.1-alt1
- Updated to 1.2.1.
- Removed docs and pickles subpackages.

* Wed Jan 18 2023 Grigory Ustinov <grenka@altlinux.org> 1.1.1-alt1
- Automatically updated to 1.1.1.
- Build with check.

* Mon Jan 16 2023 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.

* Mon Oct 03 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt2
- Fixed build requires.

* Sat May 28 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Automatically updated to 1.0.1.

* Tue Jun 01 2021 Grigory Ustinov <grenka@altlinux.org> 0.15.1-alt1
- Automatically updated to 0.15.1.

* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.14.2-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.14.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.14.2-alt1
- Updated to upstream version 0.14.2.

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1.git20141005
- Initial build for Sisyphus

