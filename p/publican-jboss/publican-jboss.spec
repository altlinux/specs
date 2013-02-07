BuildRequires: /proc
BuildRequires: jpackage-compat
%define brand JBoss
%define pub_name Publican
%define RHEL6 %(test %{?dist} == .el6 && echo 1 || echo 0)

Name:		publican-jboss
Summary:	Common documentation files for %{brand}
Version:	2.6
Release:	alt1_3jpp7
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
for %%{brand} with publican.

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
* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_3jpp7
- initial build

