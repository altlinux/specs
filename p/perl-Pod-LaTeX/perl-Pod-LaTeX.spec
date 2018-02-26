%define dist Pod-LaTeX
Name: perl-%dist
Version: 0.59
Release: alt1

Summary: Convert Pod data to formatted Latex
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 28 2011
BuildRequires: perl-Module-Build perl-Pod-Parser

%description
Pod::LaTeX is a module to convert documentation in the Pod format
into Latex.  The pod2latex command uses this module for translation.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/Pod
%_bindir/pod2latex

%changelog
* Thu Apr 28 2011 Alexey Tourbin <at@altlinux.ru> 0.59-alt1
- initial revision
