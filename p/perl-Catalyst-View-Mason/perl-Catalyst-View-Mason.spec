# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Catalyst/Log.pm) perl(Catalyst/View.pm) perl(Config.pm) perl(Cwd.pm) perl(ExtUtils/Command.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Spec/Functions.pm) perl(FileHandle.pm) perl(FindBin.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Catalyst-View-Mason
Version:        0.18
Release:        alt3_12
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
# use deprecated Catalyst
rm t/match.t t/action.t

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Fri Oct 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt3_12
- fixed build

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_12
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_11
- update to new release by fcimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2_10
- moved to Sisyphus

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_10
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_8
- fc import

