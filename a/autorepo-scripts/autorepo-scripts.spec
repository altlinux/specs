# BEGIN SourceDeps(oneline):
BuildRequires: perl(RPM/Header.pm) perl(Source/Repository/Mass/ALTLinuxBackport.pm) perl-devel perl-ALTLinux-ACL
# END SourceDeps(oneline)
Name: autorepo-scripts
Version: 0.33
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: common scripts for an automated packaging node
Group: Development/Other
License: GPL2+
#Url: 
Source: %name-%version.tar

Requires: /usr/bin/relative /usr/bin/parentlock
# for mail 
Requires: perl(Date/Format.pm) qa-robot

%description
%summary

%package -n autorepo-altnode-misc
Summary: autorepo scripts for an axiliary node
Group: Development/Other

%description -n autorepo-altnode-misc
%summary

%package -n autorepo-altnode-builder
Summary: autorepo scripts for a builder node
Group: Development/Other
Requires: %name = %version-%release

%description -n autorepo-altnode-builder
%summary

%package autoports
Summary: autorepo scripts for an autoports node
Group: Development/Other

%description autoports
%summary

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

mkdir -p $RPM_BUILD_ROOT%_bindir
cp autoports-* autorepo-* $RPM_BUILD_ROOT%_bindir/
rm $RPM_BUILD_ROOT%_bindir/*.spec
rm $RPM_BUILD_ROOT%_bindir/autorepo-config.*

mkdir -p %buildroot%_datadir/%name/templates/
install -m 755 *.template %buildroot%_datadir/%name/templates/

%files
%doc autorepo-config.*
%doc DEPLOY.txt
%doc rsync-local
%_bindir/autorepo*
%perl_vendor_privlib/Autorepo*
%_datadir/%name/templates
%exclude %_bindir/autorepo-altnode-*

#files autoports
%_bindir/autoports*

%files -n autorepo-altnode-builder
%_bindir/autorepo-altnode-builder-statistics

%files -n autorepo-altnode-misc
%_bindir/autorepo-altnode-misc-statistics-wrapper

%changelog
* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- new version

* Sat Oct 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- autorepo-check-health

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- local build support 

* Sat Aug 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt3
- cpanbuilder support

* Mon Aug 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt2
- pld support

* Fri Aug 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- merge support

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- bugfixes

* Sun Aug 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- autopurge in managed mode

* Fri Jul 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- better autoports purge

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- generic daily script

* Thu Jul 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- autoports support
- auxiliary-node subpackage

* Wed Jul 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- support for auxiliary nodes

* Tue Jul 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- more altnode messages

* Mon Jul 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- support for altnode monitoring

* Sat May 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- developmant release

* Wed Jan 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- developmant release

* Tue Jan 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- developmant release

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
