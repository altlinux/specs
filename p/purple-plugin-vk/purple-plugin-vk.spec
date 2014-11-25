%add_findprov_lib_path %_libdir/purple-2
%define pidgin_ver 2.0.0

Name: purple-plugin-vk
Version: 0.9
Release: alt1.hg.r402
Summary: vk.com plugin for pidgin

Group: Networking/Instant messaging
License: %gpl3only
Url: https://bitbucket.org/olegoandreev/purple-vk-plugin
Packager: Vladimir Didenko <cow@altlinux.org>

Source0: %name-%version.tar

Requires: libpurple >= %pidgin_ver
BuildRequires(pre): rpm-build-licenses rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: pidgin-devel >= %pidgin_ver
BuildRequires: libxml2-devel

%description
Purple-vk-plugin is plugin for Pidgin that allows to receive
and send personal messages from web site Vk.com(VKontakte)

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%find_lang purple-vk-plugin

%files -f purple-vk-plugin.lang
%doc COPYING README.rst TODO.txt
%_libdir/purple-2/libpurple-vk-plugin.so
%_datadir/pixmaps/pidgin/emotes/vk
%_datadir/pixmaps/pidgin/protocols/*/vkontakte.png

%changelog
* Tue Nov 25 2014 Vladimir Didenko <cow@altlinux.org> 0.9-alt1.hg.r402
- r402

* Mon Jul 14 2014 Vladimir Didenko <cow@altlinux.org> 0.9-alt1.hg.r341
- Initial build
