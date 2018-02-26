Name:		browser-plugins-npapi
Version:	3.0
Release:	alt1
Summary:	Netscape Gecko Plug-in API common files
Group:		System/Base
License:	GPL3
Packager:	Alexey Gladkov <legion@altlinux.ru>

%description
This package contains directories for storage of plug-ins 
for NPAPI(Netscape Gecko Plug-in API) compatible browsers.

%package devel
Summary:	Netscape Gecko Plug-in API common packaging files 
Group:		Development/Other

%description devel
This package contains files for package NPAPI plugins.

%install
mkdir -p \
	%buildroot/%_libdir/browser-plugins \
	%buildroot/%_rpmmacrosdir \
	%buildroot/%_rpmlibdir

cat >%buildroot/%_rpmmacrosdir/%name<<EOF
%%browser_plugins_api	npapi
%%browser_plugins_path	%%_libdir/browser-plugins
EOF

cat >%buildroot/%_rpmlibdir/npapi-files.req.list<<EOF
/usr/lib/browser-plugins	%name
/usr/lib64/browser-plugins	%name
EOF

%files
%dir %_libdir/browser-plugins

%files devel
%_rpmmacrosdir/%name
%_rpmlibdir/npapi-files.req.list

%changelog
* Wed Oct 07 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1
- Add npapi-files.req.list

* Mon Sep 28 2009 Alexey Gladkov <legion@altlinux.ru> 2.0-alt1
- Rename %%_libdir/browser-plugins-npapi -> %%_libdir/browser-plugins

* Tue Nov 22 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt2
- package become an arch-specific.

* Tue Jan 04 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- first build for ALT linux.
