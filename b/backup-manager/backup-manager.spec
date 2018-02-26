Name: backup-manager
Summary: Versatile Command Line Backup Tool
Version: 0.7.9
Release: alt2.1
License: GPL
Group: System/Servers
BuildArch: noarch
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar
Url: http://www.backup-manager.org/
BuildRequires: perl-podlators

%description
%summary

%prep
%setup

%build
make
%install
%makeinstall_std
install -D -m 0600 backup-manager.conf.tpl %buildroot/etc/backup-manager.conf

%files
%config(noreplace) /etc/backup-manager.conf

%dir %perl_vendor_privlib/BackupManager
%dir %_datadir/%name
%dir %_datadir/%name/contrib
%_sbindir/backup-manager
%_bindir/backup-manager-purge
%_bindir/backup-manager-upload
%perl_vendor_privlib/BackupManager/Config.pm
%perl_vendor_privlib/BackupManager/Dialog.pm
%perl_vendor_privlib/BackupManager/Logger.pm
%_datadir/backup-manager/actions.sh
%_datadir/backup-manager/backup-manager.conf.tpl
%_datadir/backup-manager/backup-methods.sh
%_datadir/backup-manager/burning-methods.sh
%_datadir/backup-manager/contrib/sanitize.sh
%_datadir/backup-manager/contrib/upgrade-conffile.sh
%_datadir/backup-manager/dbus.sh
%_datadir/backup-manager/dialog.sh
%_datadir/backup-manager/externals.sh
%_datadir/backup-manager/files.sh
%_datadir/backup-manager/gettext-dummy.sh
%_datadir/backup-manager/gettext-real.sh
%_datadir/backup-manager/gettext.sh
%_datadir/backup-manager/logger.sh
%_datadir/backup-manager/md5sum.sh
%_datadir/backup-manager/sanitize.sh
%_datadir/backup-manager/upload-methods.sh
%_datadir/locale/cs/LC_MESSAGES/backup-manager.mo
%_datadir/locale/de/LC_MESSAGES/backup-manager.mo
%_datadir/locale/es/LC_MESSAGES/backup-manager.mo
%_datadir/locale/fr/LC_MESSAGES/backup-manager.mo
%_datadir/locale/it/LC_MESSAGES/backup-manager.mo
%_datadir/locale/nl/LC_MESSAGES/backup-manager.mo
%_datadir/locale/vi/LC_MESSAGES/backup-manager.mo
%_man8dir/backup-manager-purge.8.gz
%_man8dir/backup-manager-upload.8.gz
%_man8dir/backup-manager.8.gz

%changelog
* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.7.9-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Jul 12 2010 Denis Smirnov <mithraen@altlinux.ru> 0.7.9-alt2
- add directories to files section

* Sun Jul 11 2010 Denis Smirnov <mithraen@altlinux.ru> 0.7.9-alt1
- first build for Sisyphus
