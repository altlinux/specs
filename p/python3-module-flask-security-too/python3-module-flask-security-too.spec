%define        _unpackaged_files_terminate_build 1
%define        pypiname flask-security-too
%define        modname Flask_Security_Too
%define        distname flask_security
%def_disable   check
%def_disable   doc

Name:          python3-module-%pypiname
Version:       5.3.3
Release:       alt1
Summary:       Quick and simple security for Flask applications
License:       MIT
Group:         Development/Python3
Url:           https://github.com/Flask-Middleware/flask-security
Vcs:           https://github.com/Flask-Middleware/flask-security.git

BuildArch:     noarch
Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
%{?!_disable_doc:BuildRequires: python3-module-sphinx-sphinx-build-symlink}
%{?!_disable_doc:BuildRequires: python3(pallets_sphinx_themes)}
%{?!_disable_doc:BuildRequires: python3(sphinx_issues)}
%if_enabled check
BuildRequires: python3(pytest)
BuildRequires: python3(flask)
BuildRequires: python3(passlib)
BuildRequires: python3(flask_mailman)
BuildRequires: python3(flask_login)
BuildRequires: python3(flask_principal)
BuildRequires: python3(flask_wtf)
BuildRequires: python3(importlib_resources)
BuildRequires: python3(email_validator)
BuildRequires: python3(dateutil)
BuildRequires: python3(flask_sqlalchemy)
BuildRequires: python3(webauthn)
BuildRequires: python3(peewee)
#BuildRequires: python3(pony)
BuildRequires: python3(webauthn)
%endif

%description
Quickly add security features to your Flask application.

Goals:

* Regain momentum for this critical piece of the Flask eco-system. To that end
  the the plan is to put out small, frequent releases starting with pulling the
  simplest and most obvious changes that have already been vetted in the
  upstream version, as well as other pull requests. This was completed with the
  June 29 2019 3.2.0 release.
* Continue work to get Flask-Security to be usable from Single Page
  Applications, such as those built with Vue and Angular, that have no html
  forms. This is true as of the 3.3.0 release.
* Use OWASP to guide best practice and default configurations.
* Be more opinionated and 'batteries' included by reducing reliance on abandoned
  projects and bundling in support for common use cases.
* Follow the Pallets lead on supported versions, documentation standards and any
  other guidelines for extensions that they come up with.

%prep
%setup
%autopatch -p1

%build
%pyproject_build
%{?!_disable_doc:%make -C docs html SPHINXBUILD=sphinx-build-3}

%install
%pyproject_install

%check
PYTHONWARNINGS=ignore %pyproject_run_pytest
PYTHONWARNINGS=ignore %pyproject_run_unittest

%files
%doc *.rst
%{?!_disable_doc:%doc docs/_build/html/*}
%python3_sitelibdir/%{distname}
%python3_sitelibdir/%{modname}*/METADATA

%changelog
* Tue Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 5.3.3-alt1
- Initial build v5.3.3 for Sisyphus.
