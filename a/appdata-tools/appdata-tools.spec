%define _unpackaged_files_terminate_build 1

Name: appdata-tools
Version: 0.1.7
Release: alt1

Summary: Tools for AppData files
Group: Text tools
License: GPLv2+
Url: http://people.freedesktop.org/~hughsient/appdata/

Source: http://people.freedesktop.org/~hughsient/releases/%name-%version.tar.xz

BuildRequires: glib2-devel >= 2.26
BuildRequires: libsoup-devel libgdk-pixbuf-devel
BuildRequires: intltool docbook-dtds docbook-style-xsl xsltproc
BuildRequires: trang python-module-lxml >= 2.3
#BuildRequires: emacs-common emacs-leim

%description
appdata-tools contains a command line program designed to validate AppData
application descriptions for standards compliance and to the style guide.

%prep
%setup

%build
%configure --enable-schemas
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/appdata-validate
%dir %_datadir/appdata/schema
%_datadir/appdata/schema/appdata.xsd
%_datadir/appdata/schema/appdata.rnc
%_datadir/appdata/schema/appdata.rng
%_datadir/appdata/schema/appdata.sch
%_datadir/appdata/schema/schema-locating-rules.xml
%_datadir/aclocal/appdata-xml.m4
%_man1dir/appdata-validate.1.*
%doc AUTHORS NEWS README
%exclude %_datadir/emacs/site-lisp/site-start.d/appdata-rng-init.el

%changelog
* Tue Feb 04 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- first build for Sisyphus

