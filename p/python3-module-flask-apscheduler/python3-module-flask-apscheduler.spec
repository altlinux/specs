%define pypi_name flask-apscheduler

%def_without check

Name:    python3-module-%pypi_name
Version: 1.13.1
Release: alt1

Summary: Adds APScheduler support to Flask
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/viniciuschiele/flask-apscheduler

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Flask-APScheduler is a Flask extension which adds support for the APScheduler.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/flask_apscheduler
%python3_sitelibdir/Flask_APScheduler-*.dist-info/

%changelog
* Wed Nov 08 2023 Andrey Cherepanov <cas@altlinux.org> 1.13.1-alt1
- New version.

* Sat Sep 16 2023 Andrey Cherepanov <cas@altlinux.org> 1.13.0-alt1
- New version.

* Tue May 02 2023 Andrey Cherepanov <cas@altlinux.org> 1.12.4-alt1
- Initial build for Sisyphus.
