%define _unpackaged_files_terminate_build 1
%define soversion 2
%define optflags_lto %nil

Name: openpmix
Version: 5.0.5
Release: alt1
Summary: PMIx Reference Library (OpenPMIx)

License: BSD
Group: Development/Tools

Url: https://openpmix.org
Vcs: https://github.com/openpmix/openpmix

Source0: %name-%version.tar
Source1: %name-%version-oac.tar

# Unsupported architecture by UCX
ExcludeArch: i586

BuildRequires: libhwloc-devel libevent-devel python3 flex zlib-devel
# HWLOC Support configure requirementes below
BuildRequires: libxml2-devel liblzma-devel

%description
PMIx Reference Library (OpenPMIx).

%package -n %name-devel
Summary: Development files of PMIx Reference Library (OpenPMIx)
Group: System/Libraries

%description -n %name-devel
Development files of PMIx Reference Library (OpenPMIx).

%package -n libpmix%soversion
Summary: PMIx Reference Library (OpenPMIx)
Group: System/Libraries

%description -n libpmix%soversion
PMIx Reference Library (OpenPMIx).

%prep
%setup -a1

%build
./autogen.pl
%configure \
    --disable-static \
    --with-sysroot=%prefix \
    --localstatedir=%_runtimedir \
    --disable-option-checking \
    --without-tests-examples \
    --enable-pmix-binaries \
    --disable-pmix-backward-compatibility \
    --disable-visibility \
    --disable-devel-check

%make_build

%install
%makeinstall_std

rm %buildroot%_libdir/*.la
rm %buildroot%_libdir/pmix/*.la

%files
%doc AUTHORS LICENSE README.md VERSION
%_bindir/palloc
%_bindir/pattrs
%_bindir/pctrl
%_bindir/pevent
%_bindir/plookup
%_bindir/pmixcc
%_bindir/pmix_info
%_bindir/pps
%_bindir/pquery
%config(noreplace) %_sysconfdir/pmix-mca-params.conf
%_datadir/pmix/

%files -n %name-devel
%_includedir/*
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc

%files -n libpmix%soversion
%dir %_libdir/pmix
%_libdir/pmix/pmix_mca_pcompress_zlib.so
%_libdir/libpmix.so.%soversion
%_libdir/libpmix.so.%soversion.*

%changelog
* Wed Sep 17 2025 Alexey Romanyuta <r9odt@altlinux.org> 5.0.5-alt1
- Initial build 5.0.5.
