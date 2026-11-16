Name: avogadro2-fragments
Version: 2.1.0
Release: alt1

Summary: Molecular fragments and monomers used by Avogadro2
Group: Sciences/Chemistry
License: BSD-3-Clause
URL: https://avogadro.cc/
VCS: https://github.com/OpenChemistry/fragments

Source: %name-%version.tar

BuildArch: noarch

%description
Molecular fragments and inorganic ligands for building structures in Avogadro2,
including functional groups, amino acids for the peptide builder and monomers
for the polymer builder. This package contains ready-to-use data files.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/avogadro2/fragments
cp -a amino groups ligands polymers %buildroot%_datadir/avogadro2/fragments/

%files
%_datadir/avogadro2/fragments
%doc README.md LICENSE

%changelog
* Tue Nov 10 2026 Valentin Sokolov <sova@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus.
