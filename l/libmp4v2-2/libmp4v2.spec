Summary: This library provides functions to read, create, and modify mp4 files
Name: libmp4v2-2
Version: 1.9.1
Release: alt1
License: MPLv1.1
Group: System/Libraries
Url: http://code.google.com/p/mp4v2/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ help2man texinfo

%description
The MP4v2 library provides an API to create and modify mp4 files
as defined by ISO-IEC:14496-1:2001 MPEG-4 Systems.
This file format is derived from Apple's QuickTime file format
that has been used as a multimedia file format in a variety of platforms and applications.
It is a very powerful and extensible format that can accommodate practically any type of media.

MP4v2 was originally bundled with mpeg4ip library, but has been moved into its own maintained library
due to a combination of the cessation of support of mpeg4ip and the usefulness of this library on its own.


%package -n libmp4v2-devel
Summary: Development files for the mp4v2 library
Group: Development/Other
Requires: %name = %version-%release
Conflicts: libmpeg4ip-devel

%description -n libmp4v2-devel
Development files and documentation needed to develop and compile programs
using the libmp4v2 library.

%package -n mp4v2-utils
Group: Sound
Summary: Command line utils to handle MP4 metadata
Conflicts: mpeg4ip-tools

%description -n mp4v2-utils
The libmp4v2 library provides an abstraction layer for working with files
using the mp4 container format. This library is developed by mpeg4ip project
and is an exact copy of the library distributed in the mpeg4ip package.

This contains the command line example utilities.


%prep
%setup
%patch -p1

%build
%autoreconf
%configure --disable-static --disable-debug

%make_build
%make txt

%install

%makeinstall_std

%files
%doc COPYING
%_libdir/*.so.*

%files -n libmp4v2-devel
%doc README
%doc doc/articles/txt/*.txt
%_includedir/*
%_libdir/*.so

%files -n mp4v2-utils
%_bindir/*
%_man1dir/*

%changelog
* Mon Jan 17 2011 Alexey Shabalin <shaba@altlinux.ru> 1.9.1-alt1
- initial build for ALT Linux Sisyphus
