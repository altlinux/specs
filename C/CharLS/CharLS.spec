Name:           CharLS
Version:        1.0
Release:        alt1
Summary:        JPEG-LS compliant compressor/decompressor codec
Group:          System/Libraries
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

%package -n	lib%name
Summary:        JPEG-LS compliant compressor/decompressor codec
Group:          System/Libraries
Provides:	libcharls = %version-%release

%description -n lib%name
CharLS is a JPEG-LS compliant compressor/decompressor codec. 
In the program you are writing you can call the CharLS codec and 
pass it bitmaps (sometimes called raster images), to have them 
encoded to JPEG-LS, or JPEG-LS streams, which CharLS will decode to bitmaps. 

%package -n	lib%name-devel
Summary:        Development files for %name
Group:          System/Libraries
Requires:       lib%name = %version-%release

%description -n lib%name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
find . -type f -name '*.txt' -o -name '*.h' -o -name '*.cpp' | xargs dos2unix -U

%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%cmake -Dcharls_BUILD_SHARED_LIBS:BOOL=ON

%make_build -C BUILD

%install
%makeinstall_std -C BUILD

%files -n lib%name
%doc License.txt
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/%name

%changelog
* Wed Nov 09 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1
- first build for ALT Linux
