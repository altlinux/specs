Name: perl-CHI
Version: 0.52
Release: alt1
Summary: CHI - Unified cache handling interface

Group: Development/Perl
License: Perl
Url: %CPAN CHI

BuildArch: noarch
# Cloned from git://github.com/jonswar/perl-chi.git
Source: %name-%version.tar
# TODO: build Makefile.PL with Dist::Zilla at build time
Patch: %name-%version-%release.patch
BuildRequires: perl-Log-Any perl-Time-Duration perl-Data-UUID perl-Try-Tiny perl-Moose perl-JSON perl-List-MoreUtils perl-Task-Weaken perl-Hash-MoreUtils perl-Digest-JHash perl-Time-Duration perl-Time-Duration-Parse perl-Carp-Assert perl-Test-Deep perl-Test-Exception perl-TimeDate perl-Test-Warn perl-Test-Class perl-IO-Compress perl-Cache-Cache perl-Cache-FastMmap

%description
%summary

%prep
%setup -q
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/CHI*
%exclude %perl_vendor_privlib/Pod/Weaver/Section/SeeAlsoCHI.pm
%doc Changes

%changelog
* Tue Apr 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.52-alt1
- New version 0.52

* Mon Dec 05 2011 Vladimir Lettiev <crux@altlinux.ru> 0.50-alt1
- New version 0.50

* Fri Jul 29 2011 Vladimir Lettiev <crux@altlinux.ru> 0.49-alt1
- initial build
