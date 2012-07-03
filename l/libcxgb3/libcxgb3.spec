%def_enable shared
%def_enable static

Name: libcxgb3
Version: 1.2.5
Release: alt1
Summary: Chelsio T3 RNIC Open Fabrics Userspace Library
Group: System/Libraries
License: %gpl2only, %bsdstyle
Url: http://www.openfabrics.org
Source: %name-%version.tar
Requires: libibverbs
Packager: Andriy Stepanov <stanv@altlinux.ru>


BuildRequires(pre): rpm-build-licenses
BuildRequires: libibverbs-devel

%description
%name provides a device-specific userspace driver for Chelsio RNICs
for use with the libibverbs library.

%if_enabled static
%package devel-static
Summary: Static %name driver
Group: Development/C
Requires: %name = %version-%release

%description devel-static
Static version of %name that may be linked directly to an
application, which may be useful for debugging.
%endif


%prep
%setup


%build
./autogen.sh
%configure %{subst_enable shared} %{subst_enable static}
%make_build
bzip2 -9fk ChangeLog


%install
%make_install DESTDIR=%buildroot install


%files
%doc AUTHORS COPYING ChangeLog.* README
%{?_enable_shared:%_libdir/*.so}
%config %_sysconfdir/libibverbs.d/cxgb3.driver


%if_enabled static
%files devel-static
%_libdir/libcxgb3*.a
%endif


%changelog
* Mon Aug 16 2010 Andriy Stepanov <stanv@altlinux.ru> 1.2.5-alt1
- New version

