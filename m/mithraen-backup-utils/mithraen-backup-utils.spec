Name: mithraen-backup-utils
Summary: Simple utilites for more easy backup used by Mithraen
Version: 0.1
Release: alt2
License: GPL
Group: Archiving/Backup

Obsoletes: seiros-backup-utils

BuildArch: noarch

BuildRequires: git-core

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

%description
%summary

%prep
%setup
%install
%makeinstall install

%files
%dir %_datadir/%name
%_bindir/gitbackup
%_datadir/%name/functions
%changelog
* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt2
- auto rebuild

* Sat Aug 29 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- first build for Sisyphus
