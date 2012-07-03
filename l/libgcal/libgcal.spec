Name: libgcal
Version: 0.9.6
Release: alt1
Group: System/Libraries
Summary: This is a library to access google calendar events and contacts
License: Own/Free
Url: http://code.google.com/p/libgcal/downloads/list

Source: %name-%version.tar

# Automatically added by buildreq on Mon Oct 31 2011 (-bi)
# optimized out: cmake-modules elfutils emacs-common pkg-config
#BuildRequires: cmake doxygen libcheck-devel libcurl-devel libxml2-devel xml-utils
BuildRequires: cmake doxygen libcheck-devel libcurl-devel libxml2-devel xml-utils kde-common-devel

%description
This is a library to access google calendar events and contacts,
its purpose is
    - provide easy access to available events/contacts
    - enable common operations: add, delete, edit
    - have few dependencies (up until now, only requires libcurl and libxml)

It implements Google Data API 2.0 and is tested on Linux and MacOSX.


%package devel
Summary: libgcal development libraries
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libgcal development files for Linux.

%prep
%setup -q

%build
%Kbuild

%install
%Kinstall

%files
%doc COPYING Changelog.txt README
%dir %_libdir/LibGCal/
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_libdir/LibGCal/cmake/

%changelog
* Mon Oct 31 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.6-alt1
- new version (ALT#26506)

* Wed Dec 23 2009 Grigory Milev <week@altlinux.ru> 0.9.3-alt1
- Initial build for ALT Linux.
