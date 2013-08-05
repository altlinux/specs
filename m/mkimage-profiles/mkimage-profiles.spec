Name: mkimage-profiles
Version: 1.1.5
Release: alt1

Summary: ALT Linux based distribution metaprofile
License: GPLv2+
Group: Development/Other

Url: http://altlinux.org/m-p
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
BuildRequires: rsync asciidoc-a2x xmlgraphics-fop fonts-ttf-dejavu
BuildRequires: /proc

Requires: rsync git-core
Requires: time schedutils sfdisk
Requires: mkimage >= 0.2.5

# Recommends: graphviz qemu-img

%define mpdir %_datadir/%name
%add_findreq_skiplist %mpdir/*.in/*

%define docs $HOME/docs

%package doc
Summary: %name documentation
Group: Development/Documentation

%description
mkimage-profiles is a collection of bits and pieces useful for
distributions construction: it contains package lists, features,
and whole subprofiles (like "rescue" building block) for you
to choose from, and some ready-made image recipes as well.

Make no mistake: constructing distributions isn't just fun, it takes
a lot of passion and knowledge to produce a non-trivial one.  So m-p
(the short alias for mkimage-profiles) is complex too.  If you need
-- or want -- to make just a few tweaks to an existing recipe, it might
be easier to comprehend the generated profile (aka builddir) which
contains only the needed subprofiles, script hooks and package lists
and is way more compact.

Virtual environment template caches (OpenVZ/LXC) can be made either.

In short, setup hasher (http://en.altlinux.org/hasher) and here we go:
  cd %mpdir
  head README
  make syslinux.iso

But if you're into regular distro hacking and are not afraid of make
and modest metaprogramming (some code generation and introspection),
welcome to the metaprofile itself; read the docs and get the git:
%url

%description doc
This package holds developer docs for %name
as a book in HTML and PDF formats.

%prep
%setup

%build
make BUILDDIR=%docs docs

%install
mkdir -p %buildroot%mpdir
cp -a * %buildroot%mpdir

%files
%mpdir/

%files doc
%doc README
%doc QUICKSTART
%doc %docs/*

%changelog
* Mon Aug 05 2013 Michael Shigorin <mike@altlinux.org> 1.1.5-alt1
- armh related fixes

* Mon Jul 29 2013 Michael Shigorin <mike@altlinux.org> 1.1.4-alt1
- assorted fixups

* Mon Jul 22 2013 Michael Shigorin <mike@altlinux.org> 1.1.3-alt1
- armh fixes and tweaks

* Mon Jul 15 2013 Michael Shigorin <mike@altlinux.org> 1.1.2-alt1
- control and sound features

* Mon Jul 01 2013 Michael Shigorin <mike@altlinux.org> 1.1.1-alt1
- cuboxism

* Mon Jun 17 2013 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1
- 1.1.x branch: public alpha development status
  + new subprofile: rootfs
  + new features: armh*, deflogin, init, services
  + refactored features: build-*, efi, fonts, live, x11*
  + tar2vm got rewritten as tar2fs, gained ARM support
- minor spec metadata update

* Mon Jun 17 2013 Michael Shigorin <mike@altlinux.org> 1.0.0-alt1
- 1.0

* Mon Jun 10 2013 Michael Shigorin <mike@altlinux.org> 0.9.16-alt1
- 1.0pre

* Mon May 27 2013 Michael Shigorin <mike@altlinux.org> 0.9.15-alt1
- +installer

* Mon May 20 2013 Michael Shigorin <mike@altlinux.org> 0.9.14-alt1
- more regular fixes

* Mon May 13 2013 Michael Shigorin <mike@altlinux.org> 0.9.13-alt1
- regular fixes

* Mon Apr 22 2013 Michael Shigorin <mike@altlinux.org> 0.9.12-alt1
- four weeks later...

* Mon Mar 25 2013 Michael Shigorin <mike@altlinux.org> 0.9.11-alt1
- persistent icewm

* Mon Mar 18 2013 Michael Shigorin <mike@altlinux.org> 0.9.10-alt1
- fonts: axios!

* Tue Feb 26 2013 Michael Shigorin <mike@altlinux.org> 0.9.9-alt1
- regular refactoring

* Tue Feb 19 2013 Michael Shigorin <mike@altlinux.org> 0.9.8.1-alt1
- works with make-initrd 0.8.1+ (see #28578)

* Mon Feb 18 2013 Michael Shigorin <mike@altlinux.org> 0.9.8-alt1
- live fixes/tweaks galore

* Mon Feb 11 2013 Michael Shigorin <mike@altlinux.org> 0.9.7-alt1
- going nightly

* Mon Feb 04 2013 Michael Shigorin <mike@altlinux.org> 0.9.6-alt1
- assorted fixes

* Mon Jan 21 2013 Michael Shigorin <mike@altlinux.org> 0.9.5-alt1
- homeros

* Mon Jan 14 2013 Michael Shigorin <mike@altlinux.org> 0.9.4-alt1
- restricted boot

* Mon Dec 31 2012 Michael Shigorin <mike@altlinux.org> 0.9.3-alt1
- regular images

* Mon Dec 17 2012 Michael Shigorin <mike@altlinux.org> 0.9.2-alt1
- enhanced uefi support

* Mon Dec 03 2012 Michael Shigorin <mike@altlinux.org> 0.9.1-alt1
- initial kde4 support

* Mon Nov 19 2012 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- initial uefi, luks, armh support
- enhanced arm, gnome3/systemd, vm support

* Sun Nov 11 2012 Michael Shigorin <mike@altlinux.org> 0.8.7-alt1
- regressions--

* Mon Nov 05 2012 Michael Shigorin <mike@altlinux.org> 0.8.6-alt1
- docs subpackage (HTML/PDF book)

* Mon Oct 29 2012 Michael Shigorin <mike@altlinux.org> 0.8.5-alt1
- diffable logs
- AMD APU support

* Tue Oct 16 2012 Michael Shigorin <mike@altlinux.org> 0.8.4-alt1
- worked around enhancements in current make-initrd-propagator
  (thus fixed live image boot, finally)

* Mon Oct 15 2012 Michael Shigorin <mike@altlinux.org> 0.8.3-alt1
- make-3.82 support
- fixed live image boot to some extent (see #27640, #27852)

* Mon Sep 24 2012 Michael Shigorin <mike@altlinux.org> 0.8.2-alt1
- fixed build with recent make-initrd-propagator

* Mon Sep 03 2012 Michael Shigorin <mike@altlinux.org> 0.8.1-alt1
- misc fixes

* Mon Aug 13 2012 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- stage2@live

* Mon Aug 06 2012 Michael Shigorin <mike@altlinux.org> 0.7.6-alt1
- minor improvements

* Mon Jul 30 2012 Michael Shigorin <mike@altlinux.org> 0.7.5-alt1
- a bunch of fixups and cleanups

* Mon Jul 16 2012 Michael Shigorin <mike@altlinux.org> 0.7.4-alt1
- ppc builds

* Mon Jul 09 2012 Michael Shigorin <mike@altlinux.org> 0.7.3-alt1
- arm builds

* Mon Jul 02 2012 Michael Shigorin <mike@altlinux.org> 0.7.2-alt1
- simply fixes

* Mon Jun 25 2012 Michael Shigorin <mike@altlinux.org> 0.7.1-alt1
- vm improvements and assorted tweaks/fixes

* Mon Jun 18 2012 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- new features:
  + initial build-vm
  + plymouth

* Mon May 28 2012 Michael Shigorin <mike@altlinux.org> 0.6.8-alt1
- minor bugfixes

* Mon May 21 2012 Michael Shigorin <mike@altlinux.org> 0.6.7-alt1
- docs updates

* Mon May 14 2012 Michael Shigorin <mike@altlinux.org> 0.6.6-alt1
- build helpers refactored
- initial frontend support

* Mon May 07 2012 Michael Shigorin <mike@altlinux.org> 0.6.5-alt1
- branding feature

* Mon Apr 23 2012 Michael Shigorin <mike@altlinux.org> 0.6.4-alt1
- simply better (tm)

* Mon Apr 09 2012 Michael Shigorin <mike@altlinux.org> 0.6.3-alt1
- massive squashfs tuning

* Mon Apr 02 2012 Michael Shigorin <mike@altlinux.org> 0.6.2-alt1
- better live-webkiosk and initial live-flightgear
- cleanup, syslinux, xorg feature tweaks

* Mon Mar 26 2012 Michael Shigorin <mike@altlinux.org> 0.6.1-alt1
- ISO9660 metadata support
- initial alien VE image

* Mon Mar 19 2012 Michael Shigorin <mike@altlinux.org> 0.6.0-alt1
- reports (targets graph)

* Mon Mar 12 2012 Michael Shigorin <mike@altlinux.org> 0.5.7-alt1
- distro tweaks

* Mon Feb 20 2012 Michael Shigorin <mike@altlinux.org> 0.5.6-alt1
- minor fixups

* Mon Feb 06 2012 Michael Shigorin <mike@altlinux.org> 0.5.5-alt1
- live-related tweaks (including live.hooks support)
- terminal server and webkiosk images

* Mon Jan 16 2012 Michael Shigorin <mike@altlinux.org> 0.5.4-alt1
- better diags for initial deployment

* Mon Jan 02 2012 Michael Shigorin <mike@altlinux.org> 0.5.3-alt1
- multi-target, multi-arch, single-job builds

* Mon Dec 19 2011 Michael Shigorin <mike@altlinux.org> 0.5.2-alt1
- THE_{KMODULES,PACKAGES,LISTS,GROUPS}
- incremental development, refactoring and bugfixing

* Fri Dec 02 2011 Michael Shigorin <mike@altlinux.org> 0.5.1-alt1
- generic VE archive type (added cpio and xz either)
- minor additions/fixes

* Mon Nov 21 2011 Michael Shigorin <mike@altlinux.org> 0.5.0-alt1
- add_feature for autoregistration (simple but invasive)
- added features: isomd5sum, repo, systemd
- changed features: powerbutton -> power

* Tue Nov 08 2011 Michael Shigorin <mike@altlinux.org> 0.4.3.2-alt1
- mkimage version required/checked

* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 0.4.3.1-alt1
- CLEAN by default unless DEBUG

* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 0.4.3-alt2
- include %mpdir/ itself as well

* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 0.4.3-alt1
- enhancements to logging
- NICE variable: employ nice(1) and ionice(1) if available
- features.in/syslinux: banner tweaked to include target name
- features.in/live: set up unicode locale/consolefont

* Wed Nov 02 2011 Michael Shigorin <mike@altlinux.org> 0.4.2-alt1
- initial package
