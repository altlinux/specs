%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define brand JBoss
%define pub_name Publican
%define RHEL6 %(test %{?dist} == .el6 && echo 1 || echo 0)

Name:		publican-jboss
Summary:	Common documentation files for %{brand}
Version:	2.6
Release:	alt2_8jpp8
License:	CC-BY-SA
Group:		Text tools
# Limited to these arches on RHEL 6 due to PDF + Java limitations
%if %{RHEL6}
ExclusiveArch:   i686 x86_64
%else
BuildArch:   noarch
%endif
Source:		https://fedorahosted.org/releases/p/u/publican/%{name}-%{version}.tgz
Requires:	publican >= 2.5
BuildRequires:	publican >= 2.5
URL:		https://fedorahosted.org/publican/
Provides:	documentation-devel-%{brand} = %{version}-%{release}
Obsoletes:	documentation-devel-%{brand} < %{version}-%{release}
Source44: import.info

%description
This package provides common files and templates needed to build documentation
for %{brand} with publican.

%prep
%setup -q 

%build
publican build --formats=xml --langs=all --publish

%install
mkdir -p -m755 $RPM_BUILD_ROOT%{_datadir}/publican/Common_Content
publican install_brand --path=$RPM_BUILD_ROOT%{_datadir}/publican/Common_Content

%files
%doc README
%doc COPYING
%{_datadir}/publican/Common_Content/%{brand}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.6-alt2_8jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.6-alt2_6jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.6-alt2_5jpp7
- new release

* Tue Nov 05 2013 Igor Vlasenko <viy@altlinux.ru> 2.6-alt2_3jpp7
- NMU: added missing Pod dependencies

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_3jpp7
- initial build

