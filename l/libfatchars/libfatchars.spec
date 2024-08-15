%define soname 1

Name: libfatchars
Version: 0.9
Release: alt1

Summary: Lowlevel UTF-8 library
License: GPLv3
Group: System/Libraries

URL: https://github.com/saahriktu/libfatchars
Source: %name-%version.tar

%description
Lowlevel UTF-8 library

%package -n %name%soname
Summary: Lowlevel UTF-8 library
Group: System/Libraries

%description -n %name%soname
Lowlevel UTF-8 library

int sizeoffatc(int); - returns the character size by head byte
int rsizeoffatc(int); - returns the characrer size by code point
int ismodifierfatc(int); - check for modifiers ranges
int decodefatc(int, int, int, int, int); - decode character bytes
int fgetfatc(FILE *); - reads the UTF-8 character from stream
int nextfatc(FILE *); - jumps to next UTF-8 character in stream
int nextvisfatc(FILE *); - jumps to next visible UTF-8 character in stream
int fputfatc(int, FILE *); - puts the UTF-8 character into stream

%package devel
Summary: Development files for Lowlevel UTF-8 library
Group: Development/C

%description devel
This package provides header files to include and libraries to link with
Lowlevel UTF-8 library

%prep
%setup

%build
%make

%install
libdir=%_libdir prefix=%_usr %makeinstall_std

%files -n %name%soname
%_libdir/libfatchars.so.%soname

%files devel
%_libdir/libfatchars.so
%_includedir/fatchars/fatchars.h

%changelog
* Wed Jun 12 2024 Artem Kurashov <saahriktu@altlinux.org> 0.9-alt1
- Initial package.
