# BEGIN SourceDeps(oneline):
BuildRequires: perl(RPM/Header.pm) perl(Source/Repository/Mass/ALTLinuxBackport.pm) perl-devel perl-ALTLinux-ACL
# END SourceDeps(oneline)
Name: autorepo-scripts
Version: 0.18
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

mkdir -p %buildroot%_datadir/%name/templates/
install -m 755 *.template %buildroot%_datadir/%name/templates/

%files
%doc autorepo-config.*
%doc DEPLOY.txt
%_bindir/*
%perl_vendor_privlib/Autorepo*
%_datadir/%name/templates

%changelog
* Fri Dec 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- autorepo-mail-mainrepo-older

* Fri Dec 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- unmets autorebuild

* Thu Nov 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt4
- rm-out-dups hasher tars as well

* Wed Nov 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt3
- support for install environment apt.conf

* Wed Nov 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2
- developmant release

* Sat Oct 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- bugfix release

* Mon Oct 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- implemented install test

* Sat Oct 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- devel release

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- bugfix release

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
