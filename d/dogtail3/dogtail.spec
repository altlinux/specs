%define modname dogtail

Name: %{modname}3
Version: 0.9.11
Release: alt1

Summary: GUI test tool and automation framework
Group: Development/Other
License: GPL2
Url: https://gitlab.com/dogtail/dogtail

Source: %modname-%version.tar

BuildArch: noarch
Conflicts: %modname

# Mac OS X only
%add_python3_req_skip Accessibility

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: desktop-file-utils

%description
dogtail is a GUI test tool and automation framework written in Python.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

rm -rf %buildroot%_docdir/dogtail/
find examples -type f -exec chmod 0644 \{\} \;

%files
%_bindir/*
%python3_sitelibdir/%modname/
%python3_sitelibdir/%modname-*.egg-info
%_desktopdir/*
%_datadir/%modname/
%_iconsdir/hicolor/scalable/*
%doc ChangeLog README* examples/

%changelog
* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 0.9.11-alt1
- first build for Sisyphus (DOGTAIL_0_9_11-5-ge9424a1)

