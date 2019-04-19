# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg dicom
Name: octave-%octpkg
Version: 0.2.2
Release: alt1
Summary: dicom: file io for medical images and other data

Group: Sciences/Mathematics
License: GPL version 3 or later
URL: http://octave.org/wiki/index.php?title=Dicom

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(dicom) = %version

# SystemRequirements: libgdcm2.0 (>= 2.0.16)
BuildRequires: gdcm-devel >= 2.0.16


%description
Digital communications in medicine (DICOM) file io.

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc DESCRIPTION COPYING NEWS
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Fri Apr 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1
- regenerated from template by package builder

* Wed Mar 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1
- initial import by package builder

