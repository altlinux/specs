%define _unpackaged_files_terminate_build 1
%define dist Audio-MPD
Name: perl-%dist
Version: 2.004
Release: alt3

Summary: Class to talk to MPD (Music Player Daemon) servers
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/J/JQ/JQUELIN/Audio-MPD-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Apr 25 2011
BuildRequires: perl-Audio-MPD-Common perl-DBM perl-Getopt-Euclid perl-Module-Build perl-MooseX-SemiAffordanceAccessor perl-Proc-Daemon perl(IO/Socket/IP.pm) perl(List/AllUtils.pm) perl(List/MoreUtils.pm)

%description
Audio::MPD gives a clear object-oriented interface for talking to and
controlling MPD (Music Player Daemon) servers. A connection to the MPD
server is established as soon as a new Audio::MPD object is created.

%prep
%setup -n %dist-%version

%build
# launches mpd
%def_without test

%perl_vendor_build
#--install_path bindoc=%_man1dir

%install
%perl_vendor_install

sed -i -e '1,4s,perl[0-9a-z\.]*,perl,' %buildroot%_bindir/*

%files
%doc AUTHORS Changes README
%perl_vendor_privlib/Audio
%_bindir/mpd-*
%_man1dir/mpd-*

%changelog
* Mon Feb 06 2017 Igor Vlasenko <viy@altlinux.ru> 2.004-alt3
- removed explicit perl version in bin

* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 2.004-alt2
- fixed build

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.004-alt1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.002-alt1
- automated CPAN update

* Mon Jun 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.000-alt1
- automated CPAN update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.120610-alt1
- automated CPAN update

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.112670-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.111200-alt1
- automated CPAN update

* Mon Apr 25 2011 Alexey Tourbin <at@altlinux.ru> 1.110560-alt1
- 0.19.4 -> 1.110560

* Sun Oct 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.19.4-alt1
- initial build
