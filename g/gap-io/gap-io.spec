%define repo io

Name: gap-io
Version: 4.9.3
Release: alt1
Summary: GAP: Bindings for low level C library IO
License: GPL-3.0-or-later
Group: Sciences/Mathematics
Url: https://gap-packages.github.io/io/
VCS: https://github.com/gap-packages/io

# Source-url: https://github.com/gap-packages/%repo/archive/v%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Patch: %repo-%version-%release.patch

BuildPreReq: rpm-macros-gap
BuildRequires: gap-devel

# PackageInfo.g
Requires: gap >= 4.12

%description
The IO package provides bindings for GAP to the lower levels of
Input/Output functionality in the C library.

%prep
%setup -n io
%patch -p1

%build
export LDFLAGS+=' -lgap'
%autoreconf
%configure \
  --with-gaproot=%gapdir
%make_build

%install
%gappkg_simple_install
# cleanup packaged sources
cd %buildroot%gap_sitearch/%repo/
rm -Rf aclocal* autom4* cnf config* m4 gen src
find . -type f -name "*.la" -print -delete

%files -f %name.files
%gap_sitearch/%repo/

%changelog
* Thu Oct 02 2025 Leontiy Volodin <lvol@altlinux.org> 4.9.3-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
- Packaged for gap-4ti2Interface.
