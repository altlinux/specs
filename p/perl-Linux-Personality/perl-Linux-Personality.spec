# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(AutoLoader.pm) perl(Exporter.pm) perl(XSLoader.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Linux-Personality
%define upstream_version 0.01

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt3_14

Summary:    Perl interface to the personality(2) Linux system call
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Linux/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl-devel
Source44: import.info

%description
This is a Perl interface to the personality(2) Linux system call.

You can use this for instance when running 32bit compiles started from
inside a Perl program in a 32bit chroot but running on a 64bit host kernel.
Without hints the compile tools get confused and try do do 64bit in the
32bit environment.

It's somewhat comparable to the 'setarch' (also known as 'linux32')
utility. With 'personality' you can get similar effect inside a Perl
program.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog README META.yml
%perl_vendor_archlib/L*
%perl_vendor_archlib/auto/L*

%changelog
* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.01-alt3_14
- update by mgaimport

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2.1
- rebuild with new perl 5.20.1

* Mon Sep 02 2013 Vladimir Lettiev <crux@altlinux.ru> 0.01-alt2
- built for perl 5.18

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_4
- update by mgaimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  0.01-alt1_2
- mageia import by cas@ requiest

