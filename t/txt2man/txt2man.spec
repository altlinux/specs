Name: txt2man
Version: 1.6.0
Release: alt1.1
Summary: Convert flat ASCII text to man page format

Group: Text tools
License: GPLv2+
Url: https://github.com/mvertes/txt2man
# Repacked %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

%filter_from_requires /^\/bin\/ksh/d

%description
tx2man is a shell script using gnu awk, that should run on any Unix-like
system. The syntax of the ASCII text is very straightforward and looks very
much like the output of the man(1) program.

%prep
%setup

%install
%makeinstall

%files
%doc COPYING Changelog README
%_bindir/*
%_man1dir/*

%changelog
* Sat Oct 17 2026 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1.1
- NMU: rebuild without the unused /bin/ksh requirement

* Wed Nov 30 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.6.0-alt1
- Updated to 1.6.0.

* Tue Aug 30 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.5.6-alt1
- Initial build from Fedora
