%define _unpackaged_files_terminate_build 1

Name: python3-module-makefun
Version: 1.14.0
Release: alt1

Summary: Dynamically create python functions with a proper signature
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/smarie/python-makefun
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(setuptools-scm)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest)

%description
Small library to dynamically crate python functions.

%prep
%setup

%build

# set version for the package manually
export PKG_VERSION=%version
export PKG_VERSION_TUPLE=$(echo "$PKG_VERSION" | sed 's/\./\, /g')
sed -i setup.cfg -e "/download_url/ s/.*/version = $PKG_VERSION/"
cat << EOF >> src/makefun/_version.py
__version__ = version = '$PKG_VERSION'
__version_tuple__ = ($PKG_VERSION_TUPLE)
EOF
rm setup.py

%pyproject_build

%install
%pyproject_install

cp -r docs %_builddir/docs

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.md docs
%python3_sitelibdir/*

%changelog
* Sat Jul 23 2022 Anton Zhukharev <ancieg@altlinux.org> 1.14.0-alt1
- initial build for Sisyphus

