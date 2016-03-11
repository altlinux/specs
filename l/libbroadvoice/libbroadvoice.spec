Summary: broadvoice - a library for the BroadVoice 16 and 32 speech codecs
Name: libbroadvoice
Version: 0.1.0
Release: alt1
License: LGPL2.1
Group: System/Libraries
Url: http://www.soft-switch.org/broadvoice
Source: http://www.soft-switch.org/downloads/codecs/%name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libaudiofile-devel
BuildRequires: doxygen

%description
broadvoice is a library for the BroadVoice 16 and 32 speech codecs.

%package devel
Summary: BroadVoice development files
Group: Development/C
Requires: libbroadvoice = %version

%description devel
libbroadvoice development files.

%prep
%setup
%patch0 -p1

%build
./autogen.sh
%configure --enable-doc --disable-static --disable-rpath --exec-prefix=/usr
%make

%install
%makeinstall

%files
%doc ChangeLog AUTHORS COPYING NEWS README

%_libdir/libbroadvoice.so.*

%files devel
%doc doc/api
%_includedir/broadvoice.h
%_includedir/broadvoice
%_libdir/libbroadvoice.so
%_libdir/pkgconfig/broadvoice.pc

%changelog
* Thu Feb 11 2016 Anton Farygin <rider@altlinux.ru> 0.1.0-alt1
- first build for Sisyphus