# BEGIN SourceDeps(oneline):
BuildRequires: perl(RPM/Header.pm) perl(Source/Repository/Mass/ALTLinuxBackport.pm) perl-devel
# END SourceDeps(oneline)
Name: autorepo-scripts
Version: 0.12
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: common scripts for an automated packaging node
Group: Development/Other
License: GPL2+
#Url: 
Source: %name-%version.tar

Requires: /usr/bin/relative
# for mail 
Requires: perl(Date/Format.pm) qa-robot

%description
%summary

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

mkdir -p $RPM_BUILD_ROOT%_bindir
cp autorepo-* $RPM_BUILD_ROOT%_bindir
rm $RPM_BUILD_ROOT%_bindir/*.spec
rm $RPM_BUILD_ROOT%_bindir/autorepo-config.*

%files
%doc autorepo-config.*
%doc DEPLOY.txt
%_bindir/*
%perl_vendor_privlib/Autorepo*

%changelog
* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- debuginfo support, archive support

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- maintainance release

* Tue Jun 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- cybertalk support

* Tue Jun 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- continuous mass build mode

* Fri Jun 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- autorepo hasher options

* Fri Jun 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- AUTOREPO_HOME support

* Sat May 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- added Config.pm

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added proper autorepo-purge

* Sun May 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added separate apt config for unmets check

* Fri May 18 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- First build for Sisyphus.
