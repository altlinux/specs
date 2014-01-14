%define octave_pkg_name ode
%define octave_descr_name ODE
Name: octave-%octave_pkg_name
Version: 1.0.1
Release: alt2
Summary: Ordinary Differential Equation (ODE) Solvers

Group: Sciences/Mathematics
License: GPL version 2 or later
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
# Depends: octave (>= 2.9.7)
Requires: octave >= 2.9.7
Provides: octave(ode) = 1.0.1


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Ordinary Differential Equation (ODE) Solvers

%prep
%setup -n %octave_pkg_name

%build
octave -q -H --no-site-file --eval "pkg build -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
octave -q -H --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -local -nodeps %octave_pkg_name-%version.tar.gz"

# The package contains a CVS/.svn/.git/.hg/.bzr/_MTN directory of revision control system.
# It was most likely included by accident since CVS/.svn/.hg/... etc. directories 
# usually don't belong in releases. 
# When packaging a CVS/SVN snapshot, export from CVS/SVN rather than use a checkout.
find $RPM_BUILD_ROOT -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:
# the find below is useful in case those CVS/.svn/.git/.hg/.bzr/_MTN directory is added as %%doc
find . -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:

%files
%_datadir/octave/packages/%octave_pkg_name-%version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%version
%endif

%changelog
* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1.0.1-alt2
- Rebuild with the next version of Octave: 3.8.0

* Mon Aug 27 2012 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.1-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * pkg-contains-cvs-or-svn-control-dir for octave-ode

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1
- initial import by octave-package-builder

