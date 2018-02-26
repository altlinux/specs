%define dist Makefile-DOM
Name: perl-%dist
Version: 0.006
Release: alt1

Summary: Simple DOM parser for Makefiles
License: %perl_license
Group: Development/Perl
Packager: Artem Zolochevskiy <azol@altlinux.ru>

URL: %CPAN %dist
# http://search.cpan.org/CPAN/authors/id/A/AG/AGENT/Makefile-DOM-0.004.tar.gz
Source: %dist-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Jan 12 2010
BuildRequires: perl-Clone perl-Filter perl-List-MoreUtils perl-Params-Util perl-PerlIO perl-Text-Balanced perl-devel

%description
This libary can serve as an advanced lexer for (GNU) makefiles. It
parses makefiles as "documents" and the parsing is lossless. The results
are data structures similar to DOM trees. The DOM trees hold every
single bit of the information in the original input files, including
white spaces, blank lines and makefile comments. That means it's
possible to reproduce the original makefiles from the DOM trees. In
addition, each node of the DOM trees is modifiable and so is the whole
tree, just like the PPI module used for Perl source parsing and the
HTML::TreeBuilder module used for parsing HTML source.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README TODO
%perl_vendor_privlib/MDOM/
%perl_vendor_privlib/Makefile/

%changelog
* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jan 12 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.004-alt1
- initial build for Sisyphus

