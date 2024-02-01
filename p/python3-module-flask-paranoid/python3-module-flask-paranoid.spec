%define        _unpackaged_files_terminate_build 1
%define        oname Flask-Paranoid
%define        pypiname flask-paranoid
%define        modname Flask_Paranoid
%define        distname flask_paranoid
%def_enable    check
%def_enable    doc

Name:          python3-module-%pypiname
Version:       0.3.0
Release:       alt1
Summary:       Simple user session protection
License:       MIT
Group:         Development/Python3
Url:           https://flask-paranoid.readthedocs.io
Vcs:           https://github.com/miguelgrinberg/flask-paranoid.git

BuildArch:     noarch
Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
%{?!_disable_doc:BuildRequires: python3-module-sphinx-sphinx-build-symlink}
%if_enabled check
BuildRequires: python3(pytest)
BuildRequires: python3(flask)
%endif

%description
Simple user session protection.

Flask-Paranoid is a simple extension for the Flask microframework that protects
the application against certain attacks in which the user session cookie is
stolen and then used by the attacker.


%prep
%setup
%autopatch -p1

%build
%pyproject_build
%{?!_disable_doc:%make -C docs html SPHINXBUILD=sphinx-build-3}

%install
%pyproject_install

%check
%pyproject_run_pytest
%pyproject_run_unittest

%files
%doc *.md
%{?!_disable_doc:%doc docs/_build/html/*}
%python3_sitelibdir/%{distname}
%python3_sitelibdir/%{modname}*/METADATA

%changelog
* Mon Aug 14 2023 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus.
