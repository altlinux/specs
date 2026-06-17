%global srcname NBping

Name:    nbping
Version: 0.7.0
Release: alt1

Summary: Nping mean NB Ping, A Ping Tool in Rust with Real-Time Data and Visualizations
License: MIT
Group:   Other
Url:     https://github.com/hanshuaikang/NBping
VCS:     https://github.com/hanshuaikang/NBping.git

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires: rpm-build-rust
BuildRequires: gcc-c++

Provides: nping = %version-%release
Obsoletes: nping < 0.6.1

%description
NBping is a Ping tool developed in Rust. It supports concurrent Ping for
multiple addresses, visual chart display, real-time data updates,
and other features.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

%files
%doc LICENSE README.*
%_bindir/%name

%changelog
* Wed Jun 17 2026 Sergey Palcheh <minergenon@altlinux.org> 0.7.0-alt1
- new version 0.7.0

* Mon May 18 2026 Sergey Palcheh <minergenon@altlinux.org> 0.6.1-alt1
- new version 0.6.1
- upstream renamed project to NBping
- package renamed from nping to nbping

* Wed Dec 03 2025 Sergey Palcheh <minergenon@altlinux.org> 0.5.0-alt1
- new version 0.5.0

* Mon Jul 14 2025 Sergey Palcheh <minergenon@altlinux.org> 0.4.0-alt1
- initial build for ALT Sisyphus
