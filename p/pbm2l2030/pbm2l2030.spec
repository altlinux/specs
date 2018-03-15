Summary: Driver for the Lexmark 2030 printer

Name: pbm2l2030
Version: 1.4
Release: alt1.qa2

Packager: Stanislav Ievlev <inger@altlinux.org>

Group: Publishing
License: GPL
Url: http://home.fhtw-berlin.de/~s0226426/projects/pbm2l2030_faq.html
Source: %name-%version.tar

%description
Lexmark 2030 Color Jetprinter printer driver.

%prep

%setup -q

%build
%__cc %optflags -o pbm2l2030 pbm2l2030.c pbm.c

%install
%__install -Dpm 755 %name %buildroot%_bindir/%name

%files
%doc README* LICENSE *.pbm
%_bindir/*

%changelog
* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1.qa2
- NMU: added URL

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Nov 06 2007 Stanislav Ievlev <inger@altlinux.org> 1.4-alt1
- Initial build
