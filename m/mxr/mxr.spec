%global _unpackaged_files_terminate_build 1
%global release_bin target-cli/release/mxr
%def_with check

Name: mxr
Version: 0.6.29
Release: alt1
Summary: Local-first, keyboard-native terminal email client
License: MIT or Apache-2.0
Group: Networking/Mail
URL: https://mxr-mail.vercel.app
VCS: https://github.com/planetaryescape/mxr

Source: %name-%version.tar
Source1: vendor.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(openssl)

%description
Your email, on your computer, usable from the terminal or your agent.
mxr syncs Gmail, Outlook, Microsoft 365, and IMAP accounts into one local mailbox.
It keeps your message history in SQLite, builds a local search index, and exposes
the same mail controls through a TUI, a pipeable CLI, a web app, MCP, and an agent
skill. Attachment names, types, and sizes are local; mxr downloads attachment
contents when you open them. Send through Gmail, Outlook, or any SMTP server.
Write mxr, say 'Mixer'.

%prep
%setup -a1
%rust_prep

%build
%rust_build
%release_bin completions bash > %name.bash
%release_bin completions zsh > %name.zsh
%release_bin completions fish > %name.fish

%install
install -Dm 0755 %release_bin %buildroot%_bindir/%name
install -Dm 0755 %release_bin-chime-player %buildroot%_bindir/%name-chime-player
install -Dm 0644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dm 0644 %name.zsh %buildroot%_datadir/zsh/site-functions/_%name
install -Dm 0644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%check
%rust_test

%files
%_bindir/%name
%_bindir/%name-chime-player
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Tue Aug 25 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.29-alt1
- Updated to version 0.6.29.

* Wed Aug 19 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.23-alt1
- Updated to version 0.6.23.

* Wed Aug 19 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.20-alt1
- Updated to version 0.6.20.

* Wed Aug 05 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.17-alt1
- Updated to version 0.6.17.

* Sat Aug 01 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.14-alt1
- Initial build for ALT.
