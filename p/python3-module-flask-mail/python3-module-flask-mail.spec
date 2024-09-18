%define        _unpackaged_files_terminate_build 1
%define        pypiname flask-mail
%define        mname flask_mail
%define        oname flask_mail
%def_disable   check

Name:          python3-module-%pypiname
Version:       0.10.0
Release:       alt1
Summary:       Flask-Mail adds SMTP mail sending to your Flask applications
License:       BSD-3-Clause
Group:         Development/Python3
Url:           https://pythonhosted.org/Flask-Mail/
Vcs:           https://github.com/mattupstate/flask-mail.git

BuildArch:     noarch
Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(flit_core)
%if_enabled check
BuildRequires: python3(tox)
BuildRequires: python3(mock)
BuildRequires: python3(flask)
BuildRequires: python3(speaklater)
%endif

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%description
Flask-Mail is a Flask extension providing simple email sending capabilities.


%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.*
%if_enabled doc
%doc docs/_build/html/*
%endif
%python3_sitelibdir/%{oname}
%python3_sitelibdir/%{mname}*/METADATA

%changelog
* Wed Sep 18 2024 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt1
- ^ 0.9.1 -> 0.10.0 (without tests)

* Mon Aug 14 2023 Pavel Skrylev <majioa@altlinux.org> 0.9.1-alt1
- Initial build v0.9.1 for Sisyphus.
