%define _unpackaged_files_terminate_build 1
%define dovecot_confdir %_libdir/dovecot
%define dovecot_moduledir %dovecot_confdir/modules

Name: dovecot-fts-xapian
Version: 1.9.3
Release: alt1

Summary: Dovecot FTS plugin based on Xapian
License: LGPL-2.1-only
Group: System/Servers
Url: https://github.com/grosjo/fts-xapian
VCS: https://github.com/grosjo/fts-xapian

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: dovecot-devel
BuildRequires: gcc-c++
BuildRequires: libicu-devel
BuildRequires: libsqlite3-devel
BuildRequires: libxapian-devel

Requires: dovecot

%description
This plugin provides a straightforward, simple and maintenance free way
to configure the FTS (full text search) plugin for Dovecot, leveraging
the efforts by the Xapian.org team.

It came after the Dovecot team decided to deprecate "fts_squat" included
in the Dovecot core, and due to the complexity of the Solr plugin
capabilities, unneeded for most users.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--with-dovecot=%dovecot_confdir
%make_build

%install
%makeinstall_std
find %buildroot -name '*.la' -delete

%files
%doc AUTHORS COPYING README.md
%dovecot_moduledir/lib21_fts_xapian_plugin.so
%dir %dovecot_moduledir/settings
%dovecot_moduledir/settings/lib21_fts_xapian_settings.so

%changelog
* Fri Sep 18 2026 Egor Ignatov <egori@altlinux.org> 1.9.3-alt1
- First build for ALT.
