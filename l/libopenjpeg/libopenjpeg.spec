Name: libopenjpeg
Version: 1.3
Release: alt1.1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: JPEG 2000 codec library
License: BSD
Group: System/Libraries

URL: http://www.openjpeg.org/
%define fversion %(echo %{version} | sed -e 's/\\./_/g')
Source: http://www.openjpeg.org/openjpeg_v%{fversion}.tar.gz

Patch1: openjpeg-1.3-libtiff.patch
Patch2: openjpeg-1.3-cmake.patch
Patch3: openjpeg-1.3-shlibname.patch

# Automatically added by buildreq on Mon Feb 22 2010
BuildRequires: libstdc++-devel libtiff-devel

### Be aware of https://bugzilla.redhat.com/show_bug.cgi?id=504663
### But with current gcc4.4 in our repo bug is not reprodused

%description
OpenJPEG is an open-source JPEG 2000 codec written in C. This package contains
runtime libraries for applications that use OpenJPEG.

%package devel
Summary: Development tools for programs which will use the %name library
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package includes the header files necessary for developing
programs which will use the %name library.

%package -n openjpeg-tools
Summary: JPEG 2000 command line tools
Group: Graphics

%description -n openjpeg-tools
OpenJPEG is an open-source JPEG 2000 codec written in C.

%prep
%setup -n OpenJPEG_v%{fversion}
%patch1 -p1
#%patch2 -p1
%patch3 -p1

# Delete Windows stuff
rm -rf jp3d
# Make sure we use system libraries
rm -rf libs
find . -type f -print0 | xargs -0 chmod a-x


%build
# We build from packaged makefiles not touching cmake machinery

subst 's/-lstdc++/-lm/' Makefile
%make_build
%make_build -C codec

%install
# To allow non-root packaging
subst 's/-o root -g root//' Makefile

%make_install install DESTDIR=%buildroot INSTALL_LIBDIR=%_libdir

ln -sf libopenjpeg.so.2 %buildroot%_libdir/libopenjpeg.so

install -d %buildroot%_bindir
install -pm755 codec/{image_to_j2k,j2k_to_image} %buildroot%_bindir/

%files
%_libdir/lib*.so.2*
%exclude %_libdir/*.a

%files devel
%_includedir/*
%_libdir/lib*.so

%files -n openjpeg-tools
%_bindir/*

%changelog
* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.1
- Rebuilt for soname set-versions

* Mon Feb 22 2010 Victor Forsiuk <force@altlinux.org> 1.3-alt1
- Initial build.
