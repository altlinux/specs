# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl(inc/Module/Install.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-MouseX-Types
Summary:        Organize your Mouse types in libraries
Version:        0.06
Release:        alt2_12
License:        GPL+ or Artistic
Group:          Development/Perl
Source0:        http://search.cpan.org/CPAN/authors/id/G/GF/GFUJI/MouseX-Types-%{version}.tar.gz
URL:            http://search.cpan.org/dist/MouseX-Types
BuildArch:      noarch

BuildRequires:  perl(Any/Moose.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Mouse.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Sub/Exporter.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)

Requires:       perl(Mouse.pm) >= 0.41

# obsolete/provide old tests subpackage
# can be removed during F19 development cycle
Obsoletes:      %{name}-tests < 0.06-2
Provides:       %{name}-tests = %{version}-%{release}


Source44: import.info

%description
Organize your Mouse types; much as MooseX::Types does for your Moose types.
For more information, please see the MooseX::Types manpage.

This library was split off from Mouse as of Mouse 0.15.


%prep
%setup -q -n MouseX-Types-%{version}

find lib -type f -name '*.pm' -print0 | xargs -0 chmod 0644
chmod 0644 t/*.t

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README t/
%{perl_vendor_privlib}/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_11
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_8
- update to new release by fcimport

* Thu Oct 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_7
- Sisyphus build

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_7
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_5
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_4
- update to new release by fcimport

* Sat May 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_2
- fc import

