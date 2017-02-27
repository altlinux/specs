
%define branch_prefix .
%define branch_id S1
%define branch_suffix %%nil

Name: ubt-common
Version: 0.2
Release: alt2

Group: Development/Other
Summary: Common Universal Branch Tag
Url: http://www.altlinux.org
License: GPL

BuildArch: noarch

Source1: macros

%description
Base set of RPM macroses for building one tag for all binary branches.

%package -n rpm-macros-ubt
Summary: Base set of RPM macros for packaging Universal Branch Tag
Group: Development/Other
%description -n rpm-macros-ubt
Base set of RPM macroses for building one tag for all binary branches.

%prep
%setup -cT

%install
install -D -m 0644 %SOURCE1 %buildroot/%_rpmmacrosdir/ubt
cat <<__EOF__ >%buildroot/%_rpmmacrosdir/ubt
%%__ubt_branch_prefix %branch_prefix
%%__ubt_branch_id %branch_id
%%__ubt_branch_suffix %branch_suffix
__EOF__

%files -n rpm-macros-ubt
%_rpmmacrosdir/ubt

%changelog
* Mon Feb 27 2017 Sergey V Turchin <zerg@altlinux.org> 0.2-alt2
- bump release

* Fri Dec 02 2016 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- extend internal macros

* Thu Dec 01 2016 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
