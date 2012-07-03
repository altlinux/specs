%define ispelldir	%_libdir/ispell
%define ispell_version	3.2.06
%define aspell_version	0.60.0

Name:		ispell-ru-rk
Version:	1.1
Release:	alt6

Summary:	Russian dictionary for ispell -- KOI8-R encoding
Summary(ru_RU.UTF-8): Словарь русского языка для ispell -- кодировка KOI8-R
License:	GPL
Group:		System/Internationalization

# Note: ispell and aspell hash files are architecture-dependent.
# Do not put BuildArch: noarch here.

Source0:	ispell-rus-1.1.tar.bz2
Source2:	russianw.aff
Source3:	ispell-rus-aspellfiles-0.3.tar.bz2

PreReq:		alternatives >= 0.4
Requires:	ispell >= %ispell_version
Provides:	ispell-dictionary, ispell-ru = %version
Obsoletes:	russian, ispell-rus, ispell-russian, rispell, ispell-ru

# Automatically added by buildreq on Sat Nov 22 2003
BuildRequires:	aspell ispell libalternatives-devel

BuildPreReq:	ispell >= %ispell_version
BuildPreReq:	aspell >= %aspell_version

# The real ispell is required - not the aspell-provided emulation.
BuildConflicts:	aspell-ispell

%package cp1251
Summary:	Russian dictionary for ispell -- CP1251 encoding
Summary(ru_RU.UTF-8): Словарь русского языка для ispell -- кодировка CP1251
Group:		System/Internationalization
PreReq:		alternatives >= 0.0.6
Requires:	ispell >= %ispell_version
Provides:	ispell-dictionary, ispell-ru-cp1251 = %version
Obsoletes:	irussian, ispell-rus, ispell-russian, rispell, ispell-ru-cp1251


%package -n aspell-ru-rk
Summary:	Russian dictionary for GNU Aspell
Summary(ru_RU.UTF-8): Словарь русского языка для GNU Aspell
Group:		System/Internationalization
PreReq:		alternatives >= 0.0.6
Requires:	aspell >= %aspell_version
Provides:	aspell-dictionary, aspell-ru = %version
Obsoletes:	aspell-ru


%description
Russian dictionary for ispell in KOI8-R encoding, created by
Vladimir Roganov and Konstantin Knizhnik. 

This dictionary is installed under the name "russian-rk".  Default
Russian dictionary in KOI8-R encoding (with the name "russian") is
selected using the alternatives subsystem.

%description -l ru_RU.UTF-8
Словарь русского языка для ispell в кодировке KOI8-R, подготовленный
Владимиром Рогановым и Константином Книжником.

Этот словарь устанавливается под именем "russian-rk".  Словарь для
проверки русских текстов в кодировке KOI8-R по умолчанию (с именем
"russian") выбирается с помощью подсистемы альтернатив.


%description cp1251
Russian dictionary for ispell in CP1251 encoding, created by
Vladimir Roganov and Konstantin Knizhnik. 

This dictionary is installed under the name "russianw-rk".  Default
Russian dictionary in CP1251 encoding (with the name "russianw") is
selected using the alternatives subsystem.

%description cp1251 -l ru_RU.UTF-8
Словарь русского языка для ispell в кодировке CP1251, подготовленный
Владимиром Рогановым и Константином Книжником.

Этот словарь устанавливается под именем "russianw-rk".  Словарь для
проверки русских текстов в кодировке CP1251 по умолчанию (с именем
"russianw") выбирается с помощью подсистемы альтернатив.


%description -n aspell-ru-rk
Russian dictionary for use with GNU Aspell.  The word list for this
dictionary was created by Vladimir Roganov and Konstantin Knizhnik.

This dictionary is installed under the name "ru-rk".  Default Russian
dictionary for GNU Aspell (with the name "ru") is selected using the
alternatives subsystem.

%description -n aspell-ru-rk -l ru_RU.UTF-8
Словарь русского языка для GNU Aspell на основе списка слов,
подготовленного Владимиром Рогановым и Константином Книжником.

Этот словарь устанавливается под именем "ru-rk".  Словарь для проверки
русских текстов по умолчанию (с именем "ru") выбирается с помощью
подсистемы альтернатив.


%prep
%setup -n ispell-rus-%version -a 3
cp -a %SOURCE2 russianw.aff

%build
# ispell, KOI8-R
make all

# ispell, CP1251
iconv -f koi8-r -t cp1251 <russian.sml >russianw.sml
buildhash russianw.sml russianw.aff russianw.hash
pushd docs
for f in *.russian; do
	iconv -f koi8-r -t cp1251 <"$f" >"$f"w
done
popd

# aspell
ispell -d ./russian.hash -e <russian.sml | \
	tr ' ' '\n' | grep -v '^$' | \
	aspell --lang=ru-rk create master ./ru-rk.rws


%install
mkdir -p $RPM_BUILD_ROOT%ispelldir
cp -avf russian.aff $RPM_BUILD_ROOT%ispelldir/russian-rk.aff
cp -avf russian.hash $RPM_BUILD_ROOT%ispelldir/russian-rk.hash

cp -avf russianw.aff $RPM_BUILD_ROOT%ispelldir/russianw-rk.aff
cp -avf russianw.hash $RPM_BUILD_ROOT%ispelldir/russianw-rk.hash

