%define        _unpackaged_files_terminate_build 1
%define        oname Flask-Mailman
%define        pypiname flask-mailman
%define        distname flask_mailman
%define        modname %distname
%def_enable    check

Name:          python3-module-%pypiname
Version:       1.0.0
Release:       alt1
Summary:       Simple user session protection
License:       MIT
Group:         Development/Python3
Url:           https://waynerv.github.io/flask-mailman/
Vcs:           https://github.com/waynerv/flask-mailman.git

BuildArch:     noarch
Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
%if_enabled check
BuildRequires: python3(pytest)
BuildRequires: python3(flask)
BuildRequires: python3(poetry)
BuildRequires: python3(poetry.core)
%endif

%description
Simple user session protection.

Flask-Mailman is a simple extension for the Flask microframework that protects
the application against certain attacks in which the user session cookie is
stolen and then used by the attacker.


%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest
#pyproject_run_unittest

%files
%doc *.md docs/*.md
%python3_sitelibdir/%{distname}
%python3_sitelibdir/%{modname}*/METADATA

%changelog
* Tue Jan 30 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- Initial build v1.0.0 for Sisyphus.
