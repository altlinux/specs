%define dist Mouse
Name: perl-%dist
Version: 0.95
Release: alt1

Summary: Moose minus the antlers
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# XXX syntax check fails
%define __spec_autodep_custom_pre export MOUSE_PUREPERL=1
%add_findreq_skiplist */Mouse/PurePerl.pm

# Automatically added by buildreq on Sun Oct 09 2011 (-bi)
BuildRequires: perl-HTTP-Message perl-IO-String perl-Locale-US perl-Module-Install perl-Moose perl-Package-Stash-XS perl-Params-Coerce perl-Path-Class perl-Regexp-Common perl-Test-Deep perl-Test-Output perl-autodie perl-threads

%description
Moose, a powerful metaobject-fuelled extension of the Perl 5 object system,
is wonderful.  Unfortunately, it's a little slow.  Though significant progress
has been made over the years, the compile time penalty is a non-starter for
some applications.  Mouse aims to alleviate this by providing a subset of
Moose's functionality, faster.

%prep
%setup -n %dist-%version

%build
export XSUBPP_NO_STATIC_XS=1
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Mouse*
%perl_vendor_autolib/Mouse*
%perl_vendor_archlib/ouse.pm
%perl_vendor_archlib/Squirrel*
%perl_vendor_archlib/Test

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.95-alt1
- 0.93 -> 0.95
- built for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1
- automated CPAN update

* Fri Feb 25 2011 Vladimir Lettiev <crux@altlinux.ru> 0.90-alt1
- 0.88 -> 0.90
- fixed build

* Tue Jan 25 2011 Alexey Tourbin <at@altlinux.ru> 0.88-alt1
- 0.40 -> 0.88

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Mar 22 2010 Victor Forsiuk <force@altlinux.org> 0.40-alt1
- 0.40

* Thu Oct 15 2009 Victor Forsyuk <force@altlinux.org> 0.39-alt1
- Initial build.
