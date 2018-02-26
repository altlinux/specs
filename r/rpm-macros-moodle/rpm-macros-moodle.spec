# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define macrosname moodle

Name: rpm-macros-%macrosname
Version: 2.4
Release: %branch_release alt1

Summary: RPM helper macros and dependency utils to build Mooodle packages
License: %gpl2plus
Group: Development/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source1: %macrosname.rpm-macros

Requires: rpm-macros-webserver-common >= 1.1
Conflicts: rpm-build-moodle < 2.0

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses

%description
These helper macros and dependency calculation utils facilitate creation of 
RPM packages containing Moodle bytecode archives etc.

%install
install -pD -m644 %SOURCE1 %buildroot%_rpmmacrosdir/%macrosname

%files
%_rpmmacrosdir/%macrosname

%changelog
* Fri Feb 17 2012 Aleksey Avdeev <solo@altlinux.ru> 2.4-alt1
- Update mascros
  + %%moodle_datadir
- Add new mascros:
  + %%moodle_domainsdir
  + %%moodle_defaultdatadirname
  + %%moodle_olddatadir2

* Fri Aug 26 2011 Aleksey Avdeev <solo@altlinux.ru> 2.3-alt1
- Add new masros:
  + %%moodle_questiondir
  + %%moodle_questionformatdir

* Thu Aug 04 2011 Aleksey Avdeev <solo@altlinux.ru> 2.2-alt1
- Add new masros %%moodle_admindir

* Thu Aug 04 2011 Aleksey Avdeev <solo@altlinux.ru> 2.1-alt1
- Set macros %%moodle_datadir to %%_localstatedir/%%moodle_name
- Add new masros:
  + %%moodle_olddatadir (contains an obsolete value of
    the macro %%moodle_datadir)
  + %%moodle_name
  + %%moodle_calendardir
  + %%moodle_coursedir
  + %%moodle_docdir
  + %%moodle_filesdir
  + %%moodle_logindir
  + %%moodle_pixdir
  + %%moodle_olddatadir

* Tue Aug 02 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0-alt1
- Rename package to rpm-macros-moodle
- Rename macros %%_moodle* to %%moodle_*

* Sat Jun 23 2007 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.0-alt1
- Initial release
