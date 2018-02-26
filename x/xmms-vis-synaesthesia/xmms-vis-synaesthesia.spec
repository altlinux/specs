Name: xmms-vis-synaesthesia
Version: 0.0.3
Release: alt4

Summary: Synaesthesia for xmms
License: GPL v2+
Group: Sound

Url: http://zinx.xmms.org/xmms
Source0: %url/synaesthesia-xmms-%version-rc3.tar.gz
Patch0: %url/xmms-synaesthesia-hide-on-stop.patch
Patch1: xmms-synaesthesia-0.0.3_rc3-gcc34.patch
Patch2: xmms-synaesthesia-0.0.3_rc3-amd64.patch
Patch3: xmms-synaesthesia-open-window.patch

Summary(pl): Synaesthesia dla xmms

# Automatically added by buildreq on Mon Sep 28 2009
BuildRequires: libxmms-devel

%description
Synaesthesia port for xmms

%description -l pl
Port Synaesthesii dla xmms

%prep
%setup -n synaesthesia-xmms-%version-rc3
#patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1

%build
%autoreconf
%configure
%make

%install
%makeinstall_std

%files
%doc AUTHORS NEWS README
%xmms_visualizationdir/*

%changelog
* Sun Jan 30 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.0.3-alt4
- Increase data buffer
- Fix window resizing

* Mon Sep 28 2009 Michael Shigorin <mike@altlinux.org> 0.0.3-alt3
- x86_64 build fix (following proposal by ldv@)
- buildreq && minor spec cleanup
- NB: patch2 is needed on i586 too AAMOF

* Mon Jun 26 2006 Michael Shigorin <mike@altlinux.org> 0.0.3-alt2
- no more autoreconf
- patch0 conflicts with patch2, commented out for now
  (that is, trade in hide-on-stop for amd64)
- volunteers to update it to Synaesthesia 2.4 wanted!

* Sun Dec 11 2005 Michael Shigorin <mike@altlinux.org> 0.0.3-alt1
- built for ALT Linux (again)
- these PLD people worked on it (PLD Team <feedback@pld-linux.org>):
  blues, grzegol, juandon, kloczek, malekith, misi3k, qboosh, wolf
- spec cleanup
- updated package Url
- added "hide on stop" patch by Robert Macomber
- added Gentoo patches (gcc34, amd64[-])
- WARNING: fullscreen is broken for me! (hide patch doesn't matter)
