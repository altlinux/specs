# vim: set ft=spec: -*- rpm-spec -*-
# hey Emacs, its -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define macrosname apache2

%define repocop_testdatadir %_datadir/repocop/testdata.d
%define rpm_masrosdir %_sysconfdir/rpm/macros.d

# do we need to co-exist with apache-ru ?
%def_enable apache_ru_compat

Name: rpm-macros-%macrosname
Version: 3.7
Release: %branch_release alt1

Summary: RPM macros to Apache2 Web server
Summary(ru_RU.KOI8-R): RPM макросы для веб-сервера Apache2
License: %asl
Group: Development/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

# rpm macro definitions
Source1: apache2.rpm-macros
Source2: apache2-compat.rpm-macros

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-macros-webserver-common >= 1.3

Conflicts: rpm-macros-webserver-common < 1.4
Conflicts: apache2-devel <= 2.2.16-alt1
Requires: rpm-macros-webserver-common >= 1.4

%description
The package provide a set of macros for packaging Web applications
according to the ALT Linux Web Packaging Policy.

%description -l ru_RU.KOI8-R
Макросы для обеспечения сборки пакетов веб серверов и приложений
в соответствии с ALT Linux Web Packaging Policy.


%package compat
Summary: RPM macros to Apache2 Web server
Summary(ru_RU.KOI8-R): RPM макросы для веб-сервера Apache2
Group: Development/Other

Conflicts: apache-devel <= 1.3.41rusPL30.23-alt4.2
Conflicts: apache2-devel <= 2.2.9-alt2
Conflicts: rpm-macros-apache
Requires: %name >= %version

%description compat
The package provide a set of macros for packaging Web applications
according to the ALT Linux Web Packaging Policy.

%description compat -l ru_RU.KOI8-R
Макросы для обеспечения сборки пакетов веб серверов и приложений
в соответствии с ALT Linux Web Packaging Policy.


%package -n repocop-unittest-data-%name
Summary: Data file for repocop test platform
Summary(ru_RU.KOI8-R): Данные для тестов repocop
Group: Development/Other

Provides: %repocop_testdatadir/%name
Provides: %repocop_testdatadir/%name-compat

%description -n repocop-unittest-data-%name
The package provide data file for repocop test platform.

%description -n repocop-unittest-data-%name -l ru_RU.KOI8-R
Пакет предоставляет данные для тестов repocop.


%install
install -pD -m644 %SOURCE1 %buildroot%rpm_masrosdir/%name
install -pD -m644 %SOURCE2 %buildroot%rpm_masrosdir/%name-compat

%if_disabled apache_ru_compat
find %buildroot%rpm_masrosdir/ -type f -print0 \
	| xargs -r0 sed -ri "
/^[[:space:]]*%%apache2_branch[[:space:]]/s/^([[:space:]]*%%apache2_branch[[:space:]]+)[^[:space:]].*$/\1%%nil/
"
%endif

mkdir -p %buildroot%repocop_testdatadir/
egrep '^[[:space:]]*%%[^%%[:space:]]+[[:space:]]' \
		%buildroot%rpm_masrosdir/%name \
	| sort -r > %buildroot%repocop_testdatadir/%name
egrep '^[[:space:]]*%%[^%%[:space:]]+[[:space:]]' \
		%buildroot%rpm_masrosdir/%name-compat \
	| sort -r > %buildroot%repocop_testdatadir/%name-compat

%files
%rpm_masrosdir/%name

%files compat
%rpm_masrosdir/%name-compat

%files -n repocop-unittest-data-%name
%repocop_testdatadir/%name
%repocop_testdatadir/%name-compat

%changelog
* Fri Jul 15 2011 Aleksey Avdeev <solo@altlinux.ru> 3.7-alt1
- Add new macros %%apache2_rpmhtcachecleanrestartfile

* Wed Jul 06 2011 Aleksey Avdeev <solo@altlinux.ru> 3.6-alt1
- Add new macros:
  + %%apache2_htcacheclean_dname
  + %%apache2_htcacheclean_cachepath
  + %%apache2_htcacheclean_lockdir
  + %%apache2_htcacheclean_piddir

* Sun Jun 05 2011 Aleksey Avdeev <solo@altlinux.ru> 3.5-alt1
- Add new macros %%triggerun_apache2_rpmhttpdstartfile

* Fri Jun 03 2011 Aleksey Avdeev <solo@altlinux.ru> 3.4-alt1
- Add new macros %%apache2_httpdlockfile

* Fri Jun 03 2011 Aleksey Avdeev <solo@altlinux.ru> 3.3-alt1
- Add new macros %%apache2_rpmhttpdstartfile

* Fri May 27 2011 Aleksey Avdeev <solo@altlinux.ru> 3.2-alt1
- Add new macros:
  + %%apache2_rpmfiletriggerdir
  + %%apache2_rpmhttpdrestartfile
  + %%apache2_rpma2chkconfigfile

* Wed Oct 20 2010 Aleksey Avdeev <solo@altlinux.ru> 3.1-alt1
- Add new macros %%apache2_confdir_inc

* Wed Oct 20 2010 Aleksey Avdeev <solo@altlinux.ru> 3.0-alt1
- Remove %%apache2_distr_switch macros
- Set Conflicts: apache2-devel <= 2.2.16-alt1
- Add new macros:
  + %%apache2_uploadsdir
  + %%apache2_uploadslink
  + %%apache2_lockdir
  + %%apache2_locklink

* Wed Dec 10 2008 Aleksey Avdeev <solo@altlinux.ru> 2.1-alt1
- Fix %%apache2_apr_buildreq sets (Closes: #18167)

* Wed Nov 12 2008 Aleksey Avdeev <solo@altlinux.ru> 2.0-alt1
- Remove %%name-%%apache2_libdb_name provides and %%apache2_libdb* macros
- Add Conflicts: apache2-devel < 2.2.9-alt12.1

* Fri Aug 15 2008 Aleksey Avdeev <solo@altlinux.ru> 1.1-alt2
- Use libdb4.4-devel by default

* Thu Aug 14 2008 Aleksey Avdeev <solo@altlinux.ru> 1.1-alt1
- Fix %%apache2_libssl* macros sets

* Thu Aug 14 2008 Aleksey Avdeev <solo@altlinux.ru> 1-alt1
- Add libdb and distr switchers (%%nil by default)
- Add new macros:
  + %%apache2_libdb*
  + %%apache2_distr_switch
  + %%apache2_libdb_soname
- Add new provides: %%name-%%apache2_libdb_name = %%apache2_libdb_soname
- Turn back conditional libdb4-devel default, libdb4.4-devel (for M40 and M41),
  libdb4.3-devel (for M30) or libdb4.2-devel (for M24) build

* Tue Aug 05 2008 Aleksey Avdeev <solo@altlinux.ru> 0.3-alt2
- Fix Requires/Conflicts

* Tue Aug 05 2008 Aleksey Avdeev <solo@altlinux.ru> 0.3-alt1
- Create repocop-unittest-data-%%name subpacage for repocop tests
- Add new macros:
  + %%apache2_manualaddonsdir
  + %%apache2_compat_manualaddonsdir
- Remove %%apache2_compat_htdocsaddondir macros (move to %%name-compat
  subpackage)

* Sat Aug 02 2008 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt2
- Add conflict with the package rpm-macros-apache

* Sat Aug 02 2008 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt1
- Add macros for pid file

* Fri Aug 01 2008 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Add apache_ru_compat switcher (enabled by default)

* Tue Jul 15 2008 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt0.1
- First build for ALT Linux
