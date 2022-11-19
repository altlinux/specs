%define ver_major 42
%define tag_ver release-%ver_major
%def_enable check

Name: cldr-emoji-annotation
Version: %ver_major
Release: alt1

# Annotation files are in Unicode license
Summary: Emoji annotation files in CLDR
Group: Development/Other
License: LGPL-2.0-or-later and Unicode
Url: https://github.com/unicode-org/cldr

Vcs: https://github.com/unicode-org/cldr.git
Source: %url/archive/%tag_ver.zip

BuildArch: noarch

BuildRequires: unzip xmllint

%description
This package provides the emoji annotation files by language in CLDR.
See http://cldr.unicode.org/translation/short-names-and-keywords

%package devel
Summary: Files for development using cldr-annotations
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package contains the pkg-config files for development
when building programs that use cldr-annotations.

%prep
%setup -n cldr-%tag_ver

%install
pushd $PWD
ANNOTATION_DIR=common/annotations
CLDR_DIR=%_datadir/unicode/cldr/$ANNOTATION_DIR
pushd $ANNOTATION_DIR
for xml in *.xml ; do
    install -pm 644 -D $xml $RPM_BUILD_ROOT$CLDR_DIR/$xml
done
popd

ANNOTATION_DIR=common/annotationsDerived
CLDR_DIR=%_datadir/unicode/cldr/$ANNOTATION_DIR
pushd $ANNOTATION_DIR
for xml in *.xml ; do
    install -pm 644 -D $xml $RPM_BUILD_ROOT$CLDR_DIR/$xml
done
popd

DTD_DIR=common/dtd
CLDR_DIR=%_datadir/unicode/cldr/$DTD_DIR
pushd $DTD_DIR
for dtd in *.dtd ; do
    install -pm 644 -D $dtd $RPM_BUILD_ROOT$CLDR_DIR/$dtd
done
popd

install -pm 755 -d $RPM_BUILD_ROOT%_datadir/pkgconfig
cat >> $RPM_BUILD_ROOT%_datadir/pkgconfig/%name.pc <<_EOF
prefix=/usr

Name: cldr-emoji-annotations
Description: annotation files in CLDR
Version: %version
_EOF

%check
ANNOTATION_DIR=common/annotations
CLDR_DIR=%_datadir/unicode/cldr/$ANNOTATION_DIR
for xml in $ANNOTATION_DIR/*.xml ; do
    xmllint --noout --valid --postvalid $xml
done

ANNOTATION_DIR=common/annotationsDerived
CLDR_DIR=%_datadir/unicode/cldr/$ANNOTATION_DIR
for xml in $ANNOTATION_DIR/*.xml ; do
    xmllint --noout --valid --postvalid $xml
done

%files
%_datadir/unicode/cldr/common/annotations
%_datadir/unicode/cldr/common/annotationsDerived
%dir %_datadir/unicode/cldr
%dir %_datadir/unicode/cldr/common
%_datadir/unicode/cldr/common/dtd
%doc README.md readme.html
%doc docs

%files devel
%_datadir/pkgconfig/*.pc

%changelog
* Thu Nov 17 2022 Yuri N. Sedunov <aris@altlinux.org> 42-alt1
- 42

* Mon Mar 14 2022 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0 (adapted fc spec)

* Tue Mar 17 2020 Yuri N. Sedunov <aris@altlinux.org> 36.12.120191002_0-alt1
- 36.12.120191002_0

* Thu Aug 22 2019 Yuri N. Sedunov <aris@altlinux.org> 35.12.14971_0-alt1
- first build for Sisyphus

