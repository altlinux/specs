%define _unpackaged_files_terminate_build 1
%define dist Syntax-Highlight-Engine-Kate
Name: perl-%dist
Version: 0.08
Release: alt1

Summary: Port to Perl of the syntax highlight engine of the Kate texteditor
License: %perl_license
Group: Development/Perl
Packager: Artem Zolochevskiy <azol@altlinux.ru>

URL: %CPAN %dist
# http://search.cpan.org/CPAN/authors/id/S/SZ/SZABGAB/Syntax-Highlight-Engine-Kate-0.06.tar.gz
Source: http://www.cpan.org/authors/id/S/SZ/SZABGAB/Syntax-Highlight-Engine-Kate-%{version}.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Jan 19 2010
BuildRequires: perl-Module-Install perl(Test/Differences.pm)

BuildRequires: perl-XML-Dumper perl-HTML-Parser perl-XML-TokeParser

%description
Syntax::Highlight::Engine::Kate is a port to perl of the syntax highlight
engine of the Kate text editor.

%prep
%setup -n %dist-%version
# newer kate engine; diff, not regression
[ %version = 0.08 ] && rm t/perl_highlighting.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README samples
%perl_vendor_privlib/Syntax/

%changelog
* Fri Oct 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jan 19 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.06-alt1
- initial build for Sisyphus

