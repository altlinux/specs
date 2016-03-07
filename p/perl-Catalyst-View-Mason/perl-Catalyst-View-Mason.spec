Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Cwd.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Spec/Functions.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(FindBin.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Catalyst-View-Mason
Version:        0.19
Release:        alt1_5
Summary:        Mason View Class
License:        GPL+ or Artistic

URL:            http://search.cpan.org/dist/Catalyst-View-Mason/
Source0:        http://www.cpan.org/authors/id/F/FL/FLORA/Catalyst-View-Mason-%{version}.tar.gz
# Use stderr capturing mechanims that works with Catalyst > 5.90079,
# bug #1190033, CPAN RT#102381
Patch0:         Catalyst-View-Mason-0.19-Use-Capture-Tiny-IO-Capture.patch

BuildArch:      noarch
BuildRequires:  perl(Catalyst.pm)
BuildRequires:  perl(Catalyst/Helper.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(HTML/Mason.pm)
BuildRequires:  perl(Capture/Tiny.pm)
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
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/Catalyst*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_4
- update to new release by fcimport

* Tue Jan 13 2015 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_1
- update to new release by fcimport

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

