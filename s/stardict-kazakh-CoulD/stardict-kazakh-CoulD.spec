Name: stardict-kazakh-CoulD
Version: 0.1
Release: alt1
Summary: Kazakh-Russian and Russian-Kazakh dictionaries for stardict
Summary(ru_RU.UTF-8): Казахско-русский (46972 слов) и Русско-казахский (7716 слов) словари
License: GPL2
Group: Text tools
Url: http://gnu.kz/
BuildArch: noarch

Requires: stardict >= 2.4.2

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: ftp://ftp.gnu.kz/pub/software_gnu_kazakhstan/kazrus-ruskaz-dict/kazrus-ruskaz-dict-0.1.tar
#.bz2
Source1: %name-ifo.tar

# Automatically added by buildreq on Fri Oct 15 2010 (-bi)
BuildRequires: dict-tools stardict-tools

%description
Kazakh-Russian (46972 words) and Russian-Kazakh (7716 words) Dictionaries
Kazakh language code is kk and Kazakhstan code is KZ

%description -l ru_RU.UTF-8
Вашему вниманию предлагаются Казахско-русский (46972 слов) и
Русско-казахский (7716 слов) словари.

Словари распространяются на устовиях лицензии GNU General Pubpic Lisence.
Если в месте с этими словарями Вы не получили копию лицензии, пожалуйста
поситите сайт www.gnu.org для получения дополнительной информации о условиях
использования данных словарей.
Автор словарей Алексей 'CoulD' Липчанский.

%prep
%setup -n kazrus-ruskaz-dict-%version
dictzip -d *.dz ||:

tar xf %SOURCE1

%build
for d in kazrus ruskaz; do
	dictd2dic $d | tee dictd2dic.out
	rename dictd_www.dict.org_ '' dictd_www.dict.org_*
	WORDCOUNT=`grep ^wordcount: dictd2dic.out | sed 's|^wordcount: ||'`
	IDXFILESIZE=`wc -c < $d.idx`
	subst "s|@WORDCOUNT@|$WORDCOUNT|;
		s|@IDXFILESIZE@|$IDXFILESIZE|" $d.ifo
done

gzip -9 *.idx

%install
mkdir -p %buildroot%_datadir/stardict/dic/
install -m 644 *.dz *.idx.gz *.ifo %buildroot%_datadir/stardict/dic/

%files
%_datadir/stardict/dic/*
%doc README*

%changelog
* Fri Oct 15 2010 Ildar Mulyukov <ildar@altlinux.ru> 0.1-alt1
- 1st build for ALTLinux
