# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define mod_name protocol_lib

Name: protocol
Version: 0.1.0.20190528
Release: alt1.2

Summary: An ASCII Header Generator for Network Protocols
License: GPL-3.0
Group: Networking/Other
Url: http://www.luismg.com/protocol/
Vcs: https://github.com/luismartingarcia/protocol.git

Source: %name-%version.tar
Patch0: protocol-0.1-modernize-setuptools-configuration.patch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-tools
BuildArch: noarch

%description
              ____            _                  _
             |  _ \ _ __ ___ | |_ ___   ___ ___ | |
             | |_) | '__/ _ \| __/ _ \ / __/ _ \| |
             |  __/| | | (_) | || (_) | (_| (_) | |
             |_|   |_|  \___/ \__\___/ \___\___/|_|

Protocol is a simple command-line tool that serves two purposes:

- Provide a simple way for engineers to have a look at standard network
  protocol headers, directly from the command-line, without having to
  google for the relevant RFC or for ugly header image diagrams.

- Provide a way for researchers and engineers to quickly generate ASCII
  RFC-like header diagrams for their own custom protocols.

%prep
%setup
%autopatch -p1
%python3_fix_shebang .
sed -i 's/@VERSION@/%version/' setup.py

%build
%pyproject_build

%install
%pyproject_install
# don't ship tests
rm %buildroot%python3_sitelibdir/%mod_name/test.py

%check
%pyproject_run -- python test.py

%files
%doc LICENSE.txt README.txt
%_bindir/protocol
%python3_sitelibdir_noarch/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %name}/

%changelog
* Mon May 05 2025 Stanislav Levin <slev@altlinux.org> 0.1.0.20190528-alt1.2
- NMU: fixed FTBFS (setuptools 76.0.0).

* Sun Mar 03 2024 Daniel Zagaynov <kotopesutility@altlinux.org> 0.1.0.20190528-alt1.1
- NMU:
    + replace pathfix.py with find-sed
    + fix FTBFS with removed python3 imp package

* Fri Jul 03 2020 Vitaly Chikunov <vt@altlinux.org> 0.1.0.20190528-alt1
- First import of version 0.1 from git at 2019-05-28.
