%define _unpackaged_files_terminate_build 1

%def_with check

Name: python3-module-grimp
Version: 3.15
Release: alt1

Summary: Queryable graph of the imports
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/grimp/
VCS: https://github.com/seddonym/grimp

Source0: %name-%version.tar
Source1: vendor_rust.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-pyproject

BuildRequires: python3-module-maturin

%if_with check
BuildRequires: python3-module-requests
BuildRequires: python3-module-pytest
BuildRequires: python3-module-django
BuildRequires: python3-module-flask
BuildRequires: python3-module-sqlalchemy
%endif

%description
Builds a queryable graph of the imports within one or more Python packages

%prep
%setup -a1
cat < vendor_cargoconf.toml >> .cargo/config.toml
mv ./vendor ./rust/vendor
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests \
	--ignore=tests/benchmarking \
	--ignore=tests/functional/test_build_graph_on_real_packages.py \
	#

%files
%python3_sitelibdir/grimp/
%python3_sitelibdir/grimp-%version.dist-info/

%changelog
* Mon Jul 06 2026 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.15-alt1
- v3.5 -> v3.15.

* Mon Feb 03 2025 Yaroslav Bahtin <alpacost@altlinux.org> 3.5-alt2
- Fix FTBFS.

* Wed Nov 20 2024 Yaroslav Bahtin <alpacost@altlinux.org> 3.5-alt1
- Initial build.
