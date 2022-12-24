# BEGIN SourceDeps(oneline):
BuildRequires: perl(RPM/Header.pm) perl(Source/Repository/Mass/ALTLinuxBackport.pm) perl-devel perl-ALTLinux-ACL perl(ALTLinux/RepoList.pm)
# END SourceDeps(oneline)
Name: autorepo-scripts
Version: 0.630
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: common scripts for an automated packaging node
Group: Development/Other
License: GPLv2+
Url: https://www.altlinux.org/Autorepo
Source: %name-%version.tar

Requires: /usr/bin/relative /usr/bin/parentlock /usr/bin/parallel
# for mail
%filter_from_requires /^mutt/d
Requires: perl(Date/Format.pm) qa-robot /usr/bin/mutt
Requires: %name-common = %EVR
Requires: autorepo-builder = %EVR

%description
%summary

%package common
Summary: autorepo scripts common files
Group: Development/Other

%description common
%summary


%package -n autorepo-builder
Summary: autorepo builder scripts
Group: Development/Other
Requires: autorepo-scripts-common = %EVR
Requires: hsh-clone-workdir > 0.001
Conflicts: autorepo-scripts < 0.622

%description -n autorepo-builder
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

mkdir -p %buildroot%_datadir/%name/templates/
install -m 755 *.template %buildroot%_datadir/%name/templates/

%files
%doc configs
%doc DEPLOY.txt
%doc rsync-local
%_bindir/autorepo*
%perl_vendor_privlib/Autorepo*
%_datadir/%name/templates
# altnode
%exclude %_bindir/autorepo-altnode-*
# common
%exclude %_bindir/autorepo-lock-sh-functions
# builder
%exclude %_bindir/autorepo-build-config
%exclude %_bindir/autorepo-buildhelper-*
%exclude %_bindir/autorepo-build-sh-functions
%exclude %_bindir/autorepo-ls
%exclude %_bindir/autorepo-ls-bad-ugly
%exclude %_bindir/autorepo-parallel-build
%exclude %_bindir/autorepo-sequential-build

#files autoports
%_bindir/autoports*

%files -n autorepo-builder
%_bindir/autorepo-build-config
%_bindir/autorepo-buildhelper-*
%_bindir/autorepo-build-sh-functions
%_bindir/autorepo-ls
%_bindir/autorepo-ls-bad-ugly
%_bindir/autorepo-parallel-build
%_bindir/autorepo-sequential-build

%files common
%_bindir/autorepo-lock-sh-functions

%files -n autorepo-altnode-builder
%_bindir/autorepo-altnode-builder-statistics

%files -n autorepo-altnode-misc
%_bindir/autorepo-altnode-misc-statistics-wrapper

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.630-alt1
- new version

* Tue Dec 20 2022 Igor Vlasenko <viy@altlinux.org> 0.629-alt1
- new version

* Fri Jul 08 2022 Igor Vlasenko <viy@altlinux.org> 0.628-alt1
- new version

* Fri Jul 08 2022 Igor Vlasenko <viy@altlinux.org> 0.627-alt1
- new version

* Sun Dec 05 2021 Igor Vlasenko <viy@altlinux.org> 0.626-alt1
- new version

* Mon Mar 01 2021 Igor Vlasenko <viy@altlinux.org> 0.625-alt1
- better autoports p9

* Sun Nov 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.624-alt1
- new version

* Wed Oct 14 2020 Igor Vlasenko <viy@altlinux.ru> 0.623-alt1
- new version

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.622-alt1
- added autorepo-builder subpackage

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.621-alt1
- new version

* Wed Sep 30 2020 Igor Vlasenko <viy@altlinux.ru> 0.620-alt1
- new version

* Sun Sep 13 2020 Igor Vlasenko <viy@altlinux.ru> 0.619-alt1
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.618-alt1
- new version

* Wed Mar 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.617-alt1
- new version

* Sat Mar 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.616-alt1
- new version

* Sat Mar 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.615-alt1
- new version

* Fri Mar 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.614-alt1
- new version

* Thu Mar 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.613-alt1
- added helpers

* Thu Mar 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.612-alt1
- new version

* Fri Feb 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.611-alt1
- new version

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 0.610-alt1
- new version

* Tue Jan 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.609-alt1
- new version

* Fri Jan 18 2019 Igor Vlasenko <viy@altlinux.ru> 0.608-alt1
- new version

* Sat Dec 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.607-alt1
- new version

* Sun Jun 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.606-alt1
- new version

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.605-alt1
- new version

* Mon Apr 09 2018 Igor Vlasenko <viy@altlinux.ru> 0.604-alt1
- added autorepo-health-find-intersections

* Fri Apr 06 2018 Igor Vlasenko <viy@altlinux.ru> 0.603-alt1
- new version

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.602-alt1
- better GB_ARCH support

* Wed Mar 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.601-alt1
- better purge for py3copycat

* Tue Mar 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.600-alt1
- new version
