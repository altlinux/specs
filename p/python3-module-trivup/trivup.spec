%define  modulename trivup

Name:    python3-module-%modulename
Version: 0.12.1
Release: alt1

Summary: Trivially Up a cluster of applications (such as a Kafka cluster!)

License: BSD-2-Clause
Group:   Development/Python3
URL:     https://github.com/edenhill/trivup

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
# needs curl and network

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version-py%_python3_version.egg-info
%doc LICENSE *.md

%changelog
* Wed Nov 30 2022 Grigory Ustinov <grenka@altlinux.org> 0.12.1-alt1
- Automatically updated to 0.12.1.

* Thu May 26 2022 Grigory Ustinov <grenka@altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus.
