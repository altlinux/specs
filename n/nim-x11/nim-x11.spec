%define _unpackaged_files_terminate_build 1

%def_with check

Name: nim-x11
Version: 1.2
Release: alt1

Summary: X11 wrapper for Nim
License: MIT
Group: Development/Other
Url: https://github.com/nim-lang/x11
Vcs: https://github.com/nim-lang/x11

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: nim
%if_with check
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXext-devel
%endif

%description
X11 wrapper library for the Nim programming language.
Provides bindings to the X11 display system.

%prep
%setup

%install
install -d %buildroot%_target_libdir_noarch/nim/lib/x11
install -m644 x11/*.nim %buildroot%_target_libdir_noarch/nim/lib/x11/

%check
nim c --path:. examples/x11ex.nim

%files
%doc LICENSE
%_target_libdir_noarch/nim/lib/x11/

%changelog
* Thu Jun 11 2026 Timofei Fedotov <sovtouch@altlinux.org> 1.2-alt1
- Initial build for ALT Sisyphus.
