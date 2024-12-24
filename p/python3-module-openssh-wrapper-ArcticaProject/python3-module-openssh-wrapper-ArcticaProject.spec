Name: python3-module-openssh-wrapper-ArcticaProject
Version: 0.5
Release: alt1.1

Summary: OpenSSH python wrapper
License: BSD
Group: Development/Python3
Url: https://github.com/ArcticaProject/openssh-wrapper
BuildArch: noarch

Conflicts: python3-module-openssh-wrapper
Provides: python3(openssh_wrapper) = %EVR

Source: %name-%version.tar

Patch: openssh-wrapper-ArcticaProject-remove-pipes.patch

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
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc AUTHORS README.rst
%python3_sitelibdir/*

%changelog
* Wed Dec 25 2024 Grigory Ustinov <grenka@altlinux.org> 0.5-alt1.1
- Remove dependency on pipes.

* Sun Jul 24 2022 Anton Zhukharev <ancieg@altlinux.org> 0.5-alt1
- initial build for Sisyphus
