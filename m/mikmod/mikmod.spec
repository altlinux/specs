Name: mikmod
Version: 3.2.1
Release: alt3

%define fversion 3.2.1

Summary: A MOD music file player
License: LGPL
Group: Sound
Url: http://mikmod.raphnet.net
Source: %name-%fversion.tar.gz
Patch1: %name-3.1.6-tmpfile.patch
Patch2: %name-3.1.6-security.patch

# Automatically added by buildreq on Tue Aug 31 2004
BuildRequires: libmikmod-devel libncurses-devel libtinfo-devel

Summary(ru_RU.KOI8-R): Мультиформатный проигрыватель трекерной музыки
Summary(uk_UA.KOI8-U): Мультиформатний програвач трекерно╖ музыки

%description
MikMod is one of the best and most well known MOD music file players for
UNIX-like systems.  This particular distribution is intended to compile
fairly painlessly in a Linux environment. MikMod uses the OSS /dev/dsp
driver including all recent kernels for output, and will also write .wav
files. Supported file formats include MOD, STM, S3M, MTM, XM, ULT, and IT.
The player uses ncurses for console output and supports transparent
loading from gzip/pkzip/zoo archives and the loading/saving of playlists.

Install the %name package if you need a MOD music file player.

%description -l ru_RU.KOI8-R  
MikMod - высококачественный консольный проигрыватель трекерных модулей в
форматах IT, XM, S3M, MTM, 669, STM, ULT, FAR, MED, AMF, DSM, IMF, GDM,
STX, OKT и MOD, умеет работать с плей-листами, выдает информацию о
треках, работает с драйверами различных устройств вывода и сетевыми
звуковыми сервисами, может записывать в RAW- и WAV-файлы, поддерживает
перенаправление вывода в "трубу", читает треки из архивов (zoo, gz, bz2,
lha, lzh, rar, zip).

%description -l uk_UA.KOI8-U  
MikMod - як╕сний консольний програвач трекерних модул╕й у форматах
IT, XM, S3M, MTM, 669, STM, ULT, FAR, MED, AMF, DSM, IMF, GDM,
STX, OKT та MOD, що вм╕╓ працювати ╕з плей-л╕стами, вида╓ ╕нформац╕ю щодо
трек╕в, працю╓ ╕з драйверами р╕зних пристро╖в виведення та мережевими 
звуковими серв╕сами, може записувати до RAW- та WAV-файл╕в, п╕дтриму╓
перенаправлення виводу до "труби", чита╓ треки з арх╕в╕в (zoo, gz, bz2,
lha, lzh, rar, zip).

%prep
%setup -q -n %name-%fversion
%patch1 -p1
#patch2 -p1

%build
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS NEWS README

%changelog
* Fri Nov 23 2007 Michael Shigorin <mike@altlinux.org> 3.2.1-alt3
- removed Obsoletes: tracker (#13512)

* Fri Sep 28 2007 Michael Shigorin <mike@altlinux.org> 3.2.1-alt2
- built against fixed libmikmod package

* Sat Aug 05 2006 Michael Shigorin <mike@altlinux.org> 3.2.1-alt1
- 3.2.1
- removed patch2 (fixed upstream)

* Tue Aug 31 2004 Michael Shigorin <mike@altlinux.ru> 3.1.6a-alt4
- fixed #5127 (description encoding);
  thanks to Andrey Rahmatullin (wrar@)
- added Ukrainian description
- updated Url (not the source still)

* Mon Jul 07 2003 Michael Shigorin <mike@altlinux.ru> 3.1.6a-alt3
- Security update
- patch taken from gentoo as www.mikmod.org doesn't resolve

* Sun Oct 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 3.1.6a-alt2
- Rebuild with gcc-3.2. 

* Fri Dec 21 2001 Yuri N. Sedunov <aris@altlinux.ru> 3.1.6a-alt1
- Rebuilt with modified libmikmod.
- URL's changed.
- Russian summary and description added.

* Fri Jan 19 2001 Dmitry V. Levin <ldv@fandra.org> 3.1.6a-ipl5mdk
- RE adaptions.
- Create tmpfiles in more secure way.

* Wed Sep  6 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.1.6a-5mdk
- fix the build, better fix of mandir (dynamic)

* Wed Aug 30 2000 Etienne Faure <etienne@mandrakesoft.com> 3.1.6a-4mdk
- rebuilt with _mandir macro

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.1.6a-3mdk
- automatically added BuildRequires

* Mon Mar 27 2000 Daouda Lo <daouda@mandrakesoft.com> 3.1.6a-2mdk
- fix group + cleanup spec file.

* Sat Sep 11 1999 Giuseppe GhibР <ghibo@linux-mandrake.com>
- updated to version 3.1.6.

* Sat Jul 17 1999 Giuseppe GhibР <ghibo@linux-mandrake.com>
- fixed to work with shared libmikmod 3.1.6.

* Tue May 11 1999 Bernhard RosenkrДnzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Mon Mar 22 1999 Cristian Gafton <gafton@redhat.com>
- fixed spec file description and group according to sepcspo

* Mon Mar 22 1999 Michael Maher <mike@redhat.com>
- changed spec file, updated package
- added libmikmod to the package

* Mon Feb 15 1999 Miodrag Vallat <miodrag@multimania.com>
- Created for 3.1.5

* Tue Jan 24 1999 Michael Maher <mike@redhat.com>
- changed group
- fixed bug #145

* Fri Sep 04 1998 Michael Maher <mike@redhat.com>
- added patch for alpha

* Wed Sep 02 1998 Michael Maher <mike@redhat.com>
- built package; obsoletes the ancient tracker program.
