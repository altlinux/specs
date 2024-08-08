Name: shadow
Version: 4.16.0
Release: alt2
Epoch: 1

Summary: Utilities for managing shadow password files and user/group accounts
License: BSD-3-Clause and GPL-2.0-or-later
Group: System/Base
Url: https://github.com/shadow-maint/shadow

Source0: %url/%name-%version.tar
Source1: login.defs
Source2: useradd.default
Source3: user-group-mod.pamd
Source4: chage-chfn-chsh.pamd
Source5: chpasswd-newusers.pamd
Source6: chage.control
Source7: chfn.control
Source8: chsh.control
Source9: gpasswd.control
Source10: newgrp.control
Source11: groupmems.control
Source12: groupmems.pamd
Source13: newuidmap.control
Source14: newgidmap.control

Patch: %name-%version-%release.patch

%def_disable bootstrap
%if_enabled bootstrap
%def_without selinux
%def_without audit
%def_without btrfs
%def_without pam
%def_disable man
%else
%def_with selinux
%def_with audit
%def_with btrfs
%def_with pam
%def_enable man
%endif

%define lsubid_sovers 5

# libbsd support for readpassphrase().
# Using in-source implementation instead.
%def_without libbsd

%set_verify_elf_method strict

BuildPreReq: mktemp >= 1:1.3.1, rpm-build >= 4.0.4-alt10
# for man pages generation
%if_enabled man
BuildRequires: xsltproc docbook-style-xsl docbook-dtds
%endif

%if_with selinux
BuildPreReq: libselinux-devel libsemanage-devel
%endif

%{?_with_audit:BuildRequires: libaudit-devel}

%if_with pam
BuildRequires: libpam-devel libtcb-devel pam_userpass-devel
%endif
BuildRequires: libcrypt-devel >= 4.0.1-alt1

%{?_with_libbsd:BuildRequires: libbsd-devel}

%description
This package includes the tools necessary for manipulating local user and
group databases. It supports both traditional and tcb shadow password files.

%package utils
Summary: Utilities for managing shadow password files and user/group accounts
Group: System/Base
Requires: %name-convert = %EVR
%if_with pam
Requires: tcb-utils >= 0.9.8
%endif
Obsoletes: adduser

%description utils
This package includes utilities for managing shadow password files and
user/group accounts:
+ useradd: creates a new user or updates default new user information;
+ userdel: deletes a user account and related files;
+ usermod: modifies a user account;
+ groupadd: creates a new group;
+ groupdel: deletes a group;
+ groupmod: modifies a group;
+ newusers: updates and creates new users in batch;
+ chpasswd: updates password file in batch.

%package check
Summary: Utilities for checking integrity of the password, group, shadow-password, or shadow-group files
Group: System/Base
Requires: %name-convert = %EVR

%description check
This package includes utilities for checking integrity of the password, group,
shadow-password, or shadow-group files:
+ pwck: verifies the integrity of the system password authentication information;
+ grpck: verifies the integrity of the system group authentication information.

%package convert
Summary: Utilities for convertion to and from shadow passwords and groups
Group: System/Base

%description convert
This package includes utilities for convertion to and from shadow passwords
and groups:
+ pwconv: creates shadow from passwd and an optionally existing shadow;
+ pwunconv: creates passwd from passwd and shadow and then removes shadow;
+ grpconv: creates gshadow from group and an optionally existing gshadow;
+ grpunconv: creates group from group and gshadow and then removes gshadow.

%package change
Summary: Utilities for changing user shell, finger and password information
Group: System/Base
Requires: %name-utils = %EVR

%description change
This package includes utilities for changing user shell, finger and password
information:
+ chage: changes the number of days between password changes and the date of
         the last password change;
+ chfn: changes user fullname, office number, office extension, and home phone
        number information for a user's account;
+ chsh: changes the user login shell.

%package edit
Summary: Utilities for editing the password, group, shadow-password, or shadow-group files
Group: System/Base
Requires: %name-utils = %EVR

%description edit
This package includes utilities for editing the password, group,
shadow-password, or shadow-group files:
+ vipw: edits the /etc/passwd and /etc/shadow files;
+ vigr: edits the /etc/group and /etc/gshadow files.

%package groups
Summary: Utilities for execute command as different group ID
Group: System/Base
Requires: %name-utils = %EVR

%description groups
This package includes utilities for execute command as different group ID:
+ gpasswd: is used to administer the /etc/group and etc/gshadow files;
+ newgrp: is used to change the current group ID during a login session;
+ sg: is used to execute command as different group ID.

%package submap
Summary: Utilities for creating uid and gid mappings in user namespaces
Group: System/Base
Requires: %name-utils = %EVR

%description submap
This package includes utilities for creating uid and gid mappings
in user namespaces:
* newuidmap: set the uid mapping of a user namespace;
* newgidmap: set the gid mapping of a user namespace.

