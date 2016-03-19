%define _unpackaged_files_terminate_build 1
%define module_name Email-Folder

Name: perl-%module_name
Version: 0.860
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Read all the messages from a folder as Email::Simple objects
License: Perl
Group: Development/Perl

Url: %CPAN %module_name
Source: http://www.cpan.org/authors/id/P/PA/PALI/Email-Folder-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Feb 18 2010
BuildRequires: perl-Email-FolderType perl-Email-Simple perl-devel perl-parent perl(Capture/Tiny.pm)

%description
Read all the messages from a folder as Email::Simple objects.

%prep
%setup -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Email

%changelog
* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.860-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.859-alt1
- automated CPAN update

* Thu Jan 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.858-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.857-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.855-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Feb 18 2010 Victor Forsiuk <force@altlinux.org> 0.855-alt1
- Initial build.
