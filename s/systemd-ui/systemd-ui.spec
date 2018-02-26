
Name: systemd-ui
Url: http://www.freedesktop.org/wiki/Software/systemd
Version: 1
Release: alt1
License: GPLv2+
Group: System/Configuration/Other
Summary: Graphical front-end for systemd
Source: %name-%version.tar
BuildRequires: libdbus-devel >= 1.3.2
BuildRequires: libgtk+2-devel libgee-devel
BuildRequires: glib2-devel >= 2.26 libgio-devel
BuildRequires: libnotify-devel
BuildRequires: vala >= 0.10
BuildRequires: desktop-file-utils
BuildRequires: xsltproc docbook-style-xsl
Requires: systemd >= 183-alt1
Obsoletes: systemd-gtk < 45
Provides: systemd-gtk = 45-alt1

%description
Graphical front-end for systemd. It provides a simple user interface to manage
services, and a graphical agent to request passwords from the user.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

desktop-file-install --delete-original  \
  --dir=%buildroot%_datadir/applications \
  %buildroot%_datadir/applications/systemadm.desktop

%files
%_bindir/systemadm
%_bindir/systemd-gnome-ask-password-agent
%_datadir/applications/systemadm.desktop
%_man1dir/systemadm.*

%changelog
* Mon Jun 04 2012 Alexey Shabalin <shaba@altlinux.ru> 1-alt1
- initial release after split-off from systemd package
