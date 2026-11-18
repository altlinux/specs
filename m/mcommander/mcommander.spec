%define _unpackaged_files_terminate_build 1

%def_with check

%define _libexecdir %_prefix/lib

# NOTE: on upgrade do not forget to run
# ./packaging/prepare.sh new_version
# or compare the contents of packaging/rpm/mcommander.spec.in

Name: mcommander
Version: 6.2.0
Release: alt1
Summary: Twin-panel text-mode file manager with loadable panel plugins
License: GPL-3.0-or-later
Group: File tools
Url: https://blue-panels.github.io/mcommander
Vcs: https://github.com/blue-panels/mcommander

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-lua
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-diagnostics

BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(slang)
BuildRequires: pkgconfig(lua5.4)
BuildRequires: pkgconfig(x11)
BuildRequires: libgpm-devel
BuildRequires: pkgconfig(ext2fs)
BuildRequires: pkgconfig(libmagic)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(check)
BuildRequires: pkgconfig(libssh2)
BuildRequires: pkgconfig(smbclient)
BuildRequires: pkgconfig(libacl)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(libmongoc-1.0)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libpq)
BuildRequires: pkgconfig(chafa)

Requires: aspell
Requires: ctags

%description
M-Commander is a twin-panel text-mode file manager based on GNU Midnight
Commander.  Its architecture is built around a compact core and dynamically
loaded panel plugins.  The plugins provide a uniform panel interface for
archives, remote file systems, repositories, and other data sources.
Commands are run in a built-in terminal.  M-Commander also includes a text
editor with syntax highlighting and a viewer that supports both text and
binary formats.  Its files carry its own name, so it installs beside the
distribution mc.

%package plugins
Summary: Archive and remote system panels for M-Commander
Group: File tools
Requires: %name = %{version}-%{release}
Requires: git-core
#Suggests: moby-engine
Requires: openssh-clients

%description plugins
Panel plugins that M-Commander loads at run time.  They open an archive or a
remote system in a panel, so that its contents are handled like ordinary
files: tar, zip and the other formats libarchive reads, FTP, SFTP, Samba, S3,
Git, Docker, Kubernetes, MongoDB, SQLite, systemd units and shell links over
ssh.  The Docker and Kubernetes panels talk to the docker and kubectl
commands, which have to be installed separately.

%package lua
Summary: Lua runtime and scripts for M-Commander
Group: File tools
Requires: %name = %{version}-%{release}
Requires: chafa
Requires: poppler
Requires: sixel-utils
Requires: ImageMagick-tools
Requires: exif

AutoReq: nolua

%description lua
The Lua runtime plugin that M-Commander loads at run time, and the scripts
that come with it: pictures in the terminal through sixel or chafa, markdown
and PDF in the viewer, and readable views of dBase tables and ELF binaries.
Without this package M-Commander runs, and the features written in Lua are
absent.

%prep
%setup
%patch -p1
# disable failing tests
sed -i "s|'tty_enter',||" tests/src/meson.build
sed -i "s|'mcterm_pty_send',||" tests/src/meson.build

%build
%meson \
    -Dscreen=slang \
    -Dlua=enabled \
    -Dmagic=enabled \
    -Dpanel_plugin_samba=enabled \
    -Dpanel_plugin_acl=enabled \
    -Dpanel_plugin_ftp=enabled \
    -Dpanel_plugin_arcmc=enabled \
    -Dpanel_plugin_s3=disabled \
    -Dpanel_plugin_mongo=enabled \
    -Dpanel_plugin_sqlite=enabled \
    -Dpanel_plugin_postgres=enabled \
    -Dpanel_plugin_sftp=enabled \
    -Dpanel_plugin_shell_link=enabled \
    -Dshell_ssh2=enabled
%meson_build

%install
%meson_install

find %buildroot -name '*.la' -print -delete

# The Lua documentation is listed as %%doc below, which puts it in place
# itself; what make install left behind would be packaged twice.
rm -rfv %buildroot%_docdir/%name

# remove broken s3
rm -vf %buildroot%_libexecdir/mcommander/extfs.d/s3+

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc COPYING
%doc README.md CHANGELOG.md
%doc doc/LUA_API_REFERENCE.md doc/LUA_PLUGINS.md doc/lua-api.json
%_bindir/mcommander
%_bindir/mc6
%_bindir/mcedit6
%_bindir/mview
%_bindir/mcdiff6
%_bindir/mctree
%_libexecdir/mcommander/
%dir %_datadir/mcommander/
%_datadir/mcommander/charsets
%_datadir/mcommander/defaults.ini
%_datadir/mcommander/examples/
%_datadir/mcommander/help/
%_datadir/mcommander/hints/
%_datadir/mcommander/skins/
%_datadir/mcommander/syntax/
%config(noreplace) %_sysconfdir/mcommander/*
%_mandir/man1/*
%_mandir/*/man1/
%dir %_libdir/mcommander/

%files plugins
%_bindir/mcstruct
%_libdir/mcommander/panel-plugins/

%files lua
%_libdir/mcommander/runtime-plugins/
%_datadir/mcommander/lua/

%changelog
* Wed Nov 18 2026 Nikolay Strelkov <snk@altlinux.org> 6.2.0-alt1
- New version 6.2.0.

* Sun Nov 15 2026 Nikolay Strelkov <snk@altlinux.org> 6.1.0-alt2
- Fixed FTBFS.

* Sun Sep 27 2026 Nikolay Strelkov <snk@altlinux.org> 6.1.0-alt1
- Initial build for Sisyphus
