%define dist Tk-HistEntry
Name: perl-%dist
Version: 0.43_50
Release: alt1

Summary: Entry widget with history capability
Group: Development/Perl
License: GPL or Artistic

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Apr 23 2011
BuildRequires: perl-Tk perl-devel xvfb-run

%description
Tk::HistEntry implements an entry widget with history. You may use the
up and down keys to select older entries (or use the associated listbox).

%prep
%setup -q -n %dist-%version

%build
%ifndef _build_display
%def_without test
%endif

%perl_vendor_build
xvfb-run -a make test

%install
%perl_vendor_install

%files
%doc Changes README
%dir %perl_vendor_privlib/Tk
%perl_vendor_privlib/Tk/HistEntry.pm

%changelog
* Sat Apr 23 2011 Alexey Tourbin <at@altlinux.ru> 0.43_50-alt1
- 0.42 -> 0.43_50

* Mon May 22 2006 Alexey Tourbin <at@altlinux.ru> 0.42-alt2
- fixed segv in test by running fc-list (cpan #14355)

* Thu Jun 30 2005 Alexey Tourbin <at@altlinux.ru> 0.42-alt1
- initial revision (for perl-Tk-Pod)
