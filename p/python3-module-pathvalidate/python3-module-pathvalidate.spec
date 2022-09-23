%define _unpackaged_files_terminate_build 1
%define  modulename pathvalidate

%def_enable check

Name:    python3-module-%modulename
Version: 2.5.2
Release: alt1

Summary: pathvalidate is a Python library to sanitize/validate a string such as filenames/file-paths/etc.
License: MIT
Group:   Development/Python3
URL:     https://github.com/thombashi/pathvalidate.git

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_enabled check
BuildRequires: python3-module-tox
BuildRequires: python3-module-pytest
BuildRequires: python3-module-click
%endif

BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

%description
%summary

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
# enable as much tests as possible due to missing extra dependencies
%tox_check_pyproject -- -vra \
  --ignore=test/test_common.py \
  --ignore=test/test_filename.py \
  --ignore=test/test_filepath.py

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info/


%changelog
* Thu Sep 22 2022 Danil Shein <dshein@altlinux.org> 2.5.2-alt1
- initial build for Sisyphus

