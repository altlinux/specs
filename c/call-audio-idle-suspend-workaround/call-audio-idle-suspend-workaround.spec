%define _unpackaged_files_terminate_build 1

Name: call-audio-idle-suspend-workaround
Version: 1
Release: alt1
Summary: Qualcomm config for wireplumber
License: MIT
Group: System/Kernel and hardware

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-systemd

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_userunitdir
install -m 0755 call_audio_idle_suspend_workaround.sh %buildroot%_bindir/call_audio_idle_suspend_workaround
install -m 0644 call-audio-idle-suspend-workaround.service %buildroot%_userunitdir

%files
%_bindir/call_audio_idle_suspend_workaround
%_userunitdir/call-audio-idle-suspend-workaround.service

%changelog
* Sat May 09 2026 Vasiliy Doylov <neko@altlinux.org> 1-alt1
- Initial build for ALT
