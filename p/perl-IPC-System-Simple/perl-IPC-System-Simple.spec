# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(English.pm) perl(Fatal.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:		perl-IPC-System-Simple 
Version:	1.25
Release:	alt2_1
License:	GPL+ or Artistic 
Group:		Development/Perl
Summary:	Run commands simply, with detailed diagnostics 
URL:		http://search.cpan.org/dist/IPC-System-Simple
Source0:	http://search.cpan.org/CPAN/authors/id/P/PJ/PJF/IPC-System-Simple-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(BSD/Resource.pm)
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(Config.pm)
BuildRequires:	perl(constant.pm)
BuildRequires:	perl(Exporter.pm)
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	perl(File/Basename.pm)
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(List/Util.pm)
BuildRequires:	perl(Pod/Coverage/TrustPod.pm)
BuildRequires:	perl(POSIX.pm)
BuildRequires:	perl(re.pm)
BuildRequires:	perl(Scalar/Util.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Test.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/NoWarnings.pm)
BuildRequires:	perl(Test/Perl/Critic.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
BuildRequires:	perl(warnings.pm)
Source44: import.info

%description
Calling Perl's in-built 'system()' function is easy; determining if it
was successful is _hard_. Let's face it, '$?' isn't the nicest variable
in the world to play with, and even if you _do_ check it, producing a
well-formatted error string takes a lot of work. 'IPC::System::Simple'
takes the hard work out of calling external commands. In fact, if you
want to be really lazy, you can just write: 

    use IPC::System::Simple qw(system);

and all of your "system" commands will either succeed (run to completion and
return a zero exit value), or die with rich diagnostic messages.

%prep
%setup -q -n IPC-System-Simple-%{version}

# Avoid doc-file dependencies
chmod -c -x examples/*.pl

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}

%files
%doc Changes LICENSE README examples/
%{perl_vendor_privlib}/IPC/

%changelog
* Sat Jan 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.25-alt2_1
- Sisyphus build

* Tue Nov 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1_1
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_8
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_7
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_6
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_5
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_3
- fc import

