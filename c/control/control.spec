Name: control
Version: 0.7.6
Release: alt2

Summary: A set of scripts to control installed system facilities
License: GPLv2+
Group: System/Base
BuildArch: noarch

Source: %name-%version.tar

# due to sed -i support
Requires: sed >= 1:4.1.1

%define _controldir %_sysconfdir/control.d/facilities

%description
The scripts included in this package provide a common interface to
control system facilities provided by a number of other packages.
This is intended for use primarily by packages which are providing
a facility that can potentially be dangerous to system security,
to let you enable, disable, or configure the facility independently
from package installation.

%prep
%setup

%build
sed -i s/@VERSION@/%version-%release/ control

%install
mkdir -p %buildroot{%_controldir,%_sbindir,%_man8dir,%_mandir/ru/man8,/var/run/control}
install -p -m755 control{,-dump,-restore} %buildroot%_sbindir/
install -p -m755 functions %buildroot%_sysconfdir/control.d/
install -p -m644 control{,-dump,-restore}.8 %buildroot%_man8dir/
install -p -m644 ru/control{,-dump,-restore}.8 %buildroot%_mandir/ru/man8/
install -pD -m644 control.macros %buildroot%_rpmmacrosdir/control

# Generate shell functions provides list.
(
	echo '# shell functions provides list'
	for f in %buildroot%_sysconfdir/control.d/*; do
		[ -f "$f" -a -x "$f" ] || continue
		sed -ne 's/^\([A-Za-z][A-Za-z_0-9]*[[:space:]]*\)()$/\1/pg' "$f"
	done |LC_COLLATE=C sort -u
) >%buildroot%_controldir/.provides.sh

%files
%_sbindir/control*
%_rpmmacrosdir/control
%config %_sysconfdir/control.d
%attr(0700,root,root) %ghost /var/run/control/
%_man8dir/*.8*
%_mandir/ru/man8/*.8*

%changelog
* Mon Nov 27 2017 Dmitry V. Levin <ldv@altlinux.org> 0.7.6-alt2
- Packaged translated manpages (from gremlin@; closes: #33920).

* Thu May 05 2011 Dmitry V. Levin <ldv@altlinux.org> 0.7.6-alt1
- control_subst: changed to use "sed -i --follow-symlinks"
  instead of plain "sed -i".
- /var/run/control/:
  + changed permissions from 0755 to 0700;
  + packaged as %%ghost;
  + control-dump: changed to create /var/run/control/ (closes: #25575).

* Mon Jun 28 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.5-alt1
- Added --help and --version options (closes: #16712).
- Optimized functions for speed (legion@).
- Changed code to use "sed -i" instead of "subst".
- Relocated control macro file from /etc/rpm/macros.d/ to
  /usr/lib/rpm/macros.d/

* Tue Sep 18 2007 Dmitry V. Levin <ldv@altlinux.org> 0.7.4-alt1
- functions/stat_file: Speed up.

* Sun Apr 22 2007 Dmitry V. Levin <ldv@altlinux.org> 0.7.3-alt1
- control: Changed facility names filter to allow dots in facility
  names and disallow rpmi and editor backup files (legion).

* Fri Apr 28 2006 Dmitry V. Levin <ldv@altlinux.org> 0.7.2-alt1
- functions/is_builtin_mode: handle "help *" and "summary".

* Thu Apr 27 2006 Dmitry V. Levin <ldv@altlinux.org> 0.7.1-alt1
- control: New builtin directive: summary.
- control.8: Document help and status directives.
- functions/{new_summary,control_summary}: New functions.
- functions/{control_fmode,control_subst}: Use control_summary.

* Fri May 27 2005 Dmitry V. Levin <ldv@altlinux.org> 0.7.0-alt1
- Optimized functions for speed.

* Thu Mar 31 2005 Dmitry V. Levin <ldv@altlinux.org> 0.6.2-alt1
- functions/new_subst:
  + extended to support several rules for each mode (legion).
- Do not add private functions to the .provides.sh file.

* Thu Nov 11 2004 Dmitry V. Levin <ldv@altlinux.org> 0.6.1.1-alt1
- functions/stat_file: fixed "find -maxdepth" warning.

* Sat Sep 25 2004 Dmitry V. Levin <ldv@altlinux.org> 0.6.1-alt1
- functions/{new_help,control_help}:
  new functions for help support.
- functions/control_list:
  new function for use by complex facilities.
- functions/control_fmode:
  don't change files when the new setting is the same.
- Packaged %_sysconfdir/control.d/.provides.sh file.

* Wed Oct 29 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6-alt2
- functions: use colon instead of dot as user/group name
  separator with invocations of chown(1).
- Added rpm macros file (#2972).

* Sat Apr 19 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6-alt1
- Synced with owl-control-0.6:
  * Fri Apr 18 2003 Solar Designer <solar@owl.openwall.com> 0.6-owl1
  - Avoid *roff commands within .SH NAME to not confuse makewhatis
    and apropos(1).

* Sat Apr 12 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.2-alt1
- control-restore: be more verbose.

* Sun Jan 19 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt1
- Refined output for facilities with slashes.

* Wed Jan 08 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5-alt1
- Synced with owl-control-0.5:
  * Wed Jan 08 2003 Solar Designer <solar@owl.openwall.com>
  - Wrote control(8) and control-dump(8) manual pages.

* Sun Nov 03 2002 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt1
- Synced with owl-control-0.4, including:
  + minor syntax fixes in control, control-dump and control-restore;
  + in control_subst(), don't rewrite files when the new setting is the same.

* Sat Oct 12 2002 Dmitry V. Levin <ldv@altlinux.org> 0.3.1-alt1
- ALT adaptions.
- Added control-dump and control-restore utilities.

* Sun Jul 07 2002 Solar Designer <solar@owl.openwall.com>
- Use grep -q in the provided shell functions.

* Wed Feb 06 2002 Michail Litvak <mci@owl.openwall.com>
- Enforce our new spec file conventions.

* Wed Nov 22 2000 Solar Designer <solar@owl.openwall.com>
- Support extended regexp's in control_subst().

* Fri Aug 11 2000 Solar Designer <solar@owl.openwall.com>
- Various important changes to the provided shell functions.
- Wrote the package description.
- Moved the symlink: /sbin/control is now /usr/sbin/control.

* Thu Aug 10 2000 Solar Designer <solar@owl.openwall.com>
- Initial version.
