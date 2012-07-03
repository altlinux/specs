Summary: Computational Chemistry DFT program
Name: abinit
Version: 6.0.4
Release: alt1
License: GPL
Group: Sciences/Chemistry
Url: http://www.abinit.org/

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: ftp://ftp.abinit.org/pub/abinitio/ABINIT_v%version/abinit-%version.tar.gz
Patch0: abinit-gfortran.patch

BuildRequires: gcc4.3-fortran

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
%setup -q
#patch0 -p1

%build
%configure
make

%install
mkdir -p $RPM_BUILD_ROOT%_bindir
cd src/98_main
install abinetcdf $RPM_BUILD_ROOT%_bindir
install abinis $RPM_BUILD_ROOT%_bindir
install aim $RPM_BUILD_ROOT%_bindir
install anaddb $RPM_BUILD_ROOT%_bindir
#install anascr $RPM_BUILD_ROOT%_bindir 
install band2eps $RPM_BUILD_ROOT%_bindir
install conducti $RPM_BUILD_ROOT%_bindir
install cut3d $RPM_BUILD_ROOT%_bindir
install lwf $RPM_BUILD_ROOT%_bindir
install macroave $RPM_BUILD_ROOT%_bindir
install mrgddb $RPM_BUILD_ROOT%_bindir
install mrggkk $RPM_BUILD_ROOT%_bindir
install mrgscr $RPM_BUILD_ROOT%_bindir
install newsp $RPM_BUILD_ROOT%_bindir
install optic $RPM_BUILD_ROOT%_bindir

find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

%files
%doc doc/tutorial doc/users doc/features
%_bindir/*

%changelog
* Tue Jun 01 2010 Ilya Mashkin <oddity@altlinux.ru> 6.0.4-alt1
- 6.0.4

* Tue Aug 11 2009 Ilya Mashkin <oddity@altlinux.ru> 5.8.4-alt1
- 5.8.4

* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 5.6.4-alt1
- 5.6.4
- spec cleanup

* Mon Jul 10 2006 Andrey Khavryuchenko <akhavr@altlinux.org> 4.6.5-alt1
- Initial build
