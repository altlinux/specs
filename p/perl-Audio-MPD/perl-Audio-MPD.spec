%define dist Audio-MPD
Name: perl-%dist
Version: 1.112670
Release: alt1

Summary: Class to talk to MPD (Music Player Daemon) servers
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/J/JQ/JQUELIN/Audio-MPD-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Apr 25 2011
BuildRequires: perl-Audio-MPD-Common perl-DBM perl-Getopt-Euclid perl-Module-Build perl-MooseX-SemiAffordanceAccessor perl-Proc-Daemon

%description
Audio::MPD gives a clear object-oriented interface for talking to and
controlling MPD (Music Player Daemon) servers. A connection to the MPD
server is established as soon as a new Audio::MPD object is created.

%prep
%setup -n %dist-%version

%build
# launches mpd
%def_without test

%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%doc AUTHORS Changes README
%perl_vendor_privlib/Audio
%_bindir/mpd-*
%_man1dir/mpd-*

%changelog
* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.112670-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.111200-alt1
- automated CPAN update

* Mon Apr 25 2011 Alexey Tourbin <at@altlinux.ru> 1.110560-alt1
- 0.19.4 -> 1.110560

* Sun Oct 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.19.4-alt1
- initial build
