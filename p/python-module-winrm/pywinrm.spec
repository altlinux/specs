%define shortname winrm
%define origname py%shortname
Name: python-module-%shortname
Version: 0.2.0
Release: alt1.git

Summary: Python library for Windows Remote Management

License: MIT
Group: Networking/Remote access
Url: https://github.com/diyan/%origname.git

# https://github.com/diyan/pywinrm.git
Source: %origname-%version.tar

%define python3_settings %python3_req_hier
%define python_settings %python_req_hier
%python_settings

BuildArch: noarch

BuildRequires(pre): rpm-build-python
# For the long description (i.e., useless):
# (Well, consider this to be just a test for pypandoc.)
BuildPreReq: python-module-pypandoc
BuildRequires: python-module-setuptools
# For %%check:
BuildPreReq: python-module-setuptools-tests

%package tests
Summary: Tests for the Python library for Windows Remote Management
Group: Networking/Remote access

%description
%origname is a Python client for the Windows Remote Management (WinRM)
service. WinRM allows you to perform various management tasks
remotely. These include, but are not limited to: running batch
scripts, powershell scripts, and fetching WMI variables.

Usage example:

import winrm

s = winrm.Session('windows-host.example.com', auth=('john.smith', 'secret'))
r = s.run_cmd('ipconfig', ['/all'])

%description tests
%origname is a Python client for the Windows Remote Management (WinRM)
service.

This package contains tests for %origname.

%prep
%setup -n %origname-%version

%build
%python_build

%install
%python_install

%check
python setup.py test

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/winrm/tests
%doc README.md LICENSE

%files tests
%python_sitelibdir/winrm/tests

%changelog
* Tue Jul 26 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git
- initial build for ALT Sisyphus (ALT#32317).
