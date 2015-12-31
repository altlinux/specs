Summary: This library provides functions to read, create, and modify mp4 files
Name: libmp4v2-2
Version: 1.9.1
Release: alt3
License: MPLv1.1
Group: System/Legacy libraries
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

%prep
%setup
%patch -p1

%build
%autoreconf
%configure --disable-static --disable-debug

%make_build

%install

%makeinstall_std

%files
%doc COPYING
%_libdir/*.so.*

%changelog
* Fri Jan  1 2016 Terechkov Evgenii <evg@altlinux.org> 1.9.1-alt3
- Fix FTBFS

* Sat Sep  5 2015 Terechkov Evgenii <evg@altlinux.org> 1.9.1-alt2
- Rebuilt as compat package without subpackages (devel,utils)

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.1-alt1.1
- Fixed build

* Mon Jan 17 2011 Alexey Shabalin <shaba@altlinux.ru> 1.9.1-alt1
- initial build for ALT Linux Sisyphus
