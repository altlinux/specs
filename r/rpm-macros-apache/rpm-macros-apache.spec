# vim: set ft=spec: -*- rpm-spec -*-
# hey Emacs, its -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define macrosname apache

Name: rpm-macros-%macrosname
Version: 0.2
Release: %branch_release alt5

Summary: RPM macros to Apache Web server
Summary(ru_RU.UTF-8): RPM макросы для веб-сервера Apache
License: %asl
Group: Development/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>

# rpm macro definitions
Source1: %macrosname.rpm-macros

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-macros-webserver-common >= 1.1

Conflicts: rpm-macros-webserver-common < 1.1
Conflicts: apache-devel <= 1.3.41rusPL30.23-alt4.2
Conflicts: apache2-devel <= 2.2.9-alt2
Requires: rpm-macros-webserver-common >= 1.1

BuildArch: noarch

%description
The package provide a set of macros for packaging Web applications
according to the ALT Linux Web Packaging Policy.

%description -l ru_RU.UTF-8
Макросы для обеспечения сборки пакетов веб серверов и приложений
в соответствии с ALT Linux Web Packaging Policy.


%install

install -pD -m644 %SOURCE1 %buildroot%_rpmmacrosdir/%name

%files
%_rpmmacrosdir/%name

%changelog
* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 0.2-alt5
- NMU: use %%_rpmmacrosdir instead of /etc/rpm

* Wed Sep 30 2015 Michael Shigorin <mike@altlinux.org> 0.2-alt4
- Re-added %%apache_{root,home} macros as aliases
- Converted spec to UTF-8

* Tue Aug 14 2012 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt3
- Remove repocop-unittest-data-%%name subpacage (Closes: #26075)

* Mon Aug 04 2008 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt2
- Create repocop-unittest-data-%%name subpacage for repocop tests

* Mon Jul 14 2008 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt1
- Readd %%post/%%postun scripts and %%version/%%release macros

* Mon Jul 14 2008 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Fix Conflicts/Requires

* Sun Jul 13 2008 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt0.1
- First build for ALT Linux
