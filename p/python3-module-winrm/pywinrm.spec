%define shortname winrm
%define origname py%shortname
Name: python3-module-%shortname
Version: 0.2.0
Release: alt3.git

%if "3" == ""
%define pyver 2
%else
%define pyver 3
%endif
Summary: Python%pyver library for Windows Remote Management

License: MIT
Group: Networking/Remote access
Url: https://github.com/diyan/%origname.git

# Repeat the install_requires from setup.py (TODO: autoreqs)
# (particularly useful because of the version constraints):
Requires: python3-module-xmltodict
Requires: python3-module-requests >= 2.9.1
# not packaged yet (and optional according to the actual code):
#Requires: python3-module-requests_ntlm >= 0.3.0
Requires: python3-module-six
# not packaged yet (and optional):
#Requires: python3-module-requests-kerberos >= 0.10.0

# https://github.com/diyan/pywinrm.git
Source: %origname-%version.tar

%define python3_buildtweaks %python3_req_hier
%define python_buildtweaks %python_req_hier
%python3_buildtweaks

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
# For the long description (i.e., useless):
# (Well, consider this to be just a test for pypandoc.)
BuildPreReq: python3-module-pypandoc
BuildRequires: python3-module-setuptools

%package tests
Summary: Tests for the Python library for Windows Remote Management
Group: Networking/Remote access

%package checkpkg
Summary: Immediately test the Python library for Windows Remote Management
Group: Networking/Remote access
Requires(post): %name-tests = %EVR
Requires(post): python3-module-setuptools-tests

%description
%origname is a Python client for the Windows Remote Management (WinRM)
service. WinRM allows you to perform various management tasks
remotely. These include, but are not limited to: running batch
scripts, powershell scripts, and fetching WMI variables.

This package is for Python%pyver.

To try it out, you can run the included winexe_py3winrm script
(needs Python3) or consider the following usage example:

import winrm

s = winrm.Session('windows-host.example.com', auth=('john.smith', 'secret'))
r = s.run_cmd('ipconfig', ['/all'])

%description tests
%origname is a Python client for the Windows Remote Management (WinRM)
service.

This package contains tests for %name.

%description checkpkg
%origname is a Python client for the Windows Remote Management (WinRM)
service.

This package runs %name's tests immediately at install time.
(This is a way to test a Python package in ALT Sisyphus Girar.)

%prep
%setup -n %origname-%version

%build
%python3_build

%install
%python3_install

%if "3" == "3"
mkdir -p %buildroot%_bindir
install -m755 winexe_py3winrm -t %buildroot%_bindir
%endif

mkdir -p %buildroot%_usrsrc/%name
{
  echo '#!/usr/bin/python3'
  cat setup.py
} > %buildroot%_usrsrc/%name/setup.py
chmod a+x %buildroot%_usrsrc/%name/setup.py
# It is being read by setup.py:
ln -s %_docdir/%name-%version/README.md -t %buildroot%_usrsrc/%name/

%post checkpkg
cd %_usrsrc/%name/
# RPM_BUILD_DIR is needed until all reqs are packaged:
su nobody -s /bin/sh \
-c 'RPM_BUILD_DIR="$PWD" ./setup.py test'

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/winrm/tests
%if "3" == "3"
%_bindir/*py3*
%endif
%doc README.md LICENSE CHANGELOG.md

%files tests
%python3_sitelibdir/winrm/tests

%files checkpkg
%_usrsrc/%name

%changelog
* Fri Jul 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt3.git
- winexe_py3winrm -- simple wrapper around pywinrm with a command-line interface
  similar to winexe based on Samba <https://sourceforge.net/projects/winexe/>.

* Wed Jul 27 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt2.git
- (.spec) checkpkg subpkg - Immediately test %%name (at install time).
- Repeat the install_requires from setup.py (particularly useful
  because of the version constraints).

* Tue Jul 26 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git
- initial build for ALT Sisyphus (ALT#32317).