mkdir -p $RPM_BUILD_ROOT%_libdir/aspell
mkdir -p $RPM_BUILD_ROOT%_datadir/aspell
install -p -m 644 ru-rk.rws $RPM_BUILD_ROOT%_libdir/aspell
install -p -m 644 ru-rk.multi $RPM_BUILD_ROOT%_libdir/aspell
install -p -m 644 russian-rk.alias $RPM_BUILD_ROOT%_libdir/aspell
install -p -m 644 ru-rk.dat $RPM_BUILD_ROOT%_datadir/aspell
install -p -m 644 ru-rk_phonet.dat $RPM_BUILD_ROOT%_datadir/aspell

install -d $RPM_BUILD_ROOT%_altdir
cat > $RPM_BUILD_ROOT%_altdir/%name <<'EOF'
%ispelldir/russian.hash	%ispelldir/russian-rk.hash	10
%ispelldir/russian.aff	%ispelldir/russian-rk.aff	%ispelldir/russian-rk.hash
EOF
cat > $RPM_BUILD_ROOT%_altdir/%name-cp1251 <<'EOF'
%ispelldir/russianw.hash	%ispelldir/russianw-rk.hash	10
%ispelldir/russianw.aff	%ispelldir/russianw-rk.aff	%ispelldir/russianw-rk.hash
EOF
cat > $RPM_BUILD_ROOT%_altdir/aspell-ru-rk <<'EOF'
%_libdir/aspell/ru.multi	%_libdir/aspell/ru-rk.multi	10
%_libdir/aspell/russian.alias	%_libdir/aspell/russian-rk.alias	%_libdir/aspell/ru-rk.multi
EOF


%files
%doc docs/Readme.russian
%doc docs/copyright
%doc docs/cyrispell
%doc docs/readme.makedict
%doc docs/INSTALL.russian
%_altdir/%name
%ispelldir/russian-rk.*


%files cp1251
%doc docs/Readme.russianw
%doc docs/copyright
%doc docs/cyrispell
%doc docs/readme.makedict
%doc docs/INSTALL.russianw
%_altdir/%name-cp1251
%ispelldir/russianw-rk.*


%files -n aspell-ru-rk
%doc docs/Readme.russian
%doc docs/copyright
%doc LICENSE.phonet
%_altdir/aspell-ru-rk
%_libdir/aspell/*
%_datadir/aspell/*

%changelog
* Fri Aug 26 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt6
- converted alternatives to modern tab format (closes: #25739)
- bugfix for alternatives (/usr/lib instead of libdir)

* Tue Feb 09 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.1-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-alternatives-0.3 for aspell-ru-rk
  * obsolete-call-in-post-alternatives-0.3 for ispell-ru-rk-cp1251
  * obsolete-call-in-post-alternatives-0.3 for ispell-ru-rk
  * postclean-05-filetriggers for spec file

* Thu Jul 29 2004 Sergey Vlasov <vsu@altlinux.ru> 1.1-alt5
- Rebuild for aspell 0.60.0 (new dictionary format).

* Sun Nov 23 2003 Sergey Vlasov <vsu@altlinux.ru> 1.1-alt4
- Updated for new aspell (no more pspell, different dictionary names).
- Updated BuildRequires.
- Spec file cleanup.
- Added Russian descriptions.

* Tue May 06 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt3.1
- move to new alternatives scheme

* Tue Nov 19 2002 AEN <aen@altlinux.ru> 1.1-alt3
- rebuilt

* Tue Apr 02 2002 Sergey Vlasov <vsu@altlinux.ru> 1.1-alt2
- Added aspell phonetic rules file from Andrey Grozin.
- Fixed bugs in %%preun scripts (alternatives were lost after upgrading).
- Addef %%triggerpostun to clean up after my %%preun bugs in the previous
  version :-(

* Sun Dec 02 2001 Sergey Vlasov <vsu@altlinux.ru> 1.1-alt1
- Spec file cleanup.
- Package renamed to ispell-ru-rk (rk = Roganov & Knizhnik).
- Use update-alternatives for choosing the dictionary.
- Build ispell-cp1251 and aspell dictionaries from the same source.
- Do not set BuildArch: noarch because hash files really are
  architecture-dependent; set it to %%_build_arch instead.

* Wed Jun 13 2001 AEN <aen@logic.ru> 1.1-ipl4mdk
- Provides: ispell-dictionary

* Thu Feb 15 2001 AEN <aen@logic.ru>
- back to old style spec

* Wed Dec 06 2000 AEN <aen@logic.ru>
- spec fix
- build for RE


* Sun Oct 8 2000 AEN <aen@logic.ru>
- recoding from KOI8-R to 1251

* Mon Dec 06 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added Obsoletes: for easier installation over other rpms of same language
- added Requires: locales-ru for proper pre-selection by DrakX
- changed name to ispell-ru for standardization

* Thu Oct 21 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- rebuild with ispell-3.1.20-7mdk (which uses a MASKBITS of 64)

* Sun Oct 16 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Fix incorrect Path in path #0 (ispell-rus-prefix.patch.bz2)
- Change group "Utilities/Text" to "Applications/Text" (rpmlint lament)

* Tue Jul 13 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- bzip2 source

* Wed Jul 07 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- First version contribued by IPLabs (http://www.iplabs.ru/Linux)
- Rewriting the .spec.
