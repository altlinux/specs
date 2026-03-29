%define _unpackaged_files_terminate_build 1
%define pypi_name flask-compress
%define mod_name flask_compress

%def_with check

Name: python3-module-%pypi_name
Version: 1.23
Release: alt1.1
Summary: Compress responses in your Flask app with gzip, deflate or brotli
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Flask-Compress
VCS: https://github.com/colour-science/flask-compress
BuildArch: noarch
Source: %name-%version.tar

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-flask-caching
BuildRequires: python3-module-pytest

BuildRequires: python3-module-brotli
BuildRequires: python3-module-flask
BuildRequires: python3-module-backports-zstd
%endif

%description
Flask-Compress allows you to easily compress your Flask application's
responses with gzip, deflate or brotli. It originally started as a fork
of Flask-gzip.
The preferred solution is to have a server (like Nginx) automatically
compress the static files for you. If you don't have that option
Flask-Compress will solve the problem for you.

%prep
%setup
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m "release"
    git tag "%version"
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.23-alt1.1
- Demodernized packaging.

* Mon Dec 15 2025 Stanislav Levin <slev@altlinux.org> 1.23-alt1
- 1.18 -> 1.23.

* Mon Jul 14 2025 Stanislav Levin <slev@altlinux.org> 1.18-alt1
- 1.17 -> 1.18.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 1.17-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Wed Feb 05 2025 Stanislav Levin <slev@altlinux.org> 1.17-alt1
- 1.14 -> 1.17.

* Tue Oct 24 2023 Andrey Limachko <liannnix@altlinux.org> 1.14-alt1
- Initial build for Sisyphus
