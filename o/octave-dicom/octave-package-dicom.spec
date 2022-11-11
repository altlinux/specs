AutoReqProv: yes,nopython
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave-config makeinfo texinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg dicom
Name: octave-%octpkg
Version: 0.4.1
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
# Depends: octave (>= 3.8.0)
Requires: octave >= 3.8.0


%description
Digital communications in medicine (DICOM) file io.

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc README.md COPYING DESCRIPTION NEWS doc
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Fri Apr 08 2022 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt1
- new version

* Tue May 18 2021 Igor Vlasenko <viy@altlinux.org> 0.4.0-alt2
- fixed build

* Tue Dec 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- regenerated from template by package builder

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt2
- rebuild with gbcm

* Fri Apr 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1
- regenerated from template by package builder

* Wed Mar 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1
- initial import by package builder

