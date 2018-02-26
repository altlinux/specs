Name: sgmltools-lite
Version: 3.0.3
Release: alt6.2.1

Summary: Transforms SGML DocBook files to various formats
Group: Publishing
License: GPL
Url: http://sgmltools-lite.sourceforge.net
Packager: Yuri N. Sedunov <aris@altlinux.ru>
BuildArch: noarch

Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.bz2
Patch0: %name-3.0.3-cvs-20020815.patch
Patch1: %name-3.0.3-deb-fixes.patch

Requires: docbook-style-dsssl jadetex
# hack
Provides: python%__python_version(Backend), python%__python_version(utils)

BuildRequires: openjade, python

%description
This package contains some scripts to transform SGML (not XML) DocBook
(with some limitations LinuxDoc) source code to various formats,
including PDF, PostScript, DVI, HTML, ASCII, iSilo, and RTF.

%{expand:%define sgml_base_dir		%(sed -ne 's/^SGML_BASE_DIR=\\(.\\+\\)/\\1/p' `sgmlwhich`)}
%{expand:%define sgml_catalogs_dir	%(sed -ne 's/^SGML_CATALOGS_DIR=\\(.\\+\\)/\\1/p' `sgmlwhich`)}
%{expand:%define openjade_catalog	%(find %sgml_base_dir -type f -path '*openjade*/catalog')}
%{expand:%define iso_entities_catalog	%(find %sgml_base_dir -type f -path '*iso-entities-8879.1986*/catalog')}
%define dsssldir		%sgml_base_dir/docbook/dsssl-stylesheets
%define sgmltools_dir		%sgml_base_dir/stylesheets/sgmltools
%define sgmltools_dtd_dir	%sgml_base_dir/dtd/sgmltools
%define sgmltools_python_dir	%sgml_base_dir/misc/sgmltools/python

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
export ac_cv_path_W3M=no
export ac_cv_path_LYNX=/usr/bin/lynx
%configure --with-etcsgml=%sgml_catalogs_dir --with-dbimages=%dsssldir/images
%make_build

%install
# make install specific we create own catalog tree
%__mkdir_p %buildroot{%_bindir,%sgmltools_dir,%sgmltools_dtd_dir,\
%sgmltools_python_dir/backends,%sgml_catalogs_dir,%_man1dir}

%__install -m755 bin/{sgmltools,gensgmlenv,buildcat} %buildroot%_bindir/
%__install -m644 dsssl/{*.dsl,*.cat} %buildroot%sgmltools_dir/
%__install -m644 dtd/[a-z]* %buildroot%sgmltools_dtd_dir/
%__install -m644 python/*.py %buildroot%sgmltools_python_dir/
%__install -m644 python/backends/*.py %buildroot%sgmltools_python_dir/backends/
%__install -m644 VERSION %buildroot%sgml_base_dir/misc/sgmltools/
%__install -m644 aliases %buildroot%sgml_catalogs_dir/aliases
%__install -m644 man/sgmltools-lite.1 %buildroot%_man1dir/

# Create catalog for %name
%__cat <<__EOF__ >%name.cat
CATALOG "%sgmltools_dtd_dir/catalog"
CATALOG "%sgmltools_dir/sgmltools.cat"
CATALOG "%openjade_catalog"
CATALOG "%iso_entities_catalog"
__EOF__

%__install -pD -m644 %name.cat %buildroot%sgml_catalogs_dir/sgml-linuxdoc.cat

%define catalog_entry CATALOG "%sgml_catalogs_dir/sgml-linuxdoc.cat"

%post
echo '%catalog_entry' >> %sgml_catalogs_dir/catalog

%preun
if [ "$1" -eq 0 -a -s %sgml_catalogs_dir/catalog ]; then
	%__subst '\|%catalog_entry|d' %sgml_catalogs_dir/catalog ||:
fi

%files
%_bindir/*
%_man1dir/*
%sgmltools_dir
%sgmltools_dtd_dir
%sgml_base_dir/misc/sgmltools
%config %sgml_catalogs_dir/*
%doc README *INSTALL index.html

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.3-alt6.2.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt6.2
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 3.0.3-alt6.1
- Rebuilt with python-2.5.

* Sun Sep 04 2005 Dmitry V. Levin <ldv@altlinux.org> 3.0.3-alt6
- Specfile cleanup.

* Tue Jun 01 2004 Alexey Voinov <voins@altlinux.ru> 3.0.3-alt5.1
- rebuild with new openjade and new python
- added provides for new python

* Sun Nov 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 3.0.3-alt5
- Removed dependence on w3m.

* Thu Apr 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 3.0.3-alt4
- broken pipe bug fixed.
- man page improved.
- sgml catalog files selection in Ld2db.py fixed (#781). Also thanks
  Maxim Dzumanenko <mvd@altlinux.ru>

* Wed Jan 30 2002 Yuri N. Sedunov <aris@altlinux.ru> 3.0.3-alt3
- more cleanups

* Tue Jan 29 2002 Konstantin Volckov <goldhead@altlinux.ru> 3.0.3-alt2
- Rebuilt with python-2.2
- Some spec cleanup

* Wed Nov 28 2001 Yuri N. Sedunov <aris@altlinux.ru> 3.0.3-alt1
- first build for Sisyphus
