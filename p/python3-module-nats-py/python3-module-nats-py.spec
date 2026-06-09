%define _unpackaged_files_terminate_build 1
%define ns_name nats
%define nats_py_version 2.15.0
%define nats_core_version 0.2.0
%define nats_server_version 0.0.0
%define nats_jetstream_version 0.3.0
%define nats_key_value_version 0.1.0

# flaky tests
%def_without check

Name: python3-module-nats-py
Version: %nats_py_version
Release: alt1

Summary: NATS client for Python
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/nats-py/
Vcs: https://github.com/nats-io/nats.py

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- nats_py_metadata %{?pyproject_deps_runtime_filter:--exclude %pyproject_deps_runtime_filter}
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps -- nats_py_pep518 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- nats_core_pep518 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- nats_server_pep518 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- nats_jetstream_pep518 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- nats_key_value_pep518 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%if_with check
BuildRequires: nats-server
%pyproject_builddeps -- nats_py_pep517 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- nats_py_metadata %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter} --extra aiohttp
%pyproject_builddeps -- nats_py_metadata %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter} --extra fast-parse
%pyproject_builddeps -- nats_py_metadata %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter} --extra nkeys

%pyproject_builddeps -- nats_core_pep517 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- nats_core_metadata %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter} --extra nkeys

%pyproject_builddeps -- nats_server_pep517 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- nats_server_metadata %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter}

%pyproject_builddeps -- nats_jetstream_pep517 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- nats_jetstream_metadata %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter}

%pyproject_builddeps -- nats_key_value_pep517 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- nats_key_value_metadata %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter}
%endif

%description
An asyncio Python client for the NATS messaging system.

%package -n python3-module-nats-core
Version: %nats_core_version
Summary: NATS core implementation in Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/nats-core/
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- nats_core_metadata %{?pyproject_deps_runtime_filter:--exclude %pyproject_deps_runtime_filter}

%description -n python3-module-nats-core
A Python client for the NATS messaging system..

%package -n python3-module-nats-server
Version: %nats_server_version
Release: alt3
Summary: Python library for managing NATS server for development and testing
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/nats-server/
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- nats_server_metadata %{?pyproject_deps_runtime_filter:--exclude %pyproject_deps_runtime_filter}

%description -n python3-module-nats-server
Manage NATS server instances from python.

%package -n python3-module-nats-jetstream
Version: %nats_jetstream_version
Summary: Python client for NATS JetStream
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/nats-jetstream/
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- nats_jetstream_metadata %{?pyproject_deps_runtime_filter:--exclude %pyproject_deps_runtime_filter}

%description -n python3-module-nats-jetstream
%summary.

%package -n python3-module-nats-key-value
Version: %nats_key_value_version
Summary: Python client for NATS KeyValue Store
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/nats-key-value/
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- nats_key_value_metadata %{?pyproject_deps_runtime_filter:--exclude %pyproject_deps_runtime_filter}

%description -n python3-module-nats-key-value
%summary.

%prep
%setup
%autopatch -p1

# nats-py
cd nats
%pyproject_deps_resync nats_py_pep518 pep518
%pyproject_deps_resync nats_py_pep517 pep517
%pyproject_deps_resync nats_py_metadata metadata
cd -

# nats-core
cd nats-core
%pyproject_deps_resync nats_core_pep518 pep518
%pyproject_deps_resync nats_core_pep517 pep517
%pyproject_deps_resync nats_core_metadata metadata
%if_with check
%pyproject_deps_resync nats_core_check pep735 dev
%endif
cd -

# nats-server
cd nats-server
%pyproject_deps_resync nats_server_pep518 pep518
%pyproject_deps_resync nats_server_pep517 pep517
%pyproject_deps_resync nats_server_metadata metadata
cd -

# nats-jetstream
cd nats-jetstream
%pyproject_deps_resync nats_jetstream_pep518 pep518
%pyproject_deps_resync nats_jetstream_pep517 pep517
%pyproject_deps_resync nats_jetstream_metadata metadata
%if_with check
%pyproject_deps_resync nats_jetstream_check pep735 dev
%endif
cd -

# nats-key-value
cd nats-key-value
%pyproject_deps_resync nats_key_value_pep518 pep518
%pyproject_deps_resync nats_key_value_pep517 pep517
%pyproject_deps_resync nats_key_value_metadata metadata
%if_with check
%pyproject_deps_resync nats_key_value_check pep735 dev
%endif
cd -

