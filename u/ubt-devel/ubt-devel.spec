
Name: ubt-devel
Version: 0.1
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
Requires: rpm-macros-ubt
%description -n rpm-build-ubt
Set of RPM macroses and utilities for building one tag for all binary package branches.

%prep
%setup -cT

%install
install -D -m 0644 %SOURCE1 %buildroot/%_rpmmacrosdir/ubt-build
mkdir -p %buildroot/%_bindir/
install -m 0755 %SOURCE2 %buildroot/%_bindir/
install -m 0755 %SOURCE3 %buildroot/%_bindir/

%files -n rpm-build-ubt
%_rpmmacrosdir/ubt-build
%_bindir/ubt-*

%changelog
* Thu Dec 01 2016 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
