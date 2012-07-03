%define module txt2html
%define m_distro txt2html
%define m_name txt2html
%define _disable_test 1

Name: txt2html
Version: 2.51
Release: alt1.1

Summary: Convert raw text to something with a little HTML formatting

License: Artistic / GPL
Group: Text tools
Url: http://txt2html.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://downloads.sourceforge.net/%name/%name-%version.tar.bz2

# Automatically added by buildreq on Thu Sep 04 2008
BuildRequires: perl-Getopt-ArgvFile perl-Module-Build perl-YAML-Syck

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
This tools is intented to provide an easier way of
converting existing text documents to HTML format. txt2html can also
be used to aid in writing new HTML documents, but there are probably
better ways of doing that.

%prep
%setup -q

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/*
%perl_vendor_privlib/HTML/
%_man1dir/*

%changelog
* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 2.51-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Sep 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.51-alt1
- new version 2.51 (with rpmrb script)
- update buildreq
- fix directory ownership violation

* Mon Nov 12 2007 Vitaly Lipatov <lav@altlinux.ru> 2.46-alt1
- new version 2.46 (with rpmrb script)

* Fri Mar 16 2007 Vitaly Lipatov <lav@altlinux.ru> 2.44-alt1
- new version 2.44 (with rpmrb script)

* Tue Sep 06 2005 Vitaly Lipatov <lav@altlinux.ru> 2.42-alt0.1
- first build for ALT Linux Sisyphus
