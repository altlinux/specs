# spec file for package trinity-filesystem (version R14)
#
# Copyright (c) 2014 Trinity Desktop Environment
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# TDE variables
Name: rpm-macros-trinity
Version: 14.0.3
Release: alt6
Summary: RPM helper macros to rebuild TDE packages
BuildArch: noarch
Provides: trinity-cmake-macros

Group: Other
Url: http://www.trinitydesktop.org/

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source1: rpm.macros.trinity.standalone

License: GPL-2.0+

%description
These helper macros provide possibility to rebuild
TDE packages by some Alt Linux Team Policy compatible way.

%prep
%build
%install
mkdir -p -- %buildroot/%_rpmmacrosdir

install -m 0644 %SOURCE1 %buildroot/%_rpmmacrosdir/trinity

%files
%_rpmmacrosdir/trinity

%changelog
* Mon Nov 07 2016 Hihin Ruslan <ruslandh@altlinux.ru> 14.0.3-alt6
- Correct macros

* Fri Nov 04 2016 Hihin Ruslan <ruslandh@altlinux.ru> 14.0.3-alt5
- development release

* Sun Oct 30 2016 Hihin Ruslan <ruslandh@altlinux.ru> 14.0.3-alt4
- Add macros %%simply_cmake

* Fri Oct 28 2016 Hihin Ruslan <ruslandh@altlinux.ru> 14.0.3-alt3
- Fix provides trinity-cmake-macros

* Thu Oct 27 2016 Hihin Ruslan <ruslandh@altlinux.ru> 14.0.3-alt2
- add provides trinity-cmake-macros

* Thu Oct 27 2016 Hihin Ruslan <ruslandh@altlinux.ru> 14.0.3-alt1
- initial build for ALT Linux Sisyphus
