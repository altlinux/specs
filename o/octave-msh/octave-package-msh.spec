# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 1.0.10
%define octave_pkg_name msh
%define octave_descr_name msh
Name: octave-%octave_pkg_name
Version: 1.0.10
Release: alt1
Summary: MeSHing software package for octave

Group: Sciences/Mathematics
License: GPLv2+
URL: http://octave.sf.net

Source0: http://downloads.sourceforge.net/octave/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(msh) = %version

# SystemRequirements: gmsh (>= 1.6.5 (optional)), awk (optional), dolfin (>= 1.3 optional)
BuildRequires: gmsh >= 1.6.5
# Depends: octave (>= 3.0), splines
Requires: octave >= 3.0 octave(splines)


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Create and manage triangular and tetrahedral meshes for Finite Element or Finite Volume PDE solvers. Use a mesh data structure compatible with PDEtool. Rely on gmsh for unstructured mesh generation.

%prep
%setup -q -n %{octave_pkg_name}

%build
octave -q -H --no-site-file --eval "pkg build -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
octave -q -H --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -local -nodeps %octave_pkg_name-%octave_pkg_version.tar.gz"

%files
%_datadir/octave/packages/%octave_pkg_name-%octave_pkg_version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%octave_pkg_version
%endif

%changelog
* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1.0.2-alt3
- Rebuild with the next version of Octave: 4.0.0

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1.0.2-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1
- initial import by octave-package-builder

