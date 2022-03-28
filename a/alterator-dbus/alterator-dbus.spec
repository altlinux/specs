%define dname ru.basealt.alterator

Name: alterator-dbus
Version: 0.0.4
Release: alt1

Summary: D-Bus woo-bus gate
License: GPL-2
Group: System/Configuration/Other

BuildRequires: cmake gcc
BuildRequires: glib2-devel libcurl-devel libdbus-glib-devel libpolkit-devel libsystemd-devel

Source0: %name-%version.tar

%description
D-Bus woo-bus gate.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std

%files
%_sbindir/%name
%_unitdir/%name.service
%_datadir/dbus-1/system.d/%dname.conf
%_datadir/polkit-1/actions/%dname.policy
%_datadir/polkit-1/rules.d/%dname.rules

%changelog
* Mon Mar 28 2022 Ivan Savin <svn17@altlinux.org> 0.0.4-alt1
- Added the ability to use boolean type function parameters in introspection

* Mon Feb 28 2022 Valery Sinelnikov <greh@altlinux.org> 0.0.3-alt1
- Used new define CONTENT_BETWEEN_METHODNAME_EMPTY
- Changed the method of generating a request
- Addede define CONTENT_BETWEEN_METHODNAME_EMPTY
- ActionName dynamic memory allocation for
  converting_answer_to_strings
- ActionName dynamic memory allocation for make_request_woobus


* Thu Jul 08 2021 Valery Sinelnikov <greh@altlinux.org> 0.0.2-alt3
- Fixed losing arguments when querying woobus

* Mon Jul 05 2021 Valery Sinelnikov <greh@altlinux.org> 0.0.2-alt2
- Fix for p9

* Fri Jul 02 2021 Valery Sinelnikov <greh@altlinux.org> 0.0.2-alt1
- Update to newest version 0.0.2

* Wed Apr 21 2021 Valery Sinelnikov <greh@altlinux.org> 0.0.1-alt1
- Initial build

