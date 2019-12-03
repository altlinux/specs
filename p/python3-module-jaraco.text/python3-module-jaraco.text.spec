%define  modulename jaraco.text
%def_disable check

Name:    python3-module-%modulename
Version: 3.2.0
Release: alt2

Summary: Module for text manipulation
License: MIT
Group:   Development/Python3
URL:     https://github.com/jaraco/jaraco.text

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools_scm
BuildRequires: python3-module-tox
BuildArch: noarch
Source:  %name-%version.tar
Patch0: %name-%version-%release.patch

%description
%summary

%prep
%setup
%patch0 -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install
install -pm0644 jaraco/text/Lorem\ ipsum.txt %buildroot%python3_sitelibdir/jaraco/text/

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -v

%files
%python3_sitelibdir/jaraco/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/jaraco/__init__*
%exclude %python3_sitelibdir/jaraco/__pycache__/__init__*

%changelog
* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 3.2.0-alt2
- install missing in previous build Lorem\ ipsum.txt

* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 3.2.0-alt1
- first build for ALT

