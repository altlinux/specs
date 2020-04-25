Name: rpmidentity
Version: 0.1
Release: alt1

Summary: calculate rpm package identity

License: GPL-3.0-or-later
Group: Development/Other
Url: git://git.altlinux.org/gears/r/rpmidenity.git

VCS: git://git.altlinux.org/gears/r/rpmidenity.git
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
* Sat Apr 25 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.1-alt1
- Initial build for ALT Sisyphus.

