Name:    thoth
Version: 0.1.88
Release: alt1

Summary: Terminal scratchpad inspired by the Heynote app
License: MIT
Group:   Other
Url:     https://github.com/jooaf/thoth
VCS:     https://github.com/jooaf/thoth.git

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires: rpm-build-rust
BuildRequires: gcc-c++

%description
%summary

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

%files
%doc CHANGELOG.* CONTRIBUTING.* LICENSE README.*
%_bindir/%name

%changelog
* Mon May 18 2026 Sergey Palcheh <minergenon@altlinux.org> 0.1.88-alt1
- new version 0.1.88

* Wed Dec 03 2025 Sergey Palcheh <minergenon@altlinux.org> 0.1.87-alt1
- new version 0.1.87

* Mon Jul 14 2025 Sergey Palcheh <minergenon@altlinux.org> 0.1.84-alt1
- Initial build for Sisyphus

