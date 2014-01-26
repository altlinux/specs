Name: rinse
Version: 0
Release: alt0.1
Summary: A collection of scripts for working with Xen guest images
License: GPLv2
Group: System/Base
URL: https://gitorious.org/%name
Source: %name.tar
BuildArch: noarch

BuildRequires: perl-podlators
BuildRequires: perl(Encode.pm) perl(HTTP/Date.pm) perl(HTTP/Message.pm)
BuildRequires: perl(Pod/Escapes.pm) perl(Pod/Simple.pm) perl(Pod/Usage.pm)
BuildRequires: perl(URI.pm) perl(LWP/UserAgent.pm)

%description
%name contains a collection of Perl scripts for working with Xen guest images
under Linux.
Using this software, you can easily create new Xen guests configured to be
accessible over the network via OpenSSH.
xen-tools currently has scripts to install most releases of Debian and Ubuntu and
some RPM-based distributions.


%prep
%setup -q -n %name

sed -i 's|/usr/lib\(/%name/\)|%_datadir\1|g' Makefile bin/%name


%build


%install
%make_install PREFIX=%buildroot install


%files
%doc BUGS README
%_sysconfdir/bash_completion.d
%config(noreplace) %_sysconfdir/%name
%_prefix/lib/*
%_sbindir/*
%_man8dir/*
%_datadir/%name


%changelog
* Sun Jan 26 2014 Led <led@altlinux.ru> 0-alt0.1
- initial build
