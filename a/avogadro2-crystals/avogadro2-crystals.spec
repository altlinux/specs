Name: avogadro2-crystals
Version: 2.0.0
Release: alt1

Summary: Crystal structure database used by Avogadro2.
Group: Sciences/Chemistry
License: BSD-3-Clause
URL: http://avogadro.openmolecules.net/
VCS: https://github.com/OpenChemistry/crystals

Source: %name-%version.tar

BuildArch: noarch

%description
Crystallographic files of common materials, elements, oxides,
for visualization in Avogadro, including:
* All elements
* Common oxides (SiO2, CaO, etc.)
* Common halides (NaCl, etc.)
* Ice
* Zeolites
* Silicates, Carbonates, etc.
* Sulfides, Selenides, Tellurides (e.g., ZnS, etc.)
* Nitrides, Phosphides, Arsenides (e.g., GaAs, InP, etc.)

%prep
%setup

%install
mkdir -p %buildroot%_datadir/avogadro2/crystals
cp -a * %buildroot%_datadir/avogadro2/crystals/
rm -f %buildroot%_datadir/avogadro2/crystals/README*

%files
%_datadir/avogadro2/crystals
%doc README.md

%changelog
* Fri Apr 24 2026 Valentin Sokolov <sova@altlinux.org> 2.0.0-alt1
- Update to version 2.0.0.

* Fri Feb 06 2026 Valentin Sokolov <sova@altlinux.org> 1.103.0-alt1
- Update to version 1.103.0.

* Mon Jan 26 2026 Valentin Sokolov <sova@altlinux.org> 1.102.1-alt1
- Initial build for Sisyphus.
