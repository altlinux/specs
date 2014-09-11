Name: modplugtools
Version: 0.5.3
Release: alt1

Summary: Command line mod music players
License: GPLv3
Group: Sound

Url: http://modplug-xmms.sourceforge.net/
Source: http://download.sourceforge.net/modplug-xmms/%name-%version.tar.gz
# Make modplugplay more likely to work out of the box (not for upstream)
Patch1: %name-0.5.0-modplugplay-aoss.patch
# http://sf.net/tracker/?func=detail&aid=3019146&group_id=1275&atid=301275
Patch2: 0001-Remove-unused-s-from-modplugplay-output-status-forma.patch

BuildRequires: libmodplug-devel
BuildRequires: libao-devel >= 0.8.0

%description
Olivier Lapicque, writer of ModPlug (the BEST mod-like music
player out there), sent me his mod rendering code, under the GPL,
in early December. Seeing as how the current version of ModPlug
for Linux was rather outdated and had no GUI, I took it upon
myself to make ModPlug into an XMMS Plugin. For those who don't
know, XMMS is a music player for Unix-like operating systems
which resembles WinAmp, exept that it looks nicer.

%prep
%setup
%patch1 -p1
%patch2 -p2

%build
%configure --disable-silent-rules
%make_build -C mp123

%install
%makeinstall_std -C mp123

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%_bindir/modplug123

%changelog
* Thu Sep 11 2014 Michael Shigorin <mike@altlinux.org> 0.5.3-alt1
- initial build for ALT Linux Sisyphus (based on fedora's 0.5.3-8)
