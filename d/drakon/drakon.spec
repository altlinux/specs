%define oname drakon_editor
Name: drakon
Version: 1.13
Release: alt1.qa1

Summary: DRAKON Editor is a free cross-platform editor for the DRAKON visual language

License: Public domain
Group: Office
Url: http://drakon-editor.sourceforge.net/

Source: http://prdownloads.sf.net/drakon-editor/%oname%version.tar

%add_findreq_skiplist %_datadir/%name/examples/*
%add_findreq_skiplist %_datadir/%name/testdata/*

# TODO: package in separate package
%add_tcl_req_skip pdf4tcl::glyph2unicode pdf4tcl::stdmetrics

BuildRequires(pre): rpm-build-tcl tcl

BuildRequires: tcl

Requires: sqlite3-tcl tcl-img


%description
DRAKON Editor is a free cross-platform editor for the DRAKON visual language.

DRAKON language was developed within the Russian space program. Its
primary objective is presenting complex software systems in a way which
is easy to understand by humans.

DRAKON's motto: took a glance - understood at once.

This tool is aimed at software architects, developers and quality specialists.

%prep
%setup

%install
install -d %buildroot%_bindir/
cat <<EOF >%buildroot%_bindir/%name
#!/bin/sh
exec tclsh %_datadir/%name/%oname.tcl $$@
EOF

cat <<EOF >%buildroot%_bindir/drakon_gen
#!/bin/sh
exec tclsh %_datadir/%name/drakon_gen.tcl $$@
EOF

chmod 755 %buildroot%_bindir/*

install -d %buildroot%_datadir/%name/
cp -a . %buildroot%_datadir/%name/
rm -f %buildroot%_datadir/%name/readme.html
rm -rf %buildroot%_datadir/%name/docs/
rm -rf %buildroot%_datadir/%name/unittest/

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%files
%doc readme.html
%doc docs
%_bindir/%name
%_bindir/drakon_gen
%_datadir/%name/

%changelog
* Mon Aug 27 2012 Repocop Q. A. Robot <repocop@altlinux.org> 1.13-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * macos-ds-store-file-in-package for drakon

* Mon Aug 06 2012 Vitaly Lipatov <lav@altlinux.ru> 1.13-alt1
- initial build for ALT Linux Sisyphus
