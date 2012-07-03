# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define macrosname branch

# script name for %%branch_release use
%define script_name branch_release

Name: rpm-macros-%macrosname
Version: 0.2
Release: %branch_release alt2

Summary: RPM macros for support branches
Summary(ru_RU.UTF-8): RPM макросы поддержки бранчей
License: %gpl2plus
Group: Development/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source1: %name.spec.inc
Source2: %script_name.sh

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses

%description
Macros for the assembly of packages for different branches.

%description -l ru_RU.UTF-8
Макросы для обеспечения сборки пакетов под разные бранчи.

%build
sed -e 's/^%%define[[:space:]]\+/%%/
s/%%SOURCE2/%script_name/g
/^[[:space:]]*#/s/%%%%/%%/g' %SOURCE1 > %name.rpm-macros

%install
install -pD -m644 %name.rpm-macros %buildroot%_rpmmacrosdir/%macrosname
install -pD -m755 %SOURCE2 %buildroot%_bindir/%script_name

%files
%_rpmmacrosdir/%macrosname
%_bindir/%script_name

%changelog
* Sun Aug 15 2010 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt2
- Relocated macro files to %%_rpmmacrosdir/

* Sat Aug 08 2009 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt1
- Add %%_bindir/branch_release script
- Fix for use buildreq (for %%branch_switch undefine only)

* Wed Aug 05 2009 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Initial build
