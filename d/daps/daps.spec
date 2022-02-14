Name:     daps
Version:  3.3.1
Release:  alt1

Summary:  DocBook Authoring and Publishing Suite (DAPS)
License:  GPL-2.0 or GPL-3.0
Group:    Other
Url:      https://github.com/openSUSE/daps

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch1: daps-remove-isopub.ent.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: ImageMagick
BuildRequires: dia
BuildRequires: docbook-dtds
BuildRequires: docbook-style-xsl
BuildRequires: docbook5-schemas
BuildRequires: docbook5-style-xsl
BuildRequires: fop
BuildRequires: ghostscript
BuildRequires: inkscape
BuildRequires: python3-module-libxml2
BuildRequires: python3-module-lxml
BuildRequires: sgml-common
BuildRequires: w3m
BuildRequires: xml-commons-apis
BuildRequires: xmlstarlet
BuildRequires: xsltproc
BuildRequires: zip
BuildRequires: asciidoctor
BuildRequires: epubcheck
BuildRequires: jing
BuildRequires: trang
BuildRequires: perl-Config-IniFiles
BuildRequires: perl-File-Copy-Recursive
BuildRequires: perl-File-Rsync
BuildRequires: perl-Image-ExifTool
BuildRequires: optipng
BuildRequires: xfig

BuildArch: noarch

%filter_from_requires /jing/d

%description
A complete environment to build HTML, PDF, EPUB and other formats from
DocBook XML. See https://github.com/openSUSE/daps for more information.
Documentation is available from
https://opensuse.github.io/daps/doc/index.html.

%package docs
Summary: Documentation for DAPS
Group: Development/Documentation

%description docs
Documentation for %name.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure \
	--disable-edit-rootcatalog
%make_build redhat

%install
%makeinstall_std

%check
%make_build check

%files
%doc AUTHORS README.adoc COPYING
%_sysconfdir/%name
%_bindir/*
%_man1dir/*
%_datadir/%name
%_sysconfdir/xml/catalog.d/daps.xml
%_datadir/bash-completion/completions/daps
%_datadir/emacs/site-lisp/docbook_macros.el
%_datadir/xml/daps/schema/daps-autobuild.rnc

%files docs
%_datadir/doc/%name

%changelog
* Mon Feb 14 2022 Andrey Cherepanov <cas@altlinux.org> 3.3.1-alt1
- New version.

* Tue Feb 08 2022 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1
- New version.

* Fri Jun 11 2021 Andrey Cherepanov <cas@altlinux.org> 3.2.0-alt1
- New version.

* Sat May 22 2021 Andrey Cherepanov <cas@altlinux.org> 3.1.2-alt1
- New version.

* Wed May 12 2021 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- New version.

* Tue May 11 2021 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version.

* Mon May 03 2021 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt2
- Add rpm-build-python3 to build requirements.

* Thu May 14 2020 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus
