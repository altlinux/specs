Name: tc-netsysinfo
Version: 0.0.3
Release: alt1
License: %gpl2plus
Group: System/Configuration/Other
Summary: Thin client identification tool
Packager: Packager: Andriy Stepanov <stanv@altlinux.ru>

Source: %name-%version.tar

BuildPreReq: python-modules-encodings
BuildPreReq: rpm-build-licenses

BuildArch: noarch

%description
Thin client identification.
Tool written by Ivan Ovcherenko (asdus@altlinux.org).

%prep
%setup -q

%install
install -D -m 755 %name-init %buildroot%_initdir/%name
install -D -m 755 %name %buildroot%_sbindir/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%_initdir/%name
%_sbindir/%name

%changelog
* Mon Jun 25 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt1
- Fix init-script

* Mon Jun 25 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt1
- Fix init-script

* Mon Jun 25 2012 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt1
- Initial build

