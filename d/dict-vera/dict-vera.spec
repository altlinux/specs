%define dictname vera
%define dictdesc V.E.R.A. -- Virtual Entity of Relevant Acronyms
%define dictdir %_datadir/dictd

Name: dict-%dictname
Version: 1.17
Release: alt1

Summary: %dictdesc

License: FDL
Group: Text tools
#Group: Applications/Dictionaries
Url: http://home.snafu.de/ohei/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://home.snafu.de/ohei/FTP/vera-%version.tar.bz2
Source1: %name.sedfile
#Patch: %name-%version.patch

BuildArchitectures: noarch

Requires(post,preun): dictd

# Please do not use buildreq
BuildPreReq: flex dict-tools stardict-tools

%description
This is a special GNU edition of V.E.R.A., a list dealing with
computational acronyms.
Copyright (C) 1993/2003 Oliver Heidelbach <ohei [at] snafu . de>

Please send corrections to Oliver Heidelbach <ohei [at] snafu . de>.

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.1 or
any later version published by the Free Software Foundation; with no
Invariant Sections, with no Front-Cover Texts, and with no Back-Cover
Texts.  A copy of the license is included in the section entitled "GNU
FDL".

%package -n stardict-%dictname
Summary:	%dictdesc
#Group:		Applications/Dictionaries
Group: Text tools
Obsoletes: stardict-%name
Provides: stardict-%name

%description -n stardict-%dictname
This is a special GNU edition of V.E.R.A., a list dealing with
computational acronyms.
Copyright (C) 1993/2003 Oliver Heidelbach <ohei [at] snafu . de>

Please send corrections to Oliver Heidelbach <ohei [at] snafu . de>.

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.1 or
any later version published by the Free Software Foundation; with no
Invariant Sections, with no Front-Cover Texts, and with no Back-Cover
Texts.  A copy of the license is included in the section entitled "GNU
FDL".

%prep
%setup -q -n vera-%version
#%%patch -p0

%build

cat <<EOF >vera
This is a special GNU edition of V.E.R.A., a list dealing with
computational acronyms.
   Copyright (C) 1993/2003 Oliver Heidelbach <ohei [at] snafu . de>
   
   Please send corrections to Oliver Heidelbach <ohei [at] snafu . de>.
   
   Permission is granted to copy, distribute and/or modify this document
   under the terms of the GNU Free Documentation License, Version 1.1 or
   any later version published by the Free Software Foundation; with no
   Invariant Sections, with no Front-Cover Texts, and with no Back-Cover
   Texts.  A copy of the license is included in the section entitled "GNU
   FDL".
   
   Within the above restrictions the distribution of this document is
   explicitly encouraged and I hope you'll find it of some value.
   
   This dictionary has nothing to do with Systems Science Inc.  or its
   products.
EOF

sed -f %SOURCE1 vera.? >>vera
/usr/bin/dictfmt -f -u %url -s "%dictdesc" %dictname <vera
rm -f vera1 vera.tmp vera

# prepare stardict

# dictd to stardict conversion
word=`dictd2dic %dictname | grep wordcount | cut -d " " -f 2`
size=`cat dict*%dictname.idx | wc -c`
gzip dict*%dictname.idx

cat << EOF > %dictname.ifo
StarDict's dict ifo file
version=2.4.2
wordcount=$word
website=http://home.snafu.de/ohei
date=%version
idxfilesize=$size
bookname=%dictname
description=%dictdesc
sametypesequence=m
EOF

# compress dict file
/usr/bin/dictzip -v %dictname.dict

%install
%__install -D -m 644 %dictname.dict.dz %buildroot%dictdir/%dictname.dict.dz
%__install -D -m 644 %dictname.index %buildroot%dictdir/%dictname.index

# stardict
%__install -d %buildroot%_datadir/stardict/dic

%__install -m 644 dict*%dictname.dict.dz %buildroot%_datadir/stardict/dic/%dictname.dict.dz
%__install -m 644 dict*%dictname.idx.gz %buildroot%_datadir/stardict/dic/%dictname.idx.gz
%__install -m 644 %dictname.ifo %buildroot%_datadir/stardict/dic/%dictname.ifo

%post
%_sbindir/dictdconfig -w
%_initdir/dictd condreload

%postun
%_sbindir/dictdconfig -w
%_initdir/dictd condreload

%files
%dictdir/%dictname.*

%files -n stardict-%dictname
%_datadir/stardict/dic/*

%changelog
* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 1.17-alt1
- new version 1.17 (with rpmrb script)
- update buildreqs

* Mon Feb 13 2006 Vitaly Lipatov <lav@altlinux.ru> 1.16-alt1
- new version
- fix build with new stardict-tools

* Thu May 05 2005 Vitaly Lipatov <lav@altlinux.ru> 1.15-alt2
- fix broken stardict package name

* Wed Apr 13 2005 Vitaly Lipatov <lav@altlinux.ru> 1.15-alt1
- first build for ALT Linux Sisyphus
