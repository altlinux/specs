%define dictname wn
%define dictdesc Dict-wn - WordNet (r) database for the programs dict and dictd
%define dictdir %_datadir/dictd

Name: dict-wn
Version: 2.0
Release: alt2

Summary: %dictdesc

License: GPL
Group: Text tools
#Group: Applications/Dictionaries
Url: http://linux.maruhn.com/sec/dict-wn.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://ftp.dict.org/pub/dict/pre/%name-%version.tar.bz2

BuildArchitectures: noarch

# Automatically added by buildreq on Thu Sep 15 2005
BuildRequires: dict-tools flex fontconfig libfreetype stardict-tools xorg-x11-locales

%description
The files contained herein are designed to convert the WordNet (r) 1.6 data
into a working database and index for the DICT server.

The original data for this version of:
    WordNet (r): A Lexical Database for English fromthe Cognitive Science
    Laboratory at Princeton University
is available from: ftp://clarity.princeton.edu/pub/wordnet/wn1.6unix.tar.gz

This package contains conversion software and a copy of the original data.
Please see the raw data for distribution terms for the raw and formatted
data.  The formatting _software_ is currently distributed under the GNU
General Public License.  If you need it use it under another license,
contact the author.

%package -n stardict-%dictname
Summary: GCIDE - The Collaborative International Dictionary of English
#Group:		Applications/Dictionaries
Group: Text tools

%description -n stardict-%dictname
The files contained herein are designed to convert the WordNet (r) 1.6 data
into a working database and index for the DICT server.

The original data for this version of:
    WordNet (r): A Lexical Database for English fromthe Cognitive Science
    Laboratory at Princeton University
is available from: ftp://clarity.princeton.edu/pub/wordnet/wn1.6unix.tar.gz

This package contains conversion software and a copy of the original data.
Please see the raw data for distribution terms for the raw and formatted
data.  The formatting _software_ is currently distributed under the GNU
General Public License.  If you need it use it under another license,
contact the author.

%prep
%setup -q
#%patch1 -p0

%build
#autoreconf -fisv
%configure --build i586-linux --host i586-linux

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
* Sun Jan 18 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt2
- cleanup spec, fix Url, fix Summary (bug #14980)

* Mon Feb 13 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- fix build with new stardict-tools

* Thu Sep 15 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt0.1
- first build for ALT Linux Sisyphus

