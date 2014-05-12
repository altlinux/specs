Name:    alt-test
Version: 1.1.3
Release: alt1

Summary: Test environment based on Tapper
License: GPLv3+
Group:   System/Libraries
URL:     http://altlinux.org/alt-test

Packager: Andrey Cherepanov <cas@altlinux.org>

Requires: perl-Tapper-Cmd
Requires: perl-devel
Requires: libshell
Requires: cdrkit-utils
Requires: gawk

Source:  %name-%version.tar

BuildArch: noarch

%description
Test environment based on Tapper

%prep
%setup
subst 's/@version@/%version/' alt-test

%install
install -m 0755 -D %name %buildroot%_bindir/%name
install -m 0755 -D %name-functions %buildroot%_bindir/%name-functions
mkdir -p %buildroot%_libexecdir/%name
cp -av tests/* %buildroot%_libexecdir/%name/

%files
%_bindir/%{name}*
%_libexecdir/%name

%changelog
* Mon May 12 2014 Andrey Cherepanov <cas@altlinux.org> 1.1.3-alt1
- Fix environment variable name in program help

* Wed Apr 02 2014 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- Version check support for test_package
- Rename TESTED_PACKAGE_SOURCE environment variable to TEST_PACKAGE_SOURCE
- Add many tests for SPT

* Mon Nov 11 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt2
- Automatically use package version for alt-test script

* Fri Nov 08 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- Put in result successful tests too
- Put each test name in comment
- Add Qt4 driver for PostgreSQL and APC UPS monitoring daemon for spt test
- Add tests:
  + for desktop file localization (desktop-l10n)
  + for Mozilla extension versions (mozilla-extensions)
  + for unwaned echo in tests (tests-extra-log)

* Thu Oct 24 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Support -f option to show only failed tests
- Support $TESTED_PACKAGE_SOURCE for ISO image for existing package checks
- Fix missing package name for default explanation
- Add test:
  + spt

* Wed Oct 09 2013 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- Add tests:
  + process
  + system-statistic

* Tue Oct 08 2013 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Support full path to test file
- Add tests:
  + filesystems
  + text-editor
  + text-processing

* Thu Oct 03 2013 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
