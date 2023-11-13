%define _name quvi
%define ver_major 0.9

Name: %_name
Version: %ver_major.5
Release: alt3

Summary: Command line tool for parsing video download links
Group: Networking/Other
#License: LGPLv2+
License: LGPL-2.1-or-later

Url: http://quvi.sourceforge.net/

Source: http://downloads.sourceforge.net/project/%name/%ver_major/%_name-%version.tar.xz

# opensuse
Patch0: reproducible.patch
Patch1: quvi-glibc-2.34.patch
# debian
Patch2: 0001-Fix-FTBFS-with-autoconf-2.70.patch

BuildRequires: lib%_name-devel >= 0.9.3
BuildRequires: libgio-devel libxml2-devel libcurl-devel libjson-glib-devel
# for check
#BuildRequires: perl-Test-Deep perl-JSON perl-Test-Pod

Conflicts: quvi0.9 <= 0.9.5-alt1
Obsoletes: quvi0.9 <= 0.9.5-alt1

%description
%name is a command line tool for parsing video download links. It
supports Youtube and other similar video websites.

%prep
%setup -n %_name-%version
%autopatch -p1

%build
# Autoconf version 2.69 or higher is required
%autoreconf
%configure
%make_build

%check
#%%make check

%install
%makeinstall_std

%files
%_bindir/%_name
%_man1dir/quvi-dump.1.*
%_man1dir/quvi-get.1.*
%_man1dir/quvi-info.1.*
%_man1dir/quvi-scan.1.*
%_man1dir/quvi.1.*
%_man5dir/quvirc.5.*

%doc AUTHORS NEWS README

%changelog
* Mon Nov 13 2023 Igor Vlasenko <viy@altlinux.org> 0.9.5-alt3
- fixed build (thanks to Debian patch)

* Mon Jan 24 2022 Igor Vlasenko <viy@altlinux.org> 0.9.5-alt2
- consolidated quvi and quvi0.9

* Mon Sep 15 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.5-alt1
- 0.9.5

* Fri Oct 25 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.4-alt1
- 0.9.4

* Tue Sep 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.3.1-alt1
- first build for Sisyphus

* Sat May 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.19-alt2
- used %autoreconf to fix RPATH problem

* Fri Aug 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.19-alt1
- 0.2.19

* Fri Jul 22 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.18-alt1
- 0.2.18 (ALT #25914)

* Thu May 12 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.15-alt1
- 0.2.15

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.14-alt1
- 0.2.14

* Fri Jan 28 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.12-alt1
- first build for Sisyphus

