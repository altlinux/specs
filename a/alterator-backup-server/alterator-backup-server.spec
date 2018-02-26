Name: alterator-backup-server
Version: 0.2
Release: alt1

Summary: Backup server management for plain distros
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
BuildRequires: alterator-distro-backup-server
Requires: alterator-distro-backup-server
Source: %name-%version.tar

%description
Contains desktop files to bridge alterator-ditro-backup-server to
plain distros

%prep
%setup

%install
%define altdir %_datadir/alterator
mkdir -p %buildroot/%altdir/{applications,desktop-directories}
install -m644 *directory %buildroot/%altdir/desktop-directories/

for n in archive director clients schedule; do
   sed 's/X-Backup-Server/X-Alterator-Backup/' \
      %altdir/applications/backup_server_$n.desktop \
      > %buildroot/%altdir/applications/bacula-$n.desktop
done


%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*
%altdir/applications/*
%altdir/desktop-directories/*

%changelog
* Thu Feb 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- hide local-backup

* Wed Feb 09 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial state



