%define _unpackaged_files_terminate_build 1

%def_with check

Name: gtimelog
Version: 0.12.0
Release: alt1

Summary: time logging application
License: GPL-2.0-only
Group: Office
URL: https://github.com/gtimelog/gtimelog

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: /usr/bin/rst2man
BuildRequires: /usr/bin/desktop-file-install

%if_with check
BuildRequires: python3(freezegun)
%endif

Requires: libsoup3.0-gir
Requires: libsecret-gir

BuildArch: noarch

Source: %name-%version.tar

%description
gtimelog provides a time tracking application to allow the user to track
what they work on during the day and how long they spend doing it.

%prep
%setup
sed -i "s/Categories=.*/Categories=GTK;Office;Calendar;ProjectManagement;/" gtimelog.desktop gtimelog.desktop.in

%build
%pyproject_build
%make all

%install
%pyproject_install

desktop-file-install \
                     --dir %buildroot%_desktopdir \
                     gtimelog.desktop

mkdir -p %buildroot%_iconsdir/hicolor/48x48/apps/
cp -v src/gtimelog/gtimelog.png %buildroot%_iconsdir/hicolor/48x48/apps/

install -Dpm 644 gtimelog.1 %buildroot%_man1dir/gtimelog.1
install -Dpm 644 gtimelog.appdata.xml %buildroot%_datadir/appdata/gtimelog.appdata.xml
install -Dpm 644 src/gtimelog/data/org.gtimelog.gschema.xml %buildroot%_datadir/glib-2.0/schemas/org.gtimelog.gschema.xml

%check
%__python3 ./runtests

%files
%doc CHANGES.rst CONTRIBUTING.rst src/gtimelog/CONTRIBUTORS.rst README.rst TODO.rst COPYING
%_bindir/gtimelog
%_man1dir/gtimelog.1.*
%_iconsdir/hicolor/48x48/apps/gtimelog.png
%_desktopdir/gtimelog.desktop
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}
%_datadir/appdata/gtimelog.appdata.xml
%_datadir/glib-2.0/schemas/org.gtimelog.gschema.xml

%changelog
* Sat Dec 13 2025 Nikolay Strelkov <snk@altlinux.org> 0.12.0-alt1
- Initial build for Sisyphus
