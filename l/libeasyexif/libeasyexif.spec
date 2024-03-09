%define        _unpackaged_files_terminate_build 1
%define        cname EasyExif
%define        oname easyexif

Name:          lib%{oname}
Version:       2.2.1
Release:       alt1
Summary:       Tiny ISO-compliant C++ EXIF parsing library
License:       BSD-2-Clause
Group:         System/Libraries
Url:           https://github.com/mayanklahiri/easyexif
Vcs:           https://github.com/mayanklahiri/easyexif.git

Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

%description
A tiny ISO-compliant C++ EXIF parsing library.

EasyEXIF is a tiny, lightweight C++ library that parses basic information out of
JPEG files. It uses only the std::string library and is otherwise pure C++. You
pass it the binary contents of a JPEG file, and it parses several of the most
important EXIF fields for you.

Why use this library? Include one .h file, compile one .cc file, and that's it.

Sometimes you just need to quickly extract basic information from a JPEG file's
EXIF headers: the time the image was taken (not the file timestamp, the camera's
internal time), the F-stop or exposure time, GPS information embedded in the
EXIF file, what the camera make and model was, etc. Unfortunately, all the EXIF
libraries out there are not very lightweight or easy to integrate into larger
programs. EasyEXIF aims to solve that problem, and is released under a very
liberal BSD License for use practically anywhere.


%package       -n %name-devel
Summary:       Tiny ISO-compliant C++ EXIF parsing library development files
Group:         Development/Other
Requires:      %name = %version-%release

Requires:      cmake
Requires:      gcc-c++

%description   -n %name-devel
Tiny ISO-compliant C++ EXIF parsing library development files.

A tiny ISO-compliant C++ EXIF parsing library.

EasyEXIF is a tiny, lightweight C++ library that parses basic information out of
JPEG files. It uses only the std::string library and is otherwise pure C++. You
pass it the binary contents of a JPEG file, and it parses several of the most
important EXIF fields for you.

Why use this library? Include one .h file, compile one .cc file, and that's it.

Sometimes you just need to quickly extract basic information from a JPEG file's
EXIF headers: the time the image was taken (not the file timestamp, the camera's
internal time), the F-stop or exposure time, GPS information embedded in the
EXIF file, what the camera make and model was, etc. Unfortunately, all the EXIF
libraries out there are not very lightweight or easy to integrate into larger
programs. EasyEXIF aims to solve that problem, and is released under a very
liberal BSD License for use practically anywhere.


%prep
%setup
%autopatch -p1

%build
%cmake_insource
%cmake_build

%install
%cmakeinstall_std

%files
%doc *.md CONTRIBUTORS LICENSE
%_libdir/lib%{oname}*.so.*

%files         -n %name-devel
%doc *.md CONTRIBUTORS LICENSE
%_libdir/lib%{oname}*.so
%_includedir/%oname/
%_cmakedir/%{cname}
%_datadir/cmake/Modules/%{oname}*.cmake

%changelog
* Wed Mar 06 2024 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt1
- Initial build v2.2.1 for Sisyphus
