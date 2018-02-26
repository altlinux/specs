Name: perl-Text-Xslate
Version: 1.5007
Release: alt2
Summary: Text::Xslate - Scalable template engine for Perl5

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~gfuji/Text-Xslate/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-devel perl-Mouse perl-MouseX-Getopt perl-Test-Requires perl-Data-MessagePack perl-Any-Moose perl-parent perl-Module-Install-XSUtil perl-Module-Install-TestTarget perl-Module-Install-AuthorTests perl-unicore perl-autodie perl-CGI perl-Encode-JP perl-podlators perl-HTTP-Message perl-IPC-Run perl-File-Which perl-Data-Section-Simple perl-URI-Find perl-HTML-FillInForm-Lite perl-JavaScript-Value-Escape perl-Plack perl-Amon2-Lite perl-HTML-Shakan perl-Mojolicious perl-MojoX-Renderer-Xslate perl-Data-Localize perl-Locale-Maketext perl-Locale-Maketext-Lexicon

%description
Xslate is a template engine for Perl5 with the following features:
* Extremely fast - Up to 50~100 times faster than TT2!
* Supports multiple template syntaxes - TT2 compatible syntax,
  for example
* Easy to enhance - by importing subroutines and/or by calling
  object methods
* Safe - Escapes HTML meta characters by default

%prep
%setup -q
%patch -p1

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/xslate
%_man1dir/xslate.1*
%perl_vendor_archlib/Text/Xslate*
%perl_vendor_autolib/Text/Xslate
%doc Changes README HACKING 

%changelog
* Sun Dec 04 2011 Vladimir Lettiev <crux@altlinux.ru> 1.5007-alt2
- Buildreq Amon2 -> Amon2::Lite

* Fri Dec 02 2011 Vladimir Lettiev <crux@altlinux.ru> 1.5007-alt1
- New version 1.5007

* Wed Oct 12 2011 Alexey Tourbin <at@altlinux.ru> 1.5003-alt1
- 1.5002 -> 1.5003
- built for perl-5.14

* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 1.4001-alt1
- New version 1.4001

* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 1.4000-alt1
- New version 1.4000

* Sat Mar 05 2011 Vladimir Lettiev <crux@altlinux.ru> 1.0012-alt1
- New version 1.0012

* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 1.0011-alt1
- New version 1.0011

* Thu Feb 17 2011 Vladimir Lettiev <crux@altlinux.ru> 1.0008-alt1
- initial build
