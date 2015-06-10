Name: livecd-kde4-akonadi-sqlite
Version: 0.1
Release: alt1

Summary: Configure akonadi server for a livecd environment
License: Public domain
Group: Graphical desktop/KDE

Url: http://altlinux.org/m-p
Packager: Denis Pynkin <dans@altlinux.org>

BuildArch: noarch

Source0: akonadiserverrc

%description
%summary
Used sqlite DB instead MySQL.

%prep

%build

%install
install -pDm644 %SOURCE0 %buildroot/%_sysconfdir/skel/.config/akonadi/akonadiserverrc

%files
%_sysconfdir/skel/.config/akonadi/akonadiserverrc


%changelog
* Wed Jun 10 2015 Denis Pynkin <dans@altlinux.org> 0.1-alt1
- Added configuration for akonadi server with sqlite DB
