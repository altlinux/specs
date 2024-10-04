%def_disable    bootstrap
%define         short_version 0.1.9998
%define         svn_revision 3606

ExclusiveArch: %ix86 x86_64

Name:           kBuild
Version:        %short_version.r%svn_revision
Release:        alt1
License:        %gpl3plus
Group:          Development/Other
Summary:        A cross-platform build environment framework for complex tasks
Packager:       Evgeny Sinelnikov <sin@altlinux.ru>
Url:            http://svn.netlabs.org/kbuild

Source:         %name-%version.tar.bz2
Patch2:         kBuild-0.1.3-escape.patch
Patch3:         kBuild-alt-compat.patch
Patch4:         kBuild-use-bison.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires:  cvs flex libacl-devel
BuildRequires: perl-podlators

%if_disabled bootstrap
BuildRequires: kBuild
%endif

%description
This is a GNU make fork with a set of scripts to simplify
complex tasks and portable versions of various UNIX tools to
ensure cross-platform portability.

The goals of the kBuild framework:
- Similar behavior across all supported platforms
- Flexibility, don't create unnecessary restrictions preventing
  ad-hoc solutions
- Makefiles can be simple to write and maintain
- One configuration file for a subtree automatically included
- Target configuration templates as the primary mechanism for
  makefile simplification
- Tools and SDKs for helping out the templates with flexibility
- Non-recursive makefile method by using sub-makefiles

It is used mainly to build VirtualBox OSE packages for RPM Fusion
repository.

Authors:
--------
    Knut St. Osmundsen <bird-kbuild-spam@anduin.net>

%prep
%setup -q
%patch2 -p1
%patch3 -p2
%patch4 -p2
chmod a+x kBuild/env.sh
chmod a+x src/sed/configure

%build
%define bootstrap_mflags %_smp_mflags   \\\
        CFLAGS="%optflags"              \\\
        KBUILD_SVN_REV=%svn_revision    \\\
        KBUILD_VERBOSE=1

%define mflags %bootstrap_mflags        \\\
        NIX_INSTALL_DIR=%_prefix        \\\
        BUILD_TYPE=release              \\\
        MY_INST_MODE=0644               \\\
        MY_INST_BIN_MODE=0755

%if_enabled bootstrap
kBuild/env.sh --full make -f bootstrap.gmk %bootstrap_mflags
kBuild/env.sh kmk rebuild PATH_INS=`pwd` %mflags
%else
kBuild/env.sh kmk %mflags
%endif
pod2man -c 'kBuild for ALT Linux' -r %name-%version dist/debian/kmk.pod |sed -e 's/Debian/ALT Linux/' > kmk.1

%install
kBuild/env.sh kmk install PATH_INS=%buildroot %mflags
install -m 644 -D kmk.1 %buildroot%_man1dir/kmk.1


%files
%_docdir/%name-%short_version
%_bindir/*
%_man1dir/*
%_datadir/%name

%changelog
* Mon Sep 30 2024 Valery Sinelnikov <greh@altlinux.org> 0.1.9998.r3606-alt1
- Update to last unstable release from svn trunk (r3606)

* Thu Oct 19 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.9998.r3592-alt2.p10.1
- Backport new version to p10 branch

* Fri Jun 02 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.9998.r3592-alt3
- Removed use of rpm-build-ubt

* Thu Jun 01 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.9998.r3592-alt2
- Added to BuildRequires(pre): rpm-build-ubt

* Mon Apr 24 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.9998.r3592-alt1
- Update to last unstable release from svn trunk (r3592) with LIBSDL2 support

* Fri Apr 16 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.9998.r3493-alt5
- Update to last unstable release from svn trunk (r3493)
- Replace using of yacc with bison during building kash

* Mon Dec 03 2018 Evgeny Sinelnikov <sin@altlinux.org> 0.1.9998.r3178-alt4
- Disable ubt macros due binary package identity changes

* Wed Jul 11 2018 Evgeny Sinelnikov <sin@altlinux.org> 0.1.9998.r3178-alt3
- Exclusive build for x86 architectures only

* Thu May 24 2018 Evgeny Sinelnikov <sin@altlinux.org> 0.1.9998.r3178-alt2
- Fixed kBuild svn revision output for kmk --version detect

* Thu Mar 22 2018 Evgeny Sinelnikov <sin@altlinux.org> 0.1.9998.r3178-alt1
- Update to last unstable release from svn trunk (r3178) for VirtualBox-5.2.x

* Thu Feb 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.9998.r2813-alt2
- Fixed build with new toolchain.

* Wed Jul 27 2016 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.9998.r2813-alt1
- Update to last unstable release from svn trunk (r2813) with qt5 support
- Build with default gcc

* Wed Nov 20 2013 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.9998.r2694-alt1
- Update to last unstable release from svn trunk (r2694)
- Build with gcc-4.5 due kmk_sed support

* Thu Aug 09 2012 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.9998.r2578-alt1
- Update to last unstable release from svn trunk (r2578)
- Build without bootstrap

* Sun Oct 30 2011 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.9998.r2546-alt1
- Update to last unstable release from svn trunk (r2546)

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.1.5.r2373-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Mar 03 2010 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.5.r2373-alt1
- Update to last stable release - 0.1.5-p2 (r2373)

* Sun May 10 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.5.r2336-alt2
- Fix build for gcc-4.4
- Fix summary and description
- Add patches from Fedora
+ Fix typoes (Robert P. J. Day, RH#495393)
+ Comment out the colliding dprintf

* Fri May 08 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.5.r2336-alt1
- Update to last stable release - 0.1.5-p1 (r2336)

* Thu Jan 29 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.5.r2259-alt1
- Update to release
- Add QuickReference

* Mon Dec 22 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.5.r2108-alt2
- Fixed license to GPLv3 (thanks to vsu@)

* Mon Dec 22 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.5.r2108-alt1
- Update from svn

* Fri Nov 07 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.4.r1779-alt1
- Update to new release

* Fri Aug 29 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.3.r1651-alt1
- Initial ALTLinux Sisyphus release from builds for Suse
- Rename package to kBuild
