%define ext_dir  %{_libdir}/LibreOffice-still/share/extensions/
%define ext_name altcsp

Name: LibreOffice-plugin-altcsp
Version: 0.0.3
Release: alt1

Group: File tools
Summary: LibreOffice plugin for alt-csp-cryptopro
License: GPL-2.0-or-later

Source: %ext_name.tar
Requires: alt-csp-cryptopro

%description
LibreOffice plugin for alt-csp-cryptopro

%prep
# noop

%build
# noop

%install
install -dm0755 %buildroot%ext_dir/
cd %buildroot%ext_dir/
tar -xvf %SOURCE0
cp %_licensedir/%license %buildroot%ext_dir/%ext_name/license.txt

%files
%ext_dir/%ext_name/

%changelog
* Tue Jul 13 2021 Oleg Solovyov <mcpain@altlinux.org> 0.0.3-alt1
- write module on basic

* Tue May 11 2021 Oleg Solovyov <mcpain@altlinux.org> 0.0.2-alt2
- fix build

* Tue Apr 06 2021 Oleg Solovyov <mcpain@altlinux.org> 0.0.2-alt1
- add license to code

* Sat Apr 03 2021 Oleg Solovyov <mcpain@altlinux.org> 0.0.1-alt2
- remove unused files

* Wed Dec 09 2020 Oleg Solovyov <mcpain@altlinux.org> 0.0.1-alt1
- initial build

