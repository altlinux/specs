#BuildRequires: 
Name: autorepo-altnode-repocop
Version: 0.03
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop scripts for an automated packaging node
Group: Development/Other
License: GPL2+
#Url: 
Source: %name-%version.tar

Requires: repocop > 0.57

%description
%summary

%prep
%setup

%build

%install

mkdir -p $RPM_BUILD_ROOT%_bindir
cp repocop-* $RPM_BUILD_ROOT%_bindir

%files
%doc daily.conf.*
%doc crontab
%_bindir/*

%changelog
* Sun Jul 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- repocop 0.58 support

* Fri Jul 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- support for repocop-report-prometeus2-sqlite

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
