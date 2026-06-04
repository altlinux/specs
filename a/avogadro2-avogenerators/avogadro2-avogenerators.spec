Name: avogadro2-avogenerators
Version: 2.0.0
Release: alt1

Summary: Python input file generators for Avogadro2
Group: Sciences/Chemistry
License: BSD-3-Clause
URL: http://avogadro.openmolecules.net/
VCS: https://github.com/OpenChemistry/avogenerators

# These Python scripts are not standalone executables and are not imported
# as Python modules. They are used internally by Avogadro2
%add_findprov_skiplist %_libexecdir/avogadro2/plugins/generators*
%add_findreq_skiplist %_libexecdir/avogadro2/plugins/generators*

Source: %name-%version.tar

BuildArch: noarch

%description
This package contains the Python input generators that can be run
by the Avogadro 2 application to generate input for various codes:
* NWChem
* Gaussian
* MOPAC
* Orca
* Q-Chem
* Dalton
* GAMESS-UK
* Psi4
* (etc.)


%prep
%setup

%install
mkdir -p %buildroot%_libexecdir/avogadro2/plugins/generators
cp -a scripts src tests pyproject.toml  %buildroot%_libexecdir/avogadro2/plugins/generators

%files
%_libexecdir/avogadro2/plugins/generators
%doc README.md LICENSE

%changelog
* Fri Apr 24 2026 Valentin Sokolov <sova@altlinux.org> 2.0.0-alt1
- Update to version 2.0.0

* Fri Feb 06 2026 Valentin Sokolov <sova@altlinux.org> 1.103.0-alt1
- Update to version 1.103.0

* Mon Jan 26 2026 Valentin Sokolov <sova@altlinux.org> 1.102.1-alt1
- Initial build for Sisyphus.
