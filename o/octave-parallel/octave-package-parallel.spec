# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave-config makeinfo texinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg parallel
Name: octave-%octpkg
Version: 4.0.1
Release: alt1
Summary: Parallel Computing.

Group: Sciences/Mathematics
License: GPLv3+
Url: http://octave.sourceforge.net/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz
Patch: parallel-3.1.3-octave5.patch

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(parallel) = %version

# octave module BuildRequires: libgnutls..-dev
BuildRequires: libgnutls-devel
# Depends: octave (>= 4.0.0), struct (>= 1.0.12)
Requires: octave >= 4.0.0 octave(struct) >= 1.0.12


%description
Parallel execution package. See also package mpi, maintained

%prep
%setup -q -n %{octpkg}-%{version}
%patch -p1

%build
%octave_build

%install
%octave_install
mkdir -p %buildroot%_bindir
mv %buildroot%_datadir/octave/packages/parallel-%version/bin/octave-pserver %buildroot%_bindir/octave-pserver

%files
%doc NEWS DESCRIPTION COPYING doc
%_bindir/octave-pserver
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Fri Apr 08 2022 Andrey Cherepanov <cas@altlinux.org> 4.0.1-alt1
- new version

* Mon Dec 14 2020 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- new version

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 3.1.3-alt2
- rebuild with octave 5

* Tue Mar 12 2019 Igor Vlasenko <viy@altlinux.ru> 3.1.3-alt1
- regenerated from template by package builder

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 3.1.2-alt1
- initial import by package builder