%package -n libsubid%lsubid_sovers
Summary: Subordinate id handling library
Group: System/Libraries

%description -n libsubid%lsubid_sovers
The library provides an interface for querying, granding and ungranting
subordinate user and group ids.

%package -n libsubid-devel
Summary: Development files for the subordinate id handling library
Group: Development/C
Requires: libsubid%lsubid_sovers = %EVR

%description -n libsubid-devel
The library provides an interface for querying, granding and ungranting
subordinate user and group ids.
This package contains development files for libsubid.

%package log
Summary: Utilities for examining lastlog and faillog files
Group: System/Base
Requires: %name-utils = %EVR

%description log
This package includes utilities for examining lastlog and faillog files:
+ faillog: formats the contents of the system failure log file, and maintains
           failure counts and limits;
+ lastlog: formats the contents of the system last login file.

%package suite
Summary: The shadow suite
Group: System/Base
BuildArch: noarch
Requires: %name-change = %EVR
Requires: %name-check = %EVR
Requires: %name-convert = %EVR
Requires: %name-edit = %EVR
Requires: %name-groups = %EVR
Requires: %name-log = %EVR
Requires: %name-utils = %EVR
Requires: %name-submap = %EVR

%description suite
This virtual package unifies all shadow suite subpackages.

%prep
%setup
%patch -p1

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%ifnarch %e2k
%add_optflags -Werror -Wno-error=address -Wno-error=cpp
%endif
%add_optflags -DEXTRA_CHECK_HOME_DIR
%configure \
	--disable-static \
	--enable-lastlog \
	%{?_with_pam:--with-tcb} \
	%{?_with_pam:--with-libpam} \
	%{subst_with selinux} \
	%{subst_with audit} \
	%{subst_with btrfs} \
	%{subst_with libbsd} \
	--with-group-name-max-length=32 \
	--without-sha-crypt \
	--without-su \
	%{?_with_pam:--enable-account-tools-setuid} \
	%{subst_enable man}
%make_build

make -C po/ ru.gmo

%install
%makeinstall

install -pD -m640 %_sourcedir/login.defs %buildroot%_sysconfdir/login.defs
%if_without pam
sed -i %buildroot%_sysconfdir/login.defs \
	-r \
	-e 's/^(TCB_AUTH_GROUP.*)$/# \1/' \
	-e 's/^(USE_TCB.*)$/# \1/' \
	-e 's/^(TCB_SYMLINKS.*)$/# \1/' \
	%nil
%endif
install -pD -m600 %_sourcedir/useradd.default %buildroot%_sysconfdir/default/useradd

rm -rf %buildroot%_sysconfdir/pam.d
%if_with pam
mkdir -p %buildroot%_sysconfdir/pam.d
pushd %buildroot%_sysconfdir/pam.d
install -pm600 %_sourcedir/user-group-mod.pamd user-group-mod
ln -s user-group-mod groupadd
ln -s user-group-mod groupdel
ln -s user-group-mod groupmod
ln -s user-group-mod useradd
ln -s user-group-mod userdel
ln -s user-group-mod usermod
install -pm640 %_sourcedir/chage-chfn-chsh.pamd chage-chfn-chsh
ln -s chage-chfn-chsh chage
ln -s chage-chfn-chsh chfn
ln -s chage-chfn-chsh chsh
install -pm600 %_sourcedir/chpasswd-newusers.pamd chpasswd-newusers
ln -s chpasswd-newusers chpasswd
ln -s chpasswd-newusers newusers
install -pm600 %_sourcedir/groupmems.pamd groupmems
popd
%endif

ln -s useradd %buildroot%_sbindir/adduser

install -pD -m755 %_sourcedir/chage.control %buildroot%_controldir/chage
install -pD -m755 %_sourcedir/chfn.control %buildroot%_controldir/chfn
install -pD -m755 %_sourcedir/chsh.control %buildroot%_controldir/chsh
install -pD -m755 %_sourcedir/gpasswd.control %buildroot%_controldir/gpasswd
install -pD -m755 %_sourcedir/newgrp.control %buildroot%_controldir/newgrp
install -pD -m755 %_sourcedir/groupmems.control %buildroot%_controldir/groupmems
install -pD -m755 %_sourcedir/newuidmap.control %buildroot%_controldir/newuidmap
install -pD -m755 %_sourcedir/newgidmap.control %buildroot%_controldir/newgidmap

touch %buildroot%_sysconfdir/subuid
touch %buildroot%_sysconfdir/subgid

mkdir -p %buildroot%_sysconfdir/shadow-maint/{user,group}{add,del}-{pre,post}.d

%find_lang %name
%define _unpackaged_files_terminate_build 1

%define save_login_defs_file  /tmp/shadow-utils-update-save-old-login.defs

