Name: enconvmv
Version: 0.2.0
Release: alt1

Summary: convmv meets enca
License: GPL
Group: File tools

Source: enconvmv.sh
Packager: Michael Shigorin <mike@altlinux.org>
Requires: enca
BuildArch: noarch

%description
This is a script to traverse a directory tree and convert
file and directory names to target charset, auto-guessing
source charset given the language.

If no target language and charset are given, then they're
assumed based on current locale.

If lynx(1) is present, transliteration is also possible.

WARNING: it's not as thorough as convmv, rather a sample
which ought to be merged there (but worked for me).

NOTE: you can back up filenames with cp -al easily, do it!

%install
install -pDm755 %SOURCE0 %buildroot%_bindir/%name

%files
%_bindir/*

%changelog
* Fri Jun 10 2011 Michael Shigorin <mike@altlinux.org> 0.2.0-alt1
- merged george@'s patch for translit support (closes: #25741)
- rewrote directory traversal routine (seems to still work)
- tweaked error handling and reporting
- misc cleanups

* Sat Mar 10 2007 Michael Shigorin <mike@altlinux.org> 0.1.6-alt2
- noarch

* Sat Mar 10 2007 Michael Shigorin <mike@altlinux.org> 0.1.6-alt1
- added another one-liner by svd@ to avoid traversing symlinks
  (proper handling of symlinks is an open task though
  but this time better safe than sorry)

* Thu Mar 08 2007 Michael Shigorin <mike@altlinux.org> 0.1.5-alt1
- added patch by Sviatoslav Sviridov (svd@) to fix forkbomb
  possibility when processing partially inaccessible directory
  tree (fixes #11009)

* Tue Oct 17 2006 Michael Shigorin <mike@altlinux.org> 0.1.4-alt1
- don't silence enca's warnings

* Tue Oct 17 2006 Michael Shigorin <mike@altlinux.org> 0.1.3-alt1
- worked around getopt with "." as the last argument

* Tue Oct 17 2006 Michael Shigorin <mike@altlinux.org> 0.1.2-alt1
- fixed typo
- added another new name sanity check

* Tue Oct 17 2006 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- added forgotten --help
- fixed usage() usage

* Tue Oct 17 2006 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- added enca req

* Tue Oct 17 2006 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

