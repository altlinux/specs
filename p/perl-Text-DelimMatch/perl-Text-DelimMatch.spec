%define dist DelimMatch
Name: perl-Text-DelimMatch
Version: 1.06a
Release: alt3

Summary: find regexp delimited strings with proper nesting
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-devel

%description
These routines allow you to match delimited substrings in a buffer.
The delimiters can be specified with any regular expression and the start
and end delimiters need not be the same.  If the delimited text is properly
nested, entire nested groups are returned.  In addition, you may specify
quoting and escaping characters that contribute to the recognition of start
and end delimiters.

%prep
%setup -q -n %dist-1.06

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/Text

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 1.06a-alt3
- rebuilt

* Sat Aug 09 2008 Alexey Tourbin <at@altlinux.ru> 1.06a-alt2
- noarch

* Sat Aug 09 2008 Alexey Tourbin <at@altlinux.ru> 1.06a-alt1
- initial revision (for R)
