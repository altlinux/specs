Name: lua-arepo-transaction
Version: 0
Release: alt1
Summary: temporary package until arepo packages will be rebuilt
License: LGPLv2+
Group: Development/Other
BuildArch: noarch
Provides: i586-liblua5-devel
#Requires: i586-liblua5.3-devel

%description
%summary

%prep

%build

%install
mkdir -p %buildroot/%_altdir

%files

%changelog
* Wed Feb 08 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1
- temporary package until arepo packages will be rebuilt
