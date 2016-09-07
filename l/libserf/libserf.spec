Name:           libserf
Version:        1.3.9
Release:        alt1

Summary:        High-Performance Asynchronous HTTP Client Library
License:        ASL 2.0
URL:            http://serf.apache.org/
Group:		System/Libraries

Source0:        https://archive.apache.org/dist/serf/serf-%{version}.tar.bz2
Patch1:         libserf-norpath.patch

BuildRequires:  libapr1-devel
BuildRequires:  libaprutil1-devel
BuildRequires:  libkrb5-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  scons
BuildRequires:  pkgconfig

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
%patch1 -p1

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

find %buildroot%_libdir -name '*.a' -or -name '*.la' -delete -print

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
* Wed Sep 07 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.9-alt1
- New version
- Change homepage URL

* Fri Aug 21 2015 Andrey Cherepanov <cas@altlinux.org> 1.3.8-alt1
- Inital build in Sisyphus (thanks Fedora)

