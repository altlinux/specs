%define _unpackaged_files_terminate_build 1
%define pypi_name uvloop

# tests are broken: https://github.com/MagicStack/uvloop/issues/429
%def_without check

Name: python3-module-%pypi_name
Version: 0.17.0
Release: alt1

Summary: Ultra fast asyncio event loop
License: MIT Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/uvloop

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(cython)
BuildRequires: libuv-devel

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: /proc
BuildRequires: /dev/pts
BuildRequires: python3(pytest)
BuildRequires: python3(aiohttp)
BuildRequires: python3(flake8)
BuildRequires: python3(mypy)
BuildRequires: python3(pycodestyle)
BuildRequires: python3(OpenSSL)
BuildRequires: python3(psutil)
%endif

%description
uvloop is a fast, drop-in replacement of the built-in asyncio event loop.
uvloop is implemented in Cython and uses libuv under the hood.

%prep
%setup
# there are no ways to pass options right to setup.py through
# pyproject_installer (--backend-config-settings doesn't do that),
# so we need to modify setup.py's default settings manually
sed -i setup.py -e '/self.use_system_libuv/ s/False/True/'
sed -i setup.py -e '/self.cython_always/ s/False/True/'

# remove tests/__init__.py, because we use pytest
rm tests/__init__.py

%build
%pyproject_build --backend-config-settings='{"user-option": ["--inline"]}'

%install
%pyproject_install

%check
%tox_create_default_config
cat << EOF >> tox.ini
passenv = PYTHONPATH
EOF
export PYTHONPATH="%buildroot%python3_sitelibdir"
%tox_check_pyproject

%files
%doc README.rst LICENSE-APACHE LICENSE-MIT
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Nov 06 2022 Anton Zhukharev <ancieg@altlinux.org> 0.17.0-alt1
- update to 0.17.0

* Thu Aug 11 2022 Anton Zhukharev <ancieg@altlinux.org> 0.16.0-alt1
- initial build for Sisyphus

