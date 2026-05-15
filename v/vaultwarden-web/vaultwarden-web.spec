Name:    vaultwarden-web
Version: 2026.4.1
Release: alt1

Summary: Web vault builds for vaultwarden
License: GPL-3.0+
Group:   Security/Networking
Url:     https://github.com/dani-garcia/bw_web_builds
# Source-url: https://github.com/dani-garcia/bw_web_builds/releases/download/v2026.4.1/bw_web_v2026.4.1.tar.gz

Source0: %name-%version.tar
Source1: web-vault.tar

BuildArch: noarch

%description
Scripts and CI to patch (including branding) and build the Bitwarden web client,
to make it compatible with Vaultwarden.

%prep
%setup -a1

%install
install -d %buildroot%_datadir
%__cp -dRv web-vault %buildroot%_datadir/%name

%files
%doc *.md LICENSE.txt
%_datadir/%name

%changelog
* Fri May 15 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 2026.4.1-alt1
- New version.

* Wed Feb 25 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 2026.2.0-alt1
- New version.

* Mon Dec 29 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 2025.12.0-alt1
- New version.

* Tue May 27 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 2025.5.0-alt1
- New version.

* Fri Jan 31 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 2025.1.1-alt1
- New version.

* Fri Dec 13 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 2024.6.2-alt1
- Initial build for Sisyphus.
