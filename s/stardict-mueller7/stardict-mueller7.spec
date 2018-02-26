%define dict_name	mueller7

Name: stardict-%dict_name
Version: 1.0
Release: alt8

Summary: V.K. Mueller English-Russian Dictionary, 7th Edition, for stardict
License: GPLv2+
Group: Text tools
Requires: stardict >= 2.4.2
Url: http://mueller-dic.chat.ru/
Packager: Anton V. Boyarshinov <boyarsh@altlinux.ru>
BuildArch: noarch

# http://mueller-dic.chat.ru/Mueller7GPL.tgz
Source: Mueller7GPL.tar

BuildRequires: dict-tools perl-Unicode-Map8 stardict-tools >= 3.0.3

%description 
Electronic version of V.K. Mueller English-Russian Dictionary,
7th Edition, in stardict format, for use with a stardict client.

%prep
%setup -c

%build
cd usr/local/share/dict
mueller2stardict.sh Mueller7GPL.koi %dict_name
sed -i 's/^\(bookname\)=.*/\1=V.K.Mueller English-Russian Dictionary, 7th Edition/' %dict_name.ifo
gzip -9n %dict_name.idx
dictzip %dict_name.dict
cd - >/dev/null

%install
%define stardictdir %_datadir/stardict/dic
mkdir -p %buildroot%stardictdir
install -pm644 -D usr/local/share/dict/%dict_name.{dict.dz,idx.gz,ifo} \
	%buildroot%stardictdir/

%files 
%stardictdir/*

%changelog
* Wed May 30 2012 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt8
- Fixed using fresh stardict-tools.

* Tue Sep 14 2010 Alex Murygin <murygin@altlinux.ru> 1.0-alt7
- reformat using mueller2stardict.sh

* Tue Oct 07 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt6
- resurrect from orphaned

* Wed Nov 26 2003 Alex Murygin <murygin@altlinux.ru> 1.0-alt5
- new format

* Wed Oct 15 2003 Alex Murygin <murygin@altlinux.ru> 1.0-alt4
- commpress dictionaries

* Sat Sep 20 2003 Alex Murygin <murygin@altlinux.ru> 1.0-alt3
- fixed error (PreReq -> BuildPreReq)
- fixed buildrequires

* Wed May 21 2003 Alex Murygin <murygin@altlinux.ru> 1.0-alt2
- new stardict format
- fixed transcription
- used mueller2utf8 script from dict-mueller7-unicode

* Sun May 04 2003 Alex Murygin <murygin@altlinux.ru> 1.0-alt1
- initial revision

