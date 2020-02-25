%define oldname CharLS
Name:           libCharLS1
Version:        1.0
Release:        alt4
Summary:        JPEG-LS compliant compressor/decompressor codec
Group:          System/Legacy libraries
License:        BSD
URL:            http://charls.codeplex.com
Source:         %name-%version.tar
Patch1:		charls_add_cmake_install_target.patch
Patch2:		charls_add_sharedlib_soname.patch
Patch3:		charls_fix_tests.patch

BuildRequires: cmake gcc-c++ dos2unix

%description
CharLS is a JPEG-LS compliant compressor/decompressor codec. 
In the program you are writing you can call the CharLS codec and 
pass it bitmaps (sometimes called raster images), to have them 
encoded to JPEG-LS, or JPEG-LS streams, which CharLS will decode to bitmaps. 

%package -n	lib%oldname
Summary:        JPEG-LS compliant compressor/decompressor codec
Group:          System/Libraries
Provides:	libcharls = %version-%release

%description -n lib%oldname
CharLS is a JPEG-LS compliant compressor/decompressor codec. 
In the program you are writing you can call the CharLS codec and 
pass it bitmaps (sometimes called raster images), to have them 
encoded to JPEG-LS, or JPEG-LS streams, which CharLS will decode to bitmaps. 

%package -n	%name-devel
Summary:        Development files for %name
Group:          System/Libraries
Requires:       lib%oldname = %version-%release
Conflicts:	lib%oldname-devel < %EVR

%description -n %name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
find . -type f -name '*.txt' -o -name '*.h' -o -name '*.cpp' | xargs dos2unix

%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%cmake -Dcharls_BUILD_SHARED_LIBS:BOOL=ON
%cmake_build

%install
%cmakeinstall_std

%files -n lib%oldname
%doc License.txt
%_libdir/lib%oldname.so.*

%if 1
%files -n %name-devel
%_libdir/*.so
%_includedir/%oldname
%endif

%changelog
* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4
- added compat devel for compat gdcm for python 38 rebuild

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3
- compat build

* Sun Jan 12 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt2
- fix build

* Wed Nov 09 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1
- first build for ALT Linux
