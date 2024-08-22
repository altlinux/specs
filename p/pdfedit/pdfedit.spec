Name: pdfedit
Version: 0.4.5
Release: alt6

Summary: Editor for manipulating PDF documents
License: GPLv2
Group: File tools

Url: http://pdfedit.cz
Source0: %name-%version.tar.bz2
Source1: %name.desktop
Source100: %name.watch
Patch0: pdfedit-0.4.1-alt-fontpath.patch
Patch2: pdfedit-0.4.5-alt-docbook.patch
Patch3: pdfedit-0.4.5-alt-libpng15.patch
Patch5: pdfedit-0.4.5-format.patch
Patch6: pdfedit-0.4.5-alt-fixes.patch

Packager: Michael Shigorin <mike@altlinux.org>

Requires: fonts-type1-urw

# Automatically added by buildreq on Tue Apr 07 2009
BuildRequires: boost-devel gcc-c++ imake libqt3-devel t1lib-devel xorg-cf-files

BuildPreReq: /proc xsltproc docbook5-style-xsl
BuildPreReq: boost-program_options-devel libpng-devel

%{?!_desktopdir:%define _desktopdir %_datadir/applications}

%description
Complete editing of pdf documents is made possible with PDFedit.
You can change either raw pdf objects (for advanced users) or use
predefined gui functions. Functions can be easily added as everything
is based on a scripts.

Scripting is used to a great extent in editor and almost anything can
be scripted, it is possible to create own scripts or plugins.

%package manual
Summary: User manual for PDFedit
Group: Documentation
BuildArch: noarch

%description manual
Complete editing of pdf documents is made possible with PDFedit.
You can change either raw pdf objects (for advanced users) or use
predefined gui functions. Functions can be easily added as everything
is based on a scripts.

This package contains user manual for PDFedit.

%prep
%setup
%patch0 -p1
%patch2 -p2
%patch3 -p2
sed -i 's,bin/qmake,& "CONFIG+=no_fixpath",' src/Makefile
%patch5 -p1
%patch6 -p2
sed -i 's/-D_FORTIFY_SOURCE=2/-U_FORTIFY_SOURCE & -g -fpermissive/' configure.in
sed -i 's/-posix /-Wno-write-strings /' Makefile.flags.in
sed -i 's/-std=c++98/-std=c++11/' Makefile.flags.in
sed -i -E 's/(^|[^:/])(weak_ptr|shared_ptr)/\1boost::\2/g' \
	src/{kernel,gui,tools}/*.cc

%build
export PATH=$PATH:%_qt3dir/bin
cp -aLt . -- /usr/share/automake/config.{guess,sub}
# see README
autoreconf -fisv
%configure \
	--enable-stack-protector \
	--with-root-dir=%buildroot \
	--with-boost-lib=%_libdir \
	--docdir='$(datarootdir)/doc/$(package_name)-$(version)' \
	--with-boost-program-options=mt \
	--enable-user-manual \
	--enable-pdfedit-core-dev \
	--enable-tools
%make

%install
export PATH=$PATH:%_qt3dir/bin
%makeinstall_std
install -pDm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/*
%exclude %_bindir/pdfedit-core-dev-config
%_datadir/%name/
%_desktopdir/*
%_man1dir/*
%doc Changelog README

%files manual
%doc doc/user/OEBPS/*

%changelog
* Thu Aug 22 2024 Michael Shigorin <mike@altlinux.org> 0.4.5-alt6
- clarified License:

* Thu Aug 22 2024 Michael Shigorin <mike@altlinux.org> 0.4.5-alt5
- fixed build with ilyakurdyukov@'s patch instead

* Sat Oct 03 2015 Michael Shigorin <mike@altlinux.org> 0.4.5-alt4
- rebuilt against gcc5-built qt3

* Tue Jun 10 2014 Michael Shigorin <mike@altlinux.org> 0.4.5-alt3
- fixed build with fedora patches

* Tue Nov 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt2.1
- Fixed build
- Added user manual and tools

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
