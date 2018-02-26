Name: perl-CGI-Compile
Version: 0.15
Release: alt1
Summary: CGI::Compile - Compile .cgi scripts to a code reference like ModPerl::Registry

Group: Development/Perl
License: Perl
Url: %CPAN CGI-Compile

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-File-pushd perl-Test-Requires perl-Test-NoWarnings perl-CGI

%description
CGI::Compile is an utility to compile CGI scripts into a code reference
that can run many times on its own namespace, as long as the script is
ready to run on a persistent environment.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/CGI/Compile.pm
%doc Changes README 

%changelog
* Fri Dec 02 2011 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt1
- New version 0.15

* Sun Feb 06 2011 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- New version 0.14

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- initial build
