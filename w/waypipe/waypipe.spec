Name: waypipe
Version: 0.8.4
Release: alt1

Summary: Network transparency agent for Wayland

Group: Networking/Remote access
License: X11
URL: https://gitlab.freedesktop.org/mstoeckl/waypipe/

Source: %name-%version-%release.tar
# VCS: git://gitlab.freedesktop.org/mstoeckl/waypipe.git
#Patch: %name-%version-%release.patch

# 'man-pages' is always enabled.
# We can't embed a hyphen in a rpm macro name, and anyway
# one short man doesn't weigh much.
%def_with with_video
%def_with with_dmabuf
%def_with with_lz4
%def_with with_zstd
%def_with with_vaapi
%def_enable with_systemtap
%def_enable with_avx2
%def_enable with_avx512f
%def_enable with_sse3
%def_enable with_neon_opts

%define meson_subst_bool() %{expand:%%{?_enable_%{1}:-D%{1}=true}%%{?_disable_%{1}:-D%{1}=false}}
%define meson_subst_feature() %{expand:%%{?_with_%{1}:-D%{1}=enabled}%%{?_without_%{1}:-D%{1}=disabled}}

BuildRequires: meson >= 0.47.0
BuildRequires: gcc
%{?_with_with_video:BuildRequires: pkgconfig(libavcodec)}
%{?_with_with_video:BuildRequires: pkgconfig(libswscale)}
%{?_with_with_dmabuf:BuildRequires: libgbm-devel}
%{?_with_with_dmabuf:BuildRequires: pkgconfig(libdrm)}
%{?_with_with_lz4:BuildRequires: pkgconfig(liblz4)}
%{?_with_with_zstd:BuildRequires: pkgconfig(libzstd) >= 1.4.0}
%{?_with_with_vaapi:BuildRequires: pkgconfig(libva)}
%{?_enable_with_systemtap:BuildRequires: systemtap-sdt-devel}
BuildRequires: wayland-protocols >= 1.12
BuildRequires: libwayland-server-devel libwayland-client-devel
BuildRequires: scdoc

%define _unpackaged_files_terminate_build 1

%description
waypipe is a tool which can be used to relay both messages and data between any
Wayland client and compositor over a single transport channel. This should
enable Wayland-based workflows similar to those using `ssh -X'.

%prep
%setup -n %name-%version-%release
#patch -p1

%build
%meson \
    -D'man-pages=enabled'                \
    %{meson_subst_feature with_video}    \
    %{meson_subst_feature with_dmabuf}   \
    %{meson_subst_feature with_lz4}      \
    %{meson_subst_feature with_zstd}     \
    %{meson_subst_feature with_vaapi}    \
    %{meson_subst_bool with_systemtap}   \
    %{meson_subst_bool with_avx2}        \
    %{meson_subst_bool with_avx512f}     \
    %{meson_subst_bool with_sse3}        \
    %{meson_subst_bool with_neon_opts}   \
    #
%meson_build

%check
#export LC_ALL=en_US.UTF-8
export LC_CTYPE=en_US.UTF-8

%install
%meson_install

%files
%doc README.md COPYING
%_bindir/waypipe
%_man1dir/waypipe.1*

%changelog
* Sat Dec 03 2022 Arseny Maslennikov <arseny@altlinux.org> 0.8.4-alt1
- 0.8.2 -> 0.8.4.

* Thu Dec 16 2021 Arseny Maslennikov <arseny@altlinux.org> 0.8.2-alt1
- 0.8.1 -> 0.8.2.

* Thu Nov 04 2021 Arseny Maslennikov <arseny@altlinux.org> 0.8.1-alt1
- 0.8.0 -> 0.8.1.

* Wed May 05 2021 Arseny Maslennikov <arseny@altlinux.org> 0.8.0-alt1
- 0.7.2 -> 0.8.0.

* Tue Mar 02 2021 Arseny Maslennikov <arseny@altlinux.org> 0.7.2-alt1
- 0.6.1 -> 0.7.2.

* Sun Sep 01 2019 Arseny Maslennikov <arseny@altlinux.org> 0.6.1-alt1
- 0.6.0 -> 0.6.1.

* Tue Aug 20 2019 Arseny Maslennikov <arseny@altlinux.org> 0.6.0-alt1
- 0.4.0 -> 0.6.0.
- Built with libzstd.

* Tue Jul 30 2019 Arseny Maslennikov <arseny@altlinux.org> 0.4.0-alt1
- 0.3.0-29-gb9821d4 -> 0.4.0.

* Sat Jul 20 2019 Arseny Maslennikov <arseny@altlinux.org> 0.3.0.0.29.gitb9821d4-alt1
- 0.3.0-26-g99c24b9 -> 0.3.0-29-gb9821d4.

* Fri Jul 19 2019 Arseny Maslennikov <arseny@altlinux.org> 0.3.0.0.26.git99c24b9-alt1
- Initial build for ALT Sisyphus.
  The libzstd in Sisyphus is too old to be used by waypipe,
  so the package is built without libzstd for now.
