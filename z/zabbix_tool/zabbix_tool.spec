Name:       zabbix_tool
Version:    0.1
Release:    alt5

Summary:    Tool for CLI interaction with the Zabbix API
License:    MIT
Group:      Development/Python3
Url:        https://github.com/BrianGallew/zabbix_tool
Packager:   Evgenii Terechkov <evg@altlinux.org>

BuildArch:  noarch

Source:     %name.tar
Patch:      %name-alt.patch
Patch1:     port-on-python3.patch

Requires:   python3-module-zabbix-api


%description
Tool for CLI interaction with the Zabbix API

%prep
%setup -n %name
%patch -p1
%patch1 -p1

%build

%install
mkdir -p %buildroot%_bindir
install -m 755 %name %buildroot%_bindir/%name

%files
%_bindir/%name
%doc README.md LICENSE python_zabbix_assistant.py screen_creator make_graph_url


%changelog
* Wed Jan 29 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt5
- Porting on Python3.

* Fri Dec  4 2015 Terechkov Evgenii <evg@altlinux.org> 0.1-alt4
- git-20151204
- Add support for certificates checking/ignoring

* Mon Nov 30 2015 Terechkov Evgenii <evg@altlinux.org> 0.1-alt3
- git-20151130

* Sat Apr 12 2014 Terechkov Evgenii <evg@altlinux.org> 0.1-alt2
- Add search_host function

* Sat Apr 12 2014 Terechkov Evgenii <evg@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus
