Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Const-Fast
Version:        0.014
Release:        alt2_10
Summary:        Facility for creating read-only scalars, arrays, and hashes
License:        GPL+ or Artistic

URL:            http://search.cpan.org/dist/Const-Fast/
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/Const-Fast-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Module/Build/Tiny.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Storable.pm)
BuildRequires:  perl(Sub/Exporter.pm)
# Tests
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/Fatal.pm)
BuildRequires:  perl(Sub/Exporter/Progressive.pm)
# Optional tests
BuildRequires:  perl(Test/Script.pm)



%description
This the only function of this module and it is exported by default. It takes
a scalar, array or hash left-value as first argument, and a list of one or
more values depending on the type of the first argument as the value for the
variable. It will set the variable to that value and subsequently make it
read-only. Arrays and hashes will be made deeply read-only.


%prep
%setup -q -n Const-Fast-%{version}


%build
%{__perl} Build.PL --install_path bindoc=%_man1dir --installdirs vendor
./Build


%install
./Build install --destdir $RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'

# %{_fixperms} $RPM_BUILD_ROOT/*


%check
./Build test


%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/*


%changelog
* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.014-alt2_10
- update to new release by fcimport

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.014-alt2
- to Sisyphus

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- update

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_2
- update to new release by fcimport

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_3
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1_4
- fc import

