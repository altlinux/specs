%define        _unpackaged_files_terminate_build 1
%define        oname flask-principal
%define        pypiname flask-principal
%define        modname Flask_Principal
%define        distname flask_principal
%def_enable    check
%def_disable   doc

Name:          python3-module-%pypiname
Version:       0.4.0
Release:       alt1.1
Summary:       Identity management for Flask applications
License:       MIT
Group:         Development/Python3
Url:           https://pythonhosted.org/Flask-Principal/
Vcs:           https://github.com/mattupstate/flask-principal.git

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
Identity management for Flask applications. This extension was originally
written by Ali Afshar. Thanks to him for his great work. This is the new and
official repository for this project.


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
%doc *.rst
%{?!_disable_doc:%doc docs/_build/html/*}
%python3_sitelibdir/%{distname}.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%{modname}*/METADATA

%changelog
* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1.1
- NMU: added missing build dependency on setuptools.

* Thu Aug 17 2023 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus.
