%define _altdata_dir %_datadir/alterator

Name: alterator-net-l2tp
Version: 0.0.5
Release: alt1
Packager: Andriy Stepanov <stanv@altlinux.ru>
BuildArch: noarch
Source: %name-%version.tar
Url: http://www.altlinux.org/Alterator
Summary: Alterator module to configure L2TP connections
License: %gpl2plus
Group: System/Configuration/Other
Requires: alterator
Requires: alterator-sh-functions
Requires: alterator-net-functions
Requires: alterator-hw-functions
Requires: openl2tp
BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-macros-alterator
BuildRequires: alterator

%description
Alterator module to configure L2TP connections

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*
%_alterator_backend3dir/*
%_libexecdir/%name/

%changelog
* Thu Oct 20 2016 Andrey Cherepanov <cas@altlinux.org> 0.0.5-alt1
- Do not show this http module in alterator-browser-qt (ALT #32620)

* Tue Feb 10 2015 Andriy Stepanov <stanv@altlinux.ru> 0.0.4-alt1
- Add rpcbind startup helper

* Mon Feb 09 2015 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt2
- add file for previous build

* Mon Feb 09 2015 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt1
- Fix bool_default_route

* Thu Dec 25 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt1
- Add type check for hostname and interface name

* Mon Nov 17 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt1
- Initial build for ALTLinux Sisyphus
