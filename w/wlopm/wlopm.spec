# TODO
%define bash_completions_dir %_datadir/bash-completion/completions

Name: wlopm
Version: 1.0.0
Release: alt1

Summary: wlr-output-power-management-v1 client

License: GPL-3.0-only
Group: System/Configuration/Hardware
Url: https://sr.ht/~leon_plickat/wlopm/

# Source0: https://git.sr.ht/~leon_plickat/wlopm/archive/v%version.tar.gz#/%name-v%version.tar.gz
Source0: %name-%version.tar

BuildRequires: pkgconfig(wayland-client) >= 1.20.0
BuildRequires: pkgconfig(wayland-scanner)

%description
Wayland output power management.
Simple client implementing zwlr-output-power-management-v1.

%prep
%setup

%build
#set_build_flags
%make_build

%install
install -d %buildroot%bash_completions_dir
%makeinstall_std PREFIX=%prefix

%files
%doc LICENSE
%doc README
%_bindir/%name
%_man1dir/%name.1*
%bash_completions_dir/%name

%changelog
* Sun Mar 09 2025 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Sisyphus

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 05 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.0-6
- convert GPLv3 license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 03 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.1.0-1
- Initial import (#2095940)
