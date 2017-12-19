%define dist Encode
Name: perl-%dist
Version: 2.93
Release: alt1

Summary: Character encodings
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Thu Oct 06 2011
BuildRequires: perl-Filter perl-devel perl-unicore perl-parent

%description
The Encode module provides the interfaces between Perl's strings
and the rest of the system.  Perl strings are sequences of characters.
See "perldoc Encode" for the rest of the story.

%package devel
Summary: Perl Encode Module Generator
Group: Development/Perl
Requires: %name = %version-%release
%description devel
enc2xs builds a Perl extension for use by Encode from either Unicode
Character Mapping files (.ucm) or Tcl Encoding Files (.enc).  Besides
being used internally during the build process of the Encode module,
you can use enc2xs to add your own encoding to Perl.

%package CN
Summary: China-based Chinese Encodings
Group: Development/Perl
Requires: %name = %version-%release
%description CN
The Encode::CN module implements China-based Chinese charset encodings.
The following encodings are supported: euc-cn, gb2312-raw, gb12345-raw,
iso-ir-165, MacChineseSimp, cp936, hz.

%package TW
Summary: Taiwan-based Chinese Encodings
Group: Development/Perl
Requires: %name = %version-%release
%description TW
The Encode::TW module implements tradition Chinese charset encodings
as used in Taiwan and Hong Kong.  The following encodings are supported:
big5-eten, big5-hkscs, MacChineseTrad, cp950.

%package KR
Summary: Korean Encodings
Group: Development/Perl
Requires: %name = %version-%release
%description KR
The Encode::KR module implements Korean charset encodings.
The following encodings are supported: euc-kr, ksc5601-raw, cp949,
MacKorean, johab, iso-2022-kr.

%package JP
Summary: Japanese Encodings
Group: Development/Perl
Requires: %name = %version-%release
%description JP
The Encode::JP module implements Japanese charset encodings.
The following encodings are supported: euc-jp, shiftjis, 7bit-jis,
iso-2022-jp, iso-2022-jp-1, MacJapanese, cp932, jis0201-raw,
jis0208-raw, jis0212-raw.

%prep
%setup -q -n %dist-%version
%patch -p1
bzip2 -k Changes

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	AUTHORS README Changes
	%_bindir/piconv
	%_bindir/encguess
	%perl_vendor_archlib/encoding.pm
	%perl_vendor_archlib/Encode.pm
