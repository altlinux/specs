Name: zypak
Version: 2025.09
Release: alt2
Summary: Redirect natively sandboxed applications to use a custom sandbox environment
License: BSD
Group: System/Base
URL: https://github.com/refi64/zypak
Source0: zypak-%version.tar
Source1: nickle-0.1.tar
Source2: doctest-v2.4.12.tar

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: libsystemd-devel
BuildRequires: libdbus-devel
BuildRequires: python3-devel

%description
Zypak is a tool that redirects natively sandboxed applications (like Flatpak)
to use a custom sandbox environment.

%prep
%setup -a1 -a2

%build
sed -i 's/-Werror //g' Makefile
sed -i 's/-DZYPAK_RELEASE="\\"\$(shell git describe --tags --dirty)\\""/-DZYPAK_RELEASE="\\"%version\\""/' \
 Makefile
sed -i 's|/usr/bin/bash|/bin/bash|g' zypak-wrapper.sh
sed -i 's|/lib|/lib/zypak|g' zypak-wrapper.sh

%make_build

%install
install -Dm 755 zypak-wrapper.sh %buildroot%_bindir/zypak-wrapper.sh
install -Dm 755 build/zypak-helper %buildroot%_bindir/zypak-helper
install -Dm 755 build/zypak-sandbox %buildroot%_bindir/zypak-sandbox
ln -sf zypak-wrapper.sh %buildroot%_bindir/zypak-wrapper
install -d %buildroot%_libexecdir/zypak
find build -name "libzypak-*.so" -exec install -m 644 {} %buildroot%_libexecdir/zypak/ \;

%files
%doc README.md LICENSE
%_bindir/zypak-wrapper
%_bindir/zypak-wrapper.sh
%_bindir/zypak-helper
%_bindir/zypak-sandbox
%dir %_libexecdir/zypak
%_libexecdir/zypak/*.so

%changelog
* Mon Jan 26 2026 Anton Osipov <radiolamp@altlinux.org> 2025.09-alt2
- Fixed zypak-wrapper to handle new library paths.

* Fri Dec 26 2025 Anton Osipov <radiolamp@altlinux.org> 2025.09-alt1
- Initial package.
