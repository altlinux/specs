# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
# For initial import only; will be removed later
#global perl_bootstrap 1

Name:           perl-SOAP-Transport-TCP
Version:        0.715
Release:        alt2_11
Summary:        TCP Transport Support for SOAP::Lite
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/SOAP-Transport-TCP/
Source0:        http://www.cpan.org/authors/id/M/MK/MKUTTER/SOAP-Transport-TCP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module/Build.pm)
# Avoid circular deps
%if !%{defined perl_bootstrap}
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(IO/Select.pm)
BuildRequires:  perl(IO/SessionData.pm)
BuildRequires:  perl(IO/SessionSet.pm)
BuildRequires:  perl(IO/Socket.pm)
BuildRequires:  perl(SOAP/Lite.pm)
BuildRequires:  perl(URI.pm)
BuildRequires:  perl(URI/_server.pm)
BuildRequires:  perl(Test/More.pm)
%endif
Requires:       perl(SOAP/Lite.pm) >= 0.714


Source44: import.info
%filter_from_requires /^perl\\(SOAP.Lite\\)$/d

%description
The classes provided by this module implement direct TCP/IP communications
methods for both clients and servers.

%prep
%setup -q -n SOAP-Transport-TCP-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
# %{_fixperms} %{buildroot}/*

%check
# Avoid circular deps
%if !%{defined perl_bootstrap}
./Build test
%endif

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.715-alt2_11
- Sisyphus build

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.715-alt2_9
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.715-alt2_8
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.715-alt2_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.715-alt2_6
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.715-alt2_4
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.715-alt1_4
- fc import

