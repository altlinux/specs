
Name: ubt-devel
Version: 0.3.1
Release: alt2

Group: Development/Other
Summary: Universal Branch Tag packaging
Url: http://www.altlinux.org
License: GPL

Packager: Sergey V Turchin <zerg@altlinux.org>

BuildArch: noarch

Source1: macros
Source2: ubt-stampspec
Source3: ubt-addchangelog

BuildRequires: rpm-utils libshell /usr/bin/gear-sh-functions

%description
Set of RPM macros and utilities for building one tag for all binary package
branches.

%package -n rpm-build-ubt
Summary: Universal Branch Tag macros
Group: Development/Other
Requires: rpm-macros-ubt >= 0.2

%description -n rpm-build-ubt
Set of RPM macros and utilities for building one tag for all binary package
branches.

%package -n ubt-utils
Summary: Universal Branch Tag utils
Group: Development/Other
Requires: rpm-build-ubt = %EVR
Requires: /usr/bin/add_changelog
Requires: /usr/bin/gear-sh-functions

%description -n ubt-utils
Set of utilities for building one tag for all binary package branches.

%prep
%setup -cT

%install
install -D -m 0644 %SOURCE1 %buildroot/%_rpmmacrosdir/ubt-build
cat <<__EOF__ >%buildroot/%_rpmmacrosdir/ubt-build
%%ubt    %%{__ubt_branch_prefix}%%{__ubt_branch_id}%%{__ubt_branch_suffix}
%%ubt_id %%{__ubt_branch_id}
__EOF__
mkdir -p %buildroot/%_bindir/
install -m 0755 %SOURCE2 %buildroot/%_bindir/
install -m 0755 %SOURCE3 %buildroot/%_bindir/

%files -n rpm-build-ubt
%_rpmmacrosdir/ubt-build

%files -n ubt-utils
%_bindir/ubt-*

%changelog
* Tue Oct 31 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.1-alt2
- Move all utilities to new separate subpackage ubt-utils to avoid redundant
  dependencies.

* Wed Mar 29 2017 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- update requires

* Wed Dec 07 2016 Sergey V Turchin <zerg@altlinux.org> 0.3-alt1
- fix to current packager in changelog entry

* Fri Dec 02 2016 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- extend macros

* Thu Dec 01 2016 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
