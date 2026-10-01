%define _unpackaged_files_terminate_build 1
%define pypi_name gradio
%define mod_name %pypi_name
%define pypi_version 6.26.0
%define client_name gradio_client
%define client_version 2.6.1
%define hfg_name hf_gradio
%define hfg_version 0.4.1
%def_without check

Name: python3-module-%pypi_name
Version: 6.26.0
Release: alt1
Summary: Build and share delightful machine learning apps, all in Python
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/gradio/
Vcs: https://github.com/gradio-app/gradio.git

ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
# Offline pnpm content-addressable store for hasher builds.
Source1: pnpm-store.tar
Patch0: gradio-relax-engines-alt.patch
Patch1: gradio-after-build-pnpm.patch
Patch2: gradio-handle-ce-css-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: pnpm
BuildRequires: node
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(hatchling)
BuildRequires: python3-module-hatch-requirements-txt
BuildRequires: python3-module-hatch-fancy-pypi-readme
BuildRequires: python3(numpy)
BuildRequires: python3(fastapi)
BuildRequires: python3(orjson)
BuildRequires: python3(scipy)
BuildRequires: python3-module-groovy
BuildRequires: python3-module-python-multipart
BuildRequires: python3-module-huggingface-hub
BuildRequires: python3-module-safehttpx

# Runtime extras that are not always auto-detected from METADATA.
Requires: %name-client = %client_version-%release
Requires: python3-module-hf-gradio >= %hfg_version
Requires: python3-module-groovy
Requires: python3-module-python-multipart
Requires: python3-module-safehttpx

# Drop obsolete scaffold package from older hasher/sisyphus builds.
Obsoletes: python3-module-gradio-test

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
Gradio is an open-source Python package that allows you to quickly build a demo
or web application for your machine learning model, API, or any Python function.

This package builds the frontend with system pnpm (Sisyphus) and ships the
Python backend together with a matched gradio_client subpackage.

%package client
Version: %client_version
BuildArch: noarch
Summary: Python client library for Gradio apps
Group: Development/Python3
# Replace historically separate client packages from the same monorepo.
#Obsoletes: python3-module-gradio-client < 2.0
Provides: python3-module-gradio-client = %client_version-%release
%py3_provides %client_name

%description client
Python client for calling Gradio apps as APIs. Built from the Gradio monorepo
(client/python) and version-matched to this Gradio release.

%add_python3_req_skip python_multipart.multipart python_multipart.exceptions
%add_python3_req_skip discord discord.ext
# client: optional/lazy imports of gradio (template, LocalContext)
%add_python3_req_skip gradio gradio.context

%prep
%setup
%autopatch -p1
cat > .npmrc <<EOF
manage-package-manager-versions=false
package-manager-strict=false
engine-strict=false
# Hasher has no network; skip pnpm 11 lockfile supply-chain verification.
trustPolicy=off
trustLockfile=true
confirm-modules-purge=false
EOF

%build
# Workspace root is the repository root (pnpm-workspace.yaml), not js/.
export NODE_OPTIONS="--max-old-space-size=2048"
# pnpm appends /v11 under store-dir; tar is the contents of "pnpm store path" (…/v11).
export PNPM_STORE_DIR="$PWD/.pnpm-store"
mkdir -p "$PNPM_STORE_DIR/v11"
pnpm_offline=""
if [ -f %_sourcedir/pnpm-store.tar ]; then
	tar -xf %_sourcedir/pnpm-store.tar -C "$PNPM_STORE_DIR/v11"
	pnpm_offline="--offline"
fi
pnpm config set store-dir "$PNPM_STORE_DIR"
pnpm config set trustPolicy off
pnpm config set trustLockfile true
# spa only declares frontend tooling as devDependencies; keep them installed.
export NODE_ENV=development
pnpm install --frozen-lockfile --ignore-scripts --trust-lockfile $pnpm_offline
unset NODE_ENV
pnpm build

# Offline static assets used by the UI when CDN is unavailable.
if [ -f scripts/download_offline_assets.py ]; then
	python3 scripts/download_offline_assets.py || :
fi

%pyproject_build

# Matched client from the same monorepo.
pushd client/python
%pyproject_build
popd

%install
%pyproject_install

pushd client/python
%pyproject_install
popd
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/%mod_name \
 %buildroot%python3_sitelibdir_noarch/%{pypi_name}-%{pypi_version}.dist-info \
 %buildroot%python3_sitelibdir/

%check
%if_with check
#pyproject_run_pytest -k "not network"
%endif

%files
%doc README.md CHANGELOG.md LICENSE
%_bindir/gradio
%_bindir/upload_theme
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pypi_name}-%{pypi_version}.dist-info/

%files client
%doc client/python/README.md client/python/CHANGELOG.md
%python3_sitelibdir_noarch/%client_name/
%python3_sitelibdir_noarch/%{client_name}-%{client_version}.dist-info/

%changelog
* Tue Sep 29 2026 Pavel Shilov <zerospirit@altlinux.org> 6.26.0-alt1
- 6.9.0 -> 6.26.0.
- Build frontend with system pnpm from Sisyphus.
- Ship gradio_client as a subpackage; obsolete standalone
 python3-module-gradio-client and python3-module-gradio-test.
- Drop hard Requires on optional python3-module-gradio-pdf.

* Wed Apr 01 2026 Pavel Shilov <zerospirit@altlinux.org> 6.9.0-alt1
- 6.0.1 -> 6.9.0

* Sat Nov 29 2025 Pavel Shilov <zerospirit@altlinux.org> 6.0.1-alt1
- 5.49.1 -> 6.0.1

* Sat Nov 29 2025 Pavel Shilov <zerospirit@altlinux.org> 5.49.1-alt1
- 5.42.0 -> 5.49.1

* Fri Nov 07 2025 Pavel Shilov <zerospirit@altlinux.org> 5.42.0-alt2
- Update requires.

* Sun Aug 10 2025 Pavel Shilov <zerospirit@altlinux.org> 5.42.0-alt1
- Initial build for Sisyphus.