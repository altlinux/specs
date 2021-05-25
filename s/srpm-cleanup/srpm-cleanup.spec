%define _unpackaged_files_terminate_build 1

Name:     srpm-cleanup
Version:  0.1.1
Release:  alt3

Summary:  Remove unused source files from SRPM packages
License:  GPL-3.0-or-later
Group:    Development/Tools
Url:      http://git.altlinux.org/people/manowar/packages/srpm-cleanup.git

Packager: Paul Wolneykien <manowar@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch
BuildRequires: ronn perl(Pod/Usage.pm) pandoc >= 2

Requires: %name-parallel = %version-%release

%description
srpm-cleanup(1) removes unused source files from SRPM packages.
The list of unused files can be obtained with hsh-separate-sources(1).

This package should be installed on the main management host.


%package audit
Summary:  Default audit on/off scripts for %name
Group:    Development/Tools
License:  GPL-3.0-or-later

%description audit
Provides the default audit on/off scripts for %name.

This package should be installed on the hosts that build packages.


%package parallel
Summary:  "GNU" Parallel used in srpm-cleanup scripts
Group:    Development/Tools
License:  GPL-3.0-or-later

%description parallel
A "GNU" Parallel version with special patches used in srpm-cleanup
scripts.


%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/hsh-separate-sources
%_bindir/srpm-cleanup
%_datadir/%name/import-logs.pl
%_datadir/%name/main.mk
%_datadir/%name/exceptions.list
%_man1dir/hsh-separate-sources.1*
%_man1dir/srpm-cleanup.1*
%_man7dir/make-srpm-cleanup.7*
%_docdir/%name/*

%files audit
%_datadir/%name/audit_on
%_datadir/%name/audit_off

%files parallel
%_bindir/parallel_alt

%changelog
* Wed May 26 2021 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt3
- Package parallel_alt --- a special version of "GNU" Parallel used
  in srpm-cleanup scripts.

* Wed May 26 2021 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt2
- Added README in Russian (Quick start).

* Fri May 14 2021 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Initial version for Sisyphus.
