Name: avogadro2-avogenerators
Version: 2.1.0
Release: alt1

Summary: Python input file generators for Avogadro2
Group: Sciences/Chemistry
License: BSD-3-Clause
URL: https://avogadro.cc/
VCS: https://github.com/OpenChemistry/avogenerators

Source: %name-%version.tar

Patch0: avogadro2-avogenerators-version.patch
Patch1: avogadro2-avogenerators-orca-defaults.patch
Patch2: avogadro2-avogenerators-setuptools-build.patch

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

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
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%pyproject_build

%install
%pyproject_install

# Install source to plugin directory for app discovery
mkdir -p %buildroot%_datadir/avogadro2/plugins/generators
cp -a src scripts pyproject.toml README.md LICENSE %buildroot%_datadir/avogadro2/plugins/generators/

%files
%_bindir/avogadro-generators
%python3_sitelibdir/avogadro_generators/
%python3_sitelibdir/avogadro_generators-*.dist-info
%dir %_datadir/avogadro2/plugins
%_datadir/avogadro2/plugins/generators
%doc README.md LICENSE

%changelog
* Tue Nov 10 2026 Valentin Sokolov <sova@altlinux.org> 2.1.0-alt1
- Update to version 2.1.0.
- Apply upstream project version correction.
- Drop upstreamed debug_info fix.
- Rebase ORCA defaults and setuptools patches.

* Wed Jun 24 2026 Valentin Sokolov <sova@altlinux.org> 2.0.0-alt2
- Switch build backend from uv_build to setuptools.
- Package as noarch python3 module with avogadro-generators script.
- Install generator sources to %_datadir/avogadro2/plugins/generators.
- debug_info: convert dict to JSON string.
- orca: quote numeric defaults in options.toml.
- Update project URL.

* Fri Apr 24 2026 Valentin Sokolov <sova@altlinux.org> 2.0.0-alt1
- Update to version 2.0.0

* Fri Feb 06 2026 Valentin Sokolov <sova@altlinux.org> 1.103.0-alt1
- Update to version 1.103.0.

* Mon Jan 26 2026 Valentin Sokolov <sova@altlinux.org> 1.102.1-alt1
- Initial build for Sisyphus.
