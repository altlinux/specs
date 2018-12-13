%define _unpackaged_files_terminate_build 1
BuildRequires: perl-podlators
%define module Text-Trac

Name: perl-%module
Version: 0.24
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Perl extension for formatting text with Trac Wiki Style
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/M/MA/MANWAR/%{module}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 30 2009
BuildRequires: perl-Class-Accessor perl-Class-Data-Inheritable perl-HTML-Parser perl-List-MoreUtils perl-Test-Base perl-Test-Pod perl-Test-Pod-Coverage perl-Tie-IxHash perl-UNIVERSAL-require perl(Path/Tiny.pm)

%description
Text::Trac parses text with Trac WikiFormatting and convert it to html format.

%package scripts
Summary: %name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %name


%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md
%perl_vendor_privlib/Text/

%files scripts
%_bindir/*
#%_man1dir/*


%changelog
* Thu Dec 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Fri Dec 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Mon Sep 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Nov 30 2009 Victor Forsyuk <force@altlinux.org> 0.15-alt1
- 0.15

* Wed Jun 04 2008 Victor Forsyuk <force@altlinux.org> 0.12-alt1
- 0.12

* Mon Mar 31 2008 Victor Forsyuk <force@altlinux.org> 0.11-alt1
- 0.11

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 0.10-alt1
- Initial build.
