Name: halibut
Version: 1.3
Release: alt1
License: MIT
Group: Text tools
Summary: Yet another free document preparation system
Source: %name-%version.tar.gz
Url: http://www.chiark.greenend.org.uk/~sgtatham/halibut/
Patch: gcc10.patch

# Automatically added by buildreq on Tue Jun 21 2022
# optimized out: cmake-modules glibc-kernheaders-generic libgpg-error libsasl2-3 perl python3-base sh4
BuildRequires: cmake

%description
Halibut is a documentation production system, with elements similar to
TeX, debiandoc-sgml, TeXinfo, and others. It is primarily targeted at
people producing software manuals.

%prep
%setup
#patch -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc %_defaultdocdir/%name
%_bindir/%name
%_man1dir/*
%_infodir/%{name}*

%changelog
* Tue Jun 21 2022 Fr. Br. George <george@altlinux.org> 1.3-alt1
- Autobuild version bump to 1.3

* Sat Jan 30 2021 Fr. Br. George <george@altlinux.ru> 1.2-alt2
- Fix gcc10 build
- Fix license field

* Mon Sep 25 2017 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Autobuild version bump to 1.2

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Aug 23 2010 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial build from scratch

