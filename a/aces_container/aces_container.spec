Group: Development/C
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Force out of source build
%undefine __cmake_in_source_build

Name:           aces_container
Version:        1.0.2
Release:        alt1_8
Summary:        ACES Container Reference

License:        AMPAS BSD
URL:            https://github.com/ampas/aces_container
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         Switch-to-CMAKE-default-variables.patch
Patch1:         Set-the-appropriate-SONAME-for-the-library.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ctest cmake
Source44: import.info

%description
This folder contains a reference implementation for an ACES container
file writer intended to be used with the Academy Color Encoding
System (ACES). The resulting file is compliant with the ACES container
specification (SMPTE S2065-4). However, there are a few things that are
not demonstrated by this reference implementation.

    Stereo channels
    EndOfFileFiller
    Arbitrary attributes and naming validations
    half type attributes
    keycode value validations

%package -n libAcesContainer1
Summary:        Shared library for the %name library
Group:          System/Libraries

%description -n libAcesContainer1
This folder contains a reference implementation for an ACES container
file writer intended to be used with the Academy Color Encoding
System (ACES). The resulting file is compliant with the ACES container
specification (SMPTE S2065-4). However, there are a few things that are
not demonstrated by this reference implementation.

    Stereo channels
    EndOfFileFiller
    Arbitrary attributes and naming validations
    half type attributes
    keycode value validations

This package contains the shared library.

%package        -n libAcesContainer-devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       libAcesContainer1 = %EVR
Provides: %name-devel = %EVR

%description    -n libAcesContainer-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.



%prep
%setup -q
%patch0 -p1
%patch1 -p1

chmod -x aces_writeattributes.*


%build
%{fedora_v2_cmake}

%fedora_v2_cmake_build


%install
%fedora_v2_cmake_install





%files -n libAcesContainer1
%doc README.md
%doc --no-dereference LICENSE
%_libdir/libAcesContainer.so.1
%_libdir/libAcesContainer.so.1.*

%files -n libAcesContainer-devel
%dir %{_includedir}/aces/
%{_includedir}/aces/*.h
%dir %{_libdir}/cmake/AcesContainer
%{_libdir}/cmake/AcesContainer/*.cmake
%{_libdir}/libAcesContainer.so
%{_libdir}/pkgconfig/AcesContainer.pc


%changelog
* Sun Nov 08 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_8
- new version

