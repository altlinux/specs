Name: pdfedit
Version: 0.4.5
Release: alt2

Summary: Editor for manipulating PDF documents
License: GPL
Group: File tools

Url: http://pdfedit.cz
Source0: %name-%version.tar.bz2
Source1: %name.desktop
Source100: %name.watch
Patch0: pdfedit-0.4.1-alt-fontpath.patch
Packager: Michael Shigorin <mike@altlinux.org>

Requires: fonts-type1-urw

# Automatically added by buildreq on Tue Apr 07 2009
BuildRequires: boost-devel gcc-c++ imake libqt3-devel t1lib-devel xorg-cf-files

%{?!_desktopdir:%define _desktopdir %_datadir/applications}

%description
Complete editing of pdf documents is made possible with PDFedit.
You can change either raw pdf objects (for advanced users) or use
predefined gui functions. Functions can be easily added as everything
is based on a scripts.

Scripting is used to a great extent in editor and almost anything can
be scripted, it is possible to create own scripts or plugins.

%prep
%setup
%patch0 -p1
sed -i 's,bin/qmake,& "CONFIG+=no_fixpath",' src/Makefile

%build
export PATH=$PATH:%_qt3dir/bin
# see README
autoconf
%configure \
	--enable-stack-protector \
	--with-root-dir=%buildroot \
	--with-boost-lib=%_libdir \
	--docdir='$(datarootdir)/doc/$(package_name)-$(version)'
%make

%install
export PATH=$PATH:%_qt3dir/bin
%makeinstall_std
install -pDm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/*
%_datadir/%name/
%_desktopdir/*
%_man1dir/*
%doc Changelog README

%changelog
* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 0.4.5-alt2
- updated an Url:
- added watch file
- minor spec cleanup

* Sat Jan 07 2012 Michael Shigorin <mike@altlinux.org> 0.4.5-alt1
- 0.4.5 (closes: #26784)

* Fri Jul 24 2009 Michael Shigorin <mike@altlinux.org> 0.4.3-alt2
- fixed broken desktop file (repocop)

* Wed Jul 22 2009 Michael Shigorin <mike@altlinux.org> 0.4.3-alt1
- 0.4.3 (closes: #20846)
  + fixes hordes of security vulnerabilities in xpdf-derived JBIG2 code:
    CVE-2009-0146, CVE-2009-0147, CVE-2009-0166, CVE-2009-0799,
    CVE-2009-0800, CVE-2009-1179, CVE-2009-1180, CVE-2009-1181,
    CVE-2009-1182, CVE-2009-1183, CVE-2009-1187, CVE-2009-1188
  + thanks crux@ for prompt notification

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 0.4.2-alt1
- 0.4.2
  + removed patch1: broke
  + removed patch2: already applied

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 0.4.1-alt5
- applied repocop patch

* Wed Oct 15 2008 Michael Shigorin <mike@altlinux.org> 0.4.1-alt4
- Fixed build with newer boost (php-coder@; thanks a lot)

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt3.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for pdfedit

* Mon Mar 10 2008 Michael Shigorin <mike@altlinux.org> 0.4.1-alt3
- replaced Damir's subst with a patch proposed by 
  Michal Hocko <mstsxfx/gmail>

* Thu Mar 06 2008 Michael Shigorin <mike@altlinux.org> 0.4.1-alt2
- fixed x86_64 build, thanks damir@

* Wed Feb 27 2008 Michael Shigorin <mike@altlinux.org> 0.4.1-alt1
- 0.4.1
- added fontpath patch; thanks Slava Dikonov (slava@) for investigation:
  https://bugzilla.altlinux.org/show_bug.cgi?id=13473#c3
- danced with installation the other way around
- spec cleanup

* Wed Nov 28 2007 Michael Shigorin <mike@altlinux.org> 0.3.2-alt1
- 0.3.2 (now should actually work, see #13473)

* Mon Mar 19 2007 Michael Shigorin <mike@altlinux.org> 0.2.5-alt1
- built for ALT Linux
- desktop file and package description borrowed from Debian
- huge thanks to zerg@ and wrar@ for undocumented qmake hint
