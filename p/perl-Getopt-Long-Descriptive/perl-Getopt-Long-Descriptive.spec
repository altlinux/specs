%define dist Getopt-Long-Descriptive
Name: perl-%dist
Version: 0.091
Release: alt1

Summary: Getopt::Long, but simpler and more powerful
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 25 2011
BuildRequires: perl-Params-Validate perl-Sub-Exporter perl-devel

%description
Getopt::Long::Descriptive is yet another Getopt library.  It's built atop
Getopt::Long, and gets a lot of its features, but tries to avoid making you
think about its huge array of options.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Getopt

%changelog
* Mon Apr 16 2012 Vladimir Lettiev <crux@altlinux.ru> 0.091-alt1
- 0.090 -> 0.091

* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 0.090-alt1
- 0.087 -> 0.090

* Wed Dec 29 2010 Alexey Tourbin <at@altlinux.ru> 0.087-alt1
- 0.085 -> 0.087

* Fri Apr 09 2010 Alexey Tourbin <at@altlinux.ru> 0.085-alt1
- initial revision, for perl-DBIx-Class
