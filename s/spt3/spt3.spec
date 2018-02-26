Name: spt3
Version: 0.5
Release: alt2
Group: Development/Other
Summary: Tools for creating Sisyphus-based solutions
License: GPL
Packager: Mikhail Yakshin <greycat@altlinux.org>
Source: %name-%version.tar.bz2
BuildArch: noarch

# Self dependencies
Requires: %name-profiles = %version-%release
Requires: %name-tasks = %version-%release

%package profiles
Summary: Sample profiles for %name
Group: Development/Other

%package tasks
Summary: Low-level tasks of %name
Group: Development/Other

# Because of obsoleted --save-fakeroot
Requires: hasher >= 1.0.35-alt1
Requires: hasher-priv >= 1.2.2-alt1

# Because of isolinux-config
# (required in repository, not in host system)
# Requires: syslinux >= 3.31-alt1

%description
Tools for creating solutions (live CDs/DVDs, installable systems,
network boot clients, OpenVZ images, rescue discs, etc) based on
Sisyphus open-source package repository.

%name is a complete package that includes everything.

%description profiles
Sample profiles for %name (high-level instructions on how to build a
particular Sisyphus-based system or solution).

You'll require %name package to run these profiles.

%description tasks
Low-level tasks are basic building blocks for %name build process. Each
task has a clearly defined interface: function, input and output. Tasks
can be combined using profiles (see %name-profiles package for sample
profiles) to achieve building complete solutions.

To get generic high-level runner for these tasks and to get
documentation, install %name. For sample profiles, install
%name-profiles.

%prep
%setup

%build
mv bin/spt bin/spt3

%install
mkdir -p %buildroot{%_datadir/%name,%_bindir}
cp -a share/* %buildroot%_datadir/%name
install -m755 bin/* %buildroot%_bindir

%files
%_bindir/spt3
%_bindir/spt-deploy-*
%doc doc/*

%files profiles
%doc profiles

%files tasks
%_bindir/spt-boot-*
%_bindir/spt-clean
%_bindir/spt-create-repo
%_bindir/spt-*-chroot
%_bindir/spt-pack-*
%_bindir/spt-run-scripts
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Sat May 23 2009 Mikhail Yakshin <greycat@altlinux.org> 0.5-alt2
- Added some sanity checks

* Tue Jul 01 2008 Mikhail Yakshin <greycat@altlinux.ru> 0.5-alt1
- Added spt-copy-files-* tasks
- spt-pack-iso: added sort option
- Synchronized tasks with modern Sisyphus / branch 4.0

* Wed Apr 04 2007 Mikhail Yakshin <greycat@altlinux.ru> 0.4-alt1
- Added spt-pack-cpio (thanks to stanv@)
- Added --debug|-d option
- Minor fixes

* Sun Mar 18 2007 Fr. Br. George <george@altlinux.ru> 0.3-alt1.01
- Some usability hacks

* Fri Feb 02 2007 Mikhail Yakshin <greycat@altlinux.org> 0.3-alt1
- Separated spt3 into 3 packages (proposed by mithraen@)
- Added new gfxboot code by zerg@

* Mon Jan 29 2007 Mikhail Yakshin <greycat@altlinux.org> 0.2-alt1
- Updated to work with modern Sisyphus packages
- Fixed numerous issues
- Added sample profile with "manual installer livecd"
- Updated documentation

* Fri Jan 19 2007 Denis Pynkin <dans@altlinux.ru> 0.1-alt7.1
- fixed bug 10687
- removed obsoleted option "--save-fakeroot" for hsh-install
- in 'spt-make-chroot' script added ability to use a list of
  files in $profile/ directory. The packages list in a single
  $profile file is also supported.

* Thu Jan 18 2007 Mikhail Yakshin <greycat@altlinux.org> 0.1-alt7
- Fixed conflict with "spt" package, renamed main binary to "spt3"
- spt_dir environment variable can be used to redefine location of
  /usr/share/spt3
- All scripts use heavier error checking and unified chroot exec
  function (fixes #10313)
- Runner script "spt3" now reports line numbers, not step numbers
- Mandatory creation of /dev/console while doing chroot init
- Fixed propagator booting to current one
- Fixed isolinux config generation to create default kernel symlinks

* Wed Nov 08 2006 Mikhail Yakshin <greycat@altlinux.ru> 0.1-alt6
- Added lilo deployment
- Added tarball packing

* Fri Nov 03 2006 Denis Pynkin <dans@altlinux.ru> 0.1-alt5
- Fixed bugs: 10193,10194,10195
- Added multikernel booting
- Kernel entries in isolinux.cfg are created dynamically
- added copy of menu.c32 into live-cd

* Thu Oct 19 2006 Mikhail Yakshin <greycat@altlinux.ru> 0.1-alt4
- Added installer repositories creation
- Added "spt" tool to run recipe

* Wed Oct 18 2006 Mikhail Yakshin <greycat@altlinux.ru> 0.1-alt3
- More installer profile fixes
- Added preliminary spt-create-repo

* Mon Oct 16 2006 Mikhail Yakshin <greycat@altlinux.ru> 0.1-alt2
- Installer profile fixes

* Tue Oct 10 2006 Mikhail Yakshin <greycat@altlinux.ru> 0.1-alt1
- Initial build

