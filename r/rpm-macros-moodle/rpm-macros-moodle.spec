%define macrosname moodle

Name: rpm-macros-%macrosname
Version: 5.2
Release:alt1

Summary: RPM helper macros and dependency utils to build Mooodle packages
License: GPL-2.0+
Group: Development/Other

BuildArch: noarch

Source1: %macrosname.rpm-macros

Requires: rpm-macros-webserver-common >= 1.1
Conflicts: rpm-build-moodle < 2.0

%description
These helper macros and dependency calculation utils facilitate creation of RPM
packages containing Moodle bytecode archives etc.

%install
install -pD -m644 %SOURCE1 %buildroot%_rpmmacrosdir/%macrosname

%files
%_rpmmacrosdir/%macrosname

%changelog
* Sat Apr 25 2026 Andrey Cherepanov <cas@altlinux.org> 5.2-alt1
- Adapted macros to Moodle 5.2 (ALT #58352).

* Mon Oct 20 2025 Andrey Cherepanov <cas@altlinux.org> 5.1-alt1
- Adapted macros to Moodle 5.1.

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
