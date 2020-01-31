%define _unpackaged_files_terminate_build 1

%define shortname winrm
%define origname py%shortname

Name:       python3-module-%shortname
Version:    0.3.0
Release:    alt4

Summary:    Python library for Windows Remote Management
License:    MIT
Group:      Networking/Remote access
Url:        https://pypi.python.org/pypi/pywinrm
BuildArch:  noarch

# Source-git: https://github.com/diyan/%origname.git
Source0:    %name-%version.tar
Source1:    winexe_py3winrm

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-xmltodict
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-pep8
BuildRequires: python3-module-mock


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

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

mkdir -p %buildroot%_bindir
install -m755 %SOURCE1 -t %buildroot%_bindir

%check
py.test3 -v --pep8 --cov=winrm --cov-report=term-missing winrm/tests/

%files
%python3_sitelibdir/%shortname
%python3_sitelibdir/%origname-%version-*.egg-info
%_bindir/*py3*


%changelog
* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3.0-alt4
- Porting on Python3.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2
- NMU: remove %ubt from release

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
