Name: zabbix_tool
Version: 0.1
Release: alt2
Summary: Tool for CLI interaction with the Zabbix API

Group: Development/Python
License: MIT
Url: https://github.com/BrianGallew/zabbix_tool

Source: %name.tar
Patch: %name-alt.patch
Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch

%description
Tool for CLI interaction with the Zabbix API

%prep
%setup -n %name
%patch -p1

%build

%install
mkdir -p %buildroot%_bindir
install -m 755 %name %buildroot%_bindir/%name

%files
%_bindir/%name
%doc README.md LICENSE

%changelog
* Sat Apr 12 2014 Terechkov Evgenii <evg@altlinux.org> 0.1-alt2
- Add search_host function

* Sat Apr 12 2014 Terechkov Evgenii <evg@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus
