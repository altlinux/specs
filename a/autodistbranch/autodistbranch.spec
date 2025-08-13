%define _unpackaged_files_terminate_build 1
%def_without old_make_initrd

Name: autodistbranch
Version: 0.1.2
Release: alt1

Summary: Script to automatically update the priority branch
License: %gpl2plus
Group: System/Base
Packager: Paul Wolneykien <manowar@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildArch: noarch

%description
Contains the 'autodistbranch' script and an RPM macro file to
automatically make the %%_priority_distbranch equal to the name
of the latest distribution suite available among the APT sources.
Note, that the 'autodistbranch' script makes calculations using
/var/lib/apt/lists/*_release files.

%prep
%setup

%build
%make_build bindir=%_bindir sysconfdir=%_sysconfdir mandir=%_mandir

%install
%makeinstall_std bindir=%_bindir sysconfdir=%_sysconfdir mandir=%_mandir

%files
%doc README
%_bindir/*
%_sysconfdir/rpm/macros.d/90-%name
%_man1dir/*.1.*

%changelog
* Wed Aug 13 2025 Paul Wolneykien <manowar@altlinux.org> 0.1.2-alt1
- Fix: Filter out task repositories by default.
- Updated the manual page.

* Wed Aug 13 2025 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Compare releases by suit names using rpmvercmp.

* Mon May 05 2025 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial release.
