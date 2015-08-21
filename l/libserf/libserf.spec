Name:           libserf
Version:        1.3.8
Release:        alt1

Summary:        High-Performance Asynchronous HTTP Client Library
License:        ASL 2.0
URL:            http://code.google.com/p/serf/
Group:		System/Libraries

Source0:        http://serf.googlecode.com/svn/src_releases/serf-%{version}.tar.bz2
BuildRequires:  libapr1-devel, libaprutil1-devel
BuildRequires:  libkrb5-devel, openssl-devel, zlib-devel
BuildRequires:  scons, pkgconfig
Patch1:         serf-1.3.8-testfix.patch
Patch2:         serf-1.3.8-norpath.patch

%description
The serf library is a C-based HTTP client library built upon the Apache
Portable Runtime (APR) library. It multiplexes connections, running the
read/write communication asynchronously. Memory copies and
transformations are kept to a minimum to provide high performance
operation.

%package        devel
Summary:        Development files for %name
Group:		Development/C
Requires:       %name = %version-%release
Requires:       libapr1-devel

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn serf-%version
%patch1 -p1 -b .testfix
%patch2 -p1 -b .norpath

# Shared library versioning support in scons is worse than awful...
# minimally, here fix the soname to match serf-1.2.x.  Minor version
# handling should be fixed too; really requires better upstream support:
# http://scons.tigris.org/issues/show_bug.cgi?id=2869
sed -i '/SHLIBVERSION/s/MAJOR/0/' SConstruct

%build
scons \
      CFLAGS="%{optflags}" \
      PREFIX=%_prefix \
      LIBDIR=%_libdir \
      GSSAPI=%_prefix \
      %{?_smp_mflags}

%install
scons install --install-sandbox=%{buildroot}

find %{buildroot} -name '*.*a' -delete -print

%check
# Use the libserf from $PWD
LD_LIBRARY_PATH=$PWD scons %{?_smp_mflags} check || true

%files
%doc LICENSE NOTICE
%_libdir/*.so.*

%files devel
%doc CHANGES README design-guide.txt
%_includedir/serf-1/
%_libdir/*.so
%_libdir/pkgconfig/serf*.pc

%changelog
* Fri Aug 21 2015 Andrey Cherepanov <cas@altlinux.org> 1.3.8-alt1
- Inital build in Sisyphus (thanks Fedora)

