%define dist Text-Patch
Name: perl-%dist
Version: 1.8
Release: alt1

Summary: Patches text with given patch
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Feb 26 2011
BuildRequires: perl-Text-Diff perl-devel

%description
Text::Patch combines source text with given diff (difference) data.
Diff data is produced by Text::Diff module or by the standard diff
utility (man diff, see -u option).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/Text

%changelog
* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 1.8-alt1
- initial revision
