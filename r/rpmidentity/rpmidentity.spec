Name: rpmidentity
Version: 0.9
Release: alt1

Summary: Calculate rpm package identity

License: GPL-3.0-or-later
Group: Development/Other
Url: http://git.altlinux.org/gears/%(echo %name |cut -b1)/%name.git

VCS: git://git.altlinux.org/gears/%(echo %name |cut -b1)/%name.git
Source: %name-%version-%release.tar

BuildArch: noarch

%description
This package contains utility that is used to calculate rpm package identity.

%prep
%setup -n %name-%version-%release

%install
install -pDm755 %name %buildroot%_bindir/%name

%files
%doc CHANGES
%_bindir/rpmidentity

%changelog
* Thu Jul 29 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9-alt1
- Updated to 0.9.
- Changed hashsum to BLAKE2.
- Added --filter-cmd argument.

* Thu Jul 15 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8-alt1
- Updated to 0.8.
- taglist: Added more tags to hash.

* Sun Jul 11 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt1
- Updated to 0.7.
- taglist: Added FILENAMES.
- Fixed behavior when incorrect cmdline args.

* Wed Jul 07 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.6-alt1
- Updated to 0.6.
- Excluded FILESIZES from taglist.

* Thu Jun 24 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.5-alt1
- Updated to 0.5.
- Refactored code.
- Fixed behavior.

* Sat Apr 10 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.4-alt1
- Fixed package arguments parsing.
- Fixed bug in the regexp that removes disttag from dependency versions.
- Refactored code.
- Packed CHANGES.

* Sat Apr 10 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.3-alt1
- Updated to 0.3.
- Added support for calculation identities for multiple packages at once.
- Refactored code, fixed bugs.
- Spec: Fixed summary, url and vcs tags.

* Thu May 28 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.2-alt1
- Fixed to work with rpm 4.0.4.

* Sat Apr 25 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.1-alt1
- Initial build for ALT Sisyphus.
