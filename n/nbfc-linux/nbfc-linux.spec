Name: nbfc-linux
Version: 0.2.7
Release: alt2

Summary: NoteBook FanControl
License: GPL-3.0
Group: System/Configuration/Other

Url: https://github.com/nbfc-linux/nbfc-linux
# Source-url: https://github.com/nbfc-linux/nbfc-linux/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++ clang
BuildRequires: pkgconfig(systemd)

Requires: %_bindir/python3

ExclusiveArch: x86_64

%description
NoteBook FanControl ported to Linux

%prep
%setup

%build
%autoreconf
%configure
%make_build BUILD=debug

%install
%makeinstall_std

%files
%_bindir/ec_probe
%_bindir/nbfc
%_bindir/nbfc_service
%_unitdir/nbfc_service.service
%_datadir/bash-completion/completions/ec_probe
%_datadir/bash-completion/completions/nbfc
%_datadir/bash-completion/completions/nbfc_service
%_datadir/fish/completions/ec_probe.fish
%_datadir/fish/completions/nbfc.fish
%_datadir/fish/completions/nbfc_service.fish
%_datadir/zsh/site-functions/_ec_probe
%_datadir/zsh/site-functions/_nbfc
%_datadir/zsh/site-functions/_nbfc_service
%_man1dir/ec_probe.1.xz
%_man1dir/nbfc.1.xz
%_man1dir/nbfc_service.1.xz
%_man5dir/nbfc_service.json.5.xz
%_datadir/nbfc/configs/*

%changelog
* Sat Jun 22 2024 Boris Yumankulov <boria138@altlinux.org> 0.2.7-alt2
- rebuild for fix service path

* Sun Jun 16 2024 Boris Yumankulov <boria138@altlinux.org> 0.2.7-alt1
- new version 0.2.7

* Thu May 30 2024 Boris Yumankulov <boria138@altlinux.org> 0.1.15-alt1
- initial build for ALT Sisyphus