%post convert
if [ $1 = 1 ]; then
	if [ ! -e /etc/gshadow ]; then
		%_sbindir/grpconv
	fi
	if [ ! -e /etc/shadow -a ! -e /etc/tcb ]; then
		%_sbindir/pwconv
	fi
fi

%pre utils
if [ $1 -eq 2 ]; then
	OLD_VERSION="$(rpm -q --qf '%%{EPOCH}:%%{VERSION}-%%{RELEASE}' %name-utils)"
	[ -z "$OLD_VERSION" ] || RES="$(rpmevrcmp "$OLD_VERSION" 1:4.13-alt3)"
	if [ -n "$RES" ] && [ $RES -lt 0 ]; then
		cp -a /etc/login.defs %save_login_defs_file
		# Ensure that old /etc/login.defs.rpmnew doesn't exist
		rm -f /etc/login.defs.rpmnew
	fi
fi

%triggerpostun utils -- %name-utils < 1:4.13-alt3
if [ -e %save_login_defs_file ] && [ ! -e /etc/login.defs.rpmnew ]; then
		mv /etc/login.defs /etc/login.defs.rpmnew && \
		  mv %save_login_defs_file /etc/login.defs && \
		  echo "warning: /etc/login.defs created as /etc/login.defs.rpmnew due to UID_MIN/GID_MIN change"
fi
rm -f %save_login_defs_file

%pre change
%pre_control chage chfn chsh

%post change
%post_control -s restricted chage chfn chsh

%pre groups
%pre_control gpasswd newgrp groupmems

%post groups
%post_control -s restricted gpasswd newgrp groupmems

%pre submap
%pre_control newuidmap newgidmap

%post submap
%post_control -s restricted newuidmap newgidmap

