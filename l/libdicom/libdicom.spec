
Name:           libdicom
Version:        1.0.5
Release:        alt1
Summary:        C library and tools for reading DICOM data sets
Packager: 	Ilya Mashkin <oddity@altlinux.ru>
Group:		Sciences/Medicine
License:        MIT
URL:            https://github.com/ImagingDataCommons/%{name}
Source0:        https://github.com/ImagingDataCommons/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(check)
# header-only library
BuildRequires: libuthash-devel 
# uthash-static 

%description
libdicom is a C library and a set of tools for reading files that
follow the DICOM medical imaging standard.  It allows random access to
individual frame items of Pixel Data elements, permitting efficient
processing of large DICOM images.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Group: Sciences/Medicine

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Group: Sciences/Medicine
# add HTML documentation once Hawkmoth is packaged
# https://bugzilla.redhat.com/show_bug.cgi?id=2242888

%description    doc
The %{name}-doc package contains documentation for developing
applications that use %{name}.


%package        tools
Summary:        Tools for decoding DICOM files
Group: Sciences/Medicine

%description    tools
The %{name}-tools package contains tools for decoding DICOM files.


%prep
%setup


%build
%meson
%meson_build
mv doc/source doc/text
rm doc/text/conf.py


%install
%meson_install


%check
%meson_test


%files
%{_libdir}/%{name}.so.1*

%files devel
%{_includedir}/dicom
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc README.md doc/text

%files tools
%{_bindir}/dcm-*
%{_mandir}/man1/dcm-*.1*


%changelog
* Sun Oct 15 2023 Ilya Mashkin <oddity@altlinux.ru> 1.0.5-alt1
- Build for Sisyphus

* Mon Oct 09 2023 Benjamin Gilbert <bgilbert@backtick.net> - 1.0.5-1
- Update to 1.0.5

* Mon Oct 09 2023 Benjamin Gilbert <bgilbert@backtick.net> - 1.0.3-1
- Update to 1.0.3

* Mon Oct 09 2023 Benjamin Gilbert <bgilbert@backtick.net> - 1.0.2-1
- Initial import (fedora#2241457).
