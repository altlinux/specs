Name: open-ovf
Version: 0.1
Release: alt1
Summary: Tool for importing and exporting OVF
Url: http://open-ovf.wiki.sourceforge.net/
License: EPL
Group: System/Configuration/Other
Source0: %name-%version.tar.bz2
Source1: README.SuSE
Patch0: output-libvirtxml-file.patch
Patch1: xenfv-libvirtxml.patch
Patch2: use-before-define.patch
Patch3: libvirt-clock.patch
Patch4: python2.6.patch
Patch5: help.patch
Patch6: OvfSet-init.patch
Patch7: ova.patch
Patch8: xenpv-libvirtxml.patch
Patch9: lsovf.patch
Patch10: rmovf.patch
Patch11: chovf.patch
Patch12: ova-unpack.patch

BuildRequires: python-module-distribute
BuildArch: noarch

%description
Open-OVF project is an open source library and tools designed to promote
adoption of the OVF (Open Virtual Machine Format) specification as an
industry standard.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
%python_build

%install
%python_install


%files
%doc README LICENSE CONTRIBUTING examples extras schemas
%_bindir/*
%python_sitelibdir_noarch/ovf
%python_sitelibdir_noarch/open_ovf*

%changelog
* Mon Dec 10 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1-alt1
- Update spec for ALT

* Tue Apr  6 2010 jfehlig@novell.com
- Fix unpacking ova that contains absolute paths in file references
  bnc#590221
  ova-unpack.patch
* Tue Nov 10 2009 jfehlig@novell.com
- Changed lsovf, chovf, and rmovf to use common cli class
  instead of OptionsParser
- Fixed help of lsovf, chovf, rmovf, and ova commands
* Fri Nov  6 2009 jfehlig@novell.com
- Improved help by adding '<cmd> --help <subcmd>'
- Fixed disk device creation for xenpv appliances
- Improved README.SuSE
* Thu Nov  5 2009 jfehlig@novell.com
- spec file: conditionally specify noarch
* Tue Nov  3 2009 jfehlig@novell.com
- Fix mkovf help
  mkovf-help.patch
- Refactor OvfSet init code
  OvfSet-init.patch
- Fix ova command
  ova.patch
* Thu Oct 22 2009 jfehlig@novell.com
- spec file cleanup
* Wed Jul 22 2009 jfehlig@novell.com
- Initial packaging of open-ovf, FATE #303038
