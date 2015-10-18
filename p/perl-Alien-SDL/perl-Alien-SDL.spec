BuildRequires: perl-podlators
%define _unpackaged_files_terminate_build 1
%define dist Alien-SDL
Name: perl-%dist
Version: 1.446
Release: alt1

Summary: Building, finding and using SDL binaries
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/F/FR/FROGGS/Alien-SDL-%{version}.tar.gz
Patch: %name-1.438-alt-norpath.patch

BuildArch: noarch

# Automatically added by buildreq on Sat Feb 26 2011
BuildRequires: libSDL-devel libsmpeg-devel perl-Archive-Extract perl-Archive-Tar perl-Archive-Zip perl-Capture-Tiny perl-Digest-SHA perl-File-Fetch perl-File-ShareDir perl-File-Which perl-Locale-Maketext-Lexicon perl-Module-Build perl-Text-Patch

%description
Alien::SDL can be used to detect and get configuration settings from an
installed SDL and related libraries.  Based on your platform it offers the
possibility to download and install prebuilt binaries or to build SDL & co.
from source codes.

%package scripts
Summary: %name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %name


%prep
%setup -q -n %dist-%version
%patch -p2

%build
#perl_vendor_build --with-sdl-config
echo 1 | %{__perl} Build.PL --installdirs=vendor
./Build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Alien

%files scripts
%_bindir/*
#%_man1dir/*


%changelog
* Sun Oct 18 2015 Igor Vlasenko <viy@altlinux.ru> 1.446-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.440-alt1
- automated CPAN update

* Mon Jan 07 2013 Vladimir Lettiev <crux@altlinux.ru> 1.438-alt2
- removed rpath option for linker

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.438-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.428-alt1
- automated CPAN update

* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 1.425-alt1
- initial revision
