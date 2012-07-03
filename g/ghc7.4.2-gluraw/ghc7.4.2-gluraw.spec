%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name GLURaw
%define f_pkg_name gluraw
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.2.0.0
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://www.haskell.org/haskellwiki/Opengl
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A raw binding for the OpenGL graphics system



# Automatically added by buildreq on Sun Jul 01 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-common libGL-devel libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-alex ghc7.4.2-cpphs ghc7.4.2-doc ghc7.4.2-happy ghc7.4.2-openglraw libGLU-devel

%description
GLURaw is a raw Haskell binding for the GLU 1.3 OpenGL utility library. It
is basically a 1:1 mapping of GLU's C API, intended as a basis for a nicer
interface.

OpenGL is the industry's most widely used and supported 2D and 3D graphics
application programming interface (API), incorporating a broad set of
rendering, texture mapping, special effects, and other powerful
visualization functions. For more information about OpenGL and its various
extensions, please see <http://www.opengl.org/> and
<http://www.opengl.org/registry/>.

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all
%hs_pkgconfdir/%f_pkg_name-%version.conf
%_docdir/%name-%version

%changelog
* Sat Jun 30 2012 Denis Smirnov <mithraen@altlinux.ru> 1.2.0.0-alt1
- Spec created by cabal2rpm 0.20_08
