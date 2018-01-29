%define module_name rtl8723de
%define module_version 5.1.1.8

%define module_source %module_name.tar

Name: kernel-source-%module_name
Version: %module_version
Release: alt2%ubt

Group: Development/Kernel
Summary: Linux %module_name modules sources
License: GPL
URL: https://sourceforge.net/projects/e1000
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

BuildArch: noarch

Source: %name-%version.tar
Patch1: alt-build-time.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: kernel-build-tools

%description
%module_name modules sources for RTL8723DE Linux kernel driver

%prep
%setup -c -q
pushd %name-%version
%patch1 -p1
popd

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/kernel-source-%module_name-%version.tar.bz2 %name-%version

%files
%_usrsrc/*

%changelog
* Mon Jan 29 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt2%ubt
- remove build time

* Mon Jan 29 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt1%ubt
- initial build
