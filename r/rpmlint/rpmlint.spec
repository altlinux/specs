Name: rpmlint
Version: 0.85
Release: alt3.1

Summary: RPM correctness checker
License: GPL2
Group: Development/Other
URL: http://rpmlint.zarb.org/

Source0: %name-%version.tar.bz2
Source1: config.alt
Source2: README.ALT
BuildArch: noarch

Patch0: %name-0.78-alt-rpm-v2.patch
Patch1: %name-0.85-popen2.patch

Packager: Evgenii Terechkov <evg@altlinux.org>

Requires: bash binutils cpio cpp file findutils grep rpm-python

%description
Rpmlint is a tool to check common errors on rpm packages.
Binary and source packages can be checked.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

cp %SOURCE1 config
cp %SOURCE2 .

%build
%make_build

%install
%make_install install DESTDIR=%buildroot

bzip2 -k ChangeLog

mkdir -p %buildroot%_sysconfdir/bash_completion.d/
install -m644 %name.bash-completion %buildroot%_sysconfdir/bash_completion.d/%name

%files
%doc ChangeLog.bz2 INSTALL README*
%config(noreplace) %_sysconfdir/%name
%config(noreplace) %_sysconfdir/bash_completion.d/%name
%_bindir/*
%_man1dir/%{name}.*
%_datadir/%name

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.85-alt3.1
- Rebuild with Python-2.7

* Tue Jan 12 2010 Terechkov Evgenii <evg@altlinux.ru> 0.85-alt3
- Patch1 added to remove warnings on deprecated popen2 module

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.85-alt2.1
- Rebuilt with python 2.6

* Tue Mar 17 2009 Terechkov Evgenii <evg@altlinux.ru> 0.85-alt2
- Noarch build fix (shame on me)

* Tue Mar 17 2009 Terechkov Evgenii <evg@altlinux.ru> 0.85-alt1
- 0.85 (#19195)
- Build as noarch
- Buildrequires updated
- Packager tag updated

* Sun Mar 16 2008 Terechkov Evgenii <evg@altlinux.ru> 0.82-alt1
- 0.82
- Licencse tag changed to gpl2
- Some filters added to config (#14098)
- Spec cleanups

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.80-alt1.1
- Rebuilt with python-2.5.

* Fri Apr 27 2007 Igor Zubkov <icesik@altlinux.org> 0.80-alt1
- 0.79 -> 0.80

* Sun Mar 18 2007 Igor Zubkov <icesik@altlinux.org> 0.79-alt1
- 0.71 -> 0.79
- update Patch0 for old rpm
- add manpage
- enable all checks in rpmlint

* Tue Mar 13 2007 Igor Zubkov <icesik@altlinux.org> 0.71-alt7
- sync list groups with rpm-4.0.4-alt73
- update Url

* Tue Mar 13 2007 Igor Zubkov <icesik@altlinux.org> 0.71-alt6
- bzip2 ChangeLog file (closes #11080)
- buildreq

* Mon Oct 31 2005 Igor Zubkov <icesik@altlinux.ru> 0.71-alt5
- update ValidBuildHost
- remove not-standard-release-extension warning
- remove invalid-license warning
- remove summary-not-capitalized warning
- remove summary-ended-with-dot warning

* Mon Oct 31 2005 Igor Zubkov <icesik@altlinux.ru> 0.71-alt4
- remove requires-on-release warning 
- enable TagsCheck

* Mon Oct 31 2005 Igor Zubkov <icesik@altlinux.ru> 0.71-alt3
- disable all checks
- enable DistributionCheck

* Mon Oct 31 2005 Igor Zubkov <icesik@altlinux.ru> 0.71-alt2
- update config

* Mon Oct 31 2005 Igor Zubkov <icesik@altlinux.ru> 0.71-alt1
- update to 0.71

* Fri Sep 09 2005 Igor Zubkov <icesik@altlinux.ru> 0.70-alt0.8
- added /etc/bash_completion.d/rpmlint

* Wed Sep 07 2005 Igor Zubkov <icesik@altlinux.ru> 0.70-alt0.7
- add check for missing Packager tag

* Mon Sep 05 2005 Igor Zubkov <icesik@altlinux.ru> 0.70-alt0.6
- correct check for release tag

* Sun Sep 04 2005 Igor Zubkov <icesik@altlinux.ru> 0.70-alt0.5
- correct groups and users check

* Sat Sep 03 2005 Igor Zubkov <icesik@altlinux.ru> 0.70-alt0.4
- correct check for menu files

* Sat Aug 20 2005 Igor Zubkov <icesik@altlinux.ru> 0.70-alt0.3
- realy remove some old policy (thx to rpmlint)

* Fri Aug 19 2005 Igor Zubkov <icesik@altlinux.ru> 0.70-alt0.2
- remove some old policy from mandrake (mandriva)
- add some new policy for ALTLinux Sisyphus

* Mon Aug 15 2005 Igor Zubkov <icesik@altlinux.ru> 0.70-alt0.1
- fix work with old rpm

* Mon Aug 15 2005 Igor Zubkov <icesik@altlinux.ru> 0.70-alt0
- update to 0.70

* Mon Aug 15 2005 Igor Zubkov <icesik@altlinux.ru> 0.48-alt0
- update to 0.48

* Mon Aug 15 2005 Igor Zubkov <icesik@altlinux.ru> 0.47-alt0
- update to 0.47

* Thu Aug 11 2005 Igor Zubkov <icesik@altlinux.ru> 0.46-alt0.2
- twiks

* Wed Aug 10 2005 Igor Zubkov <icesik@altlinux.ru> 0.46-alt0.1
- add README.ALT to package

* Sat Aug 06 2005 Igor Zubkov <icesik@altlinux.ru> 0.46-alt0
- update to 0.46

* Sat Aug 06 2005 Igor Zubkov <icesik@altlinux.ru> 0.45-alt0
- update to 0.45

* Sat Aug 06 2005 Igor Zubkov <icesik@altlinux.ru> 0.44-alt0
- update to 0.44

* Sat Aug 06 2005 Igor Zubkov <icesik@altlinux.ru> 0.43-alt0
- update to 0.43

* Sat Aug 06 2005 Igor Zubkov <icesik@altlinux.ru> 0.42-alt0
- update to 0.42

* Sat Aug 06 2005 Igor Zubkov <icesik@altlinux.ru> 0.41-alt0
- update to 0.41

* Sat Aug 06 2005 Igor Zubkov <icesik@altlinux.ru> 0.40-alt1.1
- add config

* Tue Jan 29 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.40-alt1
- 0.40
- Relocated %_datadir/%name to %_libdir/%name.

* Tue Nov 28 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.39-alt1
- 0.39

* Wed Jun 27 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.32-alt1
- New version
- Killed all changelogs before 2001

* Mon Jun 18 2001 Christian Belisle <cbelisle@mandrakesoft.com> 0.32-2mdk
- Added descriptions for the -i option.

* Wed Jun 13 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.32-1mdk
- rpmlint.py: o If the file given on the command line doesn't exist,
               try to use the name as an installed package to check.
              o new -i option to give explanation on the errors/warnings (not too much
               descriptions have been added ;-)

- MenuCheck.py: added new Office sub menus.

- FilesCheck.py: o added /usr/X11R6/man subdirs to the list of
	          STANDARD_DIRS.
	         o warn for .so file only if they are in a lib dir.
                 o warn for source files in a non devel package only if they are not
                  doc files.

- TagsCheck.py: corrected description-line-too-long check.

- FilesCheck.py: add the rpm user and group per request of Jeff
	         Johnson for the future version of rpm.

* Fri May 18 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.31-1mdk
- PostCheck.py: check that a script isn't only one command.
                check postin and prein instead of postun and preun
	        for ghost files creation.

- MenuCheck.py: don't check NO_XALF in menu command.

- FilesCheck.py: Add rpcuser.

- Config.py: Expections for ldconfig, initscripts, netkit-base and iputils.

- TagsCheck.py: check length of summary and description lines.

* Fri Feb 16 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.30-1mdk

- InitScriptCheck.py: check if runlevels are set

- MenuCheck.py: added support to check launchers.

- I18NCheck.py: check subdirs of /sur/share/man.

- PostCheck.py: check that the postun creates the ghost files
                added install to dangerous commands

- LSBCheck.py: first version

- TagsCheck.py: changed Window Maker to WindowMaker
                Add https as valid url.
                Used list of licenses from www.opensource.org/licenses
                Check the full license before splitting in it
                multiple parts.

* Tue Dec 26 2000 Dmitry V. Levin <ldv@fandra.org> 0.29-ipl1mdk
- RE adaptions.
