Name: parsecvs
Version: 0.1
Release: alt7

Summary: RCS ,v file parser and GIT import tool
License: GPLv2+
Group: Development/Other
URL: http://cgit.freedesktop.org/~krh/parsecvs/

Source: %name.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Thu Jun 19 2008
BuildRequires: flex libgit-devel libssl-devel zlib-devel

%description
This directory contains code which can directly read RCS ,v files and
generate a git-style rev-list structure from them. Revision lists can be
merged together to produce a composite revision history for an arbitrary
collection of files.

%prep
%setup -n %name
%patch -p1

%build
make GIT_LIBDIR=%_libdir GIT_INCLUDEDIR=%_includedir/git

%install
install -pD -m755 %name %buildroot%_bindir/%name

%files
%doc README
%_bindir/%name

%changelog
* Wed Apr 04 2012 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt7
- Updated to ef30dde (20090112).
- Fixed build with git>=1.7.9.

* Wed Sep 01 2010 Alexey I. Froloff <raorn@altlinux.org> 0.1-alt6
- Fixed build with git>=1.7.2.

* Sat Feb 07 2009 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt5
- Fixed build with git>=1.6.1.

* Sat Nov 01 2008 Sir Raorn <raorn@altlinux.ru> 0.1-alt4
- Replace obsolete "git-foo" invocations with modern "git foo"

* Fri Aug 15 2008 Sir Raorn <raorn@altlinux.ru> 0.1-alt3
- Do not inherit keyword substitution flags from previous file
- Slider-like progressbasr when parsing and saving files

* Thu Jun 19 2008 Alexey Tourbin <at@altlinux.ru> 0.1-alt2
- updated to 72db9019 (20080117)
- fixed git_mktag (#16051)

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.1-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Oct 21 2006 Alexey Tourbin <at@altlinux.ru> 0.1-alt1
- initial revision
- implemented object tags (instead of weak tags)
- implemented `-e CMD' option for custom changelog editor invocation;
  use `-e :' to keep changelogs intact
