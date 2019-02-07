%define _unpackaged_files_terminate_build 1
%define dist Test-Easy
Name: perl-%dist
Version: 1.11
Release: alt2

Summary: Testing made absolute easy.
License: GPL or Artistic
Group: Development/Perl
Packager: Boris Savelev <boris@altlinux.org>

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/B/BE/BELDEN/Test-Easy-%{version}.tar.gz
BuildArch: noarch

# Automatically added by buildreq on Mon Mar 16 2009
BuildRequires: perl-devel perl(Data/Denter.pm) perl(Data/Difflet.pm) perl(Hash/MostUtils.pm) perl(Functional/Utility.pm) perl(Test/Resub.pm)

%description
Easy testing suite.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
#rm -f %buildroot%perl_vendor_privlib/Test/README.pod

%files
%doc README.pod
%perl_vendor_privlib/Test/Easy.pm
%perl_vendor_privlib/Test/Easy/*pm

%changelog
* Thu Feb 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2
- fixed build

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Sat Oct 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Mon Mar 16 2009 Boris Savelev <boris@altlinux.org> 1.01-alt1
- initial build
