%define _unpackaged_files_terminate_build 1
%define shortname winrm
%define origname py%shortname

Name: python-module-%shortname
Version: 0.3.0
Release: alt1%ubt

Summary: Python library for Windows Remote Management

License: MIT
Group: Networking/Remote access
# Source-git: https://github.com/diyan/%origname.git
Url: https://pypi.python.org/pypi/pywinrm

Source0: %name-%version.tar
# A simple wrapper around pywinrm with a command-line interface
# similar to winexe based on Samba <https://sourceforge.net/projects/winexe/>
Source1: winexe_py3winrm

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools
BuildRequires: python-module-xmltodict
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-xmltodict
# for tests
BuildRequires: python-module-pytest-cov
BuildRequires: python-module-pytest-pep8
BuildRequires: python-module-mock
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-pep8
BuildRequires: python3-module-mock
#

BuildArch: noarch

%description
%origname is a Python client for the Windows Remote Management (WinRM)
service. WinRM allows you to perform various management tasks
remotely. These include, but are not limited to: running batch
scripts, powershell scripts, and fetching WMI variables.

To try it out, you can run the included winexe_py3winrm script
(needs Python3) or consider the following usage example:

import winrm

s = winrm.Session('windows-host.example.com', auth=('john.smith', 'secret'))
r = s.run_cmd('ipconfig', ['/all'])

%package -n python3-module-%shortname
Summary: Python3 library for Windows Remote Management
Group: Development/Python3

%description -n python3-module-%shortname
%origname is a Python3 client for the Windows Remote Management (WinRM)
service. WinRM allows you to perform various management tasks
remotely. These include, but are not limited to: running batch
scripts, powershell scripts, and fetching WMI variables.

To try it out, you can run the included winexe_py3winrm script
(needs Python3) or consider the following usage example:

import winrm

s = winrm.Session('windows-host.example.com', auth=('john.smith', 'secret'))
r = s.run_cmd('ipconfig', ['/all'])

%prep
%setup

rm -rf ../python3
cp -a . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

mkdir -p %buildroot%_bindir
install -m755 %SOURCE1 -t %buildroot%_bindir

%check
py.test -v --pep8 --cov=winrm --cov-report=term-missing winrm/tests/

pushd ../python3
py.test3 -v --pep8 --cov=winrm --cov-report=term-missing winrm/tests/
popd

%files
%doc README.md LICENSE CHANGELOG.md
%python_sitelibdir/%shortname
%python_sitelibdir/%origname-%version-*.egg-info

%files -n python3-module-%shortname
%doc README.md LICENSE CHANGELOG.md
%python3_sitelibdir/%shortname
%python3_sitelibdir/%origname-%version-*.egg-info
%_bindir/*py3*

%changelog
* Fri Jan 26 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1%ubt
- 0.2.0 -> 0.3.0

* Fri Jul 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt3.git
- winexe_py3winrm -- simple wrapper around pywinrm with a command-line interface
  similar to winexe based on Samba <https://sourceforge.net/projects/winexe/>.

* Wed Jul 27 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt2.git
- (.spec) checkpkg subpkg - Immediately test %%name (at install time).
- Repeat the install_requires from setup.py (particularly useful
  because of the version constraints).

* Tue Jul 26 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git
- initial build for ALT Sisyphus (ALT#32317).
