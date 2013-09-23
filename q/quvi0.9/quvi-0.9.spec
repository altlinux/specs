%define _name quvi
%define ver_major 0.9

Name: %_name%ver_major
Version: %ver_major.3.1
Release: alt1

Summary: Command line tool for parsing video download links
Group: Networking/Other
License: LGPLv2+
Url: http://quvi.sourceforge.net/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: http://downloads.sourceforge.net/project/%name/%ver_major/%_name-%version.tar.xz

Conflicts: quvi

BuildRequires: lib%_name%ver_major-devel >= 0.9.3
BuildRequires: libgio-devel libxml2-devel libcurl-devel libjson-glib-devel
# for check
#BuildRequires: perl-Test-Deep perl-JSON perl-Test-Pod

%description
%name is a command line tool for parsing video download links. It
supports Youtube and other similar video websites.

%prep
%setup -n %_name-%version

%build
# Autoconf version 2.69 or higher is required
#%autoreconf
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
* Tue Sep 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.3.1-alt1
- first build for Sisyphus

