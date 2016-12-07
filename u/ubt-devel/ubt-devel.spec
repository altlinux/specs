
Name: ubt-devel
Version: 0.3
Release: alt1

Group: Development/Other
Summary: Universal Branch Tag packaging
Url: http://www.altlinux.org
License: GPL

BuildArch: noarch

Source1: macros
Source2: ubt-stampspec
Source3: ubt-addchangelog

BuildRequires: rpm-utils libshell gear

%description
Set of RPM macroses and utilities for building one tag for all binary package branches.

%package -n rpm-build-ubt
Summary: Universal Branch Tag macros and utils
Group: Development/Other
Requires: rpm-macros-ubt >= 0.2
Requires: /usr/bin/add_changelog
%description -n rpm-build-ubt
Set of RPM macroses and utilities for building one tag for all binary package branches.

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
%_bindir/ubt-*

%changelog
* Wed Dec 07 2016 Sergey V Turchin <zerg@altlinux.org> 0.3-alt1
- fix to current packager in changelog entry

* Fri Dec 02 2016 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- extend macros

* Thu Dec 01 2016 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
