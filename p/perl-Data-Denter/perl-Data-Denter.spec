# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(diagnostics.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:       perl-Data-Denter 
Version:    0.15 
Release:    alt2_13
# Denter.pod -> GPL+ or Artistic
License:    GPL+ or Artistic 
Group:      Development/Perl
Summary:    An alternative to Data::Dumper and Storable 
Source:     http://search.cpan.org/CPAN/authors/id/I/IN/INGY/Data-Denter-%{version}.tar.gz
Url:        http://search.cpan.org/dist/Data-Denter
BuildArch:  noarch

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(YAML.pm)
# test
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(Test.pm)
Source44: import.info

%description
The main problem with Data::Dumper (one of my all-time favorite modules)
is that you have to use 'eval()' to deserialize the data you've dumped.
This is great if you can trust the data you're evaling, but horrible if
you can't. A good alternative is Storable.pm. It can safely thaw your
frozen data.  But if you want to read/edit the frozen data, you're out of
luck, because Storable uses a binary format. Even Data::Dumper's output
can be a little cumbersome for larger data objects. Enter Data::Denter. 

Data::Denter is yet another Perl data serializer/deserializer. It formats
nested data structures in an indented fashion. It is optimized for human
readability/editability, safe deserialization, and (eventually) speed.


%prep
%setup -q -n Data-Denter-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README 
%{perl_vendor_privlib}/*

%changelog
* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_13
- Sisyphus build

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_13
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_12
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_11
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_10
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_8
- fc import

