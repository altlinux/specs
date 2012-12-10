# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Catalyst/Log.pm) perl(Catalyst/View.pm) perl(Config.pm) perl(File/Spec/Functions.pm) perl(FindBin.pm) perl(Scalar/Util.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Catalyst-View-Mason
Version:        0.18
Release:        alt2_10
Summary:        Mason View Class
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Catalyst-View-Mason/
Source0:        http://www.cpan.org/authors/id/F/FL/FLORA/Catalyst-View-Mason-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Catalyst.pm)
BuildRequires:  perl(Catalyst/Helper.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(HTML/Mason.pm)
BuildRequires:  perl(IO/Capture/Stderr.pm)
BuildRequires:  perl(MRO/Compat.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/File.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(Catalyst.pm) >= 5.50
Requires:       perl(Catalyst/View.pm)
Requires:       perl(parent.pm)
Source44: import.info

%description
Want to use a Mason component in your Catalyst views? No problem!
Catalyst::View::Mason comes to the rescue.

%prep
%setup -q -n Catalyst-View-Mason-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_10
- moved to Sisyphus

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_10
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_8
- fc import

