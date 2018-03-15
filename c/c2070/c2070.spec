Summary:	Lexmark 2070 Printer color driver
Name:		c2070
Version:	0.99
Release:	alt1.qa2
Group:		Publishing
License:	GPL
URL:		http://www.linuxprinting.org/show_driver.cgi?driver=c2070

Packager: Stanislav Ievlev <inger@altlinux.org>

Source:	%name-%version.tar
Patch: c2070-0.99-mdk-looplimits.patch

%description
This filter allows to color print in a Lexmark 2070 (windows GDI) printer.

%prep

%setup -q

%patch -p1

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install

%__install -Dpm755 %name %buildroot/%_bindir/%name

%files
%doc LICENSE README
%_bindir/*


%changelog
* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1.qa2
- NMU: added URL

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.99-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Nov 06 2007 Stanislav Ievlev <inger@altlinux.org> 0.99-alt1
- Initial build

