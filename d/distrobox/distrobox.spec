Name: distrobox
Version: 1.7.2.1
Release: alt1

Summary: Another tool for containerized command line environments on Linux
License: GPL-3.0
Group: System/Configuration/Other

BuildArch: noarch

Url: https://github.com/89luca89/distrobox
# Source-url: https://github.com/89luca89/distrobox/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires: %_bindir/convert

%add_findreq_skiplist %_bindir/%name-init

%description
Use any linux distribution inside your terminal. Distrobox uses podman
or docker to create containers using the linux distribution of your
choice. Created container will be tightly integrated with the host,
allowing to share the HOME directory of the user, external storage,
external usb devices and graphical apps (X11/Wayland) and audio.

%prep
%setup

%build
%install
./install -P %buildroot/%prefix

%check
%buildroot%_bindir/%name list -V
for i in create enter export init list rm stop host-exec; do
%buildroot%_bindir/%name-$i -V
done

%files
%doc docs/*.md
%doc COPYING.md
%_man1dir/%{name}*
%_bindir/%name
%_bindir/%name-create
%_bindir/%name-enter
%_bindir/%name-export
%_bindir/%name-init
%_bindir/%name-list
%_bindir/%name-rm
%_bindir/%name-stop
%_bindir/%name-host-exec
%_bindir/%name-ephemeral
%_bindir/%name-generate-entry
%_bindir/%name-upgrade
%_bindir/%name-assemble
%_iconsdir/hicolor/*/apps/terminal-distrobox-icon.png
%_iconsdir/hicolor/scalable/apps/terminal-distrobox-icon.svg
%_datadir/bash-completion/completions/%{name}*
%_datadir/zsh/site-functions/_%{name}*

%changelog
* Sun May 19 2024 Boris Yumankulov <boria138@altlinux.org> 1.7.2.1-alt1
- Initial build for Sisyphus (ALT bug: 49431)

