# TODO: use makedict
Name: foldoc
Version: 20080103
Release: alt1

Summary: FOLDOC - The Free On-line Dictionary of Computing

License: FDL
Group: Text tools
Url: http://www.foldoc.org
#Group: Applications/Dictionaries

Packager: Vitaly Lipatov <lav@altlinux.ru>

# http://foldoc.org/source.html
Source: http://foldoc.org/foldoc/Dictionary.bz2
BuildArchitectures: noarch

%define dictname %name
%define dictdesc FOLDOC -- Free On-line Dictionary of Computing 
%define dictdir %_datadir/dictd

# Please do not use buildreq
BuildPreReq: dict-tools stardict-tools

%description
This package contains Free On-line Dictionary of Computing 
for use by the dictionary server in the dictd package.

FOLDOC is a searchable dictionary of acronyms, jargon,
programming languages, tools, architecture, operating systems,
networking, theory, conventions, standards, mathematics,
telecoms, electronics, institutions, companies, projects,
products, history, in fact anything to do with computing.

%package -n dict-%name
Summary:	FOLDOC - The Free On-line Dictionary of Computing for DICTD
#Group:		Applications/Dictionaries
Group: Text tools

%description -n dict-%name
This package contains Free On-line Dictionary of Computing 
for use by the dictionary server in the dictd package.

FOLDOC is a searchable dictionary of acronyms, jargon,
programming languages, tools, architecture, operating systems,
networking, theory, conventions, standards, mathematics,
telecoms, electronics, institutions, companies, projects,
products, history, in fact anything to do with computing.

%package -n stardict-%name
Summary:	FOLDOC - The Free On-line Dictionary of Computing for Stardict
#Group:		Applications/Dictionaries
Group: Text tools

%description -n stardict-%name
This package contains Free On-line Dictionary of Computing 
for use with stardict.

FOLDOC is a searchable dictionary of acronyms, jargon,
programming languages, tools, architecture, operating systems,
networking, theory, conventions, standards, mathematics,
telecoms, electronics, institutions, companies, projects,
products, history, in fact anything to do with computing.

%prep

%build
#makedict -i dictd -o xdxf %dictname.dictd -d %dictname.xdxf
#exit 1
# prepare DictD
bzcat %SOURCE0 | iconv -f ISO-8859-1 -t utf8 | \
	dictfmt --locale ru_RU.UTF-8 -f \
		-u "http://foldoc.org/foldoc/Dictionary.gz" \
		-s "%dictdesc (%version)" %dictname

#makedict -i dictd -o xdxf %dictname.dict
# -d %dictname.xdxf

# prepare stardict
cat <<EOF >%dictname.idxhead
StarDict's dict idx file
version=2.4.2
bookname=%dictname
website=http://www.foldoc.org
description=%dictdesc
date=%version
sametypesequence=m
BEGIN:
EOF

# С ним не работает :)
%__rm -f %dictname.idxhead

# dictd to stardict conversion
word=`dictd2dic %dictname | grep wordcount | cut -d " " -f 2`
size=`cat dict*%dictname.idx | wc -c`
gzip dict*%dictname.idx

cat << EOF > %dictname.ifo
StarDict's dict ifo file
version=2.4.2
wordcount=$word
website=http://www.foldoc.org
date=%version
idxfilesize=$size
bookname=%dictname
description=%dictdesc
sametypesequence=m
EOF

# compress dict file
dictzip %dictname.dict

%install
# dictd
install -d %buildroot{%_sysconfdir/dictd,%dictdir}
install -m 644 %dictname.dict.dz %buildroot%dictdir
install -m 644 %dictname.index %buildroot%dictdir

echo "# %dictdesc
database %dictname {
	data  \"%dictdir/%dictname.dict.dz\"
	index \"%dictdir/%dictname.index\"
}" > %buildroot%_sysconfdir/dictd/%dictname.dictconf

# stardict
%__install -d %buildroot%_datadir/stardict/dic

%__install -m 644 dict*%dictname.dict.dz %buildroot%_datadir/stardict/dic/%dictname.dict.dz
%__install -m 644 dict*%dictname.idx.gz %buildroot%_datadir/stardict/dic/%dictname.idx.gz
%__install -m 644 %dictname.ifo %buildroot%_datadir/stardict/dic/%dictname.ifo

%post -n dict-%name
%_sbindir/dictdconfig -w
%_initdir/dictd condreload

%postun -n dict-%name
%_sbindir/dictdconfig -w
%_initdir/dictd condreload

%files -n dict-%name
#%_sysconfdir/dictd/%dictname.dictconf
%dictdir/%dictname.*

%files -n stardict-%name
%_datadir/stardict/dic/*

%changelog -f %name.lang
* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 20080103-alt1
- new version (20080103)

* Mon Feb 13 2006 Vitaly Lipatov <lav@altlinux.ru> 20060213-alt1
- update, fix build

* Sun Sep 11 2005 Vitaly Lipatov <lav@altlinux.ru> 20050911-alt1
- update

* Mon May 16 2005 Vitaly Lipatov <lav@altlinux.ru> 20050515-alt1
- update
- remove /etc/dictd as unneeded

* Sun Nov 07 2004 Vitaly Lipatov <lav@altlinux.ru> 20041107-alt1
- update

* Sat Jun 12 2004 Vitaly Lipatov <lav@altlinux.ru> 20040611-alt1
- first build for Sisyphus

