Name:    rmd
Version: 0.3.0
Release: alt1

Summary: Reminders with notifications and saving after reboot
License: MIT
Group:   Graphical desktop/Other
URL:     https://github.com/PaulBunch/rmd

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust rpm-macros-systemd
BuildRequires: rpm-build-rust

%description
One-shot Linux reminders that survive reboot and show up as desktop notifications.

The daemon is started automatically on first CLI use. To have it
start at login instead, enable the user service:
  systemctl --user enable --now rmd.service

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install
install -Dm644 extra/%name.service %buildroot%_userunitdir/%name.service
sed -i 's|^ExecStart=.*|ExecStart=%_bindir/%name daemon|' \
    %buildroot%_userunitdir/%name.service

%files
%doc LICENSE README.md
%_bindir/%name
%dir %_userunitdir
%_userunitdir/%name.service

%changelog
* Tue Sep 01 2026 Sergey Palcheh <minergenon@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

