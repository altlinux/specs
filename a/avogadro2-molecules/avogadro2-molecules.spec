Name: avogadro2-molecules
Version: 2.0.0
Release: alt1

Summary: Common molecule fragments for visualization in Avogadro2
Group: Sciences/Chemistry
License: BSD-3-Clause
URL: http://avogadro.openmolecules.net/
VCS: https://github.com/OpenChemistry/molecules

Source: %name-%version.tar

BuildArch: noarch

%description
Common molecule fragments for visualization in Avogadro2,
including a variety of organic functional groups:
* alcohols
* aldehydes
* alkanes
* alkenes
* alkynes
* amides
* amines
* amino acids
* aromatics
* carbamides
* carbohydrates
* carboxylic acids
* coordination
* cyclic alkanes
* cyclic alkenes
* cyclic sugars
* ethers
* fatty acids
* fullerenes
* heteroaromatics
* ketones
* ligands
* macrocycles
* nitriles
* nucleobases
* steroids
* sulfoxides
* thiols


%prep
%setup

%install
mkdir -p %buildroot%_datadir/avogadro2/molecules
cp -a * %buildroot%_datadir/avogadro2/molecules/
rm -f %buildroot%_datadir/avogadro2/molecules/README*

%files
%_datadir/avogadro2/molecules
%doc README.md

%changelog
* Mon Apr 27 2026 Valentin Sokolov <sova@altlinux.org> 2.0.0-alt1
- Update to version 2.0.0.

* Fri Feb 06 2026 Valentin Sokolov <sova@altlinux.org> 1.103.0-alt1
- Update to version 1.103.0.

* Mon Jan 26 2026 Valentin Sokolov <sova@altlinux.org> 1.102.1-alt1
- Initial build for Sisyphus.

