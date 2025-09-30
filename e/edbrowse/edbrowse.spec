Name: edbrowse
Version: 3.8.12
Release: alt2

Summary: ed-alike webbrowser written in C
License: GPL-1.0+
Group: Networking/WWW

Url: http://edbrowse.org/
Source0: https://github.com/CMB/edbrowse/archive/v%version.tar.gz#/%name-%version.tar.gz
Patch0: %name-3.8.12-alt-build-with-quickjs.patch

ExcludeArch: i586

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: libcurl-devel
BuildRequires: libssl-devel
BuildRequires: libreadline-devel
BuildRequires: libpcre2-devel
BuildRequires: libunixODBC-devel
BuildRequires: libduktape-devel
BuildRequires: quickjs-devel quickjs-devel-static

%description
edbrowse is a reimplementation of /bin/ed, with some basic
differences (it uses Perl regular expressions) with the ability to
visit webpages and ftp sites. edbrowse performs basic transformations
on the html source to produce a readable representation. edbrowse
supports Forms, Frames, Netscape-style cookies, HTTPS
connections and JavaScript.

%package doc
Summary: Documentation for ed-alike webbrowser
Group: Documentation
BuildArch: noarch

%description doc
edbrowse is a reimplementation of /bin/ed, with some basic
differences (it uses Perl regular expressions) with the ability to
visit webpages and ftp sites. edbrowse performs basic transformations
on the html source to produce a readable representation. edbrowse
supports Forms, Frames, Netscape-style cookies, HTTPS
connections and JavaScript.

This package contains Documentation and examples for the
edbrowse.

%package examples
Summary: Examples for ed-alike webbrowser
Group: Documentation
BuildArch: noarch

%description examples
edbrowse is a reimplementation of /bin/ed, with some basic
differences (it uses Perl regular expressions) with the ability to
visit webpages and ftp sites. edbrowse performs basic transformations
on the html source to produce a readable representation. edbrowse
supports Forms, Frames, Netscape-style cookies, HTTPS
connections and JavaScript.

This package contains Documentation and examples for the
edbrowse.

%prep
%setup
%patch0 -p1
sed -i -e 's|/usr/share/doc/edbrowse/usersguide.html|/usr/share/doc/edbrowse-doc-%version/usersguide.html|g' \
  doc/man-edbrowse-debian.1

%build
%make
%make_build

%install
install -Dm755 src/%name %buildroot%_bindir/%name
install -Dm644 doc/man-edbrowse-debian.1 %buildroot%_man1dir/%name.1

%files
%doc README CHANGES
%_man1dir/*
%_bindir/%name

%files doc
%doc doc/*.html

%files examples
%doc doc/*.ebrc

%changelog
* Tue Sep 30 2025 Nikolay Burykin <bne@altlinux.org> 3.8.12-alt2
- Fix path to usersguide.html in man page (Closes: #55089)

* Tue Jul 01 2025 Nikolay Burykin <bne@altlinux.org> 3.8.12-alt1
- 3.8.12

* Fri Feb 05 2021 Nikolay Burykin <bne@altlinux.org> 3.7.7-alt1
- Initial build for ALT

* Mon Oct 15 2018 Wei-Lun Chao <bluebat@member.fsf.org> 3.7.4
- Rebuild for Fedora