%files convert
%_sbindir/*conv
%if_enabled man
%_mandir/man?/*conv.*
%endif

%files utils -f %name.lang
%attr(600,root,root) %config(noreplace) %_sysconfdir/default/useradd
%attr(640,root,shadow) %config(noreplace) %_sysconfdir/login.defs
%dir %attr(770,root,root) %_sysconfdir/shadow-maint/
%dir %attr(770,root,root) %_sysconfdir/shadow-maint/user*.d/
%dir %attr(770,root,root) %_sysconfdir/shadow-maint/group*.d/
%if_with pam
%config(noreplace) %_sysconfdir/pam.d/user-group-mod
%_sysconfdir/pam.d/groupadd
%_sysconfdir/pam.d/groupdel
%_sysconfdir/pam.d/groupmod
%_sysconfdir/pam.d/useradd
%_sysconfdir/pam.d/userdel
%_sysconfdir/pam.d/usermod
%config(noreplace) %_sysconfdir/pam.d/chpasswd-newusers
%_sysconfdir/pam.d/chpasswd
%_sysconfdir/pam.d/newusers
%endif
%_sbindir/user*
%_sbindir/group*
%_sbindir/adduser
%_sbindir/newusers
%_sbindir/chpasswd
%if_enabled man
%_man5dir/login.defs.*
%_man5dir/shadow.*
%_man8dir/chpasswd.*
%_man8dir/group*.*
%_man8dir/newusers.*
%_man8dir/user*.*
%endif
%doc README
%exclude %_bindir/groupmems
%if_enabled man
%exclude %_man8dir/groupmems.*
%endif

%files check
%_sbindir/*ck
%if_enabled man
%_mandir/man?/*ck.*
%endif

%files change
%config %_controldir/chage
%config %_controldir/chfn
%config %_controldir/chsh
%if_with pam
%attr(640,root,shadow) %config(noreplace) %_sysconfdir/pam.d/chage-chfn-chsh
%_sysconfdir/pam.d/chage
%_sysconfdir/pam.d/chfn
%_sysconfdir/pam.d/chsh
%endif
%attr(700,root,root) %verify(not mode,group) %_bindir/chage
%attr(700,root,root) %verify(not mode) %_bindir/chfn
%attr(700,root,root) %verify(not mode) %_bindir/chsh
%if_enabled man
%_mandir/man?/chage.*
%_mandir/man?/chfn.*
%_mandir/man?/chsh.*
%endif

%files edit
%_sbindir/vi??
%if_enabled man
%_mandir/man?/vi??.*
%endif

%files groups
%if_with pam
%_sysconfdir/pam.d/groupmems
%endif
%config %_controldir/gpasswd
%config %_controldir/newgrp
%config %_controldir/groupmems
%attr(700,root,root) %verify(not mode,group) %_bindir/gpasswd
%attr(700,root,root) %verify(not mode,group) %_bindir/newgrp
%_bindir/sg
%attr(700,root,root) %verify(not mode,group) %_bindir/groupmems
%if_enabled man
%_mandir/man?/gpasswd.*
%_mandir/man?/newgrp.*
%_mandir/man?/sg.*
%_man8dir/groupmems.*
%endif

%files submap
%config(noreplace) %_sysconfdir/subuid
%config(noreplace) %_sysconfdir/subgid
%config %_controldir/newuidmap
%config %_controldir/newgidmap
%attr(700,root,root) %verify(not mode,group) %_bindir/newuidmap
%attr(700,root,root) %verify(not mode,group) %_bindir/newgidmap
%_bindir/getsubids
%if_enabled man
%_man1dir/newuidmap.*
%_man1dir/newgidmap.*
%_man1dir/getsubids.*
%_man5dir/subuid.*
%_man5dir/subgid.*
%endif

%files -n libsubid%lsubid_sovers
%_libdir/libsubid.so.%lsubid_sovers
%_libdir/libsubid.so.%lsubid_sovers.*

%files -n libsubid-devel
%_libdir/libsubid.so
%_includedir/shadow/

%files log
%_bindir/*log
%if_enabled man
%_mandir/man?/*log.*
%endif

%files suite

%exclude %_bindir/expiry
%exclude %_sbindir/chgpasswd
%exclude %_sbindir/logoutd
%exclude %_sbindir/nologin
%if_enabled man
%exclude %_man1dir/expiry.1.*
%exclude %_man3dir/getspnam.3.*
%exclude %_man3dir/shadow.3.*
%exclude %_man5dir/gshadow.5.*
%exclude %_man5dir/passwd.5.*
%exclude %_man5dir/suauth.5.*
%exclude %_man8dir/chgpasswd.8.*
%exclude %_man8dir/logoutd.8.*
%exclude %_man8dir/nologin.8.*
%endif
%if_without pam
%exclude %_sysconfdir/limits
%exclude %_sysconfdir/login.access
%endif

%changelog
* Thu Aug 08 2024 Mikhail Efremov <sem@altlinux.org> 1:4.16.0-alt2
- Fixed build with lastlog enabled.
- log: Returned lastlog (closes: #51106).

* Thu Jun 20 2024 Mikhail Efremov <sem@altlinux.org> 1:4.16.0-alt1
- libsubid: Added so version to subpackage name.
- Updated to 4.16.0.

* Tue Jun 11 2024 Mikhail Efremov <sem@altlinux.org> 1:4.15.1-alt2
- audit_help: Supressed unused-result warning.

* Thu Apr 18 2024 Mikhail Efremov <sem@altlinux.org> 1:4.15.1-alt1
- Fixed bogus date in the changelog.
- Dropped obsoleted patches.
- Updated to 4.15.1.

* Thu Apr 04 2024 Mikhail Efremov <sem@altlinux.org> 1:4.14.7-alt1
- tcb: Use shadowlog variables.
- Dropped duplicate chmod() call.
- Dropped most of shadow-4.0.4.1-alt-progname.patch.
- Updated to 4.14.7.

* Wed Mar 06 2024 Mikhail Efremov <sem@altlinux.org> 1:4.14.6-alt1
- Updated to 4.14.6.

* Mon Feb 12 2024 Mikhail Efremov <sem@altlinux.org> 1:4.14.4-alt1
- Updated to 4.14.4.

* Fri Jan 19 2024 Mikhail Efremov <sem@altlinux.org> 1:4.14.3-alt1
- Updated to 4.14.3.

* Wed Nov 08 2023 Mikhail Efremov <sem@altlinux.org> 1:4.14.2-alt1
- Updated to 4.14.2.

* Tue Oct 24 2023 Mikhail Efremov <sem@altlinux.org> 1:4.14.1-alt1
- Updated patches.
- Updated to 4.14.1.

* Wed Aug 16 2023 Mikhail Efremov <sem@altlinux.org> 1:4.14.0-alt1
- utils: Packaged group{add,del}-{pre,post}.d directories.
- run_part: Don't fail if directory doesn't exist.
- Fixed build: drop unused variable.
- Updated to 4.14.

* Wed Aug 02 2023 Mikhail Efremov <sem@altlinux.org> 1:4.13-alt8
- usermod: Allow group and submap operations for non-local user
  (closes: #46847).

* Wed Jun 21 2023 Nikolay Burykin <bne@altlinux.org> 1:4.13-alt7
- newuidmap/newgidmap: Added cap_dac_read_search to all modes (ALT #46462).

* Thu May 25 2023 Nikolay Burykin <bne@altlinux.org> 1:4.13-alt6
- newuidmap/newgidmap: Added check for podmanonly mode (ALT #46220).

* Thu May 18 2023 Mikhail Efremov <sem@altlinux.org> 1:4.13-alt5
- libsubid: Link against libpam_userpass.
- valid_field: Always reject control characters (fixes: CVE-2023-29383).

* Thu May 04 2023 Nikolay Burykin <bne@altlinux.org> 1:4.13-alt4
- Changed control scripts for newuidmap/newgidmap:
  + Replaced the SUID Bit with POSIX Capabilities in all the
    configuration mode.
  + A new mode ("podmanonly") was added.

* Tue Apr 25 2023 Mikhail Efremov <sem@altlinux.org> 1:4.13-alt3
- Keep old login.defs when UID_MIN/GID_MIN changed.
- Increase default UID_MIN/GID_MIN to 1000.
- remove_tree: Allow a symlink as root if it shouldn't be removed.

* Tue Apr 11 2023 Mikhail Efremov <sem@altlinux.org> 1:4.13-alt2
- Added libsubid subpackage.
- Dropped disabled libshadow* subpackages.

* Mon Apr 10 2023 Mikhail Efremov <sem@altlinux.org> 1:4.13-alt1
- Fixed build without TCB.
- spec: simplified the bootstrap sequence (by Alexey Sheplyakov).
- Fixed build without PAM.
- fixed build without TCB and/or PAM (by Alexey Sheplyakov).
- useradd: Fixed Russian translation.
- Use /bin/run-parts if able.
- utils: Packaged user{add,del}-{pre,post}.d directories.
- useradd: Set default group to 100 (users).
- login.defs: Added HOME_MODE variable.
- login.defs: Added HMAC_CRYPTO_ALGO variable.
- login.defs: Added GRANT_AUX_GROUP_SUBIDS variable.
- login.defs: Added NONEXISTENT variable.
- Explicitly enabled btrfs support.
- Use 'set_verify_elf_method strict'.
- Enabled LFS on 32-bit systems.
- lib/commonio: Fixed fprintf() format.
- tcb: Added remove_tcbdir() function.
- shadow: Don't use relaxed usernames.
- newusers,pwck,useradd,usermod: Removed --badname option.
- Ensured that prefix is not '/'.
- userdel: Fixed mailbox removing.
- Added prefix support for TCB.
- Don't install libsubid static library.
- usermod: Don't call gr_free() with const variable.
- useradd: Fixed "discards 'const' qualifiers" warning.
- Updated 'alt-progname' patch.
- tcbfuncs.c: Fixed and updated selinux support.
- Updated 'copy_dir perms' patch.
- src/Makefile.am: Fixed noinst_PROGRAMS.
- Fixed license.
- Updated url.
- Updated to 4.13 (closes: #45794).

* Mon Aug 03 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.5-alt8
- NMU: fixed build with new selinux.

* Wed Nov 06 2019 Mikhail Efremov <sem@altlinux.org> 1:4.5-alt7
- valid_field: Check that characters are ASCII.
- login.defs: Add SAFE_PWDB_FIELDS variable.
- man: Add SAFE_PWDB_FIELDS description.
- lib: Add SAFE_PWDB_FIELDS variable.
- useradd,usermod: Use valid_field() to check fields.

* Fri Nov 01 2019 Mikhail Efremov <sem@altlinux.org> 1:4.5-alt6
- Use epoch instead of serial.
- login.defs: Add REGEXP_NAME variable.
- man: Add REGEXP_NAME description.
- pwck,grpck: Use strcasecmp() to check names.
- libmisc: Don't allow leading digits in the names with regexp too.
- utils: Check that user/group is unique.
- libmisc: Allow names to be verified by regexp (closes: #9202).
- Fix build with gcc-9.

* Tue Aug 27 2019 Mikhail Efremov <sem@altlinux.org> 1:4.5-alt5
- Backported patch from shadow-4.6:
  + newgidmap: enforce setgroups=deny if self-mapping a group
    (fixes CVE-2018-7169).
- Don't use deprecated PreReq.

* Mon Nov 26 2018 Mikhail Efremov <sem@altlinux.org> 1:4.5-alt4
- chfn: Silence format-truncation warning

* Thu Jun 28 2018 Mikhail Efremov <sem@altlinux.org> 1:4.5-alt3
- Fix default hashing method.
- Request automatic entropy for salt.
- vipw: Change -u option to imply -s (closes: #35097).
- Use %%e2k macro.

* Tue Feb 27 2018 Mikhail Efremov <sem@altlinux.org> 1:4.5-alt2
- Fixed build with gcc-7:
  + Remove redundant const qualifier.
  + Ensure that we have enough room for filenames.

* Mon Sep 04 2017 Mikhail Efremov <sem@altlinux.org> 1:4.5-alt1
- Don't install files with suid.
- useradd: Fix lastlog_reset() argument type.
- Drop unused variables.
- Updated to 4.5.

* Fri Mar 03 2017 Mikhail Efremov <sem@altlinux.org> 1:4.4-alt1
- Don't own %%_sysconfdir/default/ (closes: #32541).
- Fix possible crash if gmtime() returns NULL.
- chsh: Fix duplicate warning.
- Enable audit support.
- Don't package ChangeLog/NEWS files.
- Spec cleanup.
- submap: Add control scripts for newuidmap/newgidmap.
- Fix build: ignore write() return value.
- configure.ac: Drop man/po/Makefile.
- Drop FORCE_SHADOW.
- Don't create missing files.
- Fixes from usptream git:
  + Keep the permissions of the original file when creating a backup.
  + useradd: Read defaults after changing root directories.
  + Don't crash on bogus keys in login.defs if PAM is enabled.
  + Last bits of enabling subuids.
  + Make login.def files valid ASCII instead of UTF-8.
  + include getdef.h for getdef_bool prototype.
  + Print error message if SELinux file context manipulation fails.
  + Fix regression in useradd not loading defaults properly.
  + */Makefile.am: Replace INCLUDES with AM_CPPFLAGS.
