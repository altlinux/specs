Name: xen-tools
Version: 4.4
Release: alt1
Summary: A collection of scripts for working with Xen guest images
License: GPLv2
Group: Emulators
URL: http://%name.org/software/%name
Source: %url/%name-%version.tar
Patch: %name-%version-%release.patch
BuildArch: noarch

BuildRequires: openssh-common
BuildRequires: perl(Data/Validate/URI.pm) perl(File/Slurp.pm) perl(File/Which.pm)
BuildRequires: perl(Term/UI.pm) perl(Text/Template.pm) perl-podlators

%description
%name contains a collection of Perl scripts for working with Xen guest images
under Linux.
Using this software, you can easily create new Xen guests configured to be
accessible over the network via OpenSSH.
xen-tools currently has scripts to install most releases of Debian and Ubuntu and
some RPM-based distributions.


%prep
%setup -q
%patch -p1


%build


%install
%makeinstall_std


%files
%doc AUTHORS LICENSE *.markdown
%_sysconfdir/bash_completion.d
%config(noreplace) %_sysconfdir/%name
%_bindir/*
%_man8dir/*
%_datadir/%name
%perl_vendor_privlib/*


%changelog
* Sun Jan 26 2014 Led <led@altlinux.ru> 4.4-alt1
- initial build
