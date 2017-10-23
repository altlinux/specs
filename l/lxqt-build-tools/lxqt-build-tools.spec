Name: lxqt-build-tools
Version: 0.4.0
Release: alt2

Summary: Various packaging tools and scripts for LXQt applications
License: BSD 3-clause
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: qt5-base-devel qt5-tools-devel glib2-devel

BuildArch: noarch

%description
%summary
that used to lurk in liblxqt or got spread over other subprojects.

%prep
%setup
%ifarch e2k
# lcc has -fwhole, to be tested though
sed -i '/-flto/d' cmake/modules/LXQtCompilerSettings.cmake
%endif

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%doc BSD-3-Clause
%_datadir/cmake/%name

%changelog
* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.4.0-alt2
- fix BR:
- E2K: avoid lcc-unsupported options

* Tue Sep 26 2017 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- 0.4.0

* Sat Jan 14 2017 Michael Shigorin <mike@altlinux.org> 0.3.2-alt1
- 0.3.2

* Mon Jan 09 2017 Michael Shigorin <mike@altlinux.org> 0.3.1-alt1
- initial release (based on fedora package)

