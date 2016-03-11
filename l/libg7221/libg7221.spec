Summary:    libg722_1 is a library for the ITU G.722.1 and Annex C wideband speech codecs.
Name:       libg7221
Version:    0.2.0
Release:    alt1
License:    Polycom
Group:      System/Libraries
URL:        http://www.soft-switch.org/libg722_1
# https://freeswitch.org/stash/projects/SD/repos/libg7221/browse
# https://freeswitch.org/stash/scm/sd/libg7221.git
Source:     %name-%version.tar
Patch0:     %name-%version-%release.patch

BuildRequires: libaudiofile-devel
BuildRequires: doxygen libtool

%description
libg722_1 is a library for the ITU G.722.1 and Annex C wideband speech codecs.

%package devel
Summary:    G.722.1 development files
Group:      Development/C
Requires:   %name = %version-%release

%description devel
libg722_1 development files.

%prep
%setup -q
%patch0 -p1

%build
./autogen.sh
%configure --enable-doc --disable-static --disable-rpath
%make

%install
%make install DESTDIR=%buildroot

%files
%doc ChangeLog AUTHORS COPYING NEWS README 
%{_libdir}/libg722_1.so.*

%files devel
%doc doc/api
%_includedir/g722_1.h
%_includedir/g722_1
%_libdir/libg722_1.so
%_libdir/pkgconfig/g722_1.pc

%changelog
* Wed Mar 02 2016 Anton Farygin <rider@altlinux.ru> 0.2.0-alt1
- first build for Sisyphus from Freeswitch repository
