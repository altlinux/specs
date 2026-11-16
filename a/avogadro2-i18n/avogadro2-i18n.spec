Name: avogadro2-i18n
Version: 2.1.0
Release: alt1

Summary: Translations for Avogadro app and libraries
Group: Sciences/Chemistry
License: BSD-3-Clause
URL: https://avogadro.cc/
VCS: https://github.com/OpenChemistry/avogadro-i18n

Source: %name-%version.tar

BuildArch: noarch

Requires: fonts-ttf-google-noto-sans-bengali
Requires: fonts-ttf-google-noto-sans-kannada
Requires: fonts-ttf-google-noto-sans-telugu


%description
Translations for Avogadro app and libraries.

%prep
%setup

%install

mkdir -p %buildroot%_datadir/avogadro2/i18n
install -pm 644 avogadroapp/* %buildroot%_datadir/avogadro2/i18n/
install -pm 644 avogadrolibs/* %buildroot%_datadir/avogadro2/i18n/


%files
%_datadir/avogadro2/i18n
%doc README.md LICENSE

%changelog
* Tue Nov 10 2026 Valentin Sokolov <sova@altlinux.org> 2.1.0-alt1
- Update to version 2.1.0.
- Require Bengali, Kannada and Telugu fonts for the language selector (closes: #59559).

* Mon Sep 21 2026 Valentin Sokolov <sova@altlinux.org> 2.0.0-alt2
- Update project URL.

* Tue Apr 14 2026 Valentin Sokolov <sova@altlinux.org> 2.0.0-alt1
- Update to version 2.0.0

* Fri Feb 06 2026 Valentin Sokolov <sova@altlinux.org> 1.103.0-alt1
- Update to version 1.103.0.

* Mon Jan 26 2026 Valentin Sokolov <sova@altlinux.org> 1.102.1-alt1
- Initial build for Sisyphus.
