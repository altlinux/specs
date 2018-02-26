Name: kde-settings-kded-no_media_popup
Version: 3.5.8
Release: alt2

Summary: KDE settings to avoid popups on media detection
License: GPL
Group: Graphical desktop/KDE

Url: http://www.altlinux.org/LTSP
Source: %name.kdedrc
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
BuildRequires: kde-common-devel >= 0.3.1
Requires: kde-common >= 3.5

%description
Pre-packaged KDED settings to disable Media Notifier
(the media icon will still appear on desktop or in taskbar,
Media Manager configuration is not messed with)

%prep

%build

%install
install -pDm644 %SOURCE0 %buildroot/%_kdeconfdir/share/config/kdedrc

%files
%config(noreplace) %_kdeconfdir/share/config/kdedrc

%changelog
* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 3.5.8-alt2
- updated an Url:

* Wed Mar 12 2008 Michael Shigorin <mike@altlinux.org> 3.5.8-alt1
- initial release
