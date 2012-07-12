Name: maintenance-utils
Version: 1.5
Release: alt1

Summary: Utilities for package maintenance
License: GPL
Group: Development/Other
Packager: Paul Wolneykien <manowar@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: girar-utils help2man

%description
This package contains utilities for package maintenance for Sisyphus
and git.alt build server.

%prep
%setup

%build
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%_bindir/*
%_mandir/man?/*
%_mandir/ru/man?/*

%changelog
* Thu Jul 12 2012 Paul Wolneykien <manowar@altlinux.ru> 1.5-alt1
- Take the committer name from the git config by default.
- Implement the --closes option for autoclose of bugs.

* Thu Dec 08 2011 Paul Wolneykien <manowar@altlinux.ru> 1.4-alt1
- Update the Russian manual page.
- Use `gear --describe' as a better way to obtain version/release.
- Fix/improve the branch suffix handling.

* Fri Oct 21 2011 Paul Wolneykien <manowar@altlinux.ru> 1.3-alt1
- Do not remove an existing task on fail.
- Add option to merge branches.

* Wed Apr 06 2011 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt1
- Do not add branch suffix for all sisyphus* repos.
- Handle multi-number release numbers properly.
- Handle epoch numbers properly.
- Fix package version extraction in the Makefile.

* Fri Sep 24 2010 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt1
- Add support for test only builds.
- Fix empty annotations in Sisyphus release tags.

* Wed Dec 30 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt4
- Fix changelog extract.

* Thu Dec 17 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt3
- Fix missing branch switch in dry-run mode.

* Mon Dec 14 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt2
- Do not print commit message if the files are untouched.

* Sat Dec 13 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial version of the make-release utility.
