%define soname 12
Name: mac
Version: 10.96
Release: alt1

Summary: Monkey's Audio Codec
License: BSD-3-Clause
Group: Sound

Url: https://monkeysaudio.com
Source0: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: cmake

%description
Monkey's Audio Codec is a lossless audio codec w/ good
correspondence of compression (and decompresssion) ratio
and time.

%package -n libmac%soname
Summary: Monkey's Audio Codec shared libraries
Group: System/Libraries
%description -n libmac%soname
Monkey's Audio Codec is a lossless audio codec w/ good
correspondence of compression (and decompresssion) ratio
and time.

This package contains shared libraries from
Monkey's Audio Codec SDK

%package -n libmac-devel
Summary: Headers from Monkey's Audio Codec SDK
Summary(ru_RU.UTF-8): Заголовочные файлы SDK кодека Monkey's Audio
Group: Development/C++
Requires: libmac%soname = %EVR

%description -n libmac-devel
Monkey's Audio Codec is a lossless audio codec w/ good
correspondence of compression (and decompresssion) ratio
and time.

This package contains header files from
Monkey's Audio Codec SDK

%prep
%setup
rm -r '3rd Party' Shared/{32,64} Source/'DirectShow Filter'
sed -i 's/\r$//' Readme.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/mac

%files -n libmac%soname
%doc Readme.txt License.txt
%_libdir/libMAC.so.%soname

%files -n libmac-devel
%_libdir/libMAC.so
%_includedir/*

%changelog
* Sun Mar 16 2025 Anton Farygin <rider@altlinux.ru> 10.96-alt1
- 7.09 -> 10.96
- renamed the library package in accordance with the SharedLibsPolicy
- updated the license in accordance with the SPDX policy

* Sun Oct 03 2021 Fr. Br. George <george@altlinux.ru> 7.09-alt1
- Major version update
- License updated (it's permissive now)

* Mon Jul 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.99.u4-alt6.b5.4
- Patch console application to print error code descriptions

* Fri Jun 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.99.u4-alt6.b5.3
- Fix building with gcc-6

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.99.u4-alt6.b5.2.qa1
- NMU: rebuilt for updated dependencies.

* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.99.u4-alt6.b5.2
- Rebuilt for debuginfo

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.99.u4-alt6.b5.1
- Rebuilt for soname set-versions

* Tue May 19 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 3.99.u4-alt6.b5
- Fix building with gcc4.4 (patches from rpmfusion)

* Wed Jan 16 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 3.99.u4-alt5.b5
- Fix building

* Fri Jun 23 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 3.99.u4-alt4.b5
- Resurrected from orphaned
- Updated to 3.99-u4 build 5

* Thu Jan 20 2005 Dmitry V. Levin <ldv@altlinux.org> 3.99.u4-alt3
- Fixed compilation issues detected by g++-3.4.3.
- Corrected interpackage dependencies.

* Fri Jul  9 2004 Alexey Morozov <morozov@altlinux.org> 3.99.u4-alt2
- First 'official' release
- Added Matthew T. Ashland permission to distribute the codec
- Package group changed to Sound

* Sat Jun 12 2004 Alexey Morozov <morozov@altlinux.org> 3.99.u4-alt1
- Initial build for ALT Linux
