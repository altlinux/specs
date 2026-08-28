%define _unpackaged_files_terminate_build 1

Name: asahi-audio
Version: 4.1
Release: alt1
Summary: Userspace audio for Asahi Linux
License: MIT
Group: System/Kernel and hardware
Url: https://github.com/asahilinux/asahi-audio
VCS: https://github.com/asahilinux/asahi-audio.git

ExclusiveArch: aarch64

Source: %name-%version.tar

Requires: lv2-lsp-plugins
Requires: lv2-bankstown-plugin
Requires: lv2-triforce-plugin
Requires: alsa-ucm-conf-asahi
Requires: speakersafetyd

%description
This package contains DSP configuration files for Apple Silicon Macs supported
by the Asahi Linux project. Our goal is to make the Asahi Linux audio experience
better than macOS, and in doing so demonstrate that desktop Linux audio can be
made fit for purpose with a little bit of effort.

%prep
%setup

%build
%makeinstall_std \
    DESTDIR=%buildroot \
    DATA_DIR=%_datadir

%files
%doc README.md
%_datadir/%name
%_datadir/wireplumber
%_datadir/pipewire

%changelog
* Thu Aug 27 2026 Vasiliy Doylov <neko@altlinux.org> 4.1-alt1
- Initial build for ALT.
