# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Benchmark.pm) perl(Clone.pm) perl(Config.pm) perl(Exporter.pm) perl(File/Copy/Recursive.pm) perl(File/ShareDir.pm) perl(IO/Handle.pm) perl(IO/Select.pm) perl(Math/GMP.pm) perl(Math/MatrixReal.pm) perl(Moose.pm) perl(MooseX/Declare.pm) perl(Mouse.pm) perl(Storable.pm) perl(Time/HiRes.pm) perl(threads.pm) perl(threads/shared.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Benchmark-Perl-Formance
%define upstream_version 0.33

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_2

Summary:    Benchmark Suite for Perl
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Benchmark/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Data/DPath.pm)
BuildRequires: perl(Data/Structure/Util.pm)
BuildRequires: perl(Data/YAML/Reader.pm)
BuildRequires: perl(Data/YAML/Writer.pm)
BuildRequires: perl(Devel/Platform/Info.pm)
BuildRequires: perl(List/Util.pm)
BuildRequires: perl(Sys/Hostname.pm)
BuildRequires: perl(Test/More.pm)
BuildArch: noarch
Source44: import.info

%description
This benchmark suite tries to run some stressful programs and outputs values
that you can compare against other runs of this suite, e.g. with other versions
of Perl, modified compile parameter, or another set of dependent libraries.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.json META.yml LICENSE Changes README
%perl_vendor_privlib/*
/usr/bin/benchmark-perlformance
/usr/share/man/man1/benchmark-perlformance.1.*



%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  0.33-alt1_2
- mageia import by cas@ requiest

