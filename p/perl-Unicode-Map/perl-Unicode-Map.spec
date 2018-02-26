%define dist Unicode-Map
Name: perl-%dist
Version: 0.112
Release: alt4

Summary: Maps charsets from and to utf16 unicode
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: %dist-%version.tar.gz
Source1: http://www.unicode.org/Public/MAPPINGS/VENDORS/MISC/KOI8-R.TXT

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
This module converts strings from and to 2-byte Unicode UCS2 format.
All mappings happen via 2 byte UTF16 encodings, not via 1 byte UTF8
encoding. To transform these use Unicode::String.

%prep
%setup -q -n %dist-%version

%build
# bootstrap
%perl_vendor_build

# add koi8-r support
mkdir -p Map/VENDORS/MISC
perl -Mblib tools/mkmapfile -M Map/VENDORS/MISC/KOI8-R.map %SOURCE1
[ -f Map/REGISTRY ]
cat <<\__EOF__ >>Map/REGISTRY
##
## ALT
##
name:    KOI8-R
srcURL:  $SrcUnicode/VENDORS/MISC/KOI8-R.TXT
src:     $DestUnicode/VENDORS/MISC/KOI8-R.TXT
map:     $DestMap/VENDORS/MISC/KOI8-R.map
alias:   csKOI8R
#mib:    ????
#
__EOF__

# rebuild
%perl_vendor_build

# test koi8-r support
perl -Mblib -MUnicode::Map -e 'Unicode::Map->new("KOI8-R") or die "KOI8-R broken\n"'

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/map
%_bindir/mkmapfile
%perl_vendor_archlib/Unicode
%perl_vendor_autolib/Unicode

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.112-alt4
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.112-alt3.0.1
- rebuilt with perl 5.12

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.112-alt3.0
- Automated rebuild.

* Thu May 12 2005 Alexey Tourbin <at@altlinux.ru> 0.112-alt3
- removed %_bindir/mkCSGB2312 and %_bindir/mirrorMappings
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.112-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Aug 20 2004 Alexey Tourbin <at@altlinux.ru> 0.112-alt2
- added koi8-r support

* Fri Feb 20 2004 Alexey Tourbin <at@altlinux.ru> 0.112-alt1
- initial revision
