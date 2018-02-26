%define dist MooseX-InsideOut
Name: perl-%dist
Version: 0.106
Release: alt1

Summary: Inside-out objects with Moose
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Hash-Util-FieldHash-Compat perl-Moose perl-devel perl-namespace-clean

%description
MooseX::InsideOut provides metaroles for inside-out objects.  That is,
it sets up attribute slot storage somewhere other than inside $self.
This means that you can extend non-Moose classes, whose internals you
either don't want to care about or aren't hash-based.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/MooseX

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.106-alt1
- initial revision
