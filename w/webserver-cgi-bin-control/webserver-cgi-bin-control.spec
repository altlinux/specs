# hey Emacs, its -*- rpm-spec -*-

%define rpm_masrosdir %_sysconfdir/rpm/macros.d

# for distr selected
%def_without M40
%def_without M41

# for set release
%define release_pre alt
%define release_base_num 1
%define release_base_num2 %nil
%define release_suff %nil

# for set distr
%define release_distr_num 1

# set distr
%define distr_switch %nil
%if_with M40
%define distr_switch M40
%endif
%if_with M41
%define distr_switch M41
%endif

%if "%distr_switch" == ""
%if "%release_base_num2" == ""
%define release_num %release_base_num
%else
%define release_num %release_base_num.%release_base_num2
%endif
%define release_distr %nil
%else
%if "%release_base_num2" == ""
%define release_num %(expr %release_base_num - 1)
%else
%define release_num %release_base_num.%(expr %release_base_num2 - 1)
%endif
%define release_distr .%distr_switch.%release_distr_num
%endif

# release_base set
%define release_base %release_pre%release_num%release_distr

# set package_release
%define package_release %release_base%release_suff

Name: webserver-cgi-bin-control
Version: 0.4
Release: %package_release

Summary: The base cgi-bin control facility
Summary(ru_RU.KOI8-R): Основа control для cgi-bin
License: %gpl2plus
Group: System/Servers

Packager: Aleksey Avdeev <solo@altlinux.ru>

Source0: webserver-cgi-bin-functions
Source10: webserver-cgi-bin-control.rpm-macros

BuildArch: noarch

BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-macros-webserver-common
BuildPreReq: %_datadir/rpm-build-rpm-eval/rpm-eval.sh

Provides: %_sysconfdir/control.d/webserver-cgi-bin-functions

%description
This package contains webserver-cgi-bin-functions for cgi-bin control facility.

%description -l ru_RU.KOI8-R
Этот пакет содержит webserver-cgi-bin-functions для правил управления
cgi-bin скриптами.
   

%package -n rpm-macros-%name
Summary: RPM macros to rebuild Web servers and apps packages
Summary(ru_RU.KOI8-R): RPM макросы для сборки пакетов веб-серверов и приложений
Group: Development/Other

%description -n rpm-macros-%name
The package provide a set of macros for packaging Web applications
according to the ALT Linux Web Packaging Policy.

%description -n rpm-macros-%name -l ru_RU.KOI8-R
Макросы для обеспечения сборки пакетов веб серверов и приложений
в соответствии с ALT Linux Web Packaging Policy.

%install
install -D -m644 %SOURCE0 %buildroot%_sysconfdir/control.d/webserver-cgi-bin-functions

# Substitute the real paths in files
find %buildroot%_sysconfdir -type f -print0 \
	| xargs -r0i %_datadir/rpm-build-rpm-eval/rpm-eval.sh "{}"

install -pD -m644 %SOURCE10 \
	%buildroot%rpm_masrosdir/%name

%files
%_sysconfdir/control.d/webserver-cgi-bin-functions

%files -n rpm-macros-%name
%rpm_masrosdir/%name

%changelog
* Tue Oct 14 2008 Aleksey Avdeev <solo@altlinux.ru> 0.4-alt1
- Fix symlink_* status and sets
- Add build rpm-macros-%%name subpackage for ALT Linux RPM Packaging Policy

* Sat Sep 27 2008 Aleksey Avdeev <solo@altlinux.ru> 0.3-alt1
- Fix const use

* Mon Sep 22 2008 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt1
- Add none status

* Wed Aug 27 2008 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Initial build
