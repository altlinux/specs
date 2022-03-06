# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

#%%def_disable check

%define modulename Charon
%define srcname lib%modulename

Name:    python3-module-%modulename
Version: 4.10.2
Release: alt1

Summary: File metadata and streaming library
License: LGPL-3.0
Group:   Development/Python3
URL:     https://github.com/Ultimaker/%srcname

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

%if_disabled check
%else
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-timeout
%endif

BuildArch: noarch

# Source-url: %url/archive/%version/%srcname-%version.tar.gz
Source: %srcname-%version.tar

%description
%summary

%prep
%setup -n %srcname-%version

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
py.test3 -v

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Sat Mar 05 2022 Anton Midyukov <antohami@altlinux.org> 4.10.2-alt1
- initial build
