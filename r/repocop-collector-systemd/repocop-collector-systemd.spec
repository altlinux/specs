%define collectorname systemd

Name: repocop-collector-%collectorname
Version: 0.02
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %collectorname collector for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org
Requires: repocop >= 0.40 
#BuildRequires: perl-devel

Source0: %name-%version.tar

%description
%summary

%prep
%setup

%build

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/
%__install -m 755 %collectorname.test $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/test
%__install -m 755 %collectorname.purge $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/purge
%__install -m 644 %collectorname.filepattern $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/%collectorname/filepattern


%files
#doc README ChangeLog
%_datadir/repocop/pkgcollectors/%collectorname

%changelog
* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- bugfix release

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
