Name: TheButterflyEffect
Version: 0.9.3.1
Epoch: 1
Release: alt1
License: GPL
Group: Games/Puzzles
Summary: Combine mechanical elements to achieve a simple goal in the most complex way
Source: v%version.tar.gz
Url: https://github.com/the-butterfly-effect

# Automatically added by buildreq on Mon Jan 23 2017
# optimized out: cmake-modules gcc-c++ libEGL-devel libGL-devel libqt5-core libqt5-gui libqt5-svg libqt5-widgets libqt5-xml libstdc++-devel python-base python-modules qt5-base-devel qt5-tools
BuildRequires: cmake qt5-svg-devel qt5-tools-devel

%description
A game that uses realistic physics simulations to combine lots of simple
mechanical elements to achieve a simple goal in the most complex way
possible.

%prep
%setup

%build
%cmake

%cmake_build

%install
%cmakeinstall_std

%files
%doc README*
%_gamesbindir/*
%_gamesdatadir/tbe
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*.png

%changelog
* Mon Jan 23 2017 Fr. Br. George <george@altlinux.ru> 1:0.9.3.1-alt1
- Upstream and versioning switched
- Autobuild version bump to 0.9.3.1

* Wed Jan 18 2017 Fr. Br. George <george@altlinux.ru> 8.2-alt2
- GCC6 fix

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 8.2-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Dec 06 2010 Fr. Br. George <george@altlinux.ru> 8.2-alt1
- Version up
- Milestone based versioning used

* Fri Jul 02 2010 Fr. Br. George <george@altlinux.ru> 0.0.3-alt1
- Initial build for ALT

