%define soname 1

Name: libsixel
Version: 1.10.3
Release: alt1

Summary: A SIXEL encoder/decoder implementation
License: MIT
Group: System/Libraries
URL: https://github.com/libsixel/libsixel

Source0: %name-%version.tar

BuildRequires(pre): meson

# Automatically added by buildreq on Fri Nov 23 2018 (-bb)
BuildRequires: libcurl-devel libgd3-devel libgdk-pixbuf-devel libjpeg-devel libnss-myhostname libpng-devel

%description
This package provides encoder/decoder implementation for DEC SIXEL graphics,
and some converter programs.

%package -n %{name}%{soname}
Summary: %summary
Group: System/Libraries
Provides: %name = %EVR

%description -n %{name}%{soname}
%summary

%package -n sixel-utils
Summary: %summary
Group: Graphics

%description -n sixel-utils
%summary

%package devel
Summary: %summary
Group: Development/C

%description devel
%summary

%package -n zsh-completion-%name
Summary: Zsh completion for %name
Group: Shells
BuildArch: noarch
Requires: %{name}%{soname} = %EVR

%description -n zsh-completion-%name
Zsh completion for %name.

%package -n bash-completion-%name
Summary: Bash completion for %name
Group: Shells
BuildArch: noarch
Requires: bash-completion
Requires: %{name}%{soname} = %EVR

%description -n bash-completion-%name
Bash completion for %name.

%prep
%setup -q

%build
%meson \
  -Dgdk-pixbuf2=enabled \
  -Dlibcurl=enabled
%meson_build -v

%install
%meson_install

rm -fv %buildroot%_libdir/*.a ||:

%files -n sixel-utils
%_bindir/img2sixel
%_bindir/sixel2png
%_man1dir/*

%files -n %{name}%{soname}
%_libdir/%name.so.*

%files devel
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_includedir/sixel.h
%_bindir/%name-config

%files -n zsh-completion-%name
%_datadir/zsh/site-functions/*

%files -n bash-completion-%name
%_datadir/bash-completion/completions/*

%changelog
* Thu Mar 30 2023 L.A. Kostis <lakostis@altlinux.ru> 1.10.3-alt1
- 1.10.3.
- switch to meson.
- Security fixes for CVE-2020-11721, CVE-2020-19668.

* Thu Oct 21 2021 Grigory Ustinov <grenka@altlinux.org> 1.8.5-alt2
- fixed FTBFS.

* Wed Sep 30 2020 Fr. Br. George <george@altlinux.ru> 1.8.5-alt1
- update to 1.8.5

* Mon Nov 26 2018 Denis Smirnov <mithraen@altlinux.ru> 1.8.2-alt2
- remove static library

* Fri Nov 23 2018 Denis Smirnov <mithraen@altlinux.ru> 1.8.2-alt1
- first build for Sisyphus
