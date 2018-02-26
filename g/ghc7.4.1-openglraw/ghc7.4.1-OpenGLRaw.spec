%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name OpenGLRaw
%define f_pkg_name openglraw
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.2.0.0
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://www.haskell.org/haskellwiki/Opengl
Source: %name-%version.tar
Summary: A raw binding for the OpenGL graphics system



# Automatically added by buildreq on Sun Mar 18 2012 (-bb)
# optimized out: elfutils ghc7.4.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1 libGL-devel

%description
OpenGLRaw is a raw Haskell binding for the OpenGL 3.2 graphics system and
lots of OpenGL extensions. It is basically a 1:1 mapping of OpenGL's C API,
intended as a basis for a nicer interface. OpenGLRaw offers access to all
necessary functions, tokens and types plus a general facility for loading
extension entries. The module hierarchy closely mirrors the naming
structure of the OpenGL extensions, making it easy to find the right module
to import. All API entries are loaded dynamically, so no special C header
files are needed for building this package. If an API entry is not found at
runtime, a userError is thrown.

OpenGL is the industry's most widely used and supported 2D and 3D graphics
application programming interface (API), incorporating a broad set of
rendering, texture mapping, special effects, and other powerful
visualization functions. For more information about OpenGL and its various
extensions, please see <http://www.opengl.org/> and
<http://www.opengl.org/registry/>.

%prep
%setup

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

cd %buildroot%_datadir/doc/%name-%version
rm -rf doc LICENSE examples

%files -f %name-files.nonprof
%hs_pkgconfdir/%f_pkg_name-%version.conf
%doc dist/doc/html
#%%doc LICENSE examples

%changelog
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 1.2.0.0-alt1
- Spec created by cabal2rpm 0.20_08
