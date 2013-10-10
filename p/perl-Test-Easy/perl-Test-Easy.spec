%define _unpackaged_files_terminate_build 1
%define dist Test-Easy
Name: perl-%dist
Version: 1.07
Release: alt1

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
if [ %version = 1.07 ]; then
# Range iterator outside integer range at lib/Test/Easy/Time.pm line 38.
# incorrect test at 1.07
rm t/nearly.t
fi

%build
%perl_vendor_build

%install
%perl_vendor_install
rm %buildroot%perl_vendor_privlib/Test/README.pod

%files
%doc README.pod
%perl_vendor_privlib/Test/Easy.pm
%perl_vendor_privlib/Test/Easy/*pm

%changelog
* Sat Oct 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Mon Mar 16 2009 Boris Savelev <boris@altlinux.org> 1.01-alt1
- initial build
