# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

Name: cronbuild-sh-functions-moodle
Version: 0.0.3
Release: %branch_release alt1

Summary: Common shell functions for moodle cronbuild scripts
License: %gpl2plus
Group: Development/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: cronbuild-sh-functions

Requires: %_bindir/cronbuild-sh-functions

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses

%description
%summary

%install
install -D -m 644 %SOURCE0 %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Fri Jan 20 2012 Aleksey Avdeev <solo@altlinux.ru> 0.0.3-alt1
- Update functions:
  + get_modoole_app_release()
  + get_modoole_app_releasebuild()
  + get_modoole_app_releasenum()

* Thu Jan 19 2012 Aleksey Avdeev <solo@altlinux.ru> 0.0.2-alt1
- Update functions:
  + get_modoole_app_version()
  + get_modoole_app_requires()
  + get_modoole_app_release()
  + get_modoole_app_releasebuild()
  + get_modoole_app_releasenum()

* Sat Jan 14 2012 Aleksey Avdeev <solo@altlinux.ru> 0.0.1-alt1
- Initial build for ALT Linux Sisyphus
