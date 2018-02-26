%define dist Term-ANSIColor
Name: perl-Term-ANSIColor
Version: 3.01
Release: alt1

Summary: Color output using ANSI escape sequences
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Aug 06 2011
BuildRequires: perl-devel

%description
Term::ANSIColor provides constants and simple functions for sending ANSI
text attributes, most notably colors.  It can be used to set the current
text attributes or to apply a set of attributes to a string and reset
the current text attributes at the end of that string.

%prep
%setup -q -n %dist-%version

%ifdef __buildreqs
rm t/pod*.t
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/Term

%changelog
* Sat Aug 06 2011 Alexey Tourbin <at@altlinux.ru> 3.01-alt1
- 3.00 -> 3.01

* Tue Sep 21 2010 Alexey Tourbin <at@altlinux.ru> 3.00-alt1
- initial revision, for perl-5.12
