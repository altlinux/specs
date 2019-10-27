Name: imgdiff
Version: 1.0
Release: alt3

Summary: diff for images
License: GPL
Group: Graphics

Packager: Vladislav Zavjalov <slazav@altlinux.org>
Source: %name-%version.tar

Requires: libgtkmm2
BuildRequires: gcc-c++ libgtkmm2-devel

%description
diff for images

%prep
%setup
sed -i 's,-pipe.*$,%optflags -std=c++11,' Makefile

%build
%make_build

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*

%changelog
* Sun Oct 27 2019 Michael Shigorin <mike@altlinux.org> 1.0-alt3
- E2K: explicit -std=c++11
- minor spec cleanup

* Sat Jun 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt2.qa1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0-alt2.qa1
- NMU: rebuilt for debuginfo.

* Tue Nov 25 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt2
- fix include

* Wed Jun 25 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt1
- initial version


