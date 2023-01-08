%define _unpackaged_files_terminate_build 1

Name: rpm-macros-racket
Version: 1.0.1
Release: alt1

Summary: RPM macros for the Racket programming language
Group: Development/Other
License: GPL-3.0

Source0: racket.macros

BuildArch: noarch

%description
%summary.

%build
mkdir -p %buildroot%_rpmmacrosdir
install -p -m0644 %SOURCE0 %buildroot%_rpmmacrosdir/racket

%files
%_rpmmacrosdir/racket

%changelog
* Sun Oct 23 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.1-alt1
- update arches list
- add %%racket_sharedir macro
- remove %%racket_compiled macro

* Sun Oct 16 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus

