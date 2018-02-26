Name: mkve
Version: 0.21
Release: alt1.1
Source: %name-%version.tar
Packager: Anton Protopopov <aspsk@altlinux.org>

Summary: Package for initial managing of virtual environments
License: GPL
Group: System/Configuration/Other
BuildArch: noarch

Requires: su
Requires: mkve-cache
Conflicts: ve-build-scripts

%description
Package for managing virtual environments, creating caches for such
environments.

%package cache
Summary: A tool to create caches for virtual environments
Group: System/Configuration/Other
BuildArch: noarch

%description cache
A tool to create caches for virtual environments

%prep
%setup -q

%install
%makeinstall

%files
%exclude %_bindir/mkve-cache
%exclude %_man1dir/mkve-cache*
%_datadir/%name
%_localstatedir/%name
%_bindir/*
%_man1dir/*

%files cache
%_bindir/mkve-cache
%_man1dir/mkve-cache*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.21-alt1.1
- Rebuild with Python-2.7

* Tue Feb 15 2011 Anton Protopopov <aspsk@altlinux.org> 0.21-alt1
- remove symlinks from /var/lib/vz/template/cache/ (ALT #23499)
- Setup absolute bundle path, check access (ALT #23498)
- don't remove innocent and defenceless machines

* Wed Jun 02 2010 Anton Protopopov <aspsk@altlinux.org> 0.20-alt4
- Merge with gears

* Wed Jun 02 2010 Anton Protopopov <aspsk@altlinux.org> 0.20-alt3
- Pull people/erthad/packages/mkve.git (ALT 23577)

* Wed Jun 02 2010 Timur Batyrshin <erthad@altlinux.org> 0.20-alt2
- split out mkve-cache into subpackage

* Thu Dec 03 2009 Eugeny A. Rostovtsev <real@altlinux.org> 0.20-alt1.1
- Rebuilt with python 2.6

* Fri Oct 02 2009 Anton Protopopov <aspsk@altlinux.org> 0.20-alt1
- mkve: skip empty lines when parsing ovz config

* Thu Sep 24 2009 Anton Protopopov <aspsk@altlinux.org> 0.19-alt1
- Use mkdir properly in mkve-sh-functions (ALT 20902)

* Thu Sep 17 2009 Anton Protopopov <aspsk@altlinux.org> 0.18-alt1
- Take memory from bundle if it is not given in option
- Add tools/ directory: /usr/share/mkve/tools
- Add new file: mkve-sh-functions (install in /usr/bin)
- Add new tools:
  - mkve-pack-kvm
  - mkve-pack-openvz
- Move mkve-config to tools/
- Add command pack to mkve: pack existing machines to bundles
- mkve: always use our own function system() instead of os.system()

* Mon Aug 24 2009 Anton Protopopov <aspsk@altlinux.org> 0.17-alt1
- mkve: add option --ovz-id (ALT 21024)
- mkve(qemu): use scsi instead of ide disks by default
- templates: presetup disk quotas

* Wed Jun 17 2009 Anton Protopopov <aspsk@altlinux.org> 0.16-alt1
- Add new option --vnc for create command
- mkve: show information about vnc display

* Mon Jun 15 2009 Anton Protopopov <aspsk@altlinux.org> 0.15-alt1
- Select disk bus type from metafile

* Mon Jun 08 2009 Anton Protopopov <aspsk@altlinux.org> 0.14-alt1
- mkve: new cooommand adopt

* Thu May 28 2009 Anton Protopopov <aspsk@altlinux.org> 0.13-alt1
- Append .bun suffix to $output of mkve-bundle
- Try to upload tun.ko module when starting a kvm machine
- Close #20208, #20209

* Wed May 27 2009 Anton Protopopov <aspsk@altlinux.org> 0.12-alt1
- mkve-templte: new options

* Mon May 18 2009 Anton Protopopov <aspsk@altlinux.org> 0.11-alt1
- bugfixes (#20043, #20042, #20045, #20046, #19840, #19958)

* Fri Apr 24 2009 Anton Protopopov <aspsk@altlinux.org> 0.10-alt1
- mkve: unlzma lzma'ed image
- mkve: tell if --kvm-bridge is absent/empty
- mkve: use option('kvm-memory') instead of get(..., 'memory')

* Tue Apr 21 2009 Anton Protopopov <aspsk@altlinux.org> 0.09-alt1
- remove --kvm-{disk,swap}-size options
- mkve: default dimension for memory is megabytes
- mkve: use --exclude <pattern> instead of -k
- new scheme of creating kvm machines
- new utility mkve-config: read and write config files
- mkve: use another scheme in kvm networking

* Fri Apr 03 2009 Anton Protopopov <aspsk@altlinux.org> 0.08-alt1
- fixes
- mvke-bundle: add logging (option --logfile)
- mkve-bundle: tar files in order corresponding to their sizes
- mkve-bundle: add "arch" field to bundle
- Add mkve-bundle.1
- Replace s/qemu/kvm/g
- You can set memory as <int>[MG] now

* Fri Mar 13 2009 Anton Protopopov <aspsk@altlinux.org> 0.08-alt0.1
- Update help for mkve-cache
- Introduce new routine: mkve-bundle
- Remove all templates except one
- mkve: add class InfoFile
- mkve: add class Error to Machine to replace die
- Use more verbose command when creating /dev/console
- mkve: remove __[un]lock functions
- mkve: don't create a network interface in openvz containers via veth_add
- mkve-template: new utility to create skeleton template
- goodbye, _vebuilder pseudouser
- mkve-cache: new option --hsh-workdir
- mkve: add a default IP address (192.0.2.$id) to new OpenVZ machine
- Add license/ and vendor/ to test template and to mkve-bundle
- Many removes of dead and dirty code
- Many small bugfixes
- Bugzilla
  * #19062
  * #18896
  * #19051
  * #19052

* Fri Dec 26 2008 Anton Protopopov <aspsk@altlinux.org> 0.07-alt1
- Update man page for mkve.1
- Add common options to mkve-cache

* Mon Nov 17 2008 Anton Protopopov <aspsk@altlinux.org> 0.06-alt1
  mkve changes:
  - Add command restart
  - Add command autostart
  - mkve info --ip-address
  - mkve info --start-on-boot
  - remove get and set; add option --root-password
  - add new virtual network, mkve-network, 192.0.2.1/24
  - change bridge name to mkvebr0
  - Say what logfile actually is
  - Ignore libvirt erors when undefying container
  - Make a mkve-network private
  - bugfixes
    * add logging of 'vzctl set ...' commands
    * check if machine is not running when stop it
    * check that option is absent before check that it is empty

* Thu Oct 09 2008 Anton Protopopov <aspsk@altlinux.org> 0.05-alt1
  Changes in templates:
  - Add alterator-{root,users,auth,net-eth} to packages lists

  mkve changes:
  - implemented possibility to create/destroy openvz machines
  - remove mkve-xml
  - remove old mkve, rename mkve-ctl to be new mkve
  - remove mkve-template
  - check and validate command line arguments
  - stop domain only if it is running
  - make --network argument optional and connect to bridge virbr1 instead
  - option --ssh-key instead of --no-ssh-key
  - add --help command
  - bugfixes

  mkve-cache changes:
  - remove -k,--key option
  - remove all short options except -z
  - use --hook instead of --hooks
  - option --create-fake-devices instead of --no-fake-devices
  - new options --command, --copy
  - update manual page more in a hsh-like style
  - bugfixes

* Tue Sep 16 2008 Anton Protopopov <aspsk@altlinux.org> 0.04-alt1
- global mv ovz -> openvz
- new utility, mkve-ctl, to replace mkve.
- clean spec, Makefile, man pages
- create XML description for libvirt
- add new options to mkve
- add new options to mkve-cache
- mkve-cache: install tar(1) and sed(1) if required

* Thu Sep 04 2008 Anton Protopopov <aspsk@altlinux.org> 0.03-alt1
- Rename (final, I hope) pack to mkve
- Rename all utilities
- New utility mkve-network
- New (workspace) utility mkve-xml
- Updated man pages

* Tue Jul 01 2008 Anton Protopopov <aspsk@altlinux.org> 0.02-alt1
- Implemented ve-machines(1) functionality

* Tue Jun 24 2008 Anton Protopopov <aspsk@altlinux.org> 0.01-alt1
- Rename package to ve-machines and change version
- add ve-machines utility
- ve-templates-cache: add option -z
- ve-templates: gzip some tarballs
  (depends on type of hypervisor)

* Fri Jun 20 2008 Anton Protopopov <aspsk@altlinux.org> 0.2-alt1
- The main change is the travel from mkimage to hasher and
  disabling most of the features of ve-templates-ctl,
  wich is now called ve-templates.

  New utillity, named ve-templates-cache, added.

* Tue Jun 10 2008 Anton Protopopov <aspsk@altlinux.org> 0.1-alt1
- Many changes were done:
  * New files layout
  * Assimilate files from spt-profiles
  * Add error reporting and logging
  * Add support for OpenVZ config files
  * Add support for adding/removing packages
  * Remove dependence on ve-build-scripts
  * Rewrite man-page

* Mon May 19 2008 Anton Protopopov <aspsk@altlinux.org> 0.1-alt0.1
- Initial build
