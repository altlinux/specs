%define _libexecdir %_prefix/libexec

%define _name stappler
%define libname lib%_name
%define dist_name %libname-root
%define ver_major 0.3
%define beta .beta0

Name: %_name
Version: %ver_major
Release: alt0.5%beta

Summary: Stappler SDK
License: MIT
Group: System/Libraries
Url: https://stappler.dev

Vcs: https://github.com/libstappler/libstappler-root.git

Source: %dist_name-%version%beta.tar
# fixed examples/commandline/Makefile
Patch: stappler-0.3.beta0-alt-genpasswd.patch

# [ppc64le] core/crypto/SPCrypto-openssl.cc:44:10: fatal error: gost-engine.h ...
ExcludeArch: %ix86 ppc64le

BuildRequires: gcc-c++ xxd
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libzip)
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libidn2)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(libbrotlidec)
BuildRequires: libgif-devel
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(vulkan)
BuildRequires: glslang-devel
BuildRequires: spirv-tools
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: apache2-devel

%description
Stappler SDK - a set of tools for developing modern cross-platform
applications:
* high-performance graphics and calculating on vulkan
* access to databases on the client and server
* application and web server for it in the divided components
* Script machine for Webasembly (and any language compiled compiled in it)
* Only the necessary minimum dependencies

%package -n %_name-modules
Summary: Stappler modules
Group: System/Libraries

%description -n %_name-modules
Stappler SDK - a set of tools for developing modern cross-platform
applications.

This package provides Stappler shared modules/libraries.

%package -n %_name-devel
Summary: Stappler SDK
Group: System/Libraries
Requires: %_name-modules = %EVR

%description -n %_name-devel
Stappler SDK - a set of tools for developing modern cross-platform
applications.

This package provides files required to develop and build Stappler
applications.

%package -n %_name-examples
Summary: Stappler demo programms
Group: System/Libraries
Requires: %_name-modules = %EVR

%description -n %_name-examples
Stappler SDK - a set of tools for developing modern cross-platform
applications.

This package provides demo applications from Stappler package.

%prep
%setup -n %dist_name-%version%beta
%patch

%build
# TODO for i586
%ifarch %ix86
%add_optflags -msse2 -mfpmath=sse %(getconf LFS_CFLAGS)
%endif

#SHARED_PREFIX=%_prefix \

%make_build \
LOCAL_BUILD_STATIC=0 \
SHARED_LIBDIR=%_libdir \
SHARED_INCLUDEDIR=%_includedir \
SHARED_SHAREDIR=%_datadir
%nil
# examples
pushd examples/commandline
%make_build
popd
# TODO other examples

%install
export INSTALL_PREFIX=%buildroot%_prefix \
INSTALL_LIBDIR=%buildroot%_libdir
%makeinstall_std

# examples
mkdir -p %buildroot%_libexecdir/%_name
install -pD -m755 examples/commandline/stappler-build/*/*/*/genpasswd \
    %buildroot%_libexecdir/%_name/genpasswd

%files -n %_name-modules
%_libdir/*.so
%doc README*

%files -n %_name-devel
%_includedir/%libname/
%_datadir/%libname/
%doc doc/html/

%files -n %_name-examples
%dir %_libexecdir/%_name
%_libexecdir/%_name/genpasswd


%changelog
* Sun Feb 09 2025 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt0.5.beta0
- first build for Sisyphus (v0.3-beta0)

