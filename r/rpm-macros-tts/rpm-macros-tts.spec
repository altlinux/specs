Name: rpm-macros-tts
Version: 20110208
Release: alt1
Packager: Michael Pozhidaev <msp@altlinux.ru>
BuildArch: noarch
Requires: rpm
Provides: tts-devel

Summary: RPM macros for speech synthesis engines
Group: System/Configuration/Other
License: GPL

Source: %name-%version.tar

%description
This package contains RPM settings for building packages 
with different TTS engines. 

%prep
%setup -q
%build

%install
%__install -pD -m644 tts %buildroot%_rpmmacrosdir/tts

%files
%_rpmmacrosdir/*

%changelog
* Tue Feb 08 2011 Michael Pozhidaev <msp@altlinux.ru> 20110208-alt1
- Added tts_unregister macro

* Fri Feb 04 2011 Michael Pozhidaev <msp@altlinux.ru> 20110204-alt1
- Package renamed to rpm-macros-tts

* Sun Dec 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 20080806-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * altlinux-policy-rpm-macros-packaging for tts-devel
  * postclean-05-filetriggers for spec file

* Wed Aug 06 2008 Michael Pozhidaev <msp@altlinux.ru> 20080806-alt1
- Initial RPM

