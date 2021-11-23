Name:		edid-decode
Version:	20211104
Release:	alt1

Summary:	EDID decoder and conformance tester
License:	MIT
Group:		System/Kernel and hardware
Url:		https://git.linuxtv.org/edid-decode.git/

Source:		%name-%version.tar

BuildRequires:	gcc-c++

%description
%summary

%prep
%setup

%build
%make

%install
%makeinstall

%files
%_bindir/*
%_man1dir/edid-decode.1*

%changelog
* Tue Nov 23 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 20211104-alt1
- updated from git.b00755e

* Wed Aug 26 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200720-alt1
- updated from git.56dd103

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 20170207-alt1.1
- NMU: added URL

* Mon May 29 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 20170207-alt1
- updated from git.cb0ee55

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 20100205-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue May 25 2010 Fr. Br. George <george@altlinux.ru> 20100205-alt1
- Initial build

