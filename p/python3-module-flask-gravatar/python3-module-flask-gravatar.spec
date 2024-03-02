%define        _unpackaged_files_terminate_build 1
%define        pypiname flask-gravatar
%define        modname Flask_Gravatar
%define        distname flask_gravatar
%def_disable   check

Name:          python3-module-%pypiname
Version:       0.5.0
Release:       alt1.1
Summary:       Small and simple gravatar usage in Flask
License:       BSD-3-Clause
Group:         Development/Python3
Url:           https://github.com/zzzsochi/Flask-Gravatar
Vcs:           https://github.com/zzzsochi/Flask-Gravatar.git

BuildArch:     noarch
Source:        %name-%version.tar
Patch:         %name-%version-%release.patch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel)
%if_enabled check
BuildRequires: python3(pytest-cov)
%endif

%description
This is small and simple integration gravatar into flask.

Small extension for Flask to make usage of Gravatar service easy.


%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest
%pyproject_run_unittest

%files
%doc *.rst docs/*rst
%python3_sitelibdir/%{distname}
%python3_sitelibdir/%{modname}*/METADATA


%changelog
* Fri Mar 01 2024 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1.1
- ! fixed require to ctx stack avoid deprecated _request_ctx_stack

* Mon Aug 14 2023 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- Initial build v0.5.0 for Sisyphus.
