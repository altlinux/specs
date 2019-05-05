Name: rpm-macros-valgrind
Version: 0.1
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
* Sun May 05 2019 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on rpm-macros-luajit, slightly improved)
