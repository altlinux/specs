Name: pm-utils
Version: 1.4.1
Release: alt2
Summary: Tools to suspend and hibernate computer
Summary(ru_RU.UTF-8):  Набор утилит для приостановления работы компьютера.
Url: http://pm-utils.freedesktop.org/
License: GPL
Group: System/Base

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: %name-%version.tar
Source1: hooks4main.tar
Source2: README.ALT
Patch: %name-alt-misc.patch
Patch1: %name-alt-apm.patch

Conflicts: powermgmt-base

BuildRequires: docbook-dtds
# Automatically added by buildreq on Sat Jun 21 2008
BuildRequires: xmlto

%description
Provides simple shell command line tools to suspend and hibernate computer
that can be used to run vendor or distro supplied scripts on suspend and resume.

%prep
%setup
%patch -p1
%patch1 -p1

%build
%autoreconf
%configure
%make

%install
%makeinstall_std
mv %buildroot%_docdir/%name doc
cp -a %SOURCE2 doc/

# hooks
tar xf %SOURCE1 -C %buildroot%_libexecdir/%name
cat %buildroot%_libexecdir/%name/defaults.add >> %buildroot%_libexecdir/%name/defaults
rm -f %buildroot%_libexecdir/%name/defaults.add

# disable dangerous and vanished hooks
for f in '*grub'; do
	touch %buildroot%_sysconfdir/pm/sleep.d/`basename %buildroot%_libexecdir/%name/sleep.d/$f`
done

%files
%_sysconfdir/pm
%_bindir/*
%_sbindir/*
%_libexecdir/%name
%_pkgconfigdir/%name.pc
%_man1dir/*
%_man8dir/*
%doc AUTHORS MAINTAINERS NEWS README* TODO pm/HOWTO*
%doc doc/*

%changelog
* Mon Oct 18 2010 Ildar Mulyukov <ildar@altlinux.ru> 1.4.1-alt2
- add fix to NM hook from FD bugzilla (closes: #24321) (merged into
	%name-alt-misc.patch)
- fix sleep.d/60services order in suspend sequence
- add README.ALT

* Wed Sep 08 2010 Ildar Mulyukov <ildar@altlinux.ru> 1.4.1-alt1
- new version (closes: #23337)
- Remove hal dependency (closes: #23951)

* Sun Feb 22 2009 Ildar Mulyukov <ildar@altlinux.ru> 1.2.4-alt1
- version update
- remove additional (Suse) hooks: those should be packaged separately
- cherry-pick ldv's patches
- add APM support (by ldv@)

* Thu Aug 14 2008 Ildar Mulyukov <ildar@altlinux.ru> 1.1.2.4-alt1
- new version
- added hooks (branch hooks)

* Sat May 31 2008 Ildar Mulyukov <ildar@altlinux.ru> 1.1.2.2-alt0.1
- brand new version after a long delay
- bare version, no additions

* Tue Feb 20 2007 Andriy Stepanov <stanv@altlinux.ru> 0.20.0.cvs20070215-alt4
- add use s2disk and s2ram from suspend package

* Tue Feb 20 2007 Andriy Stepanov <stanv@altlinux.ru> 0.20.0.cvs20070215-alt3
- Add hooks from SuSe

* Tue Feb 20 2007 Andriy Stepanov <stanv@altlinux.ru> 0.20.0.cvs20070215-alt2
- Upstream hooks revised for ALT Linux system

* Mon Feb 19 2007 Andriy Stepanov <stanv@altlinux.ru> 0.20.0.cvs20070215-alt1
- Initial test build for Sisyphus
