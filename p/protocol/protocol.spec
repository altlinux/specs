# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: protocol
Version: 0.1.0.20190528
Release: alt1

Summary: An ASCII Header Generator for Network Protocols
License: GPL-3.0
Group: Networking/Other
Url: http://www.luismg.com/protocol/
Vcs: https://github.com/luismartingarcia/protocol.git

Source: %name-%version.tar
BuildRequires(pre): rpm-build-python3
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

%build
pathfix.py -pni %__python3 .
# Quickie package
 mkdir -p protocol_lib
 mv specs.py     protocol_lib/
 mv constants.py protocol_lib/
 touch protocol_lib/__init__.py

%install
%python3_build_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
%buildroot/%_bindir/protocol tcp
%__python3 test.py

%files
%doc LICENSE.txt README.txt
%_bindir/protocol
%python3_sitelibdir_noarch/protocol_lib
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Fri Jul 03 2020 Vitaly Chikunov <vt@altlinux.org> 0.1.0.20190528-alt1
- First import of version 0.1 from git at 2019-05-28.
