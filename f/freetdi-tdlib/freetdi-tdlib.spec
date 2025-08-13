%define repo tdlib

Name: freetdi-tdlib
Version: 0.9.3
Release: alt1
License: GPL-2.0-or-later and GPL-3.0-or-later
Summary: Algorithms for computing tree decompositions of graphs
Group: Engineering
Url: https://github.com/freetdi/tdlib
VCS: https://github.com/freetdi/tdlib.git

Source: https://sources.archlinux.org/other/community/%repo/%repo-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ boost-devel-headers

%description
Algorithms for computing tree decompositions of graphs.

%package -n libtreedec-devel
Summary: %summary
Group: Development/C++
BuildArch: noarch
Provides: %name-devel
Obsoletes: %name-devel

%description -n libtreedec-devel
Algorithms for computing tree decompositions of graphs.

%prep
%setup -n %repo-%version
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files -n libtreedec-devel
%doc AUTHORS ChangeLog COPYING README
%_includedir/treedec/

%changelog
* Wed Aug 13 2025 Leontiy Volodin <lvol@altlinux.org> 0.9.3-alt1
- New version 0.9.3.
- Added VCS tag.
- Renamed: freetdi-tdlib-devel -> libtreedec-devel.
- Updated license tag.

* Mon Nov 29 2021 Leontiy Volodin <lvol@altlinux.org> 0.5.0-alt1
- Initial build for ALT Sisyphus (ported from archlinux).
- Built as require for sagemath.
