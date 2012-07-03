#TODO: pack tests as examples
%define minor_release MR33

Name: pccts
Version: 1.33
Release: alt3%minor_release

Summary: The Purdue Compiler-Construction Tools Set

License: Public Domain
Group: Development/C++
Url: http://www.polhode.com/pccts.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.polhode.com/%{name}133mr.tar.bz2
Patch: %name-1.33-alt-makefile.patch
Patch1: %name-1.33-debian.patch

%description
The Purdue Compiler-Construction Tools Set

%package devel
Summary: Headers for pccts
Group: Development/C++
Requires: %name = %version-%release

%description devel
Header files required to compile programs using pccts.

%prep
%setup -q -n %name
#%patch -p1
%patch1 -p1

%build
%make_build COPT="$RPM_OPT_FLAGS"

%install
install -d %buildroot{%_bindir,%_man1dir,%_includedir/%name/sorcerer}
rm -f bin/empty.txt

install -s -m755 bin/antlr %buildroot%_bindir/%name-antlr
install -s -m755 bin/dlg %buildroot%_bindir/%name-dlg
install -s -m755 bin/genmk %buildroot%_bindir/%name-genmk
install -s -m755 bin/sor %buildroot%_bindir/%name-sor

# Debian too packed with C files...
install -m644 h/*.[ch]* %buildroot%_includedir/%name/
install -m644 sorcerer/h/*.[ch]* %buildroot%_includedir/%name/sorcerer/
install -m644 antlr/antlr.1 dlg/dlg.1 %buildroot%_man1dir/

%files
%doc README RIGHTS
%_bindir/%name-antlr
%_bindir/%name-dlg
%_bindir/%name-genmk
%_bindir/%name-sor
%_man1dir/*

%files devel
%doc NOTES* *.txt *.ps MPW_Read_Me sorcerer/README sorcerer/UPDATES
%_includedir/%name/

%changelog
* Tue Jan 08 2008 Vitaly Lipatov <lav@altlinux.ru> 1.33-alt3MR33
- clean spec, change Packager
- build all binaries, add prefix pccts to it (fix bug #5938)
- remove PCCTS env variable set from profile.d

* Fri Feb 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.33-alt2MR33
- simply disabled sorcerer and genmk build, not required to compile
  cdrdao but cause errors with gcc-3.3.

* Mon Jan 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.33-alt1MR33
- remove deps on csh by fixing headers of %_sysconfdir/profile.d files
- syntax error in %_sysconfdir/profile.d/pccts.csh fixed.

* Tue Sep 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.33-alt0.9MR33
- built lastest maintenance release.

* Wed Jun 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.33-alt0.8MR31
- Minor specfile cleanup (at insistence of ldv).

* Thu Jan 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.33-alt0.7MR31
- First build for Sisyphus
