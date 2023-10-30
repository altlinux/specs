%define pypi_name mkdocs-coverage
%define mod_name mkdocs_coverage

# Tests require network
%def_without check

Name:    python3-module-%pypi_name
Version: 1.0.0
Release: alt1

Summary: MkDocs plugin to integrate your coverage HTML report into your site
License: ISC
Group:   Development/Python3
URL:     https://github.com/pawamoy/mkdocs-coverage

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm python3-module-wheel
BuildRequires: python3-module-pdm-backend

%if_with check
BuildRequires: python3-module-toml
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-randomly
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-mkdocs
BuildRequires: python3-module-mkdocs-material-extensions
BuildRequires: python3-module-markdown-exec
BuildRequires: python3-module-mkdocs-gen-files
BuildRequires: python3-module-mkdocs-literate-nav
BuildRequires: python3-module-mkdocstrings
BuildRequires: python3-module-mkdocs-git-committers-plugin
BuildRequires: python3-module-mkdocs-minify-plugin
BuildRequires: python3-module-markdown-callouts
BuildRequires: python3-module-mkdocstrings-python
BuildRequires: python3-module-mkdocs-git-committers-plugin
BuildRequires: python-sphinx-objects.inv
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version
echo "  ignore::DeprecationWarning" >> config/pytest.ini

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -c config/pytest.ini tests

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Oct 25 2023 Alexander Burmatov <thatman@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
