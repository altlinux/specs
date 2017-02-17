Name: perl-MojoX-Renderer-Xslate
Version: 0.13
Release: alt1
Summary: MojoX::Renderer::Xslate - Text::Xslate renderer for Mojo

Group: Development/Perl
License: Perl
Url: %CPAN MojoX-Renderer-Xslate

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-Try-Tiny perl-Text-Xslate perl-devel perl-Mojolicious perl-Mouse perl(Pod/Text.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/MojoX/Renderer/Xslate.pm
%perl_vendor_privlib/Mojolicious/Plugin/XslateRenderer.pm
%doc Changes README

%changelog
* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Sat Jul 07 2012 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- 0.07 -> 0.08

* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt1
- 0.07

* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt1
- initial build
