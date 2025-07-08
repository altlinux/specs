Name: remote-polkit-agent
Version: 0.1.2
Release: alt2

Summary: polkit agent for use on a remote machine via ssh.
License: %lgpl21plus
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/remote-polkit-agent

BuildRequires: cmake gcc rpm-build-licenses
BuildRequires: libpolkit-devel

Source: %name-%version.tar

%description
Polkit agent for use on a remote machine via ssh using stdin and stdout.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/remote-polkit-agent

%changelog
* Tue Jul 08 2025 Ivan Savin <svn17@altlinux.org> 0.1.2-alt2
- Add URL to the spec.

* Thu Oct 31 2024 Ivan Savin <svn17@altlinux.org> 0.1.2-alt1
- Rename package to remote-polkit-agnet.
- Remove unused variables.

* Fri Oct 11 2024 Ivan Savin <svn17@altlinux.org> 0.1.1-alt1
- First working version.

