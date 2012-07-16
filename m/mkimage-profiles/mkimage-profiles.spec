Name: mkimage-profiles
Version: 0.7.4
Release: alt1

Summary: ALT Linux based distribution metaprofile
License: GPLv2+
Group: Development/Other

Url: http://www.altlinux.org/Mkimage/Profiles/m-p
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
Requires: rsync git-core
Requires: time schedutils
Requires: mkimage >= 0.2.0

# Recommends: graphviz

%define mpdir %_datadir/%name
%add_findreq_skiplist %mpdir/*.in/*

%description
mkimage-profiles is a collection of bits and pieces useful for
distributions construction: it contains package lists, features,
and whole subprofiles (like "rescue" building block) for you
to choose from, and some ready-made image recipes as well.

Make no mistake: constructing distributions isn't just fun, it takes
a lot of passion and knowledge to produce a non-trivial one.  So m-p
(the short nick for mkimage-profiles) is complex too.  If you need
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

%prep
%setup

%build

%install
mkdir -p %buildroot%mpdir
cp -a * %buildroot%mpdir

%files
%mpdir/
%doc doc/
%doc README QUICKSTART

%changelog
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
