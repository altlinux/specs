Name: pidgin-gpg
Epoch: 1
Version: 0.9.3.0.1.git40a9f4c
Release: alt1

Summary: GPG/OpenGPG plugin for Pidgin

License: GPL-3.0-or-later
Group: Networking/Instant messaging
Url: https://github.com/segler-alex/Pidgin-GPG

VCS: git://git.altlinux.org/p/pidgin-gpg.git
Source: %name-%version-%release.tar
Source1: %name.watch

BuildRequires: libgpgme-devel libpurple-devel

%description
Select Tools > Plugins, and enable the GPG/OpenGPG plugin. Select
configure and choose your GPG key.

gpg-agent needs to be enabled for this plugin to work properly. You
may need to restart pidgin to be prompted for the key passphrase after
enabling this plugin.

%prep
%setup -n %name-%version-%release
%autoreconf

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_libdir/pidgin/pidgin_gpg.so

%changelog
* Wed Jul 08 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:0.9.3.0.1.git40a9f4c-alt1
- Update to v0.9.3-1-g40a9f4c (new upstream).
- Add watch file.

* Fri Mar 06 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9+git026bc8a-alt1
- Fixed version.
- Removed win dlls and aux script from sources.

* Thu Mar 05 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.5.0.47.git026bc8a-alt1
- Really build for Sisyphus.

* Sat Mar 09 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.5.0.47.git026bc8a-alt1
- Initial build for Sisyphus.


