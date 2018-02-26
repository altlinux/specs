%define dist Compress-Snappy
Name: perl-%dist
Version: 0.12
Release: alt2

Summary: Perl interface to Google's Snappy (de)compressor
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-devel perl-parent

%description
The `Compress::Snappy' module provides an interface to Google's Snappy
(de)compressor.

Snappy does not aim for maximum compression, or compatibility with any other
compression library; instead, it aims for very high speeds and reasonable
compression. For instance, compared to the fastest mode of zlib, Snappy is
an order of magnitude faster for most inputs, but the resulting compressed
files are anywhere from 20%% to 100%% bigger.

%prep
%setup -n %dist-%version

# do not override default CCFLAGS
sed -i- '/CCFLAGS/d' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Compress
%perl_vendor_autolib/Compress

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.12-alt2
- rebuilt for perl-5.14

* Thu Jul 28 2011 Denis Smirnov <mithraen@altlinux.ru> 0.12-alt1
- initial build for ALT Linux Sisyphus
