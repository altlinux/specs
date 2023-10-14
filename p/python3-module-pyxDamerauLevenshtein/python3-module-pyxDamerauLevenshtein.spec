%define _unpackaged_files_terminate_build 1
%define pypi_name pyxDamerauLevenshtein
%define mod_name pyxdameraulevenshtein

%def_with check

Name: python3-module-%pypi_name
Version: 1.7.1
Release: alt1

Summary: Damerau-Levenshtein (DL) edit distance algorithm for Python in Cython for high performance
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/pyxDamerauLevenshtein/
Vcs: https://github.com/lanl/pyxDamerauLevenshtein

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: python3-module-pyxDamerauLevenshtein-1.7.1-alt-add-cython-as-build-dependency.patch

%pyproject_runtimedeps_metadata
Provides: python3-module-%{pep503_name %pypi_name}
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%__rm -rf %mod_name
%pyproject_run_unittest discover -s tests -p "test_*.py"

%files
%doc LICENSE AUTHORS.md CHANGES.md README.md
%python3_sitelibdir/%mod_name.*.so
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Sat Oct 14 2023 Anton Zhukharev <ancieg@altlinux.org> 1.7.1-alt1
- Built for ALT Sisyphus.

