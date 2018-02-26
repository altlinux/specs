%define module ALTLinux-Girar-UploadMethod

Name: perl-%module
Version: 0.01
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for quering ALTLinux ACL files
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar
Url: http://search.cpan.org/dist/%module

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl(Pod/Usage.pm) perl-KyotoCabinet perl-IPC-Run3

%description
%summary

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
#doc Changes
#doc README
%perl_vendor_privlib/ALT*
#%_bindir/*

%changelog
* Fri Sep 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- new version
