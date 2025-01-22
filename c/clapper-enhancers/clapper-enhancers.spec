%def_disable snapshot

%define _name clapper
%define ver_major 0.8
%define api_ver 0.0
%define rdn_name com.github.rafostar.Clapper

%def_enable lbry
%def_enable peertube
%def_enable yt_dlp

%def_enable check

Name: %_name-enhancers
Version: %ver_major.1
Release: alt1

Summary: Plugins enhancing Clapper library capabilities
License: GPL-3.0-or-later
Group: Video
Url: https://github.com/Rafostar/clapper-enhancers

Vcs: https://github.com/Rafostar/clapper-enhancers.git

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.76
%define gtk_ver 4.10
%define adw_ver 1.4.0
%define gst_ver 1.24

Requires: %_name >= %ver_major
%{?_enable_yt_dlp:Requires: yt-dlp}

%add_python3_path %_libdir/%_name-%api_ver/enhancers

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-python3
BuildRequires: meson gcc-c++ vala-tools
BuildRequires: pkgconfig(clapper-%api_ver)
BuildRequires: pkgconfig(libpeas-2)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-tag-1.0)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(json-glib-1.0)

%description
Plugins enhancing Clapper media player library capabilities.

%prep
%setup -n %name-%version

%build
%meson \
    %{subst_enable_meson_feature lbry lbry} \
    %{subst_enable_meson_feature peertube peertube} \
    %{subst_enable_meson_feature yt_dlp yt-dlp}
%nil
%meson_build

%install
%meson_install
%find_lang --output=%name.lang %name

%check
%__meson_test

%files -f %name.lang
%dir %_libdir/%_name-%api_ver/enhancers/
%{?_enable_lbry:%_libdir/%_name-%api_ver/enhancers/lbry/}
%{?_enable_peertube:%_libdir/%_name-%api_ver/enhancers/peertube/}
%{?_enable_yt_dlp:%_libdir/%_name-%api_ver/enhancers/yt-dlp/}
%doc README*

%changelog
* Wed Jan 22 2025 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Tue Jan 21 2025 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- first build for Sisyphus


