Name: rpm-macros-valgrind
Version: 0.3
Release: alt1

Summary: arch macro to build valgrind clients
License: MIT
Group: Development/Other

Source: macros
BuildArch: noarch

%description
valgrind supports only some architectures.

This package provides macro with a list of architectures supported
by valgrind.

%install
install -pD %SOURCE0 %buildroot%_rpmmacrosdir/valgrind

%files
%_rpmmacrosdir/valgrind

%changelog
* Tue Nov 28 2023 Ivan A. Melnikov <iv@altlinux.org> 0.3-alt1
- %%valgrind_arches: drop ppc*, armh and mipsel,
  since valgrind is currently broken on these architectures.

* Thu Jun 20 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2-alt1
- %%valgrind_arches: add ppc, ppc64, ppc64le.

* Sun May 05 2019 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on rpm-macros-luajit, slightly improved)
