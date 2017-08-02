%define _unpackaged_files_terminate_build 1
%define dist XML-SAX-Writer
Name: perl-%dist
Version: 0.57
Release: alt1

Summary: SAX2 XML Writer
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/P/PE/PERIGRIN/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Encode perl-Pod-Escapes perl-XML-Filter-BufferText perl-XML-NamespaceSupport perl-devel

%description
Yet Another SAX2 XML Writer.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files 
%doc Changes README README.md
%perl_vendor_privlib/XML

%changelog
* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- automated CPAN update

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- automated CPAN update

* Sun Dec 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- automated CPAN update

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.53-alt2
- disabled build dependency on perl-Module-Install

* Wed Dec 22 2010 Alexey Tourbin <at@altlinux.ru> 0.53-alt1
- 0.52 -> 0.53

* Tue Jul 28 2009 Alexey Tourbin <at@altlinux.ru> 0.52-alt1
- 0.44 -> 0.52

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.44-alt3.1
- Rebuilt with rpm-build-perl-0.5.1.

* Wed Jul 21 2004 Alexey Tourbin <at@altlinux.ru> 0.44-alt3
- patched t/05basic.t to handle Text::Iconv >= 1.3
- updated description

* Fri Mar 21 2003 Stanislav Ievlev <inger@altlinux.ru> 0.44-alt2
- fix url

* Tue Nov 12 2002 Stanislav Ievlev <inger@altlinux.ru> 0.44-alt1
- Inital release
