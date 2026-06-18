%define pypi_name autodocsumm

%def_without check

Name:    python3-module-%pypi_name
Version: 0.2.15
Release: alt1

Summary: Extending your autodoc API docs with a summary
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/Chilipp/autodocsumm

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-versioneer

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary

%prep
%setup -n %pypi_name-%version
grep -qsF ' export-subst' .gitattributes || exit 1
vers_f="$(sed -n 's/ export-subst//p' .gitattributes)"
echo 'def get_versions():return {"version": "%version"}' > "$vers_f" 

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Jun 06 2026 Andrey Cherepanov <cas@altlinux.org> 0.2.15-alt1
- Initial build for Sisyphus.
