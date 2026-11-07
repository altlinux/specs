%define _unpackaged_files_terminate_build 1
%define sover 0.3

Name: wuffs
Version: 0.3.6
Release: alt1

Summary: Safe language and codecs for untrusted file formats
License: Apache-2.0
Group: Development/Other
URL: https://github.com/google/wuffs
VCS: https://github.com/google/wuffs.git

Source: %name-%version.tar
Source1: wuffs.pc.in
Source2: regenerate-release.py
Patch: go127-zlib-example.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: gcc
BuildRequires: pkg-config
BuildRequires: python3-base
BuildRequires: liblz4-devel
BuildRequires: libzstd-devel
BuildRequires: zlib-devel
BuildRequires: gcc-c++
BuildRequires: bzlib-devel
BuildRequires: libdeflate-devel
BuildRequires: libgif-devel
BuildRequires: libpng-devel

%description
Wuffs is a memory-safe language and standard library for parsing untrusted
file formats. Its compiler produces portable C codecs and proves bounds
and arithmetic checks before code is generated.

%package -n libwuffs%sover
Summary: Wuffs shared codec library
Group: System/Libraries

%description -n libwuffs%sover
The shared C implementation of the Wuffs standard library.

%package -n lib%name-devel
Summary: Wuffs C API development files
Group: Development/C

%description -n lib%name-devel
The C edition of the Wuffs standard library, shared library linker name
and pkg-config metadata for native consumers.

%prep
%setup
%patch -p1
# These dependencies are used only by upstream build-tag-ignored scripts.
go mod edit \
    -droprequire=github.com/russross/blackfriday/v2 \
    -droprequire=golang.org/x/image

%build
export GOPROXY=off
export GOSUMDB=off
export GOTOOLCHAIN=local
mkdir -p gen/bin gen/lib
%gobuild -trimpath -o gen/bin/ ./cmd/...
# The upstream frontend invokes its newly built wuffs-c helper by name.
export PATH="$PWD/gen/bin:$PATH"
cp release/c/wuffs-v0.3.c upstream-wuffs-v0.3.c
wuffs gen -version=%version
python3 %SOURCE2 upstream-wuffs-v0.3.c %version
%__cc %optflags -std=c99 -fPIC -DWUFFS_IMPLEMENTATION \
    -shared -Wl,-soname,libwuffs.so.%sover -Wl,--no-undefined \
    %{?__global_ldflags} release/c/wuffs-v0.3.c \
    -o gen/lib/libwuffs.so.%version

%install
install -d %buildroot%_bindir %buildroot%_libdir/pkgconfig \
    %buildroot%_includedir/wuffs %buildroot%_datadir/wuffs
BUILDDIR="$PWD/gen" IGNORE_SOURCES=1 %golang_install
install -pm755 gen/lib/libwuffs.so.%version %buildroot%_libdir/
ln -s libwuffs.so.%version %buildroot%_libdir/libwuffs.so.%sover
ln -s libwuffs.so.%sover %buildroot%_libdir/libwuffs.so
install -pm644 release/c/wuffs-v0.3.c %buildroot%_includedir/wuffs/
cp -a std %buildroot%_datadir/wuffs/
find %buildroot%_datadir/wuffs -name README.md -delete
install -pm644 wuffs-root-directory.txt %buildroot%_datadir/wuffs/
sed -e 's|@prefix@|%_prefix|g' \
    -e 's|@libdir@|%_libdir|g' \
    -e 's|@includedir@|%_includedir|g' \
    -e 's|@version@|%version|g' %SOURCE1 \
    > %buildroot%_libdir/pkgconfig/wuffs.pc

%check
export GOPROXY=off
export GOSUMDB=off
export GOTOOLCHAIN=local
export PATH="$PWD/gen/bin:$PATH"
%gotest -json ./... > go-test.jsonl
wuffs test -skipgen -mimic -ccompilers=gcc
%__cxx %optflags -std=c++11 -x c++ -c release/c/wuffs-v0.3.c \
    -o gen/lib/header-cxx.o

%files
%_bindir/wuffs
%_bindir/wuffs-c
%_bindir/wuffsfmt
%_bindir/dumbindent
%_bindir/ractool
%_datadir/wuffs
%doc LICENSE

%files -n libwuffs%sover
%_libdir/libwuffs.so.%version
%_libdir/libwuffs.so.%sover

%files -n lib%name-devel
%_includedir/wuffs
%_libdir/libwuffs.so
%_libdir/pkgconfig/wuffs.pc

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 0.3.6-alt1
- Initial build for ALT.
