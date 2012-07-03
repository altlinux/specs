%define dictname gcide
%define dictdesc GCIDE - The Collaborative International Dictionary of English
%define dictdir %_datadir/dictd

Name: dict-gcide
Version: 0.48
Release: alt5

Summary: GCIDE - The Collaborative International Dictionary of English

License: GPL
Group: Text tools
#Group: Applications/Dictionaries
Url: http://www.ibiblio.org/webster/GNU_dictionary_project.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://ftp.gnu.org/gnu/gcide/%name-%version.tar.bz2
Patch: %name-%version.debian.diff.gz
Patch1: %name-%version.patch

BuildArchitectures: noarch

# Please do not use buildreq
BuildPreReq: flex dict-tools stardict-tools

%description
A Comprehensive English Dictionary

This package contains the GNU version of the Collaborative
International Dictionary of English, formatted for use by the
dictionary server in the dictd package.  The GCIDE contains the
full text of the 1913 Webster's Unabridged Dictionary, supplemented by
many definitions from WordNet, the Century Dictionary, 1906, and many
additional definitions contributed by volunteers.

The definitions in the core of this dictionary are at least 85 years
old, so they can not be expected to be politically correct by
contemporary standards, and no attempt has been, or will be, made to
make them so.

%package -n stardict-%dictname
Summary: GCIDE - The Collaborative International Dictionary of English
#Group:		Applications/Dictionaries
Group: Text tools
Obsoletes: stardict-%name
Provides: stardict-%name

%description -n stardict-%dictname
A Comprehensive English Dictionary for stardict

This package contains the GNU version of the Collaborative
International Dictionary of English, formatted for use by the
dictionary server in the dictd package.  The GCIDE contains the
full text of the 1913 Webster's Unabridged Dictionary, supplemented by
many definitions from WordNet, the Century Dictionary, 1906, and many
additional definitions contributed by volunteers.

The definitions in the core of this dictionary are at least 85 years
old, so they can not be expected to be politically correct by
contemporary standards, and no attempt has been, or will be, made to
make them so.

%prep
%setup -q
%patch1 -p0

%build
%configure

%make
# without zipping here
%make DICTZIP=cat db

# prepare stardict

# dictd to stardict conversion
word=`dictd2dic %dictname | grep wordcount | cut -d " " -f 2`
size=`cat dict*%dictname.idx | wc -c`
gzip dict*%dictname.idx

cat << EOF > %dictname.ifo
StarDict's dict ifo file
version=2.4.2
wordcount=$word
website=ftp://ftp.gnu.org/gnu/gcide
date=%version
idxfilesize=$size
bookname=%dictname
description=%dictdesc
sametypesequence=m
EOF

# compress dict file
dictzip %dictname.dict

%install
install -d %buildroot{%_sysconfdir/dictd,%dictdir}
%makeinstall dictdir=%buildroot%dictdir

echo "# %dictdesc
database %dictname {
	data  \"%dictdir/%dictname.dict.dz\"
	index \"%dictdir/%dictname.index\"
}" > %buildroot%_sysconfdir/dictd/%dictname.dictconf

# stardict
install -d %buildroot%_datadir/stardict/dic

install -m 644 dict*%dictname.dict.dz %buildroot%_datadir/stardict/dic/%dictname.dict.dz
install -m 644 dict*%dictname.idx.gz %buildroot%_datadir/stardict/dic/%dictname.idx.gz
install -m 644 %dictname.ifo %buildroot%_datadir/stardict/dic/%dictname.ifo

%post
%_sbindir/dictdconfig -w
%_initdir/dictd condreload

%postun
%_sbindir/dictdconfig -w
%_initdir/dictd condreload

%files
#%_sysconfdir/dictd/%dictname.dictconf
%dictdir/%dictname.*

%files -n stardict-%dictname
%_datadir/stardict/dic/*

%changelog
* Sun Jan 18 2009 Vitaly Lipatov <lav@altlinux.ru> 0.48-alt5
- cleanup spec

* Mon Feb 13 2006 Vitaly Lipatov <lav@altlinux.ru> 0.48-alt4
- fix build with new stardict-tools
- add obsoletes/provides

* Thu Oct 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.48-alt3
- remove %_sysconfdir/dictd as unneeded
- fix name of stardict package

* Thu Jan 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.48-alt2
- rebuild with gcc3.4
- enable stardict package

* Tue Jun 15 2004 Vitaly Lipatov <lav@altlinux.ru> 0.48-alt1.1
- fix output package name

* Tue Jun 15 2004 Vitaly Lipatov <lav@altlinux.ru> 0.48-alt1
- first build for Sisyphus (without stardict)

