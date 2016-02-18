Summary: libcodec2 is a library for the codec2 low bit rate speech codec
Name: libcodec2
Version: 0.5
Release: alt1
License: LGPL2.1
Group: System/Libraries
Url: http://rowetel.com/codec2.html
Source: %name-%version.tar
BuildRequires: cmake

%description
libcodec2 is a library for the codec2 low bit rate speech codec.

%package devel
Summary: codec2 development files
Group: Development/C
Requires: libcodec2 = %version-%release

%description devel
codec2 development files.

%prep
%setup

%build
%cmake
%make -C BUILD

%install
make -C BUILD install DESTDIR=%buildroot

# Create and install pkgconfig file
mkdir -p %buildroot%_libdir/pkgconfig
cat > %buildroot%_libdir/pkgconfig/codec2.pc << EOF
prefix=%prefix
exec_prefix=\${prefix}
includedir=\${prefix}/include/codec2
libdir=\${exec_prefix}/%_lib
Name: codec2
Description: Next-Generation Digital Voice for Two-Way Radio
Version: %version
Cflags: -I\${includedir}
Libs: -L\${libdir} -lcodec2
EOF


%files
%_libdir/libcodec2.so.*

%files devel
%_includedir/codec2
%_libdir/libcodec2.so
%_libdir/pkgconfig/codec2.pc

%changelog
* Thu Feb 18 2016 Anton Farygin <rider@altlinux.ru> 0.5-alt1
- first build for Sisyphus
