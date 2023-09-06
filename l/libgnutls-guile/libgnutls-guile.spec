Name: libgnutls-guile
Version: 4.0.0
Release: alt1

Summary: Guile bindings for the GnuTLS library
License: LGPLv2.1+ and GPLv3+
Group: System/Libraries
Url: https://gitlab.com/gnutls/guile
Vcs: https://gitlab.com/gnutls/guile.git
Source: guile-gnutls-%version.tar

BuildRequires: libgnutls-devel >= 3.8.0
BuildRequires: makeinfo
# Unfortunately we have different version
# on e2k and don't have guile-devel.
# See https://bugzilla.altlinux.org/34496
%ifarch %e2k
BuildRequires: guile20-devel
BuildRequires: libguile20-devel
%else
BuildRequires: guile22-devel
%endif
Obsoletes: libgnutls-new-guile < %version

%description
Guile-GnuTLS provides Guile bindings for the GnuTLS library.

%prep
%setup -n guile-gnutls-%version

%build
%autoreconf
%configure \
	--disable-rpath \
	--disable-static
%make_build

%install
%makeinstall_std

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%files
%doc AUTHORS NEWS README.md
%_libdir/guile/*/extensions/guile*.so*
%_libdir/guile/*/site-ccache/*
%_datadir/guile/site/*/*
%doc %_infodir/*
%exclude %_libdir/guile/*/extensions/*.la

%changelog
* Wed Sep 06 2023 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt1
- Updated to 4.0.0.

* Tue Aug 08 2023 Mikhail Efremov <sem@altlinux.org> 3.7.14-alt1
- Extracted from libgnutls to a separate package.

