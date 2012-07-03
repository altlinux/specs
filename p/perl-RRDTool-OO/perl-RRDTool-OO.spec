Name: perl-RRDTool-OO
Version: 0.31
Release: alt1

Summary: RRDTool::OO - Object-oriented interface to RRDTool
Group: Development/Perl
License: Perl

Url: %CPAN RRDTool-OO
Source: %name-%version.tar

BuildRequires: perl-devel perl-RRD perl-Log-Log4perl

BuildArch: noarch

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/RRDTool/OO*
%doc Changes README 

%changelog
* Wed Nov 09 2011 Vladimir Lettiev <crux@altlinux.ru> 0.31-alt1
- initial build
