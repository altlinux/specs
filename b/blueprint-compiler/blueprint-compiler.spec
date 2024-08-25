%def_enable snapshot

%define ver_major 0.14
%define beta %nil
%define pypi_name blueprintcompiler
%def_enable docs
%def_enable check

Name: blueprint-compiler
Version: %ver_major.0
Release: alt1%beta

Summary: A markup language for GTK user interface files
Group: Development/GNOME and GTK+
License: GPL-3.0-or-later
Url: https://gitlab.gnome.org/jwestman/blueprint-compiler

%if_disabled snapshot
Source: %url/-/archive/v%version/%name-%version%beta.tar.bz2
%else
Vcs: https://gitlab.gnome.org/jwestman/blueprint-compiler.git
Source: %name-%version%beta.tar
%endif

BuildArch: noarch

Requires: typelib(GIRepository) = 2.0
Requires: typelib(Adw) = 1

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson
%{?_enable_check:BuildRequires: xvfb-run /bin/dbus-launch python3-module-pygobject3
BuildRequires: fontconfig at-spi2-core typelib(Adw) = 1}
%{?_enable_docs:BuildRequires: /usr/bin/sphinx-build-3 python3(sphinx_basic_ng) python3(furo)}

%description
%summary
See also https://jwestman.pages.gitlab.gnome.org/blueprint-compiler/

%prep
%setup -n %name-%version%beta

%build
%meson \
    %{subst_enable_meson_bool docs docs}
%nil
%meson_build
%if_enabled docs
pushd docs
meson compile docs -C ../%__builddir
popd
%endif

%install
%meson_install
%find_lang %name
%if_enabled docs
cp -a %__builddir/docs/en html
%endif

%check
xvfb-run %__meson_test -t 2

%files -f %name.lang
%_bindir/%name
%python3_sitelibdir_noarch/%pypi_name/
%_datadir/pkgconfig/%name.pc
%doc NEWS* README* %{?_enable_docs:html/}

%changelog
* Sun Aug 25 2024 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0
- packaged html documentation

* Fri Mar 22 2024 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Sat Jul 22 2023 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Mon Jun 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- updated to v0.8.1-2-g93392e5

* Fri Mar 17 2023 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1.1
- increased tests timeout for some slower machines, e.g. most modern
  riscv64 boards (voropaevdmtr@)

* Sun Nov 27 2022 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Mon Oct 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- first build for Sisyphus


