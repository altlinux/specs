%define _unpackaged_files_terminate_build 1
%define soversion 3
%define optflags_lto %nil

Name: prrte
Version: 3.0.8
Release: alt1
Summary: PMIx Reference RunTime Environment (PRRTE)

License: BSD
Group: Development/Tools

Url: https://pmix.org
Vcs: https://github.com/openpmix/prrte

Source0: %name-%version.tar
Source1: %name-%version-oac.tar

# Unsupported architecture by UCX
ExcludeArch: i586

BuildRequires: libhwloc-devel openpmix-devel flex chrpath zlib-devel
# HWLOC Support configure requirementes below
BuildRequires: libxml2-devel liblzma-devel

%description
PMIx is an application programming interface standard that provides libraries
and programming models with portable and well-defined access to commonly needed
services in distributed and parallel computing systems. A typical example of
such a service is the portable and scalable exchange of network addresses to
establish communication channels between the processes of a parallel
application or service. As such, PMIx gives distributed system software
providers a better understanding of how programming models and libraries can
interface with and use system-level services.

%package -n %name-devel
Summary: Development files of PMIx Reference RunTime Environment (PRRTE)
Group: System/Libraries

%description -n %name-devel
Development files of PMIx Reference RunTime Environment (PRRTE).

%package -n libprrte%soversion
Summary: PMIx Reference Library (OpenPMIx)
Group: System/Libraries

%description -n libprrte%soversion
PMIx Reference RunTime Environment (PRRTE).

%prep
%setup -a1

%build
# Autogen check submodules by condition "if file exist".
rm -f .gitmodules
./autogen.pl
%configure \
    --disable-static \
    --disable-option-checking \
    --enable-prte-ft \
    --disable-devel-check \
    --enable-prte-prefix-by-default

%make_build

%install
%makeinstall_std

rm %buildroot%_libdir/*.la

fix_rpath() {
    # Cut /usr/lib64 from rpath
    fixed_path=$(chrpath -l ${1?} | cut -d'=' -f2 | sed 's;\(^/usr/lib64$\|:/usr/lib64$\|^/usr/lib64:\);;g')
    if [ -n "$fixed_path" ]; then
      chrpath -r $fixed_path $1
    else
      chrpath -d $1
    fi
}

for f in $(ls %buildroot%_libdir/libprrte.so.%soversion.*); do
fix_rpath $f
done

for f in prte prted prte_info prun pterm; do
fix_rpath %buildroot%_bindir/$f
done

%files
%doc LICENSE README.md VERSION
%_bindir/prte
%_bindir/prted
%_bindir/prte_info
%_bindir/prterun
%_bindir/prun
%_bindir/pterm
%config(noreplace) %_sysconfdir/prte.conf
%config(noreplace) %_sysconfdir/prte-default-hostfile
%config(noreplace) %_sysconfdir/prte-mca-params.conf
%_datadir/prte/

%files -n %name-devel
%_includedir/*
%_libdir/lib*.so

%files -n libprrte%soversion
%_libdir/libprrte.so.%soversion
%_libdir/libprrte.so.%soversion.*

%changelog
* Wed Sep 17 2025 Alexey Romanyuta <r9odt@altlinux.org> 3.0.8-alt1
- Initial build 3.0.8.
