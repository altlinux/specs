%define dist Gtk2-ImageView
Name: perl-%dist
Version: 0.05
Release: alt3.1.1.1.1

Summary: Perl bindings for the GtkImageView widget
License: LPGL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: libgtkimageview-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Gtk2-devel perl-podlators

%description
Perl bindings to the GtkImageView image viewer widget
Find out more about GtkImageView at http://trac.bjourne.webfactional.com/.

The Perl bindings follow the C API very closely, and the C reference
should be considered the canonical documentation.

%prep
%setup -q -n %dist-%version

%ifndef _build_display
%def_without test
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	AUTHORS README examples
%dir	%perl_vendor_archlib/Gtk2
	%perl_vendor_archlib/Gtk2/ImageView.pm
%doc	%perl_vendor_archlib/Gtk2/ImageView.pod
	%perl_vendor_autolib/Gtk2
# XXX devel?
%dir	%perl_vendor_archlib/Gtk2/ImageView
%doc	%perl_vendor_archlib/Gtk2/ImageView/*.pod
%dir	%perl_vendor_archlib/Gtk2/ImageView/Tool
%doc	%perl_vendor_archlib/Gtk2/ImageView/Tool/*.pod
	%perl_vendor_archlib/Gtk2/ImageView/Install

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt3.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt3
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt2
- rebuilt for perl-5.16

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 0.05-alt1.2
- rebuilt for perl-5.14

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt1.1
- rebuilt with perl 5.12

* Sun Feb 07 2010 Vitaly Lipatov <lav@altlinux.ru> 0.05-alt1
- new version (0.05)

* Thu Dec 11 2008 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt1
- initial build for ALT Linux Sisyphus
