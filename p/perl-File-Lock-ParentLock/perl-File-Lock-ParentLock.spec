%define module File-Lock-ParentLock

Name: perl-%module
Version: 0.02
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for quering ALTLinux ACL files
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl(Pod/Usage.pm) perl-Proc-ProcessTable perl-podlators

%description
%summary

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
#doc Changes
#doc README
%perl_vendor_privlib/File*
%_bindir/*
%_man1dir/*

%changelog
* Wed Oct 12 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added man page

* Tue Oct 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- new version
