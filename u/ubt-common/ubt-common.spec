
%define branch_id S1

Name: ubt-common
Version: 0.1
Release: alt1

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
%%__ubt_branch_id %branch_id
__EOF__

%files -n rpm-macros-ubt
%_rpmmacrosdir/ubt

%changelog
* Thu Dec 01 2016 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
