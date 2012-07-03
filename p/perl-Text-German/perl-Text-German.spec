%define dist Text-German
Name: perl-%dist
Version: 0.06
Release: alt1

Summary: German grundform reduction
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Jan 16 2011
BuildRequires: perl-devel

%description
This is a rather incomplete implementaion of work done by Gudrun Putze-Meier.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	README
%dir	%perl_vendor_privlib/Text
	%perl_vendor_privlib/Text/German*
%doc	%perl_vendor_privlib/Text/German.pod

%changelog
* Sun Jan 16 2011 Alexey Tourbin <at@altlinux.ru> 0.06-alt1
- decoupled from perl-Lingua-Stem
