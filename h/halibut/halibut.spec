Name: halibut
Version: 1.2
Release: alt2
License: MIT
Group: Text tools
Summary: Yet another free document preparation system
Source: %name-%version.tar.gz
Url: http://www.chiark.greenend.org.uk/~sgtatham/halibut/
Patch: gcc10.patch

%description
Halibut is a documentation production system, with elements similar to
TeX, debiandoc-sgml, TeXinfo, and others. It is primarily targeted at
people producing software manuals.

%prep
%setup
%patch -p1

%build
%make_build
%make -C doc

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir
%makeinstall

%files
%_bindir/%name
%_man1dir/*

%changelog
* Sat Jan 30 2021 Fr. Br. George <george@altlinux.ru> 1.2-alt2
- Fix gcc10 build
- Fix license field

* Mon Sep 25 2017 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Autobuild version bump to 1.2

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Aug 23 2010 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial build from scratch

