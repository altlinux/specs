Name: rpmidentity
Version: 0.3
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

%build
make PREFIX=%_prefix

%install
make DESTDIR=%buildroot PREFIX=%_prefix install

%files
%_bindir/rpmidentity
%dir %_datadir/rpmidentity
%_datadir/rpmidentity/taglist

%changelog
* Sat Apr 10 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.3-alt1
- Updated to 0.3.
- Added support for calculation identities for multiple packages at once.
- Refactored code, fixed bugs.
- Spec: Fixed summary, url and vcs tags.

* Thu May 28 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.2-alt1
- Fixed to work with rpm 4.0.4.

* Sat Apr 25 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.1-alt1
- Initial build for ALT Sisyphus.

