Name: wordnet
Version: 3.0
Release: alt7

Summary: WordNet English lexical reference system
License: MIT
Group: Text tools
Url: http://wordnet.princeton.edu/
# http://wordnetcode.princeton.edu/%version/WordNet-%version.tar.bz2
Source: WordNet-%version.tar
Source1: %name.png
Patch01: wordnet-3.0-deb-bound-CVE-2008-2149.patch
Patch02: wordnet-3.0-ocert-bound-CVE-2008-3908.patch
Patch03: wordnet-3.0-deb-bound-CVE-2008-3908.patch
Patch04: wordnet-3.0-rh-man.patch
Patch05: wordnet-3.0-alt-wordnet-dir.patch
Patch06: wordnet-3.0-deb-stubs.patch
Patch07: wordnet-3.0-rh-tk.patch
Patch08: wordnet-3.0-rh-libtool.patch
Patch09: wordnet-3.0-alt-doc.patch
Patch10: wordnet-3.0-alt-DICTDIR.patch
Patch11: wordnet-3.0-deb-adjunct-derivation.patch
Patch12: wordnet-3.0-alt-wishwn.patch
Patch13: wordnet-3.0-alt-warnings.patch

Requires: lib%name = %version-%release
Requires: %name-dict = %version-%release
BuildRequires: tk-devel

%define _libexecdir /usr/libexec
%def_disable static

%description
WordNet is an online lexical reference system whose design is
inspired by current psycholinguistic theories of human lexical
memory.  English nouns, verbs, adjectives and adverbs are organized
into synonym sets, each representing one underlying lexical concept.
Different relations link the synonym sets.

WordNet was developed by the Cognitive Science Laboratory at
Princeton University under the direction of Professor George
A. Miller (Principal Investigator).  Over the years, many people
have contributed to the success of WordNet.

%package dict
Summary: WordNet electronic lexical database of English language
Group: Text tools
BuildArch: noarch

%description dict
This package contains WordNet dictionary data and manuals that
describe them.

%package dict-sense-index
Summary: WordNet electronic lexical database of English language: index.sense
Group: Text tools
BuildArch: noarch
Requires: %name-dict = %version-%release

%description dict-sense-index
This package contains a large WordNet database index.sense which
is not necessary for normal operation of the wordnet package but is
useful when using the WordNet::QueryData Perl module.

%package tk
Summary: Tcl/tk frontend WordNet English lexical reference system
Group: Text tools
Requires: %name = %version-%release

%description tk
This package contains wnb -- a GUI frontend for WordNet.

%package -n lib%name
Summary: WordNet English lexical reference system shared library
Group: System/Libraries

%description -n lib%name
This package contains WordNet shared library.

%package -n lib%name-devel
Summary: WordNet English lexical reference system development files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains development library and include files for the
WordNet English lexical reference system.

%prep
%setup -n WordNet-%version
rm -rf include/tk
%patch01 -p1
%patch02 -p1
%patch03 -p1
%patch04 -p1
%patch05 -p1
%patch06 -p1
%patch07 -p1
%patch08 -p1
%patch09 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
%autoreconf
%configure %{subst_enable static}
# SMP-incompatible
make

%install
%makeinstall_std
mkdir -p %buildroot%_niconsdir/
install -pm644 %_sourcedir/%name.png %buildroot%_niconsdir/

mkdir -p %buildroot%_desktopdir
cat <<EOF >%buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Name=WordNet
Comment=WordNet English lexical reference system
Exec=%_bindir/wnb
Icon=%name
Terminal=false
Type=Application
StartupNotify=true
Categories=Office;Dictionary;
EOF

%files
%_bindir/wn
%_man1dir/*
%exclude %_man1dir/grind.*
%exclude %_man1dir/wnb.*
%doc AUTHORS COPYING

%files dict
%dir %_datadir/%name/
%_datadir/%name/dict/
%exclude %_datadir/%name/dict/index.sense
%exclude %_datadir/%name/dict/cntlist
%exclude %_datadir/%name/dict/frames.vrb
%_man5dir/*
%exclude %_man5dir/senseidx.*
%_man7dir/*

%files dict-sense-index
%dir %_datadir/%name/
%dir %_datadir/%name/dict/
%_datadir/%name/dict/index.sense
%_datadir/%name/dict/cntlist
%_datadir/%name/dict/frames.vrb
%_man5dir/senseidx.*

%files tk
%_bindir/wnb
%_man1dir/wnb.*
%_libexecdir/%name/
%dir %_datadir/%name/
%_datadir/%name/wnres/
%_niconsdir/%name.png
%_desktopdir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_man3dir/*

%changelog
* Fri Jun 03 2011 Dmitry V. Levin <ldv@altlinux.org> 3.0-alt7
- Rebuilt for debuginfo.

* Fri Nov 05 2010 Dmitry V. Levin <ldv@altlinux.org> 3.0-alt6
- Fixed desktop entry.
- Rebuilt for soname set-versions.

* Wed Oct 28 2009 Dmitry V. Levin <ldv@altlinux.org> 3.0-alt5
- Revised patches, merged fixes from FC and Debian.
- Built and packaged libWN shared library.
- Disabled build of libWN static library.
- Moved main database to separate subpackage %name-dict.
- Moved index.sense database to separate subpackage %name-dict-sense-index.

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt4
- applied patches against CVE-2008-2149, CVE-2008-3908 (fix bug #15678)

* Wed Oct 22 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt3
- update buildreq

* Fri Mar 14 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt2
- rebuild with tcl 8.5

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt1
- new version 3.0
- rewrote path patches
- update buildreqs

* Fri Feb 24 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt2
- fix requires for wordnet-tk package (bug #9146)

* Wed Aug 31 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt1
- new version
- change dictionary location
- remove libwordnet package

* Fri Jun 11 2004 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt2
- fix location of wnb resources
- fix menu and icon

* Thu Jun 10 2004 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- first build for Sisyphus (Thanks Ark Linux)

* Fri Mar 21 2003 Sergio Visinoni <piffio@arklinux.org> 1.7.1-3ark
- Really rebuild binaries when building
- Fix dictionary path

* Mon Nov 05 2002 Natasha Sainty <natasha@arklinux.org> 1.7.1-1ark
- First pkg
