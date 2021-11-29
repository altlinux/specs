%define repo tdlib

Name: freetdi-tdlib
Version: 0.5.0
Release: alt1
License: GPL-2.0+
Summary: Algorithms for computing tree decompositions of graphs
Group: Engineering
Url: https://github.com/freetdi/tdlib

Source: https://sources.archlinux.org/other/community/%repo/%repo-%version.tar.gz

BuildRequires: gcc-c++ boost-devel-headers

%description
Algorithms for computing tree decompositions of graphs.

%package devel
Summary: %summary
Group: Development/C++
BuildArch: noarch

%description devel
Algorithms for computing tree decompositions of graphs.

%prep
%setup -n %repo-%version

%build
%configure
%make_build

%install
%makeinstall_std

%files devel
%doc AUTHORS ChangeLog COPYING README
%dir %_includedir/tdlib/
%_includedir/tdlib/*.hpp

%changelog
* Mon Nov 29 2021 Leontiy Volodin <lvol@altlinux.org> 0.5.0-alt1
- Initial build for ALT Sisyphus (ported from archlinux).
- Built as require for sagemath.
