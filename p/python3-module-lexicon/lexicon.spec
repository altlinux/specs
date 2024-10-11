%define _unpackaged_files_terminate_build 1
%define pypi_name lexicon
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.1
Release: alt1
Summary: Powerful dict subclass(es) with aliasing & attribute access
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/lexicon/
Vcs: https://github.com/bitprophet/lexicon
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: /dev/pts
%endif

%description
Lexicon is a simple collection of Python dict subclasses providing extra power.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile dev-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- inv test

%files
%doc LICENSE README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 11 2024 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1
- 1.0.0 -> 2.0.1.

* Sun Jul 18 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- drop tests packing (the tests is not used by other packages)

* Tue Feb 18 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt1
- Initial build.

