%define abiversion 2
%def_with check

Name:    munge
Version: 0.5.17
Release: alt1

Summary: MUNGE authentication service
License: GPL-3.0+ and LGPLv3+
Group:   System/Servers
Url:     https://github.com/dun/munge

Source0: %name-%version.tar
Source1: %name.sysusers

BuildRequires(pre): rpm-macros-generic-compat rpm-macros-systemd
BuildRequires: libssl-devel
BuildRequires: bzlib-devel zlib-devel
BuildRequires: pkg-config
Requires: lib%name%abiversion = %EVR
Conflicts: python3(munge)

%description
MUNGE (MUNGE Uid 'N' Gid Emporium) is an authentication service for creating
and validating user credentials.  It is designed to be highly scalable for
use in an HPC cluster environment.  It provides a portable API for encoding
the user's identity into a tamper-proof credential that can be obtained by an
untrusted client and forwarded by untrusted intermediaries within a security
realm.  Clients within this realm can create and validate credentials without
the use of root privileges, reserved ports, or platform-specific methods.

%package -n lib%name-devel
Summary: MUNGE authentication service development files
Group:   Development/C
License: LGPLv3+
Requires: lib%name%abiversion = %EVR
Provides: %name-devel = %EVR
Obsoletes: %name-devel < %EVR

%description -n lib%name-devel
Development files for building applications that use libmunge.

%package -n lib%name%abiversion
Summary: MUNGE authentication service shared library
Group:   System/Libraries
License: LGPLv3+
Provides:  %name-libs = %EVR
Obsoletes: %name-libs < %EVR

%description -n lib%name%abiversion
The shared library (libmunge) for running applications that use MUNGE.

%prep
%setup
%autoreconf

%build
%configure \
    --disable-static \
    --with-crypto-lib=openssl \
    --with-logrotateddir=%_sysconfdir/logrotate.d \
    --with-systemdunitdir=%_unitdir \
    --localstatedir=%_var \
    --with-runstatedir=%_rundir \
    --with-pkgconfigdir=%_libdir/pkgconfig \
    --with-logrotateddir="%_logrotatedir"

# Get rid of some rpaths for /usr/sbin (copied from authors spec template)
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%makeinstall_std
touch %buildroot%_localstatedir/%name/munged.seed
mkdir -p %buildroot%_runtimedir/%name
touch %buildroot%_runtimedir/%name/munged.pid
touch %buildroot%_logdir/%name/munged.log
install -Dp %SOURCE1 %buildroot%_sysusersdir/%name.conf

%check
# Run tests inside similarly-named directory requires a regular OS with network
# internals, full permissions control, sysuser account and for some cases
# root privileges.
# Upstream expects to run it on developers localhost directly.
# A couple of directories contains some functional tests to run in our isolated
# build environment.
for tdir in src/{common,munged}; do
    pushd $tdir
        LD_LIBRARY_PATH=%buildroot%_libdir \
        %make_build check root=/tmp/munge-test-$$ verbose=t
    popd
done

%pre
%sysusers_create_package %name %SOURCE1

%post
if test ! -f %_sysconfdir/%name/%name.key; then
    echo "Run %_sbindir/mungekey as the munge user to create a key."
    echo "For example: \"sudo -u munge %_sbindir/mungekey -v\"."
    echo "Refer to the mungekey(8) manpage for more information."
fi
%systemd_post munge.service

%preun
%systemd_preun munge.service

%postun
%systemd_postun_with_restart munge.service

%files
%doc AUTHORS COPYING* DISCLAIMER* HISTORY JARGON KEYS NEWS PLATFORMS
%doc QUICKSTART README* THANKS doc/credential_v3_format.txt
%_sbindir/munged
%_sbindir/mungekey
%_bindir/%name
%_bindir/re%name
%_bindir/un%name
%_unitdir/%name.service
%dir %attr(0700,%name,%name) %_sysconfdir/%name
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %attr(0700,%name,%name) %_localstatedir/%name
%attr(0600,%name,%name) %_localstatedir/%name/munged.seed
%dir %attr(0700,%name,%name) %_logdir/%name
%attr(0640,%name,%name) %_logdir/%name/munged.log
%dir %attr(0755,%name,%name) %_runtimedir/%name
%attr(0644,%name,%name) %_runtimedir/%name/munged.pid
%_sysusersdir/%name.conf
%_man1dir/*
%_man7dir/*
%_man8dir/*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc
%_man3dir/*

%files -n lib%name%abiversion
%_libdir/lib%name.so.%abiversion
%_libdir/lib%name.so.%abiversion.*

%changelog
* Thu Nov 13 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.5.17-alt1
- New version.
- Spec improvements:
  + Applied ALT Shared Libs Policy.
  + Resolved file conflict reported by repocop.
  + Included functional tests running in an isolated environment.
  + System user addition is performed using the "systemd-sysusers(8)" command
    instead of script insertion in the spec.

* Tue Jul 23 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.5.16-alt1
- new version 0.5.16

* Tue Mar 26 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.5.15-alt1
- Initial build for Sisyphus (Closes: #37332)