- Updated to 4.4 (fixes CVE-2016-6252).

* Fri Feb 26 2016 Mikhail Efremov <sem@altlinux.org> 1:4.2.1-alt6
- E2K: avoid -Werror (lcc) (by Michael Shigorin).
- Fix build on x32.
- Fix build without selinux again.

* Wed Feb 24 2016 Mikhail Efremov <sem@altlinux.org> 1:4.2.1-alt5
- Don't treat cpp warnings as error.
- Fix build without selinux support.

* Wed Dec 23 2015 Mikhail Efremov <sem@altlinux.org> 1:4.2.1-alt4
- Lazy link with -lsemanage (by Dmitry V. Levin).

* Mon Oct 26 2015 Mikhail Efremov <sem@altlinux.org> 1:4.2.1-alt3
- chage: Fix work with tcb.

* Fri Oct 23 2015 Mikhail Efremov <sem@altlinux.org> 1:4.2.1-alt2
- Package /etc/subuid and /etc/subgid files.
- Add -Werror to optflags.
- Explicitly use --with-tcb configure option.
- Fix compiler warnings.
- vipw: Check link() return status.
- useradd: Check chown/chmod return status.
- Fix uninitialized variable.
- Fix usermod's manpage.

* Tue Oct 20 2015 Mikhail Efremov <sem@altlinux.org> 1:4.2.1-alt1
- Add submap subpackage (closes: #31201).
- Merge ALT-specific tcb patch.
- userdel.c: Fix variable name in case of tcb.
- Add missing include in case of tcb.
- Fix build with --as-needed in case of tcb.
- Makefile: Drop passwd from suidubins.
- Update ALT-specific patches.
- Drop obsoleted patches.
- Updated to 4.2.1.

* Thu Nov 07 2013 Mikhail Efremov <sem@altlinux.org> 1:4.1.4.2-alt9
- Fix build: Remove deprecated AM_C_PROTOTYPES.

* Thu Jun 21 2012 Mikhail Efremov <sem@altlinux.org> 1:4.1.4.2-alt8
- Fixed groupmod.

* Fri Jun 15 2012 Mikhail Efremov <sem@altlinux.org> 1:4.1.4.2-alt7
- useradd: Print exit code if an error was occurred.

* Fri Jun 01 2012 Mikhail Efremov <sem@altlinux.org> 1:4.1.4.2-alt6
- Do not create mail spool if -M option was given.

* Thu May 31 2012 Mikhail Efremov <sem@altlinux.org> 1:4.1.4.2-alt5
- Package suite subpackage as noarch.

* Wed May 30 2012 Mikhail Efremov <sem@altlinux.org> 1:4.1.4.2-alt4
- Use _exit() for exit from child.
- spawn.c: Backport from upstream's svn.

* Tue May 29 2012 Mikhail Efremov <sem@altlinux.org> 1:4.1.4.2-alt3
- useradd: Add 'private' to allowed values of CREATE_MAIL_SPOOL.
- Don't show error message if flashing nscd cache is failed.

* Wed May 16 2012 Mikhail Efremov <sem@altlinux.org> 1:4.1.4.2-alt2
- gshadow.c: Drop unused variable.
- Added lib/spawn.c and lib/spawn.h.
- useradd.c: Fix fprintf() format string.
- useradd.c: Avoid redefinition of SHELL.
- Fix missing includes.
- Fix some const issues.
- Fix find_new_uid/gid for big UID/GID_MAX.
- Fix gshadow functions from shadow utils.

* Tue Apr 03 2012 Mikhail Efremov <sem@altlinux.org> 1:4.1.4.2-alt1.M60C.1
- Drop obsoleted %%post{,un}_ldconfig.
- Rebuild for new c6.

* Thu Dec 23 2010 Mikhail Efremov <sem@altlinux.org> 1:4.1.4.2-alt1.M55C.1
- enable SELinux support.
- Drop all patches from spec, use gear tags.
- Updated to 4.1.4.2.

* Tue Apr 22 2008 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.4.1-alt9
- def_load: Silence complains about missing /etc/login.defs file.

* Fri Mar 21 2008 Grigory Batalov <bga@altlinux.ru> 1:4.0.4.1-alt8.1
- Include local system-auth-use_first_pass into chpasswd-newusers
  PAM config as it doesn't work with ldap one (#15003).

* Sun Jan 20 2008 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.4.1-alt8
- useradd: Remove tcb user dir in case of abnormal program completion (#14091).
- Fixed a few manpage typos (#12230).
- Fixed build with new autotools.

* Sun Apr 15 2007 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.4.1-alt7
- Added summary to control scripts.

* Sun Sep 17 2006 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.4.1-alt6
- newgrp: Fixed potential NULL pointer dereference (#9362).

* Thu Jan 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1:4.0.4.1-alt5.1
- Rebuilt for new style PAM dependencies generated by rpm-build-4.0.4-alt55.

* Mon May 16 2005 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.4.1-alt5
- Fixed double free bug in userdel_rm_tcbdir().

* Sun Jan 16 2005 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.4.1-alt4
- Synced with 4.0.4.1-owl7:
  + Report /etc/login.defs read errors to stderr, not only to syslog.
  + Removed verify checks for files controlled via control(8) facility.
  + Fixed compilation issues detected by gcc-3.4.3.

* Mon Nov 22 2004 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.4.1-alt3
- userdel: fixed return code.

* Sat Nov 20 2004 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.4.1-alt2
- Synced with 4.0.4.1-owl4:
  + Added the USERNAME_MAX and GROUPNAME_MAX options.
- chage, chfn, chsh, gpasswd, newgrp:
  + Changed default mode to "restricted"; this is required to add
  shadow-change and shadow-groups packages to default install set.
- shadow-suite: new subpackage, unifies all shadow suite subpackages.

* Wed Nov 10 2004 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.4.1-alt1
- Updated to 4.0.4.1-owl2.
- Updated patches.
- Use control macros.
- Added help to control.
- Documented user/group name restrictions (#4390).
- Keep tools at mode "restricted" in the packages, but default
  them to "public" in %post when the packages are first installed.
  This avoids a race and fail-open behaviour.

* Thu Jun 10 2004 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.0-alt15
- Properly check the return value from pam_chauthtok() in
  libmisc/pwdcheck.c: passwd_check() that is used by chfn and
  chsh commands (Owl).
  Thanks to Steve Grubb, Martin Schulze and Solar Designer.

* Thu Mar 25 2004 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.0-alt14
- Fixed build with new gettext and autotools.
- Fixed typo in chage-chfn-chsh.pamd (#3904).

* Sat Nov 22 2003 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.0-alt13
- In tcbfuncs/tcb_move(), use mode 0700 instead of mode 0 for the
  directory being modified as the latter is incompatible with
  the mode 0 hack in vserver kernel patches.

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.0-alt12
- Explicitly use old libtool for build.

* Mon Jun 30 2003 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.0-alt11
- useradd, usermod:
  fixed user_group initialization (voins, #0001875).

* Sat May 24 2003 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.0-alt10
- PAM configuration policy enforcement.

* Sat Apr 12 2003 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.0-alt9
- Rebuilt with libpam_userpass.so.1.

* Mon Oct 28 2002 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.0-alt8
- Merged Owl changes:
  * Thu Oct 24 2002 Solar Designer <solar@owl.openwall.com>
  - Cleaned up the recent changes.
  - Corrected a newly introduced memory leak on an error path.
  - Changed the TCB_SYMLINKS pseudo-code in login.defs(5) manual page to be
    C/English rather than shell for consistency with the pam_tcb(8) page.
  * Mon Aug 19 2002 Rafal Wojtczuk <nergal@owl.openwall.com>
  - Merged the enhancements which remove 32K users limit.

* Thu Oct 17 2002 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.0-alt7
- Added control support for chage, chfn, chsh, gpasswd, and newgrp.

* Wed Aug 14 2002 Dmitry V. Levin <ldv@altlinux.org> 1:4.0.0-alt6
- copy_tree: ensure strict permissions of created files.
- chage: made "chage -l" drop its saved GID too (Owl).
- useradd, usermod: removed the extra space in "[-e expire ]" in the usage instructions (Owl).

* Mon Mar 18 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:4.0.0-alt5
- Updated chkname patch.

* Fri Jan 25 2002 Stanislav Ievlev <inger@altlinux.ru> 1:4.0.0-alt4
- added rollback to standart skeleton dir if it doesn't exits

* Fri Dec 21 2001 Dmitry V. Levin <ldv@alt-linux.org> 1:4.0.0-alt3
- def_load: don't exit when /etc/login.defs not available.

* Thu Dec 20 2001 Dmitry V. Levin <ldv@alt-linux.org> 1:4.0.0-alt2
- userdel: fixed long standing bug in path_prefix check.

* Tue Dec 18 2001 Dmitry V. Levin <ldv@alt-linux.org> 1:4.0.0-alt1
- 4.0.0
- Merged in 16 patches from Owl.
- Updated default_skel and progname patches (all the rest are obsolete).
- Disabled build of unused software.
- Changed interpackage dependencies.
- %name-convert: convert group and passwd files after first install.
- Disabled libshadow.

* Mon Sep 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 20000902-alt3
- Fixed typo in mailspool patch.
- Added %%post scripts to ease migration.

* Mon Aug 13 2001 Dmitry V. Levin <ldv@altlinux.ru> 20000902-alt2
- Split shadow-utils into several subpackages.
- Libification.
- Remade mailspool patch (new options: z,Z,K).
- Enable packaging of chsh, chfn, vipw, vigr, newgrp.

* Thu Aug 02 2001 Dmitry V. Levin <ldv@altlinux.ru> 20000902-alt1
- 20000902
- Merged RH (up to 20000902-3) and Owl (up to 19990827-16owl) patches and configs.
- Get rid of %_sbindir/{d,mk}passwd and its manpages.

* Sun Feb 25 2001 Dmitry V. Levin <ldv@fandra.org> 20000826-ipl1mdk
- 20000826
- Merged MDK patches.
- Added progname patch.

* Sun Nov 05 2000 Dmitry V. Levin <ldv@fandra.org> 19990827-ipl9mdk
- Merge RH patches.
- FHSification.

* Mon May 29 2000 Dmitry V. Levin <ldv@fandra.org> 19990827-ipl8mdk
- Fix: updated docs about -D -k option.
- RE and Fandra adaptions.

* Fri Dec 3 1999 Florent Villard <warly@mandrakesoft.com>
- correct a segfault problem with NIS

* Sat Nov 13 1999 AEN <aen@logic.ru>
- Feature: added -D -k option.

* Wed Sep 22 1999 Cristian Gafton <gafton@redhat.com>
- fix segfault for userdel when the primary group for the user is not defined

* Tue Sep 21 1999 Cristian Gafton <gafton@redhat.com>
- Serial: 1 because now we are using 19990827 (why the heck can't they have
  a normal version just like everybody else?!)
- ported all patches to the new code base

* Thu Apr 15 1999 Bill Nottingham <notting@redhat.com>
- SIGHUP nscd from usermod, too

* Fri Apr 09 1999 Michael K. Johnson <johnsonm@redhat.com>
- added usermod password locking from Chris Adams <cadams@ro.com>

* Thu Apr 08 1999 Bill Nottingham <notting@redhat.com>
- have things that modify users/groups SIGHUP nscd on exit

* Wed Mar 31 1999 Michael K. Johnson <johnsonm@redhat.com>
- have userdel remove user private groups when it is safe to do so
- allow -f to force user removal even when user appears busy in utmp

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- edit out unused CHFN fields from login.defs.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 7)

* Wed Jan 13 1999 Bill Nottingham <notting@redhat.com>
- configure fix for arm

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- Note that /usr/sbin/mkpasswd conflicts with /usr/bin/mkpasswd;
  one of these (I think /usr/sbin/mkpasswd but other opinions are valid)
  should probably be renamed.  In any case, mkpasswd.8 from this package
  needs to be installed. (problem #823)

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 980403
- redid the patches

* Tue Dec 30 1997 Cristian Gafton <gafton@redhat.com>
- updated the spec file
- updated the patch so that new accounts created on shadowed system won't
  confuse pam_pwdb anymore ('!!' default password instead on '!')
- fixed a bug that made useradd -G segfault
- the check for the ut_user is now patched into configure

* Thu Nov 13 1997 Erik Troan <ewt@redhat.com>
- added patch for XOPEN oddities in glibc headers
- check for ut_user before checking for ut_name -- this works around some
  confusion on glibc 2.1 due to the utmpx header not defining the ut_name
  compatibility stuff. I used a gross sed hack here because I couldn't make
  automake work properly on the sparc (this could be a glibc 2.0.99 problem
  though). The utuser patch works fine, but I don't apply it.
- sleep after running autoconf

* Thu Nov 06 1997 Cristian Gafton <gafton@redhat.com>
- added forgot lastlog command to the spec file

* Sun Oct 26 1997 Cristian Gafton <gafton@redhat.com>
- obsoletes adduser

* Thu Oct 23 1997 Cristian Gafton <gafton@redhat.com>
- modified groupadd; updated the patch

* Fri Sep 12 1997 Cristian Gafton <gafton@redhat.com>
- updated to 970616
- changed useradd to meet RH specs
- fixed some bugs

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
