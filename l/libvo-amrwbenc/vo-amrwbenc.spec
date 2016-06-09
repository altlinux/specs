%define rname vo-amrwbenc

Name:			lib%rname
Version:		0.1.3
Release:		alt1
Summary:		VisualOn AMR-WB encoder library
Group:			System/Libraries
License:		ASL 2.0
URL:			http://opencore-amr.sourceforge.net/

Source0:		http://sourceforge.net/projects/opencore-amr/files/%{rname}/%{rname}-%{version}.tar.gz

%description
This library contains an encoder implementation of the Adaptive
Multi Rate Wideband (AMR-WB) audio codec. The library is based
on a codec implementation by VisualOn as part of the Stagefright
framework from the Google Android project.

%package    devel
Summary:	Development files for %name
Group:		Development/Other
Requires:	%name = %version-%release

%description    devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q -n %rname-%version

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc COPYING README NOTICE
%_libdir/libvo-amrwbenc.so.*

%files devel
%_includedir/%rname
%_libdir/libvo-amrwbenc.so
%_libdir/pkgconfig/vo-amrwbenc.pc

%changelog
* Thu Jun 09 2016 Andrey Cherepanov <cas@altlinux.org> 0.1.3-alt1
- New version

* Wed Apr 17 2013 Andrey Cherepanov <cas@altlinux.org> 0.1.2-alt1
- Initial build in Sisyphus from Fedora

