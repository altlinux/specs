%define dist Class-Loader
Name: perl-%dist
Version: 2.03
Release: alt3

Summary: Load modules and create objects on demand
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: perl-Class-Loader-2.03-alt-no-cpan.patch

BuildArch: noarch

# Automatically added by buildreq on Thu Oct 06 2011
BuildRequires: perl-devel

%description
Certain applications like to defer the decision to use a particular module
till runtime. This is possible in perl, and is a useful trick in
situations where the type of data is not known at compile time and the
application doesn't wish to pre-compile modules to handle all types of
data it can work with. Loading modules at runtime can also provide
flexible interfaces for perl modules. Modules can let the programmer
decide what modules will be used by it instead of hard-coding their names.

Class::Loader is an inheritable class that provides a method, _load(),
to load a module from disk and construct an object by calling its
constructor. It also provides a way to map modules names and
associated metadata with symbolic names that can be used in place of
module names at _load().

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Class

%changelog
* Thu Oct 06 2011 Alexey Tourbin <at@altlinux.ru> 2.03-alt3
- don't permit installing from CPAN by default

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.03-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Sep 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.03-alt2
- fix directory ownership violation

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 2.03-alt1
- first build for ALT Linux Sisyphus
