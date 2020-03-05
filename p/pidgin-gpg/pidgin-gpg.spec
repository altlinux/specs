Name: pidgin-gpg
Version: 0.5.0.47.git026bc8a
Release: alt1

Summary: GPG/OpenGPG plugin for Pidgin

License: GPL-3.0-or-later
Group: Networking/Instant messaging
Url: https://github.com/segler-alex/Pidgin-GPG

VCS: git://git.altlinux.org/p/pidgin-gpg.git
Source: %name-%version-%release.tar

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
* Thu Mar 05 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.5.0.47.git026bc8a-alt1
- Really build for Sisyphus.

* Sat Mar 09 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.5.0.47.git026bc8a-alt1
- Initial build for Sisyphus.


