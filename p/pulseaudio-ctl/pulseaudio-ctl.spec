%define _unpackaged_files_terminate_build 1

Name: pulseaudio-ctl
Version: 1.70
Release: alt1

Summary: Control pulseaudio volume from the shell or mapped to keyboard shortcuts
License: MIT
Group: Sound
Url: https://github.com/graysky2/pulseaudio-ctl

Source: %name-%version.tar

BuildArch: noarch

%description
Simple bash script to for control of pulseaudio without alsautils.

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%doc MIT README.md
%_bindir/pulseaudio-ctl
%_man1dir/pulseaudio-ctl.1.*
%dir %_datadir/pulseaudio-ctl
%_datadir/pulseaudio-ctl/config.skel
%_datadir/zsh/site-functions/_pulseaudio-ctl

%changelog
* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 1.70-alt1
- Initial build for Sisyphus
