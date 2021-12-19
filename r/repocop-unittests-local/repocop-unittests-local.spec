Name: repocop-unittests-local
Version: 0.04
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: ALT Linux default set of pacakge tests for repocop test platform.
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 

Requires: repocop > 0.76
Requires: repocop-unittest-alt-alternatives-xml
Requires: repocop-unittest-alt-desktop-iconsdir
Requires: repocop-unittest-altlinux-find-lang
Requires: repocop-unittest-altlinux-java
Requires: repocop-unittest-altlinux-policy
Requires: repocop-unittest-altlinux-python
Requires: repocop-unittest-bin-permissions
Requires: repocop-unittest-buildreq
Requires: repocop-unittest-buildroot >= 0.04
Requires: repocop-unittest-checkbashisms
Requires: repocop-unittest-docdir-is-not-owned
Requires: repocop-unittest-fonts.alias
Requires: repocop-unittest-freedesktop
Requires: repocop-unittest-init-but-no-native-systemd
Requires: repocop-unittest-init-condrestart
Requires: repocop-unittest-init-lsb
Requires: repocop-unittest-init-x-functions
Requires: repocop-unittest-library-pkgnames >= 0.04
Requires: repocop-unittest-lintian-noncollectors >= 0.11
Requires: repocop-unittest-rpm-filetriggers >= 0.06
Requires: repocop-unittest-rpm-recursive-symlink
Requires: repocop-unittest-rpm-tags
Requires: repocop-unittest-subdirs-in-usr-games
Requires: repocop-unittest-systemd
# deprecated
#Requires: repocop-unittest-systemd-but-no-native-init
## NO MORE
##Requires: repocop-unittest-spec-has-obsolete-macroses
##Requires: repocop-unittest-spec-missing-packager

Requires: repocop-unittest-unsafe-tmp-usage-in-scripts

# distrotests
#Requires: repocop-unittest-alt-alternatives-master-slave-conflict
#Requires: repocop-unittest-alt-alternatives-vs-filesystem
#Requires: repocop-unittest-alt-alternatives-vs-ghost
#Requires: repocop-unittest-unmet-dependency
#Requires: repocop-unittest-rpm-filesystem

# moved to distribution tests
# Requires: repocop-unittest-sisyphus_check-check-dirlist

# Igor Zubkov tests
Requires: repocop-unittest-big-changelog
Requires: repocop-unittest-distribution-tag
Requires: repocop-unittest-invalid-url
Requires: repocop-unittest-missing-url
Requires: repocop-unittest-subdirs-in-usr-games
Requires: repocop-unittest-uncompressed-infos
Requires: repocop-unittest-uncompressed-manpages
Requires: repocop-unittest-vendor-tag
# seems to conflict with ALT Linux traditions;
# needs discussion to bring Games Packaging Policy
Conflicts: repocop-unittest-package-installs-file-to-usr-games

%description
Default set of repocop integration tests for ALT Linux.
It is the metapackage that requires all the recommended tests.

%prep

%build
%install
mkdir -p $RPM_BUILD_ROOT

%files

%changelog
* Sun Dec 19 2021 Igor Vlasenko <viy@altlinux.org> 0.04-alt1
- removed repocop-unittest-systemd-but-no-native-init

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added repocop-unittest-systemd-but-no-native-init

* Tue Apr 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added repocop-unittest-systemd

* Wed Aug 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first build
