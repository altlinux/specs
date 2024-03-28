%define _unpackaged_files_terminate_build 1

Name: clipboard-base
Version: 0.9.0.1
Release: alt1

Summary: Your new, ridonkuliciously smart clipboard manager
License: GPLv3
Group: Accessibility
Url: https://getclipboard.app
Vcs: https://github.com/Slackadays/Clipboard

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: libalsa-devel
BuildRequires: libX11-devel
BuildRequires: libwayland-client-devel wayland-protocols libffi-devel

Source0: %name-%version.tar
Patch0: clipboard-0.9.0.1-alt-envVarIsTrue-warnings.patch

%description
The Clipboard Project is a fast and lightweight, feature packed, and user
friendly tool that lets you do more on the computer in style. Without 
libs for X11 Wayland and support.

%package -n clipboard-extension-X11
Summary: Smart clipboard manager with X11 support
Group: Accessibility
Requires: %name

%description -n clipboard-extension-X11
The Clipboard Project is a fast and lightweight, feature packed, and user
friendly tool that lets you do more on the computer in style. Libs for X11
support.

%package -n clipboard-extension-Wayland
Summary:  Smart clipboard manager with Wayland support
Group: Accessibility
Requires: %name

%description -n clipboard-extension-Wayland
The Clipboard Project is a fast and lightweight, feature packed, and user
friendly tool that lets you do more on the computer in style. Libs for
Wayland support.

%package -n clipboard
Summary:  Smart clipboard manager with X11 and Wayland support
Group: Accessibility
Requires: clipboard-extension-X11 clipboard-extension-Wayland

%description -n clipboard
The Clipboard Project is a fast and lightweight, feature packed, and user
friendly tool that lets you do more on the computer in style. Libs for X11
and Wayland support.

%prep
%setup
%patch -p1

%build
%cmake \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install
install -m644 -D documentation/completions/cb.fish %buildroot%_datadir/fish/vendor_completions.d/cb.fish
install -m644 -D documentation/completions/cb.zsh %buildroot%_datadir/zsh/site-functions/_cb


%files
%doc *.md
%doc documentation/readme-assets
%_bindir/cb
%_datadir/bash-completion/completions/cb
%_datadir/fish/vendor_completions.d/cb.fish
%_datadir/zsh/site-functions/_cb
%_mandir/man1/cb.1*

%files -n clipboard-extension-X11
%_libdir/libcbx11.so

%files -n clipboard-extension-Wayland
%_libdir/libcbwayland.so

%files -n clipboard

%changelog
* Thu Feb 08 2024 Elena Dyatlenko <lenka@altlinux.org> 0.9.0.1-alt1
- Initial build for Sisyphus.

