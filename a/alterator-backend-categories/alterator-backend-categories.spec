%define _unpackaged_files_terminate_build 1

Name: alterator-backend-categories
Version: 0.1.5
Release: alt1

Summary: Backend for Alterator categories
License: GPLv2+
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-backend-categories

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: python3-devel

Requires: alterator-interface-categories
Requires: alterator-manager >= 0.1.25
Requires: alterator-module-executor >= 0.1.29
Requires: alterator-entry >= 0.2.0
Requires: python3

%package -n alterator-interface-categories
Summary: Interface for Alterator categories
Group: System/Configuration/Other
Version: 0.1.0
Release: alt1

%description
Backend for Alterator categories.

%description -n alterator-interface-categories
Interface for Alterator categories.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/alterator/backends
mkdir -p %buildroot%_datadir/alterator/categories
mkdir -p %buildroot%_libexecdir/%name
mkdir -p %buildroot%_datadir/dbus-1/interfaces
mkdir -p %buildroot%_datadir/polkit-1/actions

install -v -p -m 644 -D categories.backend %buildroot%_datadir/alterator/backends
install -v -p -m 755 -D category-info %buildroot%_libexecdir/%name
install -v -p -m 755 -D list-categories %buildroot%_libexecdir/%name
install -v -p -m 644 -D org.altlinux.alterator.categories.xml %buildroot%_datadir/dbus-1/interfaces
install -v -p -m 644 -D org.altlinux.alterator.categories.policy %buildroot%_datadir/polkit-1/actions

%files
%doc LICENSE
%dir %_datadir/alterator/backends
%dir %_libexecdir/%name
%_datadir/alterator/backends/categories.backend
%_libexecdir/%name/category-info
%_libexecdir/%name/list-categories

%files -n alterator-interface-categories
%_datadir/polkit-1/actions/org.altlinux.alterator.categories.policy
%_datadir/dbus-1/interfaces/org.altlinux.alterator.categories.xml

%changelog
* Fri Nov 28 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.5-alt1
- Add 'exit_status = true' for new version of executor.

* Mon Jul 07 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.4-alt1
- Fix order of categories (thx Andrey Alekseev).

* Sat Jan 25 2025 Michael Chernigin <chernigin@altlinux.org> 0.1.3-alt1
- Rewrite scripts in python.

* Tue Dec 10 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.2-alt1
- Move to toml

* Mon Oct 21 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.1-alt1
- Change prefix from ru.basealt to org.altlinux.

* Tue Jun 25 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build.
