%define dist perlindex
Name: perl-Text-English
Version: 1.605
Release: alt1

Summary: Pod indexer, Porter's stemming algorithm
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Patch0: perl-Text-English-1.302-alt-home-idir.patch
Patch1: perl-Text-English-1.302-alt-perldoc.patch

BuildArch: noarch

Provides: %dist = %version
Obsoletes: %dist < %version

# Automatically added by buildreq on Wed Dec 22 2010
BuildRequires: perl-DBM perl-IO-stringy perl-Term-ReadKey perl-devel perl-podlators perl4-compat

%description
perlindex is a program to index and search the perl documentation.
Text::English module is an implementation of the Porter stemming
algorithm.

%prep
%setup -q -n %dist-%version
%patch0 -p1
%patch1 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%_bindir/perlindex
%perl_vendor_privlib/Text*

%changelog
* Wed Dec 22 2010 Alexey Tourbin <at@altlinux.ru> 1.605-alt1
- 1.401 -> 1.605

* Tue Jul 19 2005 Alexey Tourbin <at@altlinux.ru> 1.401-alt1
- 1.302 -> 1.401
- manual pages not packaged (use perldoc)
- home-idir.patch: use $HOME/.perlindex whenever applicable
- export.patch: export/import stem() function
- perldoc.patch: simplify perldoc usage

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.302-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sat May 08 2004 Alexey Tourbin <at@altlinux.ru> 1.302-alt1
- 1.301 -> 1.302

* Tue Oct 07 2003 Alexey Tourbin <at@altlinux.ru> 1.301-alt1
- initial revision
