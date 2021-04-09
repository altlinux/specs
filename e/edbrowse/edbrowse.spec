Name: edbrowse
Version: 3.7.7
Release: alt1

Summary: ed-alike webbrowser written in C
License: GPL-1.0+
Group: Networking/WWW

Url: http://edbrowse.org/
Source0: https://github.com/CMB/edbrowse/archive/v%version.tar.gz#/%name-%version.tar.gz
Patch0: %name-%version-alt-pcre-and-tidy-warnings.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libcurl-devel
BuildRequires: libreadline-devel
BuildRequires: libpcre-devel
BuildRequires: libtidy-devel
BuildRequires: libduktape-devel

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
sed -i "s|%_docdir/%name|%_docdir/%name-%version|" CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc README CHANGES
%_man1dir/*
%_bindir/%name

%files doc
%doc doc/*.html

%files examples
%doc doc/*.ebrc

%changelog
* Fri Feb 05 2021 Nikolay Burykin <bne@altlinux.org> 3.7.7-alt1
- Initial build for ALT

* Mon Oct 15 2018 Wei-Lun Chao <bluebat@member.fsf.org> 3.7.4
- Rebuild for Fedora
