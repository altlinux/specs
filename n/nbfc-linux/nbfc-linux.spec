%define _unpackaged_files_terminate_build 1

Name: nbfc-linux
Version: 0.4.0
Release: alt1

Summary: NoteBook FanControl
License: GPL-3.0
Group: System/Configuration/Other

Url: https://github.com/nbfc-linux/nbfc-linux
# Source-url: https://github.com/nbfc-linux/nbfc-linux/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++ clang
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libcurl)
BuildRequires: %_bindir/python3

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
%_datadir/nbfc/model_support.json
%_datadir/bash-completion/completions/ec_probe
%_datadir/bash-completion/completions/nbfc
%_datadir/bash-completion/completions/nbfc_service
%_datadir/fish/vendor_completions.d/ec_probe.fish
%_datadir/fish/vendor_completions.d/nbfc.fish
%_datadir/fish/vendor_completions.d/nbfc_service.fish
%_datadir/zsh/site-functions/_ec_probe
%_datadir/zsh/site-functions/_nbfc
%_datadir/zsh/site-functions/_nbfc_service
%_man1dir/ec_probe.1.xz
%_man1dir/nbfc.1.xz
%_man1dir/nbfc_service.1.xz
%_man5dir/nbfc_service.json.5.xz
%_datadir/nbfc/configs/*

%changelog
* Mon Mar 23 2026 Boris Yumankulov <boria138@altlinux.org> 0.4.0-alt1
- new version 0.4.0

* Thu Jun 19 2025 Boris Yumankulov <boria138@altlinux.org> 0.3.19-alt1
- new version 0.3.19

* Sun May 25 2025 Boris Yumankulov <boria138@altlinux.org> 0.3.18-alt1
- new version 0.3.18

* Fri May 23 2025 Boris Yumankulov <boria138@altlinux.org> 0.3.17-alt1
- new version 0.3.17

* Sat May 10 2025 Boris Yumankulov <boria138@altlinux.org> 0.3.15-alt1
- new version 0.3.15

* Mon May 05 2025 Boris Yumankulov <boria138@altlinux.org> 0.3.13-alt1
- new version 0.3.13

* Sat Jun 22 2024 Boris Yumankulov <boria138@altlinux.org> 0.2.7-alt2
- rebuild for fix service path

* Sun Jun 16 2024 Boris Yumankulov <boria138@altlinux.org> 0.2.7-alt1
- new version 0.2.7

* Thu May 30 2024 Boris Yumankulov <boria138@altlinux.org> 0.1.15-alt1
- initial build for ALT Sisyphus

