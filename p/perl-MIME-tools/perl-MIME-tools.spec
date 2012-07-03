%define dist MIME-tools
Name: perl-%dist
Version: 5.502
Release: alt2
Epoch: 1

Summary: Perl modules for parsing and creating MIME entities
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

# Automatically added by buildreq on Sat Nov 19 2011
BuildRequires: perl-Convert-BinHex perl-MailTools perl-Test-Deep perl-Test-Pod

%description
MIME-tools is a collection of Perl modules for parsing, decoding,
and generating single- or multipart (even nested multipart) MIME
messages.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/MIME*

%changelog
* Sat Nov 19 2011 Alexey Tourbin <at@altlinux.ru> 1:5.502-alt2
- disabled build dependency on perl-Module-Install

* Tue Mar 15 2011 Alexey Tourbin <at@altlinux.ru> 1:5.502-alt1
- 5.500 -> 5.502

* Sun Jan 16 2011 Alexey Tourbin <at@altlinux.ru> 1:5.500-alt1
- 5.428 -> 5.550
- reverted boundary_delimiter.patch

* Wed Apr 28 2010 Alexey Tourbin <at@altlinux.ru> 1:5.428-alt1
- 5.427 -> 5.428

* Mon Jul 07 2008 Alexey Tourbin <at@altlinux.ru> 1:5.427-alt1
- 5.426 -> 5.427

* Thu Jun 19 2008 Alexey Tourbin <at@altlinux.ru> 1:5.426-alt1
- 5.420 -> 5.426

* Sun Oct 29 2006 Alexey Tourbin <at@altlinux.ru> 1:5.420-alt2
- imported sources into git and built with gear
- MIME/Body.pm (open): protection against malicious filenames (cpan #22680)
- Decoder/Gzip64.pm: use strict and fix bug in `use vars' (cpan #22681)
- MIME/Decoder.pm (new): warn when `eval require ...' fails (#22682)
- MIME/Decoder.pm (filter): use select() for IO multiplexing (cpan #22684)
- MIME/Words.pm, WordDecoder.pm: removing the nasty eval <::DATA> (cpan #20474)

* Thu Apr 20 2006 Alexey Tourbin <at@altlinux.ru> 1:5.420-alt1
- 5.418 -> 5.420
- updated patches
- alt-localize-underscore.patch merged upstream (cpan #12785)

* Tue Oct 04 2005 Alexey Tourbin <at@altlinux.ru> 1:5.418-alt1
- 5.417 -> 5.418
- cpan-7368-stderr.patch merged upstream (cpan #7368)
- updated alt-localize-underscore.patch (cpan #12785)

* Fri May 13 2005 Alexey Tourbin <at@altlinux.ru> 1:5.417-alt1
- 6.200_02 -> 5.417 (rolled back to earlier branch)
- clarified dependency on MIME::QuotedPrint 3.03
- clarified dependency on IO::InnerFile 2.110 (cpan #12784)
- fixed $_ localization (cpan #12785)
- backported and fixed boundary delimiter stuff (#5407, cpan #12787)
- dropped debugging output in MIME::WordDecoder (cpan #7368)

* Fri Aug 20 2004 Alexey Tourbin <at@altlinux.ru> 6.200-alt0.2
- alt-default-charset-fallback.patch: fall back to ISO-8859-1 when
  LC_CTYPE charset is unsupported (should fix sympa4, amavisd-new)

* Fri Feb 20 2004 Alexey Tourbin <at@altlinux.ru> 6.200-alt0.1
- 6.200_02 (beta)
- alt-syntax.patch: fixed a few bugs

* Thu Jun 12 2003 Alexey Tourbin <at@altlinux.ru> 5.411a-alt1
- 5.411a
- specfile cleanup; docs added

* Tue Nov 05 2002 Alexey Tourbin <at@altlinux.ru> 5.411-alt4
- rebuilt for perl-5.8 with new rpm macros

* Mon Jun 25 2001 Stanislav Ievlev <inger@altlinux.ru> 5.411-alt3
- Rebuilt with perl-5.6.1

* Fri Jun 13 2001 Grigory Milev <week@altlinux.ru> 5.411-alt2
- Rewrite spec for compatible with new police

* Fri Jun 08 2001 Grigory Milev <week@altlinux.ru> 5.411-alt1
- new version (5.411)

* Sun Feb 4 2001 AEN <aen@logic.ru>
- RE adaptation

* Thu Oct 12 2000 François Pons <fpons@mandrakesoft.com> 5.316-1mdk
- 5.316.

* Tue Aug 29 2000 François Pons <fpons@mandrakesoft.com> 5.311-1mdk
- 5.311.

* Thu Aug 03 2000 François Pons <fpons@mandrakesoft.com> 5.306-2mdk
- Oops, added missing clean.

* Thu Aug 03 2000 François Pons <fpons@mandrakesoft.com> 5.306-1mdk
- macroszifications.
- added doc.
- noarch.
- 5.306.

* Tue Jul 18 2000 François Pons <fpons@mandrakesoft.com> 5.304-1mdk
- 5.304.

* Mon Apr  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 4.124-2mdk
- fixed group
- rebuild with new perl
- fixed location

* Thu Dec  2 1999 Jerome Dumonteil <jd@mandrakesoft.com>
- first version of rpm.
