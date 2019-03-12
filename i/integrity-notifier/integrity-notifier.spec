Name:     integrity-notifier
Version:  0.5
Release:  alt1

Summary:  Integrity event notifier
License:  GPL v2+
Group:    Other
Url:      http://git.altlinux.org/people/nbr/packages/integrity-notifier.git

Packager: Denis Medvedev <nbr@altlinux.org>
BuildArch: noarch

Source:   %name-%version.tar


%description
Integrity violations happen when user starts damaged program.
This script notifies users and optionally admins about that.

%prep
%setup

%build

%install
mkdir -p  %buildroot/%_sysconfdir/integrity
mkdir -p  %buildroot/%_unitdir
cp notifier/* %buildroot/%_sysconfdir/integrity/
cp message %buildroot/%_sysconfdir/integrity/
cp unit/*  %buildroot/%_unitdir/

%files
%_sysconfdir/integrity/notifier.sh
%_sysconfdir/integrity/real_notify.sh
%_sysconfdir/integrity/message
%doc README

%changelog
* Tue Mar 12 2019 Denis Medvedev <nbr@altlinux.org> 0.5-alt1
Initial release.
