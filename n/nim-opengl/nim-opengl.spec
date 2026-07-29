%define _unpackaged_files_terminate_build 1

#Without %check section and the conditional BuildRequires.
#Since all examples require OpenGL/GLUT, the previous %check using || :
#was not performing any effective build validation.

Name: nim-opengl
Version: 1.2.9
Release: alt1

Summary: OpenGL wrapper for Nim
License: MIT
Group: Development/Other
Url: https://github.com/nimgl/opengl
Vcs: https://github.com/nimgl/opengl

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: nim
BuildRequires: nim-x11

%description
OpenGL wrapper library for the Nim programming language.
Provides bindings to OpenGL, GLU, GLUT and GLX.

%prep
%setup

%install
# Main opengl.nim module
install -Dm644 src/opengl.nim \
    %buildroot%_target_libdir_noarch/nim/lib/opengl.nim

# opengl submodules
install -d %buildroot%_target_libdir_noarch/nim/lib/opengl
install -m644 src/opengl/*.nim \
    %buildroot%_target_libdir_noarch/nim/lib/opengl/

# private submodules
install -d %buildroot%_target_libdir_noarch/nim/lib/opengl/private
install -m644 src/opengl/private/*.nim \
    %buildroot%_target_libdir_noarch/nim/lib/opengl/private/

%files
%doc README.md LICENSE
%_target_libdir_noarch/nim/lib/opengl.nim
%_target_libdir_noarch/nim/lib/opengl/

%changelog
* Thu May 29 2026 Timofei Fedotov <sovtouch@altlinux.org> 1.2.9-alt1
- Initial build for ALT Sisyphus.
