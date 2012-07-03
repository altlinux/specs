%define dist AnyData
Name: perl-%dist
Version: 0.10
Release: alt2

Summary: Easy access to data in many formats
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Oct 03 2011 (-bi)
BuildRequires: perl-CGI perl-XML-Twig perl-devel

%description
The AnyData modules provide simple and uniform access to data from
many sources -- perl arrays, local files, remote files retrievable via
http or ftp -- and in many formats including flat files (CSV, Fixed
Length, Tab Delimited, etc), standard format files (Web Logs,
Passwd files, etc.),  structured files (XML, HTML Tables) and binary
files with parseable headers (mp3s, jpgs, pngs, etc).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/AnyData*

%changelog
* Mon Oct 03 2011 Alexey Tourbin <at@altlinux.ru> 0.10-alt2
- rebuilt

* Mon Aug 15 2005 Alexey Tourbin <at@altlinux.ru> 0.10-alt1
- initial revision
