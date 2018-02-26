%define dist XML-Filter-BufferText
Name: perl-%dist
Version: 1.01
Release: alt3

Summary: SAX Filter to guarantee characters in one event
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: perl-XML-SAX perl-devel

%description
This is a very simple filter. One common cause of grief (and programmer
error) is that XML parsers aren't required to provide character events in one
chunk. They can, but are not forced to, and most don't. This filter does the
trivial but oft-repeated task of putting all characters into a single event.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files 
%doc Changes README
%perl_vendor_privlib/XML

%changelog
* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 1.01-alt3
- rebuilt as plain src.rpm

* Tue Jul 28 2009 Alexey Tourbin <at@altlinux.ru> 1.01-alt2
- rebuilt

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.01-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Thu Oct 30 2003 Alexey Tourbin <at@altlinux.ru> 1.01-alt1
- 1.01
- descriptions updated

* Fri Mar 21 2003 Stanislav Ievlev <inger@altlinux.ru> 1.00-alt2
- fix url

* Tue Nov 12 2002 Stanislav Ievlev <inger@altlinux.ru> 1.00-alt1
- Initial release
