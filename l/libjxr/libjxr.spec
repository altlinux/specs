%define _name jxrlib

Name: libjxr
Version: 1.1
Release: alt1

Summary: Open source implementation of jpegxr
Group: System/Libraries
# See JPEGXR_DPK_Spec_1.0.doc. Upstream request for plain text license file at
# https://jxrlib.codeplex.com/workitem/13
License: BSD
Url: https://%_name.codeplex.com/

#Source: http://jxrlib.codeplex.com/downloads/get/685249#/jxrlib_%(echo %version | tr . _).tar.gz
Source: %name-%version.tar
# Use CMake to build to facilitate creation of shared libraries
# See https://jxrlib.codeplex.com/workitem/13
Source1: CMakeLists.txt
# Converted from shipped doc/JPEGXR_DPK_Spec_1.doc
# libreoffice --headless --convert-to pdf doc/JPEGXR_DPK_Spec_1.0.doc
Source2: JPEGXR_DPK_Spec_1.0.pdf

# Fix various warnings, upstreamable
# See https://jxrlib.codeplex.com/workitem/13
Patch: jxrlib_warnings.patch

BuildRequires: cmake

%description
This is an open source implementation of the jpegxr image format standard.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
# Sanitize charset and line endings
for file in `find . -type f -name '*.c' -or -name '*.h' -or -name '*.txt'`; do
  iconv --from=ISO-8859-15 --to=UTF-8 $file > $file.new && \
  sed -i 's|\r||g' $file.new && \
  touch -r $file $file.new && mv $file.new $file
done

%patch -p1 -b .warnings

# Remove shipped binaries
rm -rf bin

cp -a %SOURCE1 .
cp -a %SOURCE2 doc

%build
%cmake_insource -DBUILD_SHARED_LIBS:BOOL=ON
%make_build

%install
%makeinstall_std

%files
%doc doc/readme.txt doc/JPEGXR_DPK_Spec_1.0.pdf
%_bindir/JxrEncApp
%_bindir/JxrDecApp
%_libdir/libjpegxr.so.*
%_libdir/libjxrglue.so.*

%files devel
%_includedir/jxrlib/
%_libdir/libjpegxr.so
%_libdir/libjxrglue.so

%changelog
* Mon Feb 08 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- initial release based on fc package

