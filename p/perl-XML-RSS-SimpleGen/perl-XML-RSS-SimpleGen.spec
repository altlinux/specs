%define dist XML-RSS-SimpleGen
Name: perl-%dist
Version: 11.11
Release: alt2

Summary: for writing RSS files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-devel perl-libwww

%description
This module is for writing RSS files, simply. It transparently handles
all the unpleasant details of RSS, like proper XML escaping, and also has
a good number of Do-What-I-Mean features, like not changing the modtime
on a written-out RSS file if the file content hasn't changed, and like
automatically removing any HTML tags from content you might pass in.

%prep
%setup -q -n %dist-%version

%ifdef __BTE
mv t/20_http.t t/20_http.t.orig
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/XML

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 11.11-alt2
- disabled live tests in hasher

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 11.11-alt1
- initial revision
