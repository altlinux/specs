Name: abinit
Version: 8.10.2
Release: alt1

Summary: Computational Chemistry DFT program
License: GPL
Group: Sciences/Chemistry

Url: http://www.abinit.org
Source: %url/sites/default/files/packages/%name-%version.tar.gz
Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildRequires: gcc-fortran
BuildRequires: liblapack-devel
BuildRequires: libopenblas-devel
BuildRequires: openmpi-devel

%description
ABINIT is a package whose main program allows one to find the total energy,
charge density and electronic structure of systems made of electrons and
nuclei (molecules and periodic solids) within Density Functional Theory (DFT),
using pseudopotentials and a planewave basis. ABINIT also includes options
to optimize the geometry according to the DFT forces and stresses, or
to perform molecular dynamics simulations using these forces, or to generate
dynamical matrices, Born effective charges, and dielectric tensors. Excited
states can be computed within the Time-Dependent Density Functional Theory
(for molecules), or within Many-Body Perturbation Theory (the GW
approximation). In addition to the main ABINIT code, different utility
programs are provided.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
#doc doc/tutorial doc/users doc/features
%_bindir/*

# TODO:
# - figure out the current docs build system
# - tests subpackage? (250+ Mb as of 8.10.2)
# - devel subpackage? (no -lab7_parser in sight though)

%changelog
* Sat Jan 26 2019 Michael Shigorin <mike@altlinux.org> 8.10.2-alt1
- 8.10.2 rebuilt for sisyphus (NB: without offline docs)
- spec cleanup

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 6.0.4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Jun 01 2010 Ilya Mashkin <oddity@altlinux.ru> 6.0.4-alt1
- 6.0.4

* Tue Aug 11 2009 Ilya Mashkin <oddity@altlinux.ru> 5.8.4-alt1
- 5.8.4

* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 5.6.4-alt1
- 5.6.4
- spec cleanup

* Mon Jul 10 2006 Andrey Khavryuchenko <akhavr@altlinux.org> 4.6.5-alt1
- Initial build
