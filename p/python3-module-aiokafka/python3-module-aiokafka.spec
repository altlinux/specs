%define _unpackaged_files_terminate_build 1
%define pypi_name aiokafka

%def_with check

Name: python3-module-%pypi_name
Version: 0.8.0
Release: alt1

Summary: Asyncio client for kafka
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/aiokafka/
Vcs: https://github.com/aio-libs/aiokafka

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

BuildRequires: zlib-devel

%if_with check
%add_pyproject_deps_check_filter diff-cover
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup

sed -i '/packages=/d' setup.py
cat << EOF >> packages
    packages=[
        "aiokafka",
        "aiokafka.consumer",
        "aiokafka.producer",
        "aiokafka.protocol",
        "aiokafka.record",
        "aiokafka.record._crecords"
    ],
EOF
sed -i '/license="Apache 2"/r packages' setup.py

%pyproject_deps_resync build pip_reqfile requirements-cython.txt
%pyproject_deps_resync_metadata

%if_with check
cat requirements-{ci,cython}.txt > requirements-tests.txt
%pyproject_deps_resync_check_pipreqfile requirements-tests.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- pytest --import-mode append tests

%files
%doc LICENSE CHANGES.rst README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed May 17 2023 Anton Zhukharev <ancieg@altlinux.org> 0.8.0-alt1
- Initial build for ALT Sisyphus.

