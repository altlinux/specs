%set_verify_elf_method unresolved=relaxed
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/g++ /usr/bin/perl gcc-c++
# END SourceDeps(oneline)
Name:		libint
Version:	1.1.4
Release:	alt1_9
Summary:	A library for computing electron repulsion integrals efficiently
Group:		System/Libraries
License:	GPLv2+
URL:		http://sourceforge.net/p/libint
Source0:	http://downloads.sourceforge.net/libint/v1-releases/libint-%{version}.tar.gz
# Required to build documentation
BuildRequires:	texlive-base-bin
BuildRequires:	texlive-latex-recommended
Source44: import.info

%description
LIBINT computes the Coulomb and exchange integrals, which in electronic
structure theory are called electron repulsion integrals (ERIs). This is by
far the most common type of integrals in molecular structure theory.

LIBINT uses recursive schemes that originate in seminal Obara-Saika method and
Head-Gordon and Poplea.'s variation thereof. The idea of LIBINT is to optimize
computer implementation of such methods by implementing an optimizing compiler
to generate automatically highly-specialized code that runs well on
super-scalar architectures.

%package devel
Summary:	Development headers and libraries for libint
Group:		Development/C
Requires:	libint = %{version}-%{release}
Requires:	libderiv = %{version}-%{release}
Requires:	libr12 = %{version}-%{release}

%description devel
This package contains development headers and libraries for libint.
It also contains a programmer's manual.

%package -n libr12
Summary:	A library for computing integrals that arise in Kutzelnigga.'s linear R12 theories
Group:		System/Libraries

%description -n libr12
libr12 computes types integrals that appear in Kutzelnigga.'s linear R12 theories
for electronic structure. All linear R12 methods, such as MP2-R12, contain
terms in the wave function that are linear in the inter-electronic distances
r_{ij} (hence the name). Appearance of several types of two-body integrals is
due to the use of the approximate resolution of the identity to reduce three-
and four-body integrals to products of simpler integrals.

%package -n libderiv
Summary:	A library for computing derivatives of electron repulsion integrals
Group:		System/Libraries

%description -n libderiv
libderiv computes first and second derivatives of ERIs with respect to the
coordinates of the basis function origin. This type of integrals are also very
common in electronic structure theory, where they appear in analytic gradient
expressions. The derivatives are typically used in the calculation of forces.


%prep
%setup -q

%build
%configure --enable-shared --disable-static \
 --with-libint-max-am=7 --with-libderiv-max-am1=5 --with-libderiv-max-am2=4 \
 --with-libr12-max-am=6 

make CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" %{?_smp_mflags}

# Build documentation
cd doc/progman
pdflatex progman
bibtex progman
pdflatex progman
pdflatex progman


%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name *.la -delete
find %{buildroot} -name *.so.*.* -exec chmod 755 {} \;

%files
%doc LICENSE
%{_libdir}/libint*.so.*

%files -n libderiv
%{_libdir}/libderiv*.so.*

%files -n libr12
%{_libdir}/libr12*.so.*

%files devel
%doc doc/progman/progman.pdf
%{_includedir}/libint/
%{_includedir}/libderiv/
%{_includedir}/libr12/
%{_libdir}/*.so


%changelog
* Wed Jan 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1_9
- initial fc import

