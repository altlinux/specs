%add_findprov_lib_path %_libdir/purple-2
%define pidgin_ver 2.0.0

Name: purple-plugin-microblog
Version: 0.3.0
Release: alt1
Summary: Libpurple (Pidgin) plug-in supporting microblog services like Twitter

Group:   Networking/Instant messaging
License: %gpl3only
Url: 	 http://code.google.com/p/microblog-purple/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: mbpurple-%version.tar

Requires: libpurple >= %pidgin_ver
BuildRequires(pre): rpm-build-licenses
BuildRequires: pidgin-devel >= %pidgin_ver
BuildRequires: libxml2-devel

%description
Purple-vk-plugin is plugin for Pidgin that allows to receive
and send personal messages from web site Vk.com(VKontakte)

%prep
%setup -q -n mbpurple-%version

%build
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc README.txt
%_libdir/purple-2/*.so
%_datadir/pixmaps/pidgin/protocols/*/*.png
%_datadir/purple/ca-certs/EquifaxSecureGlobaleBusinessCA.pem

%changelog
* Wed Mar 18 2015 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- Initial build in Sisyphus

