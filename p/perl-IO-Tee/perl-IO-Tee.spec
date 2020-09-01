# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(IO/File.pm) perl(IO/Handle.pm) perl(Symbol.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name	 IO-Tee
%define upstream_version 0.64

Name:		perl-%{upstream_name}
Version:	0.66
Release:	alt1

Summary:	Multiplex output to multiple output handles 
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/N/NE/NEILB/%{upstream_name}-%{version}.tar.gz


BuildArch:	noarch
Source44: import.info

%description
IO::Tee objects can be used to multiplex input and output in two different
ways. The first way is to multiplex output to zero or more output handles. The
IO::Tee constructor, given a list of output handles, returns a tied handle that
can be written to. When written to (using print or printf), the IO::Tee object
multiplexes the output to the list of handles originally passed to the
constructor. As a shortcut, you can also directly pass a string or an array
reference to the constructor, in which case IO::File::new is called for you
with the specified argument or arguments.

The second way is to multiplex input from one input handle to zero or more
output handles as it is being read. The IO::Tee constructor, given an input
handle followed by a list of output handles, returns a tied handle that can be
read from as well as written to. When written to, the IO::Tee object
multiplexes the output to all handles passed to the constructor, as described
in the previous paragraph. When read from, the IO::Tee object reads from the
input handle given as the first argument to the IO::Tee constructor, then
writes any data read to the output handles given as the remaining arguments to
the constructor.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendor_privlib}/IO




%changelog
* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.66-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.65-alt1
- automated CPAN update

* Mon Dec 28 2015 Lenar Shakirov <snejok@altlinux.ru> 0.64-alt3
- build for Sisyphus

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.64-alt2_5
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.64-alt2_4
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.64-alt2_3
- rebuild to get rid of unmets

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1_3
- mga update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1_1
- converted for ALT Linux by srpmconvert tools

