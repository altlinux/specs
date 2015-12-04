Name: zabbix_tool
Version: 0.1
Release: alt4
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
%doc README.md LICENSE python_zabbix_assistant.py screen_creator make_graph_url

%changelog
* Fri Dec  4 2015 Terechkov Evgenii <evg@altlinux.org> 0.1-alt4
- git-20151204
- Add support for certificates checking/ignoring

* Mon Nov 30 2015 Terechkov Evgenii <evg@altlinux.org> 0.1-alt3
- git-20151130

* Sat Apr 12 2014 Terechkov Evgenii <evg@altlinux.org> 0.1-alt2
- Add search_host function

* Sat Apr 12 2014 Terechkov Evgenii <evg@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus
