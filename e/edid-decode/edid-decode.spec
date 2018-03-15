Name:		edid-decode
Version:	20170207
Release:	alt1.1
Summary:	EDID decoder and conformance tester
Source:		%name-%version.tar
Group:		System/X11
License:	MIT
Url:		http://cgit.freedesktop.org/xorg/app/edid-decode/

%description
%summary

%prep
%setup

%build
%make

%install
%makeinstall
mkdir -p %buildroot/%_datadir
cp -a data %buildroot/%_datadir/

%files
%_bindir/*
%_datadir/data
%_man1dir/edid-decode.1*

%changelog
* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 20170207-alt1.1
- NMU: added URL

* Mon May 29 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 20170207-alt1
- updated from git.cb0ee55

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 20100205-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue May 25 2010 Fr. Br. George <george@altlinux.ru> 20100205-alt1
- Initial build

