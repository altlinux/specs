# [for (x)emacs] -*-  mode: RPM-SPEC; coding: utf-8 -*-
%define codec_ver 3.99-u4
%define pack_ver %(echo %codec_ver | sed -e 's/-/./')

%define license_file %_defaultdocdir/%name-%pack_ver/License.htm
%define permission_file %_defaultdocdir/%name-%pack_ver/MAC-ALTLinux-permission.html
%define permission_url http://www.monkeysaudio.com/cgi-bin/YaBB/YaBB.cgi?board=general;action=display;num=1088841050

Name: mac
Version: 3.99.u4
Release: alt6.b5.2

Summary: Monkey's Audio Codec
License: Distributable (see License.htm)
Group: Sound

Url: http://www.monkeysaudio.com
Source0: %name-%version.tar
Source1: MAC-ALTLinux-permission.html

Packager: Vladimir V Kamarzin <vvk@altlinux.ru>
Requires: libmac = %version-%release
BuildRequires: gcc-c++ libstdc++-devel nasm

%def_disable static

%description
Monkey's Audio Codec is a lossless audio codec w/ good
correspondence of compression (and decompresssion) ratio
and time.

Monkey's Audio Codec can be used for personal, educational
and non-commercial purposes. Commercial usage requires
prior written permission from Monkey's Audio author.
See %license_file before usage.

MAC's author Matthew T. Ashland permitted ALTLinux to include
the codec and its SDK into ALTLinux distributions. Text of
the permission can be found in %permission_file or
at %permission_url

%package -n libmac
Summary: Monkey's Audio Codec shared libraries
Group: System/Libraries
%description -n libmac
Monkey's Audio Codec is a lossless audio codec w/ good
correspondence of compression (and decompresssion) ratio
and time.

Monkey's Audio Codec can be used for personal, educational
and non-commercial purposes. Commercial usage requires
prior written permission from Monkey's Audio author.
See %license_file before usage.

MAC's author Matthew T. Ashland permitted ALTLinux to include
the codec and its SDK into ALTLinux distributions. Text of
the permission can be found in %permission_file or
at %permission_url

This package contains shared libraries from
Monkey's Audio Codec SDK

%package -n libmac-devel
Summary: Headers from Monkey's Audio Codec SDK
Summary(ru_RU.UTF-8): Заголовочные файлы SDK кодека Monkey's Audio
Group: Development/C++
Requires: libmac = %version-%release

%description -n libmac-devel
Monkey's Audio Codec is a lossless audio codec w/ good
correspondence of compression (and decompresssion) ratio
and time.

Monkey's Audio Codec can be used for personal, educational
and non-commercial purposes. Commercial usage requires
prior written permission from Monkey's Audio author.
See %license_file before usage.

MAC's author Matthew T. Ashland permitted ALTLinux to include
the codec and its SDK into ALTLinux distributions. Text of
the permission can be found in %permission_file or
at %permission_url

This package contains header files from
Monkey's Audio Codec SDK

%if_enabled static
%package -n libmac-devel-static
Summary: Static libraries from Monkey's Audio Codec SDK
Group: Development/C++
Requires: libmac-devel = %version-%release
BuildRequires: libstdc++-devel-static

%description -n libmac-devel-static
Monkey's Audio Codec is a lossless audio codec w/ good
correspondence of compression (and decompresssion) ratio
and time.

Monkey's Audio Codec can be used for personal, educational
and non-commercial purposes. Commercial usage requires
prior written permission from Monkey's Audio author.
See %license_file before usage.

MAC's author Matthew T. Ashland permitted ALTLinux to include
the codec and its SDK into ALTLinux distributions. Text of
the permission can be found in %permission_file or
at %permission_url

This package contains static libraries from
Monkey's Audio Codec SDK

%endif

%prep
%setup
install -p -m644 %SOURCE1 .
mv src/License.htm .

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall

%files
%doc License.htm NEWS README TODO AUTHORS ChangeLog MAC-ALTLinux-permission.html
%doc src/Credits.txt src/Readme.htm src/History.txt
%_bindir/mac

%files -n libmac
%doc License.htm MAC-ALTLinux-permission.html
%_libdir/libmac.so.*

%files -n libmac-devel
%doc License.htm MAC-ALTLinux-permission.html
%_libdir/libmac.so
%_includedir/*

%if_enabled static
%files -n libmac-devel-static
%doc License.htm MAC-ALTLinux-permission.html
%_libdir/libmac.a
%endif

%changelog
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
