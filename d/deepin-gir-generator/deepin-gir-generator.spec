# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
BuildRequires: libgudev-gir
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
%global repo go-gir-generator

Name: deepin-gir-generator
Version: 3.0.4
Release: alt1

Summary: Generate static golang bindings for GObject

License: GPL-3.0+
Group: Other
Url: https://github.com/linuxdeepin/go-gir-generator

Source: %url/archive/%version/%repo-%version.tar.gz
Source1: gopath.tar
Source44: import.info

BuildArch: noarch

Provides: golang(gir/gobject-2.0)
Provides: golang(gir/gio-2.0)
Provides: golang(gir/glib-2.0)
Provides: golang(gir/gudev-1.0)

BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(gdk-3.0)

%description
Generate static golang bindings for GObject

%prep
%setup -n %repo-%version
# Unpacked vendor/ into the source (used .gear/tags).
tar -xf %SOURCE1
sed -i '/rm -rf/d' Makefile

%build
export GOPATH="$(pwd)/gopath:%go_path"
export GOFLAGS="-mod=vendor"
export GO111MODULE="off"
%make_build

%install
%makeinstall_std

%files
%doc README.md
%doc --no-dereference LICENSE
%go_path/src/github.com/linuxdeepin/go-gir/

%changelog
* Mon Apr 17 2023 Leontiy Volodin <lvol@altlinux.org> 3.0.4-alt1
- New version 3.0.4.
- NMU:
  + Built as noarch package.

* Wed Mar 29 2023 Leontiy Volodin <lvol@altlinux.org> 3.0.1-alt1
- New version 3.0.1.
- NMU:
  + Removed unneeded patches.
  + Cleanup spec.

* Wed Mar 16 2022 Leontiy Volodin <lvol@altlinux.org> 3.0.0-alt1
- new version (3.0.0) with rpmgs script

* Wed Mar 03 2021 Leontiy Volodin <lvol@altlinux.org> 2.0.2-alt3.gitd9225a1
- updated from commit d9225a117934f5776fd45c52e3eca2001c044c0f
- fixed build with golang 1.16

* Wed Jul 29 2020 Leontiy Volodin <lvol@altlinux.org> 2.0.2-alt2
- fixed build with glib 2.63 or later

* Tue Jul 21 2020 Leontiy Volodin <lvol@altlinux.org> 2.0.2-alt1.1
- rebuilt with armh

* Fri Sep 06 2019 Leontiy Volodin <lvol@altlinux.org> 2.0.2-alt1
- new version (2.0.2) with rpmgs script

* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_2
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_1
- update to new release by fcimport

* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_1
- new version

