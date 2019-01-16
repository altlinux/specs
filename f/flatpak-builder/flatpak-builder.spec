%define _localstatedir %_var
%define _libexecdir %_prefix/libexec
%define _userunitdir %_prefix/lib/systemd/user

%def_enable docs

Name: flatpak-builder
Version: 1.0.2
Release: alt1
Epoch:1

Summary: Tool to build flatpaks from source
Group: Development/Other
License: LGPLv2+
Url: http://flatpak.org/

# VCS: https://github.com/flatpak/flatpak-builder.git
Source: https://github.com/flatpak/flatpak-builder/releases/download/%version/%name-%version.tar.xz

%define glib_ver 2.44
%define ostree_ver 2017.14
%define flatpak_ver 0.99.1

Requires: flatpak >= %flatpak_ver
Requires: libostree >= %ostree_ver
Requires: /usr/bin/bzip2
Requires: /usr/bin/bzr
Requires: /usr/bin/eu-strip
Requires: /usr/bin/git
Requires: /usr/bin/patch
Requires: /usr/bin/rofiles-fuse
Requires: /usr/bin/strip
Requires: /usr/bin/svn
Requires: /bin/tar
Requires: /usr/bin/unzip

BuildRequires: flatpak >= %flatpak_ver
BuildRequires: libcap-devel
BuildRequires: libdwarf-devel
BuildRequires: pkgconfig(glib-2.0) >= %glib_ver
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libelf)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(ostree-1) >= %ostree_ver
BuildRequires: pkgconfig(yaml-0.1)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: libcurl-devel
BuildRequires: xsltproc
%{?_enable_docs:BuildRequires: xmlto docbook-dtds docbook-style-xsl}

%description
Flatpak-builder is a tool for building flatpaks from sources.

See http://flatpak.org/ for more information.

%prep
%setup

%build
%autoreconf
%configure \
    %{?_enable_docs--enable-docbook-docs} \
    --with-dwarf-header=%_includedir/libdwarf
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/%name.1*
%_man5dir/flatpak-manifest.5*
%{?_enable_docs:%doc %_docdir/%name}

%changelog
* Wed Jan 16 2019 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.2-alt1
- 1.0.2

* Thu Nov 29 2018 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.1-alt1
- 1.0.1

* Wed Aug 22 2018 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt1
- 1.0.0

* Sun May 27 2018 Yuri N. Sedunov <aris@altlinux.org> 1:0.10.10-alt1
- first build for Sisyphus

