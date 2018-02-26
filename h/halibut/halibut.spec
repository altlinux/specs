Name:		halibut
Version:	1.0
Release:	alt1
License:	BSD-like
Group:		Text tools
Summary:	Yet another free document preparation system
Source:		%name-%version.tar.gz
URL:		http://www.chiark.greenend.org.uk/~sgtatham/halibut/

%description
Halibut is a documentation production system, with elements similar to
TeX, debiandoc-sgml, TeXinfo, and others. It is primarily targeted at
people producing software manuals.

%prep
%setup

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
* Mon Aug 23 2010 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial build from scratch

