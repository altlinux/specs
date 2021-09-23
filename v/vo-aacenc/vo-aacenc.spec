%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Name:           vo-aacenc
Version:        0.1.3
Release:        alt2
Summary:        VisualOn AAC encoder library
Group:          System/Libraries
License:        Apache License v2
URL:            https://github.com/mstorsjo/vo-aacenc
Source:         %name-%version.tar

%description
This library contains an encoder implementation of the Advanced Audio
Coding (AAC) audio codec. The library is based on a codec implementation
by VisualOn as part of the Stagefright framework from the Google
Android project.

%package -n lib%name
Summary:        Development files for %name
Group:          System/Libraries

%description -n lib%name
The lib%name package contains libraries and header files for
developing applications that use %name.

%package -n lib%name-devel
Summary:        Development files for %name
Group:          System/Libraries
Requires:       pkgconfig, lib%name = %version-%release

%description  -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files -n lib%name
%doc README COPYING ChangeLog NOTICE
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/%name
%_libdir/pkgconfig/*.pc

%changelog
* Thu Sep 23 2021 Igor Vlasenko <viy@altlinux.org> 0.1.3-alt2
- fixed build with LTO

* Tue Feb 25 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.3-alt1
- first build for ALT Linux
