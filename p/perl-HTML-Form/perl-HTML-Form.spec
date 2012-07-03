%define dist HTML-Form
Name: perl-%dist
Version: 6.02
Release: alt1

Summary: Class that represents an HTML form element
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Conflicts: perl-libwww < 6

BuildArch: noarch

# Automatically added by buildreq on Sat Mar 10 2012
BuildRequires: perl-HTTP-Message perl-devel

%description
Objects of the HTML::Form class represents a single HTML <form> ...
</form> instance. A form consists of a sequence of inputs that usually
have names, and which can take on various values. The state of a form
can be tweaked and it can then be asked to provide HTTP::Request
objects that can be passed to the request() method of LWP::UserAgent.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/HTML

%changelog
* Sat Mar 10 2012 Alexey Tourbin <at@altlinux.ru> 6.02-alt1
- 6.00 -> 6.02

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt2
- rebuilt as plain src.rpm

* Tue Mar 22 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt1
- initial revision
