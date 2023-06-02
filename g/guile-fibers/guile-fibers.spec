%define _unpackaged_files_terminate_build 1

%define guile_sitedir %(guile-config info sitedir)

Name: guile-fibers
Version: 1.3.1
Release: alt1

Summary: Concurrent ML-like concurrency for Guile
License: LGPL-3.0+
Group: System/Libraries
Url: https://github.com/wingo/fibers
Vcs: https://github.com/wingo/fibers

Source0: %name-%version.tar

BuildRequires(pre): /proc
BuildRequires: guile-devel
BuildRequires: texinfo

%description
Fibers is a facility that provides Go-like concurrency for
Guile Scheme, in the tradition of Concurrent ML.

%prep
%setup

%build
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
* Fri Jun 02 2023 Anton Zhukharev <ancieg@altlinux.org> 1.3.1-alt1
- New version.

* Fri May 26 2023 Anton Zhukharev <ancieg@altlinux.org> 1.2.0-alt1
- Initial build for ALT Sisyphus.

