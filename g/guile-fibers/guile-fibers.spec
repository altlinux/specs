%define _unpackaged_files_terminate_build 1

# Tests fails on i586 (do not waste time on that coprolith).
%ifarch %ix86
%def_without check
%else
%def_with check
%endif

%define guile guile30
%define guile_sitedir %(%guile-config info sitedir)
%define guile_extensiondir %(%guile-config info extensiondir)
%define guile_ccachedir %(%guile-config info siteccachedir)

Name: guile-fibers
Version: 1.4.3
Release: alt1

Summary: Concurrent ML-like concurrency for Guile
License: LGPL-3.0+
Group: System/Libraries
Url: https://codeberg.org/guile/fibers
Vcs: https://codeberg.org/guile/fibers

Source0: %name-%version.tar

BuildRequires(pre): /proc
BuildRequires: %guile-devel
BuildRequires: texinfo

%description
Fibers is a facility that provides Go-like concurrency for
Guile Scheme, in the tradition of Concurrent ML.

%prep
%setup

%build
export ac_cv_path_GUILE=%_bindir/%guile
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%doc COPYING* AUTHORS HACKING README.md
%_infodir/fibers.info*
%guile_extensiondir/fibers-epoll.so*
%guile_ccachedir/fibers*
%guile_sitedir/fibers*
%guile_ccachedir/web
%guile_sitedir/web
%exclude %guile_extensiondir/fibers-epoll.la

%changelog
* Wed Jul 01 2026 Anton Zhukharev <ancieg@altlinux.org> 1.4.3-alt1
- Updated to 1.4.3.

* Mon Sep 01 2025 Anton Zhukharev <ancieg@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.
- Started using guile30.

* Fri Jun 02 2023 Anton Zhukharev <ancieg@altlinux.org> 1.3.1-alt1
- New version.

* Fri May 26 2023 Anton Zhukharev <ancieg@altlinux.org> 1.2.0-alt1
- Initial build for ALT Sisyphus.

