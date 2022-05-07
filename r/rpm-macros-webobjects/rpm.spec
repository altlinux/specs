Name:		rpm-macros-webobjects
Version:	5.4
Release:	alt2
Summary:	RPM macros to WebObjects libraries
Summary(ru_RU.UTF-8): набор RPM макросов для упаковки WebObjects-пакетов

License:	BSD-like
Group:		Development/Other
BuildArch: 	noarch

Packager:  	Gennady Kushnir <baywind@altlinux.org>

Source1:	webobjects.rpm-macros

%description
The package provides a set of macros for packaging WebObjects applications

%install
install -pD -m644 %SOURCE1 %buildroot%_rpmmacrosdir/%name

%files
%_rpmmacrosdir/%name

%changelog
* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 5.4-alt2
- NMU: use %%_rpmmacrosdir instead of /etc/rpm

* Wed Sep 15 2010 Gennady Kushnir <baywind@altlinux.org> 5.4-alt1
- Initial release
