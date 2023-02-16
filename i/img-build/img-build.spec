Name: img-build
Version: 0.2.0
Release: alt1
License: GPL-2.0-or-later
Group: Development/Other
Summary: Scripts used to build images
BuildArch: noarch

Source: %name-%version.tar

%description
This package contains scripts that are used to build images.

%prep
%setup
sed 's/@PROG_VERSION@/%version/' -i img-build

%install
mkdir -p %buildroot%_bindir
cp img-build -t %buildroot%_bindir

%files
%_bindir/img-build

%changelog
* Thu Feb 16 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.0-alt1
- Added support for:
  + ExcludeArch and ExclusiveArch tags;
  + License tag;
  + --license mode to query License tag value.

* Tue Nov 22 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.0-alt1
- Initial build.
