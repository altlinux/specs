# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_name dicom
Name: octave-%octave_pkg_name
Version: 0.2.1
Release: alt1
Summary: dicom: file io for medical images and other data

Group: Sciences/Mathematics
License: GPL version 3 or later
URL: http://octave.org/wiki/index.php?title=Dicom

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octave_pkg_name}-%{version}.tar.gz

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
%setup -q -n %{octave_pkg_name}-%{version}

%build
octave -q -H --no-window-system --no-site-file --eval "pkg build -verbose -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
%if_with _octave_arch
octave -H --no-window-system --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -nodeps -verbose -local %octave_pkg_name-%version-$(octave -H --no-window-system --no-site-file --eval "printf([__octave_config_info__(\"canonical_host_type\"), \"-\",  __octave_config_info__(\"api_version\")])").tar.gz"
%else
octave -q -H --no-window-system --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -nodeps -verbose -local %octave_pkg_name-%version-any-none.tar.gz"
%endif

%files
%doc COPYING DESCRIPTION NEWS
%_datadir/octave/packages/%octave_pkg_name-%version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%version
%endif

%changelog
* Wed Mar 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1
- initial import by package builder