%build
for package in nats nats-core nats-server nats-jetstream nats-key-value; do
    pushd $package
    %pyproject_build
    popd
done

%install
for package in nats nats-core nats-server nats-jetstream nats-key-value; do
    pushd $package
    %pyproject_install
    popd
done

%check
export PATH="$PATH:%_sbindir"
for package in nats nats-core nats-server nats-jetstream nats-key-value; do
    pushd $package
    %pyproject_run_pytest -vra -o=addopts=-Wignore
    popd
done

%files
%doc nats/README.md
%python3_sitelibdir/nats_py-%nats_py_version.dist-info/
%dir %python3_sitelibdir/nats/
%python3_sitelibdir/nats/__init__.py
%python3_sitelibdir/nats/errors.py
%python3_sitelibdir/nats/nuid.py
%dir %python3_sitelibdir/nats/__pycache__/
%python3_sitelibdir/nats/__pycache__/__init__.*.pyc
%python3_sitelibdir/nats/__pycache__/errors.*.pyc
%python3_sitelibdir/nats/__pycache__/nuid.*.pyc
%python3_sitelibdir/nats/py.typed
%python3_sitelibdir/nats/aio/
%python3_sitelibdir/nats/js/
%python3_sitelibdir/nats/micro/
%python3_sitelibdir/nats/protocol/

%files -n python3-module-nats-core
%doc nats-core/README.md nats-core/CHANGELOG.md
%python3_sitelibdir/nats_core-%nats_core_version.dist-info/
%dir %python3_sitelibdir/nats/
%python3_sitelibdir/nats/client/

%files -n python3-module-nats-server
%doc nats-server/README.md
%python3_sitelibdir/nats_server-%nats_server_version.dist-info/
%dir %python3_sitelibdir/nats/
%python3_sitelibdir/nats/server/

%files -n python3-module-nats-jetstream
%doc nats-jetstream/README.md nats-jetstream/CHANGELOG.md
%python3_sitelibdir/nats_jetstream-%nats_jetstream_version.dist-info/
%dir %python3_sitelibdir/nats/
%python3_sitelibdir/nats/jetstream/

%files -n python3-module-nats-key-value
%doc nats-key-value/README.md nats-key-value/CHANGELOG.md
%python3_sitelibdir/nats_key_value-%nats_key_value_version.dist-info/
%dir %python3_sitelibdir/nats/
%python3_sitelibdir/nats/key_value/

%changelog
* Tue Jun 09 2026 Anton Zhukharev <ancieg@altlinux.org> 2.15.0-alt1
- Updated to 2.15.0.
- Packaged nats-key-value subproject.

* Fri Mar 06 2026 Anton Zhukharev <ancieg@altlinux.org> 2.14.0-alt2
- Shared /usr/lib/python3/site-packages/nats/ ownership.
- Corrected docs packaging for each subpackage.

* Tue Mar 03 2026 Anton Zhukharev <ancieg@altlinux.org> 2.14.0-alt1
- Updated to 2.14.0.
- Moved packages into separate RPMs.

* Tue Feb 10 2026 Egor Ignatov <egori@altlinux.org> 2.13.1-alt1
- Updated to 2.13.1.

* Wed Mar 26 2025 Anton Zhukharev <ancieg@altlinux.org> 2.10.0-alt1
- Updated to 2.10.0.

* Sun Oct 13 2024 Anton Zhukharev <ancieg@altlinux.org> 2.9.0-alt1
- Updated to 2.9.0.

* Mon Jul 08 2024 Anton Zhukharev <ancieg@altlinux.org> 2.8.0-alt1
- Updated to 2.8.0.

* Tue Apr 02 2024 Anton Zhukharev <ancieg@altlinux.org> 2.7.2-alt1
- Updated to 2.7.2.

* Tue Feb 13 2024 Anton Zhukharev <ancieg@altlinux.org> 2.7.0-alt1
- Updated to 2.7.0.

* Tue Nov 07 2023 Anton Zhukharev <ancieg@altlinux.org> 2.6.0-alt1
- Updated to 2.6.0.

* Tue Sep 26 2023 Anton Zhukharev <ancieg@altlinux.org> 2.4.0-alt1
- Updated to 2.4.0.

* Thu Sep 07 2023 Anton Zhukharev <ancieg@altlinux.org> 2.3.1-alt1
- Updated to 2.3.1.

* Sat May 13 2023 Anton Zhukharev <ancieg@altlinux.org> 2.2.0-alt1
- Initial build for ALT Sisyphus.

