%global pypi_name EasyProcess
%global modulename easyprocess

# proc test failing by chance
%ifarch ppc64le
%def_without check
%endif

Name: python3-module-%modulename
Summary: Easy to use Python subprocess interface
Version: 1.1
Release: alt2
License: BSD
Group: Development/Python3
URL: https://github.com/ponty/EasyProcess
# Source-url: %url/archive/%version/%modulename-%version.tar.gz
Source: %modulename-%version.tar

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%if_disabled check
%else
BuildRequires: /proc
BuildRequires: iputils
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-six
%endif

%description
EasyProcess is an easy to use python subprocess interface.

%prep
%setup -n %modulename-%version

# Avoid circular dependency with PyVirtualDisplay
rm tests/test_fast/test_deadlock.py

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
py.test3 -v

%files
%doc README.md
%python3_sitelibdir/%pypi_name-%version-py*.egg-info/
%python3_sitelibdir/%modulename/

%changelog
* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 1.1-alt2
- Fixed FTBFS.

* Sun Mar 13 2022 Anton Midyukov <antohami@altlinux.org> 1.1-alt1
- new version (1.1) with rpmgs script

* Sun Mar 06 2022 Anton Midyukov <antohami@altlinux.org> 0.3-alt1
- initial build