%dir	%perl_vendor_archlib/Encode
	%perl_vendor_archlib/Encode/*.pm
%doc	%perl_vendor_archlib/Encode/*.pod
%dir	%perl_vendor_archlib/Encode/MIME
	%perl_vendor_archlib/Encode/MIME/*.pm
	%perl_vendor_archlib/Encode/Unicode
	%perl_vendor_autolib/Encode
%exclude %perl_vendor_archlib/Encode/CN*
%exclude %perl_vendor_autolib/Encode/CN*
%exclude %perl_vendor_archlib/Encode/TW*
%exclude %perl_vendor_autolib/Encode/TW*
%exclude %perl_vendor_archlib/Encode/KR*
%exclude %perl_vendor_autolib/Encode/KR*
%exclude %perl_vendor_archlib/Encode/JP*
%exclude %perl_vendor_autolib/Encode/JP*

%files devel
	%_bindir/enc2xs
%dir	%perl_vendor_archlib/Encode
	%perl_vendor_archlib/Encode/*.e2x
	%perl_vendor_archlib/Encode/*.h

%files CN
%dir	%perl_vendor_archlib/Encode
	%perl_vendor_archlib/Encode/CN*
%dir	%perl_vendor_autolib/Encode
	%perl_vendor_autolib/Encode/CN*

%files TW
%dir	%perl_vendor_archlib/Encode
	%perl_vendor_archlib/Encode/TW*
%dir	%perl_vendor_autolib/Encode
	%perl_vendor_autolib/Encode/TW*

%files KR
%dir	%perl_vendor_archlib/Encode
	%perl_vendor_archlib/Encode/KR*
%dir	%perl_vendor_autolib/Encode
	%perl_vendor_autolib/Encode/KR*

%files JP
%dir	%perl_vendor_archlib/Encode
	%perl_vendor_archlib/Encode/JP*
%dir	%perl_vendor_autolib/Encode
	%perl_vendor_autolib/Encode/JP*
%dir	%perl_vendor_archlib/Encode/MIME
%dir	%perl_vendor_archlib/Encode/MIME/Header
	%perl_vendor_archlib/Encode/MIME/Header/ISO_2022_JP.pm

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 2.93-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.88-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.88-alt1.1
- rebuild with new perl 5.24.1

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 2.88-alt1
- automated CPAN update

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 2.87-alt1
- automated CPAN update

* Thu Sep 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.86-alt1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.84-alt1
- automated CPAN update

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.83-alt1
- automated CPAN update

* Wed Mar 23 2016 Igor Vlasenko <viy@altlinux.ru> 2.82-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.78-alt1.1
- rebuild with new perl 5.22.0

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.78-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.67-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.62-alt1.1
- rebuild with new perl 5.20.1

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 2.62-alt1
- new version 2.62

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.57-alt1
- 2.55 -> 2.57

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 2.55-alt1
- 2.52 -> 2.55

* Wed Aug 21 2013 Vladimir Lettiev <crux@altlinux.ru> 2.52-alt1
- 2.49 -> 2.52

* Tue Mar 12 2013 Vladimir Lettiev <crux@altlinux.ru> 2.49-alt1
- 2.47 -> 2.49

* Thu Aug 23 2012 Vladimir Lettiev <crux@altlinux.ru> 2.47-alt1
- 2.44 -> 2.47

* Thu May 03 2012 Vladimir Lettiev <crux@altlinux.ru> 2.44-alt2
- built for perl-5.16

* Thu Oct 06 2011 Alexey Tourbin <at@altlinux.ru> 2.44-alt1
- 2.42 -> 2.44
- built for perl-5.14

* Fri Feb 11 2011 Alexey Tourbin <at@altlinux.ru> 2.42-alt1
- 2.41 -> 2.42

* Sun Dec 26 2010 Alexey Tourbin <at@altlinux.ru> 2.41-alt1
- 2.40 -> 2.41
- restored 'use warnings'

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 2.40-alt1
- 2.39 -> 2.40
- built for perl-5.12

* Mon Feb 15 2010 Alexey Tourbin <at@altlinux.ru> 2.39-alt1
- 2.37 -> 2.39

* Tue Sep 08 2009 Alexey Tourbin <at@altlinux.ru> 2.37-alt1
- 2.35 -> 2.37
- made a few C functions static

* Sat Aug 29 2009 Alexey Tourbin <at@altlinux.ru> 2.35-alt1
- 2.34 -> 2.35

* Sun Jul 12 2009 Alexey Tourbin <at@altlinux.ru> 2.34-alt1
- 2.33 -> 2.34

* Wed Apr 08 2009 Alexey Tourbin <at@altlinux.ru> 2.33-alt1
- 2.32 -> 2.33

* Mon Mar 09 2009 Alexey Tourbin <at@altlinux.ru> 2.32-alt1
- 2.26 -> 2.32

* Tue Jul 15 2008 Alexey Tourbin <at@altlinux.ru> 2.26-alt1
- 2.25 -> 2.26

* Thu May 15 2008 Alexey Tourbin <at@altlinux.ru> 2.25-alt1
- 2.24 -> 2.25

* Wed Mar 12 2008 Alexey Tourbin <at@altlinux.ru> 2.24-alt1
- 2.23 -> 2.24

* Tue Aug 21 2007 Alexey Tourbin <at@altlinux.ru> 2.23-alt2
- Encode/Config.pm: added more Encode::HanExtra and Encode::JIS2K encodings
- moved Encode/MIME/Header/ISO_2022_JP.pm from perl-Encode to perl-Encode-JP
- changed src.rpm packaging to keep upstream tarball unchanged

* Sun Jun 10 2007 Alexey Tourbin <at@altlinux.ru> 2.23-alt1
- 2.20 -> 2.23

* Mon Apr 23 2007 Alexey Tourbin <at@altlinux.ru> 2.20-alt1
- 2.19 -> 2.20

* Sat Apr 07 2007 Alexey Tourbin <at@altlinux.ru> 2.19-alt1
- 2.18 -> 2.19

* Tue Apr 03 2007 Alexey Tourbin <at@altlinux.ru> 2.18-alt2
- made perl-Encode strictly depend on PerlIO::encoding; previously the
  dependency was generated only because of a bug in rpm-build-perl < 0.6.2
- also cleaned up conditional loading of modules under eval

* Mon Oct 16 2006 Alexey Tourbin <at@altlinux.ru> 2.18-alt1
- 2.17 -> 2.18
- imported sources into git and built with gear
- own Encode dir (#10020)
- removed `use warnings;'

* Mon May 22 2006 Alexey Tourbin <at@altlinux.ru> 2.17-alt1
- 2.11 -> 2.17

* Sun Aug 07 2005 Alexey Tourbin <at@altlinux.ru> 2.11-alt1
- 2.10 -> 2.11
- enabled support for Encode::HanExtra Chinese encodings (cpan #14041)

* Tue May 17 2005 Alexey Tourbin <at@altlinux.ru> 2.10-alt1
- 2.09 -> 2.10
- packaged %_bindir/enc2xs into devel subpackage

* Tue Dec 14 2004 Alexey Tourbin <at@altlinux.ru> 2.09-alt1
- initial revision (split perl-i18n)
- subpackages: CN, TW, KR, JP
