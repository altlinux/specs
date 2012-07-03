# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define macrosname %name

Name: moodle-lang-cronbuild-common
Version: 0.0.1
Release: %branch_release alt1

Summary: Shell functions for moodle-lang cronbuild scripts
License: %gpl2plus
Group: Development/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: sh-functions

Requires: %_bindir/cronbuild-sh-functions

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses

%description
%summary

%package -n rpm-macros-%macrosname
Summary: Set of RPM macros for packaging moodle-lang-cronbuild-common-based applications
Group: Development/Other

%description -n rpm-macros-%macrosname
Set of RPM macros for packaging moodle-lang-cronbuild-common-based
applications for ALT Linux. Install this package if you want to create
RPM packages that use moodle-lang-cronbuild-common.

%define moodle_lang_cronbuildcommondir %_datadir/%name

%install
install -pD -m644 %SOURCE0 %buildroot%_bindir/%name-sh-functions
install -d %buildroot%moodle_lang_cronbuildcommondir

install -d %buildroot%_rpmmacrosdir
echo "%%moodle_lang_cronbuildcommondir	%moodle_lang_cronbuildcommondir" \
	> %buildroot%_rpmmacrosdir/%macrosname

%files
%_bindir/*
%dir %moodle_lang_cronbuildcommondir

%files -n rpm-macros-%macrosname
%_rpmmacrosdir/%macrosname

%changelog
* Fri Nov 11 2011 Aleksey Avdeev <solo@altlinux.ru> 0.0.1-alt1
- Initial build for ALT Linux Sisyphus
