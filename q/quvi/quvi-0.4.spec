%define ver_major 0.4

Name: quvi
Version: %ver_major.2
Release: alt1

Summary: Command line tool for parsing video download links
Group: Networking/Other
License: LGPLv2+
Url: http://quvi.sourceforge.net/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: http://downloads.sourceforge.net/project/%name/%ver_major/%name-%version.tar.xz

BuildRequires: lib%name-devel > 0.4.0
BuildRequires: libcurl-devel
# for check
#BuildRequires: perl-Test-Deep perl-JSON perl-Test-Pod

%description
%name is a command line tool for parsing video download links. It
supports Youtube and other similar video websites.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%check
#%%make check

%install
%make DESTDIR=%buildroot install

%files
%_bindir/%name
%_man1dir/%name.*
%doc AUTHORS NEWS README

%changelog
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

