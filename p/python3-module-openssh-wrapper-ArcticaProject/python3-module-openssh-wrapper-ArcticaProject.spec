%define _unpackaged_files_terminate_build 1

Name: python3-module-openssh-wrapper-ArcticaProject
Version: 0.5
Release: alt1

Summary: OpenSSH python wrapper
License: BSD
Group: Development/Python3
Url: https://github.com/ArcticaProject/openssh-wrapper
BuildArch: noarch

Conflicts: python3-module-openssh-wrapper
Provides: python3(openssh_wrapper) = %EVR

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Under some circumstances simple wrapper around OpenSSH `ssh' command-line
utility seems more preferable than paramiko machinery.

This project proposes yet another hopefully thin wrapper around `ssh' to
execute commands on remote servers.

This is a fork of https://github.com/NetAngels/openssh-wrapper

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc AUTHORS README.rst
%python3_sitelibdir/*

%changelog
* Sun Jul 24 2022 Anton Zhukharev <ancieg@altlinux.org> 0.5-alt1
- initial build for Sisyphus
