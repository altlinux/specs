%define dist Context-Preserve
Name: perl-%dist
Version: 0.01
Release: alt1

Summary: run code after a subroutine call, preserving the context the subroutine would have seen if it were the last statement in the caller
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 13 2010
BuildRequires: perl-Module-Install perl-Test-Exception perl-Test-use-ok

%description
Sometimes you need to call a function, get the results, act on the
results, then return the result of the function.  This is painful
because of contexts; the original function can behave different if
it's called in void, scalar, or list context.  You can ignore the
various cases and just pick one, but that's fragile.  To do things
right, you need to see which case you're being called in, and then
call the function in that context.  This results in 3 code paths,
which is a pain to type in (and maintain).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Context*

%changelog
* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.01-alt1
- initial revision, for DBIx::Class
