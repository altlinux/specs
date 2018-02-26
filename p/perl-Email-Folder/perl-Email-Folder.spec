%define module_name Email-Folder

Name: perl-%module_name
Version: 0.855
Release: alt1.1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Read all the messages from a folder as Email::Simple objects
License: Perl
Group: Development/Perl

Url: %CPAN %module_name
Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Email-Folder-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Feb 18 2010
BuildRequires: perl-Email-FolderType perl-Email-Simple perl-devel

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
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.855-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Feb 18 2010 Victor Forsiuk <force@altlinux.org> 0.855-alt1
- Initial build.