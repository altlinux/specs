%define baseversion 4.64

#------------------ --------------------
# pam-based Linux (as in pine-4.58L-alt)
%define pinelinuxtype lnp
# Secure glibs Linux (as in SuSE)
#define pinelinuxtype slx
#------------------ --------------------
%def_with tinfo
%def_without pilot-package
%def_with ssl
# mlock --- external program to lock mailbox. in ALT, we use fcntl(),
# so def_with mlock with current /var/spool/mail premissions
# could cause pine to call external mlock, which impacts the perfomance. 
# Nevertheless, on NFS mailboxes it is reasonable enough to use def_with mlock.
%def_without mlock
%define mlockname mlock
# Don't forget to edit the description & summary if you change this:
%def_with maildir
%def_with utf8
%def_with suse-specific
%def_with altmisc

# Otherwise we get too many unimportant warnings
%define optflags_warnings -Wundef -Wformat
%define CustomPineBuild 1


%def_without debug
%add_optflags %optflags_debug
%if 0
%remove_optflags %optflags_optimization
%endif


%define MergeConfPostInstall 1

# The packaging of the package should be a little cumbersome:
# the main PINE package must be built & packaged for specific arch's,
# but the tools subpackage is platform-independent (just scripts),
# so a "noarch" package must be made. The difference occurs only on the
# stage of making package files.

%define mainsummary A commonly used, MIME compliant mail and news reader.
%define name pine
%define exec %_bindir/%name

%if %CustomPineBuild
%define fullversion %{baseversion}L
%else
%define fullversion %{baseversion}
%endif

%define utilver 1.1

%define ldifver 0.1.4


# there are included parts of spec file for package pine (Version 4.64)
# Copyright (c) 2006 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Bernhard Kaindl <bk@suse.de>
# URL: http://www.suse.de/~bk/pine/

Name:           pine
Version:        %{fullversion}
Release:        alt8
License:        Other License(s), see package, FSR
Group: Networking/Mail
Summary: %mainsummary
Summary(ru_RU.KOI8-R): Широко используемая, соответствующая MIME программа для чтения почты и новостей.
URL:            http://www.washington.edu/pine
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

# For nice work PINE should be able to use a spell checker
# XXX Which one? Consider pspell, aspell, ispell
# TODO: Requires: spellchecker
Requires: %_bindir/spell

Requires: url_handler

Requires(post): mktemp sed grep

Requires: pico = %version-%release
%if_with pilot-package
Requires: pilot = %version-%release
%endif

Source:         ftp://ftp.cac.washington.edu/pine/pine%{baseversion}.tar.bz2
Patch10:        http://www.math.washington.edu/~chappa/pine/patches/pine%{baseversion}/all.patch.gz
Patch11:        charset-editorial.diff 
Patch14:        pico-ucs4all.patch
Patch15:        pico-ucs4GetKey.patch
Patch16:        pico-ucs4doublewidthchars.diff
Patch18:        pico-ucs4isspace.patch
Patch21:        pine-utf8-1b.patch
Patch22:        pine-utf8-1a-pine.h.patch
Patch23:        pine-utf8-1a-GFHP_HANDLES.patch
Patch24:        send-charset.patch
Patch26:        config-options.patch
Patch28:        iconv-no-explain.patch
Patch29:        utf8-mailindx.patch 
Patch30:        mailindx-plusdraw.patch
Patch31:        gf_wrap-UTF8.patch
Patch32:        pine-no-stripwhitespace.patch
Patch33:        strings-iconv.patch
Patch34:        filter-iconv.patch
Patch35:        rfc1522_decode.patch
Patch36:        rfc1522_valid.patch
Patch37:        optionally_enter.patch
Patch38:        multipart-alternative-conversion.patch

# those 2 patches are disabled in recent SuSE (4.64N-6)
# cause crashes?
Patch39:        utf8-fillpara-color-signature.diff
Patch40:        unexpected-data-after-address.patch

Patch41:        warnings.patch
# SuSE-specific patches last:
Patch50:        pine4.61.dif
Patch51:        pine-passfile.patch
Patch52:        pine-urlquote.patch
Patch53:        pine-body.patch
Patch55:        quell-displaying-flowed-text.patch.4.60 
Patch56:        quell-flowed-text-default.patch
Patch59:        pine-talk_disallow.patch
Patch60:        pine-gcc4.patch
Patch61:        pine-missing-protos.patch
Patch62:        pine-few_arguments.patch
Patch63:        pine-use-rpm_opt_flags.patch
Patch64:        pine-ldap_auth.patch

#----------- begin ALT part -------------------

Source2: %name-4.64L-alt4-conf.ALT
Source3: %name.conf.fixed
Source5: %{name}_16x16.xpm
Source6: %{name}_32x32.xpm
Source7: %{name}_48x48.xpm
Source9: filterpineconf

#Source8: imap-c-client-maildir.tar.bz2
# deprecated by Patch10:
# Maildir Driver By Eduardo Chappa <chappa@math.washington.edu>
# http://www.math.washington.edu/~chappa/pine/

Source11: %name-4.64-UW-docs.tar.bz2
Source12: %name-4.64L-info.ALT
Source13: %name-4.64L-ALT-longinfo.txt
Source14: %name-utils.readme
Source15: %name-4.42-substitute_technotes.txt
Source16: %name-4.42-substitute_FAQ.txt
Source17: http://www.suse.de/~bk/pine/FAQ.utf-8.html

# deprecated by iconv-based recoding engine
#Source50: z-recoding-engine-0.4.3.tar

# non-UW utils:
Source101: http://www.Physik.Uni-Dortmund.DE/~wacker/elm-to-pine
Source102: pine2Mutt
Source103: http://www.muc.de/~sam/pub/pine/ldif2pine-%ldifver.tar.bz2
Source110: %name-addrbk-utils-1.0-run-pwd2pine.sh

Patch201: pine4.61-suse-alt.patch

Patch205: pine-4.02-filter.patch
Patch221: pine-4.53-filter-local_nvtnl-reset.patch
Patch210: uw-imap-2002e-debian-portability.patch
Patch211: uw-imap-2001a-debian-nonull.patch
Patch213: uw-imap-2001a-overflow.patch

Patch204: uw-imap-2004-alt8-ALT-custom.patch
Patch206: uw-imap-2004-alt9-flocksim.patch

# build with tinfo instead of ncurses --- if_with tinfo
Patch207: pine-4.44L-tinfo.patch

# seems to be deprecated (old maildir patch)
Patch215: pine4.10-c-client_directory_with_driver.patch

Patch214: pine-4.21-fixhome.patch
Patch220: pine-4.55-boguswarning.patch
# adjusting build rules (merged from Lev's and RedHat's patches):
Patch270: pine-4.51-ALT-build.patch
# Filesystem paths patch: deprecated, replaced with subst below
Patch271: pine-4.55-ALT-path.patch

#------------ end ALT part --------------------


# Automatically added by buildreq on Wed Mar 01 2006
BuildRequires: libldap-devel libpam-devel libsasl2-devel libssl-devel
BuildPreReq: lynx
# it The LDAP library "ldap/libraries/libldap.a" is missing.
BuildPreReq: libldap-devel-static
%if "%pinelinuxtype" == "lnp"
BuildPreReq: libpam-devel
#BuildRequires: mailcap
%endif
%if "%pinelinuxtype" == "slx"
BuildPreReq: libkrb5-devel 
%endif

%if_with tinfo
BuildPreReq: libtinfo-devel
%else
BuildPreReq: libncurses-devel
%endif


%description
A text-based, but menu-driven and thus easy-to-use e-mail program. It
is very customizable from easy(default) to very powerful(for
powerusers) thru it's internal config menu.

It has many features, e.g. from Color support, threading and an
integrated help system.

Pine is a very popular, easy to use, full-featured email user agent
which includes a simple text editor called pico. Pine supports MIME
extensions and can also be used to read news.  Pine also supports
IMAP, mail, MH and Maildir (used by qmail) style folders.

Pine should be installed to make possible managing mail in a text terminal;
its interface is rather handy in that sense that it allows you to start
using the program without reading any additional documenation. It is a very
commonly used email user agent and it is currently in development.

Be careful when using %name with Maildir folders: the Maildir support
is brought into %name by a non-native code and might not work as stable
as other functions.

%description -l ru_RU.KOI8-R
Pine ("Сосна") -- Program for Internet News & Email. Это популярный,
простой в использовнии, полноценный пользовательский почтовый
агент (Mail User Agent), включающий в себя
простой текстовый редактор под названием pico. Pine поддерживает
расширения MIME; может быть использован для чтения новостей. Он умеет
работать с почтовыми ящиками в формате mail, MH и Maildir (с ними
работает qmail), а также ящиками, предоставляемыми по IMAP.

Его стоит установить, чтобы иметь возможность работать с почтой в текстовом терминале;
его интерфейс удобен тем, что позволяет начать пользоваться программой, не читая
дополнительной документации. Очень широко распространен; постоянно дорабатывается и
пополняется новыми возможностями.

Будьте осторожны, используя %name с ящиками в формате Maildir:
эта возможность добавлена в %name не авторами и может функционировать
не так стабильно, как остальные составляющие.

%package doc
Summary: More documentation for %name.
Summary(ru_RU.KOI8-R): Больше документации по %name.
Group: Networking/Mail

#' (syntax highlight cheater)
# Documentation can be installed independently of binaries
# (to get acquainted, to print out, ...),
# but if the binaries are installed, the doc-pkg should correspond
# to their version. This is expressed by the following conflicts.
Conflicts: %name < %fullversion
Conflicts: %name > %fullversion

%description doc
Three major groups of the additional documentation that supplemets the
%name package are:
 - User guide (tutorial)
 - Technical notes
 - FAQs
 - historical notes.

There are also a few other minor doc-files not so important for the main package. Some
of the documentation is distributed along with the source of %name by UW
(University of Washington), some is published separately on their site.

The Technical Notes included can be of some interest and use not only
to PINE developers and hackers, but also (and even much more) for users
getting "advanced".

%description doc -l ru_RU.KOI8-R
Три основные группы, на которые разбивается документация, дополняющая
пакет %name, это:
 - Руководство пользователя (обучающее)
 - Технические заметки
 - FAQs (Frequently Asked Questions -- Часто Задаваемые Вопросы)
 - Исторические заметки.

Также включено и несколько небольших, не очень важных для главного
пакета файлов с описаниями. Часть из включенной документации
распространяется UW (University of Washington) вместе с исходниками
%name, часть публикуется на их сайте.

Технические заметки, входящие в состав пакета, могут быть интересны не
только (и даже не столько) программистам-разработчикам и хакерам, но и
пользователям, желающим стать "продвинутыми".

%package addrbk-tools
Summary: A set of tools dealing with %name addressbook files.
Summary(ru_RU.KOI8-R): Набор инструментов для работы с записными книжками (adress books) %name.
Group: File tools
Version: %utilver
Prefix: %prefix
# It should be a "noarch" package

#
#There is a separate package with tools for mailbox conversions.

%description addrbk-tools
Most of these tools are scripts either contributed to Pine project or
written independently. All of them are intended to make PINE
addressbooks by extracting appropriate information from a file with account
information stored/used by another similar program (mail user agent).
A vice versa conversion may also be possible.

You should install %name-addrbk-tools if you wouldd like to migrate between %name
and Mutt, elm, mail, Netscape, or if you want just to have the same
address lists available in several mail user agents.

This package is relocatable. That means that if you need any of the
tools included in the package and you are not the administrator at your
site, you should be able to install the package locally to your homedir,
without having root-permissions, and use the tools. Read RPM
documentation on how to do so.

%description addrbk-tools -l ru_RU.KOI8-R
Основная часть этих инструментов -- скрипты, добавленные в проект Pine
как вклады со стороны (contributions) или написанные независимо от
него. Все они нацелены на то, чтобы создавать записную книжку для %name
путем извлечения информации из аналогичных файлов, созданных другими
похожими программами (mail user agents -- пользовательскими почтовыми
агентами) в других форматах. Обратное преобразование может быть тоже
возможно.

Стоит установить %name-addrbk-tools, если Вы хотите перейти с
использования Mutt, elm, mail, Netscape на использование %name (или
наоборот) или если Вы просто хотите иметь доступ к одним и тем же
записям (спискам адресов) сразу в нескольких почтовых агентах.

Этот пакет является перемещаемым (relocatable). Это должно позволить Вам в случае,
когда Вам нужен один из скриптов-преобразователей из этого пакета, но Вы
не являетесь администратором системы, установить его к себе в домашнюю
директорию и пользоваться им. Как это сделать -- см. описание RPM.



%package -n pico
Summary:        A small, easy to use editor
Group:          Editors
Version:        %{fullversion}

%description -n pico
Pico is a simple, display-oriented text editor based on the Pine
message system composer. As with Pine, commands are displayed at the
bottom of the screen, and context-sensitive help is provided.
Characters are inserted into the text as they are typed.

%if_with pilot-package
%package -n pilot
Summary:        Simple file system browser
Group:          File tools
Version:        %{fullversion}

%description -n pilot
Pilot is a simple, display-oriented file system browser based on the
Pine message system composer. As with Pine, commands are displayed at
the bottom of the screen, and context-sensitive help is provided.
%endif


%prep
%setup -q -n pine%{baseversion}
%if_with maildir
%patch10 -p1
#cd ..
#rm -rf		      pine%{baseversion}.chappa
#cp -al pine%{baseversion} pine%{baseversion}.chappa
#cd -
%endif

%if_with utf8
%patch11
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch18 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch26 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
#%patch39 -p1
#%patch40 -p1
rm `find -name "*.orig"`
%endif
%if_with maildir
#cd ..
#%define patchver pine%{baseversion}/utf-2c-%{baseversion}
#rm -rf		      pine%{baseversion}.utf-2c
#cp -al pine%{version} pine%{baseversion}.utf-2c
#diff -rNup pine%{baseversion}.chappa pine%{baseversion}.utf-2c >%{patchver} ||
#cd -
%patch41 -p0
%endif
# SUSE-specific patches last:
#%patch50 -p1
# fixed suse->alt 50->201
%patch201 -p1
%if_with suse-specific
%patch51 -p1
%patch52 -p1
%patch53 
%patch55 -p1
%patch56 -p1
%patch59
%patch60 -p0
%patch61
%patch62
%patch63
%patch64
%endif


#----------- begin ALT part -------------------
%if_with altmisc
%patch205 -p1 -b .filter
%patch221 -p1 -b .filter-reset

pushd imap
##%patch201 -p1 -b .glibc-time
%patch210 -p1 -b .deb-port
%patch211 -p1 -b .deb-nonull
%patch213 -p1 -b .overflow
##
### old maildir patch!!!!
#####patch209 -p2 -b .forPine
#####patch202 -p1 -b .glibc-time
popd

%patch204 -p1 -b .ALT
%patch206 -p1 -b .flock
%endif

%if_with tinfo
%patch207 -p1 -b .tinfo
%endif

%if_with altmisc
##%patch215 -p1 -b .cclientdir
#patch -p1 --suffix=.cclientdir --fuzz=3 < %PATCH215

%patch214 -p1
%patch220 -p1
%patch270 -p1 -b .buildconf
%endif

##%patch271 -p1 -b .path
# replaced by subst commands below
###############################
for i in doc/tech-notes/{cmd-line,low-level,background,config,config-notes,installation,porting}.html \
doc/pine.1 \
doc/tech-notes.txt \
README \
pico/osdep/os-lnx.h \
pine/mailcap.c \
pine/osdep/os-lnx.h \
pine/pine-use.c \
pine/init.c \
pine/pine.hlp
do
    echo fixing $i ...
    %__subst 's,/usr/local/lib/pine.conf,/etc/pine.conf,' $i
    %__subst 's,/usr/local/bin,/usr/bin,' $i
    %__subst 's,/usr/spool/mail,/var/spool/mail,' $i
    %__subst 's,/usr/spool/news,/var/spool/news,' $i
    %__subst 's,/usr/lib/news/active,/var/lib/news/active,' $i
    %__subst 's,/usr/local/lib/pine.info,/usr/lib/pine.info,' $i
done

%if %CustomPineBuild
patch -p1 pine/pine.h <<'EOF'
@@ -63,7 +63,7 @@
 #ifndef _PINE_INCLUDED
 #define _PINE_INCLUDED

-#define PINE_VERSION		"%baseversion"
+#define PINE_VERSION		"%fullversion"
 #define	PHONE_HOME_VERSION	"-count"
 #define	PHONE_HOME_HOST		"docserver.cac.washington.edu"

EOF
%endif


# utils:
install -p -m755 %SOURCE101 contrib/utils/elm2pine
install -p -m755 %SOURCE102 contrib/utils/pine2Mutt

# just in case this wants /usr/local/bin/perl
find contrib -type f |
	xargs fgrep -l /usr/local/bin/perl |
	xargs perl -pi -e 's|/usr/local/bin/perl|%_bindir/perl|'

%setup -qDT -a103 -n %name%baseversion
pushd ldif2pine-%ldifver
for n in ldif2pine; do
  { echo '#!%_bindir/perl -w'; cat $n.pl; } > $n
done
popd

#------------ end ALT part --------------------

%build

%ifarch ppc64
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -mminimal-toc -Wall"
%endif
#
# Prepare thebuild with LDAP support:
#
install -d ldap
ln -fs /usr/include ldap/include
ln -fs %{_libdir}/ ldap/libraries
#
# Determine if we need to link with libsasl2 or libsasl:
#
if [ -e %_libdir/libsasl2.so.2 ]; then SASL=2;fi
if [ -e %_libdir/libsasl2.so ]; then SASL=2;fi
#
# -Wall is useless with pine to find the real problems because the standard
# warnings happen in mass during a full compile since there is apparently
# no quality control done by developers regarding warnings:
#
# In case you need to debug, decomment this line:
%if_with debug
DEBUG="-DDEBUG -g3"
%else
DEBUG=""
%endif
# -Wno-pointer-sign removed. gcc-4 :(
./build CC=gcc \
EXTRACFLAGS="${RPM_OPT_FLAGS/-O2/-Os} \
-Wno-return-type -Wno-sign-compare -Wno-implicit-function-declaration \
-DLDAP_DEPRECATED -Wno-uninitialized \
-Wno-strict-aliasing -Wno-parentheses -Wno-switch -Wno-unused" \
			DEBUG="$DEBUG"\
%if_with ssl
			SSLTYPE=unix \
		        SSLCERTS=/usr/share/ssl/certs \
				SSLINCLUDE=/usr/include/openssl \
				SSLLIB=%{_libdir} \
				EXTRALDFLAGS="-lsasl$SASL" \
%else
			SSLTYPE=none \
			NOSSL \
%endif
%if_with mlock
				LOCKPGM=/usr/sbin/%{mlockname} \
%endif
				%pinelinuxtype \
			SYSTEM_PINERC="/etc/pine.conf" \
			SYSTEM_PINERC_FIXED="/etc/pine.conf.fixed" \
			PASSWD_PROG="/usr/bin/passwd"


#----------- begin ALT part -------------------
# Making docs
pushd doc
rm -f tech-notes.txt

pushd tech-notes
  make
  # preparing for install:
  #targetDir=$RPM_BUILD_ROOT%_docdir/%name-%fullversion-%release/tech-notes
  # Let's see how %%doc will pack it:
  txtDir=tech-notes
  htDir=tech-notes/HTML
  mkdir -p "$txtDir" "$htDir"
  for n in *.html; do
    install -p -m0644 "$n" "$htDir/$n"
	txtn="${n%%.html}.txt"
    install -p -m0644 "$txtn" "$txtDir/$txtn"
  done
  for n in tech-notes.txt; do
    %__rm -f "$n"; %__install -m0644 -p %SOURCE15 "$n"
  done
#------------ end ALT part --------------------


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT/%{_man1dir} $RPM_BUILD_ROOT/etc $RPM_BUILD_ROOT/%{_libdir}
install bin/{mtest,pine,pico,pilot,rpdump,rpload,mailutil} $RPM_BUILD_ROOT%{_bindir}/
install -m 644 doc/{pine.1,pico.1,pilot.1,rpdump.1,rpload.1} $RPM_BUILD_ROOT%{_man1dir}/
install -m 644 imap/src/mailutil/mailutil.1 $RPM_BUILD_ROOT%{_man1dir}/
#%%suse_update_desktop_file -i pine ConsoleOnly Email
rm -f $RPM_BUILD_ROOT/usr/share/pixmaps/email.png
# (-f is needed here for building on older dists where this file does not exist)



#----------- end suse part --------------------

#----------- begin ws part -------------------
%if_with mlock
install -D -m755 imap/mlock/mlock $RPM_BUILD_ROOT%{_sbindir}/%{mlockname}
%endif
#----------- end   ws part --------------------

#----------- begin ALT part -------------------
# data: perhaps put it in shared?
#install -p -m644 doc/mime.types $RPM_BUILD_ROOT%_libdir/mime.types

# config files
install -p -m644 -D %SOURCE2 $RPM_BUILD_ROOT%_sysconfdir/pine.conf
install -p -m644 -D %SOURCE3 $RPM_BUILD_ROOT%_sysconfdir/pine.conf.fixed
cat >> $RPM_BUILD_ROOT%_sysconfdir/pine.conf.fixed <<EOF
# Full name for "local support" address used by "Report Bug" command.
# Default: Local Support
local-fullname=%packagerName

# Email address used to send to "local support".
# Default: postmaster
local-address=%packagerAddress
EOF

%if %CustomPineBuild

# pine-info: also a kind of data mixed with docs - shared?
{
  echo -e "You are probably using PINE %fullversion configured for %distribution.\n"
  cat %SOURCE12
} > "$RPM_BUILD_ROOT"%_libdir/pine.info

# overriding the source with a symlink - requires a hack in the %files 
# section, otherwise it will be copied, not linked
ln -s -f %_libdir/pine.info doc/pine.info

%endif

install -p -m755 -D %SOURCE9 $RPM_BUILD_ROOT%{_bindir}/filterpineconf

# docs:
bzcat %SOURCE11 | tar x
pushd doc

install -p -m644 -D %SOURCE13 ALT-packaging-info
install -p -m644 -D %SOURCE14 README.addrbk-tools
install -p -m644 -D %SOURCE17 .

# Rename txt files that we don't want to be included in the main
# package:
for n in FAQs; do
  mv "$n.txt" "$n"
done

install -m0644 -p %SOURCE16 FAQ.where
popd

install -p -m644 -D %SOURCE5 $RPM_BUILD_ROOT%_miconsdir/%name.xpm
install -p -m644 -D %SOURCE6 $RPM_BUILD_ROOT%_niconsdir/%name.xpm
install -p -m644 -D %SOURCE7 $RPM_BUILD_ROOT%_liconsdir/%name.xpm

# (fg) Menu entry 1 (pine)
mkdir -p $RPM_BUILD_ROOT%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=%name
Comment=%name: %mainsummary
Icon=%name
Exec=%exec
Terminal=true
Categories=Network;Email;ConsoleOnly;
EOF

cat > %buildroot%_desktopdir/pico.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=pico
Comment=pico: default editor for pine
Icon=%name
Exec=pico
Terminal=true
Categories=Utility;TextEditor;ConsoleOnly;
EOF

%if_with pilot-package
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=pilot
Comment=pilot: pine file browser
Icon=%name
Exec=pilot
Terminal=true
Categories=System;FileManager;ConsoleOnly;
EOF
%endif

# utils:
for n in pine2Mutt elm2pine; do
  %__install -p -m0755 "contrib/utils/$n" "$RPM_BUILD_ROOT"%_bindir/"$n"
done

for n in brk2pine; do
  %__install -p -m0755 "contrib/utils/$n.sh" "$RPM_BUILD_ROOT"%_bindir/"$n"
done

for n in ldif2pine-%ldifver/ldif2pine; do
  %__install -p -m0755 "$n" "$RPM_BUILD_ROOT"%_bindir
done

for n in "%_libdir/pwd2pine"; do
 %__install -p -m0644 "contrib/utils/$(basename "$n")" "$RPM_BUILD_ROOT$n"
 %__install -p -m0755 %SOURCE110 "$RPM_BUILD_ROOT%_bindir/$(basename "$n")"
done

#------------ end ALT part --------------------


#----------- begin ALT part -------------------
%post
%if %MergeConfPostInstall

# Set up system-wide defaults for pine by merging the config file
# already present in the system with some new settings. (The old
# settings are appended at the end of the new, so that the old ones
# override the new.)
# All this is just cosmetic.
# The enormous script is rather ugly. A better solution would be to
# teach pine to accept multiple additive feature-lists in one file.
# And to let it verify the set of options.

# hack:
# removed disable-charset-conversions

function collectItems() {
local SORT
if [[ "$1" == "-nosort" ]]; then
    SORT=cat; shift
else
    SORT='sort -u'
fi

local listID="$1"
local moved_msg="${2:-'Moved by RPM'}"

local first="^$listID="
local last='[^,]$'

local readItems="$(mktemp "$listID.XXXXXX")"

  sed -e "
      /$first\$/ b moved
      /$first.*$last/  b item
      /$first/,/$last/ b item
      b
      : item
        w $readItems
      : moved
        s/^/#$moved_msg: /
	"
    echo
    cat $readItems \
    | grep -v 'disable-charset-conversions' \
    | sed -e "
        s/$first/ /
        s/^[[:space:]]*\$//
        s/^[[:space:]]\+/ /
        s/$last/&,/
      " \
    | $SORT \
    | cat --squeeze-blank \
    | sed -e "
        1  s/^[[:space:]]*/$listID=/
        \$ s/,\$//
      "
    rm -f "$readItems"
}

echo $"Re-generating system-wide config files on the base of the old ones:"
for n in %_sysconfdir/pine.conf; do
  old="$n.rpmorig"
  new="$n.rpmnew"

  if [[ -e "$new" ]]; then cp -f "$new"{,.last}; fi

  echo -n "$n: "
  {
    cp -f "$n" "$old"

    filter=''
    for listID in feature-list '-nosort url-viewers'; do
      filter="$filter | collectItems $listID"
    done
    eval "cat '$new' '$old' 2> /dev/null" "$filter" > "$n"
    unset filter

    if [[ "$n" == %_sysconfdir/pine.conf ]]; then
      %exec -conf > "$new" && mv -f "$new" "$n"
    fi

    # We do not need an identical file saved in $old
    if diff -q "$old" "$n" &> /dev/null; then
      rm -f "$old"
    else
      printf $"original saved to %%s, " "$old"
    fi
  } && echo -e $"\tre-generated successfully :-)" \
    || echo $"\tre-generation failed :-("
  unset old new
done
%endif

#------------ end ALT part --------------------


%files
%defattr(-, root, root)
%{_man1dir}/pine.1.*
%{_man1dir}/rpdump.1.*
%{_man1dir}/rpload.1.*
%{_man1dir}/mailutil.1.*
%doc CPYRIGHT README 
%if_with maildir
%doc README.maildir
%endif
#README.SuSE
%doc doc/brochure.txt doc/mailcap.unx doc/mime.types doc/pine-ports
#%doc doc/tech-notes.txt doc/tech-notes
%{_bindir}/mtest
%{_bindir}/pine
%{_bindir}/rpdump
%{_bindir}/rpload
%{_bindir}/mailutil
%if_with mlock
%attr(2755, root, mail) %{_sbindir}/%{mlockname}
%endif
#/usr/share/applications/pine.desktop

#----------- begin ALT part -------------------
%{_bindir}/filterpineconf
%doc contrib/bitmaps imap/docs/bugs.txt
%{_desktopdir}/pine.desktop
%_miconsdir/%name.xpm
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm
#%attr(0644,root,root)	%_libdir/mime.types
%if %CustomPineBuild
%attr(0644,root,root)	%config(missingok) %_libdir/pine.info
# I like the "--no-dereference hack" ;-)
%doc --no-dereference doc/pine.info
%endif

%attr(0644,root,root)	%config(noreplace) %_sysconfdir/pine.conf
%attr(0644,root,root)	%config(noreplace) %_sysconfdir/pine.conf.fixed

## special docs:
## (RE):
%doc doc/ALT-packaging-info
%doc doc/tech-notes/tech-notes.txt
%doc doc/credits.html
# SuSE site
%doc doc/FAQ.utf-8.html
#------------ end ALT part --------------------

%if_with pilot-package
%files -n pilot
%defattr(-, root, root)
%{_desktopdir}/pilot.desktop
%endif
%{_bindir}/pilot
%doc %{_man1dir}/pilot.*

%files -n pico
%defattr(-, root, root)
%{_bindir}/pico
%{_desktopdir}/pico.desktop
%doc %{_man1dir}/pico.*
%_miconsdir/%name.xpm
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm

#----------- begin ALT part -------------------
%files doc
%doc doc/{tutorial.4,FAQs,faq}
%doc doc/tech-notes/tech-notes
%doc doc/{pine-ports,pine-info.txt}
%doc doc/{project-history,changes}.html

%files addrbk-tools
%doc doc/README.addrbk-tools ldif2pine-%ldifver/*.txt
%attr(0755,root,root) %_bindir/*2pine
%attr(0755,root,root) %_bindir/pine2*
%attr(0644,root,root) %_libdir/pwd2pine
#------------ end ALT part --------------------

%changelog -n pine
* Mon Apr 25 2011 Igor Vlasenko <viy@altlinux.ru> 4.64L-alt8
- desktop: updated categories (added ConsoleOnly).

* Tue Apr 05 2011 Igor Vlasenko <viy@altlinux.ru> 4.64L-alt7
- converted menu to .desktop

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 4.64L-alt6.1
-  rebuild with new openssl

* Mon Apr 06 2009 Igor Vlasenko <viy@altlinux.ru> 4.64L-alt6
- removed deprecated post calls

* Fri Mar 07 2008 Igor Vlasenko <viy@altlinux.ru> 4.64L-alt5
- just a rebuild to get rid of ipl*mdk

* Tue Oct 24 2006 Igor Vlasenko <viy@altlinux.ru> 4.64L-alt4
- sync with SuSE pine 4.64N-6:
  * allow connect to LDAP servers which need authentication
  * bugfixes for utf-8 console
- changes in pine.conf:
  * added compose-cancel-confirm-uses-yes to restore old pine behaviour
  * pruning-rule=ask-no instead of yes-no (does not autorename send-mail)

* Sun Oct 15 2006 Igor Vlasenko <viy@altlinux.ru> 4.64L-alt3
- fixed pico menu entry

* Wed Mar 15 2006 Igor Vlasenko <viy@altlinux.ru> 4.64L-alt2
- spec cleanup;
- built with libtinfo

* Wed Mar 08 2006 Igor Vlasenko <viy@altlinux.ru> 4.64L-alt1
- new version;
- pico moved into separate package;
- utf-8 support from SuSE pine 4.64-9 patch of Bernhard Kaindl <bk@suse.de>
- new recoding scheme obsoletes Lev Levitin's <lev@mccme.ru> recoding patch;
- new maildir driver By Eduardo Chappa <chappa@math.washington.edu>;
- MergeConfPostInstall automatically removes disable-charset-conversions
    as required for new recoding scheme to work;
- optional support of mail locking using external mlock;

* Fri Feb 11 2005 Ivan Zakharyaschev <imz@altlinux.ru> 4.58L-alt4
- Fix a bug introduced by the previous change (caused crashes on recoding).

* Thu Feb  3 2005 Ivan Zakharyaschev <imz@altlinux.ru> 4.58L-alt3
 (no user visible changes)
- gcc 3.4 adaptions (of ALT's contributed code).
- The weaker "url_handler" dependency (instead of "urlview").

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 4.58L-alt2.1
- Rebuilt with openssl-0.9.7d.

* Mon Nov  3 2003 Ivan Zakharyaschev <imz@altlinux.ru> 4.58L-alt2
- the changes are merely in packaging:
  + merge the spec/patches for ALT Master 2.0 updates 
    (by a tweak/trick in pine-4.58L-alt2-0.4.1.diff);
  + fix non-Latin characters in English description.

* Mon Sep 15 2003 Ivan Zakharyaschev <imz@altlinux.ru> 4.58L-alt1
- new upstream version (various fixes, among them for the 2 vulnerabilities
  described at http://www.idefense.com/advisory/09.10.03.txt):
  + patches incorporated into the upstream release: 22 (mbox-inbox),
    10 (partially uw-imap-2001a-debian-portability for os_lnx.h);
  + redone patches: 17 (uw-imap-2002-alt-openssl), the L diff;
  + updated docs;
- pine-addrbk-utils' "Requires" updated.

* Sat May 10 2003 Ivan Zakharyaschev <imz@altlinux.ru> 4.55L-alt2
- use some new features in the system-wide configuration (color signature,
  warn-if-blank-subject and -to-or-cc);
- update docs;
- add a note on the conflict between recoding 
  and the native Pine's conversion facilities;

* Sat May 10 2003 Ivan Zakharyaschev <imz@altlinux.ru> 4.55L-alt1
- new upstream version + upstream patch for it (bug fixes and new features:
  view: http://www.washington.edu/pine/changes/4.53-to-4.55.html);
- minor changes in the L-extension (recoding);

* Fri May  9 2003 Ivan Zakharyaschev <imz@altlinux.ru> 4.53L-alt2
- L-extension 0.4.0 (recoding):
  + fix Formatted Save ($) command dialog;
  + fix crash when replying to a recoded message;
  + fix crash when working with formatted saved msgs with recoded headers;
  + add support for smart autorecoding of rfc1522-strings (used in headers);
  + if formatted-save-stop-recode is on, bring Pine to the auto-recode mode 
    after a formatted save operation ($);
  + introduce "brute recoding of headers" mode (^R H) on top of the 
    normal "smart" recoding; it replaces the obsolete 
    "recode-header" configuration option present in previous releases;
  + change internals of the Pine-filter-recoding interaction:
    store the recoding pipe per filter;
  + other enhancements in the internals;
- spec: %%add_optflags %%optflags_debug for the normal build 
  (will be stripped at the end by rpm; useful for debugging);

* Thu Jan 23 2003 Ivan Zakharyaschev <imz@altlinux.ru> 4.53L-alt1
- new upstream version: fixes a bug with filter rules matching and actions
 (see Release Notes in the Main Menu 
 or http://www.washington.edu/pine/changes.html).

* Fri Jan 10 2003 Ivan Zakharyaschev <imz@altlinux.ru> 4.52L-alt1
- new upstream version: it does not introduce major new functionality,
  it addresses bugs found in earlier versions (see Release Notes in
  the Main Menu or http://www.washington.edu/pine/changes.html):
  + patch130 (Lev's recode) - redone;
  + docs - updated.

* Tue Dec 31 2002 Ivan Zakharyaschev <imz@altlinux.ru> 4.51L-alt2
- pine.conf: disable-charset-conversions, disable-2022-jp-conversions
  (disable the built-in recoding, added in 4.50 upstream;
  ALT's recoding is more universal -- it supports multibyte encodings).

* Sun Dec 29 2002 Ivan Zakharyaschev <imz@altlinux.ru> 4.51L-alt1
- new upstream version, patches changed:
  + patch12 (deb-blackbox) - not applied (as in Debian);
  + patch18 (client address logging) - is upstream;
  + patch19 (buffer overflow in body structure extension) - upstream;
  + patch17 (SSL paths) - redone;
  + patch120 (build conf) - redone;
  + patch130 (Lev's recode) - redone;
  + docs - updated.

* Fri Oct 18 2002 Ivan Zakharyaschev <imz@altlinux.ru> 4.44L-alt4
- Added 2 utilities: rpdump, rpload -- for Pine Remote data management
- link against libtinfo instead of libncurses
- (synced with uw-imap-2001a-alt8)
- follow the SSLDIR relocation:
  + set %%_ssldir according openssl-config output (/var/lib/ssl now)
  + fix docs
- use %_var/mail/ as the mailbox directory (instead of /var/spool/mail/) 
  as FHS requires

* Fri Oct 18 2002 Ivan Zakharyaschev <imz@altlinux.ru> 4.44L-alt3.1.1
- (synced with uw-imap-2001a-alt5.1.1)
- Fixed: 
  + locking on reiserfs (#0001400 at bugs.altlonux.ru): make the locking 
    routine work on all kinds of FS through fcntl(2), and make it not silently 
    be a no-op (always issue a warning if locking is disabled)
  + client address logging in server_init() (thanks to Andrey Khavryuchenko 
    <akhavr at kds.com.ua> and RH: #60290 at bugzilla.redhat.com)
  + libc-client's support for a certain IMAP extension 
    (not supported by UW imapd yet; more info inside patch16)
- spec-file (no impact on the binaries):
  + pass SSLCERTS directory in %%build

* Tue May 14 2002 Ivan Zakharyaschev <imz@altlinux.ru> 4.44L-alt3
- spec-file: 
    + change the %%With* macros a bit;
    + enable defining %%release in command line;

* Tue May  7 2002 Ivan Zakharyaschev <imz@altlinux.ru> 4.44L-alt2
- code fixes (the same as in uw-imap-2001a-alt3):
  + use flock simulation via fcntl to be consistent with the other part
    of ALT Linux system, fcntl's error processing changed (flocksim.patch);
  + two potential SegFaults (in message parsing -- patch13;
    and working with a specific blackbox config -- patch11);
- more ALT Linux (and RedHat- and Debian-like, FHS complaint) system specific
  customization (several patches merged):
  + change paths to the server binaries in configuration and docs;

* Sun Jan 13 2002 Ivan Zakharyaschev <imz@altlinux.ru> 4.44L-alt1
- new upstream version (4.44): security bug fixed ("URL handler
  allows embedded commands")
- config options updated (suggestions by Michael Shigorin <mike@lic145.kiev.ua>)
- for packagers: patches and various build options (make args, defines)
  synced with uw-imap pkg (no major changes)

* Fri Nov 30 2001 Ivan Zakharyaschev <imz@altlinux.ru> 4.43L-alt1
- new upstream version (4.43)

* Fri Nov 30 2001 Ivan Zakharyaschev <imz@altlinux.ru> 4.42L-alt3
- charset-editorial for autorecoded messages 
- URL-viewing via url_handler.sh from urlview pkg (originally for Mutt)
- update docs
- for packagers: the postinstall script whose task is to merge config-files 
  now can either sort alphabetically a list of Pine options or not (these
  variants are used for feature-list and url-viewers).

* Fri Nov 23 2001 Ivan Zakharyaschev <imz@altlinux.ru> 4.42L-alt2
- recoding engine improved to support multibyte charsets

* Fri Nov 23 2001 Ivan Zakharyaschev <imz@altlinux.ru> 4.42L-alt1
- new version: 4.42
- for packagers:
  + some old patches removed, most of others redone
  + paths for SSL build are now set in the the call of ./build in
    %%build (and the Makefiles are not patched as before)
  + some texts moved out of the spec into separate files
  + imap-vfs.patch thrown away
  + do not apply all the flock-patches

* Thu Mar 01 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 4.33L-ipl2mdk
- now builds on glibc 2.2.2 (two trivial patches: for imap -- from
  RedHat people & for maildir module)
- two simple cosmetic patches from the authors (21, 22)
- Changes in the spec-file:
  + maildir patch splitted into three pieces: the module, a patch that
    "embeds" it into the main source tree and pine-specific (not server)
    defs.
  + warning about Maildir added to the description
  + Russian summaries and descriptions commented out
  + no need for explicit unsetting locale before build -- done by rpm now

* Sun Feb 25 2001 Ivan Zakharyaschev <vanyaz@mccme.ru>
- some fixes in menu entries' fields

* Fri Feb 02 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 4.33L-ipl1mdk
- new source, a pair of patches redone (maildir, imap related)
- some new docs from UW
- openssl patch splitted in two (to share it with imap)
- sparc patch thrown away

* Tue Jan 23 2001 Ivan Z. <vanyaz@mccme.ru> 4.32L-ipl4mdk
- descriptions changed a bit
- "regeneration script": localized messages ($".."), don't make a copy
  identical to the newly created file

* Sun Jan 21 2001 Ivan Z. <vanyaz@mccme.ru> 4.32L-ipl3mdk
- small changes in pine.conf (to make it differ)
- cleanup_spec
- unset LANG and others before building pine
- Russian summaries & descriptions

* Fri Jan 19 2001 Ivan Z. <vanyaz@mccme.ru> 4.32L-ipl2mdk
- pine.conf generating script rewritten

* Thu Jan 18 2001 Ivan Z. <vanyaz@mccme.ru> 4.32L-ipl1mdk
- new source

* Mon Dec 25 2000 Dmitry V. Levin <ldv@fandra.org> 4.31L-ipl2mdk
- Build with openssl support (openssl-0.9.6-ipl1mdk).

* Wed Dec 13 2000 Ivan Z. <vanyaz@mccme.ru> 4.31L-ipl1mdk
  - new version
  - temporarily build without ssl (without patching imap);
    will return it back after some corrections
  - confvar, segfix, sparc patches not needed any more
  - fuzzy parts of L-patch moved to other places: adding L-suffix to the
    version in pine.h by a patch inside the spec-file; a special patch
	for relnotes
  - wmconfig finally removed

* Wed Nov 22 2000 Ivan Z. <vanyaz@mccme.ru> 4.30-ipl2mdk
  - bzip2 ps in doc/GettingStarted (perhaps make all the additional docs
	a separate subpackage?)
  - make a subpackage for docs (1.5M)

* Mon Nov 20 2000 Ivan Z. <vanyaz@mccme.ru>
  - tools package made relocatable (is it good?)
  - some verification types aren't performed on config files (useless because
	they are generated in post-install)

* Sun Nov 19 2000 Ivan Z. <vanyaz@mccme.ru>
  - post-install script now merges feature-lists of new and old config
	files before by concatenating them as whole files
  - some utilities added; the subpackage renamed (there will be a
	separate package for mailbox tools).

* Sat Nov 18 2000 Ivan Z. <vanyaz@mccme.ru>
  - direct merge with RedHat:
	+ work around a compiler bug on ia64 (do we need this anymore?)
	+ set rsh-open-timeout to 0

* Fri Nov 17 2000 Ivan Z. <vanyaz@mccme.ru>
- Almost all patches and icons bunzipped (that makes srpm's smaller!)
- Structure and install procedure of additional sources re-organized
- (RE) Lev's extension improved (L-2_2):
  + charset naming system in rules the same as in the rest of PINE;
  + Paratype-154 (Asian Cyrillic) added
- (RE) README.ipl gets fuller
- the old pine.wmconfig added to docs (contrib/)
- performing build in C locale (to get "C" dates)
- full version macro defined (a means of striking the subpackage
  overriding version-macro)

* Wed Nov 15 2000 Ivan Z. <vanyaz@mccme.ru>
- (RE) README.ipl written
- give up attempts setting the display charset automatically
- our (RE) "path" and "build" patches absorbed similar new patches
  from Mdk/RH
- "noreplace" not set for pine.conf, 'cause it's re-generated
- merged with Mdk (Cooker), which in its turn has merged with RH
  (not all changes migrated, differences are mentioned above):

###############################
# begin insertion from Mandrake

* Fri Nov 10 2000 Vincent Danen <vdanen@mandrakesoft.com> 4.30-3mdk
- merge with Red Hat
- use lnp (PAM auth) instead of slx (crypt)
- some spec fixes
- enable SSL
- make config files noreplace
- added large icon
- bzip patches and icons

* Thu Nov 09 2000 Vincent Danen <vdanen@mandrakesoft.com> 4.30-2mdk
- patch to correct pine crashing and check extra NULL pointers from RH

* Tue Nov 07 2000 Vincent Danen <vdanen@mandrakesoft.com> 4.30-1mdk
- 4.30
- security fix for incoming mailbox handling
- remove hardcoded icon directory in menus

# end of insertion from Mandarke
################################

* Thu Nov 07 2000 Ivan Z. <vanyaz@mccme.ru> 4.30-ipl1mdk
- a separate package for utilities (only those that make
  sense with the newest Pine version; they were taken from contrib/utils
  in the source tree and other references in the FAQs)
- documentation brought into order (added local and native, downloaded from UW info)
- A patch from RH (an advanced substitute for the "DEBUG" patch
  (supplied by Trond Eivind Glomsrшd <teg@redhat.com>)

* Sat Nov 4  2000 Ivan Z. <vanyaz@mccme.ru>
- configuration files:
  + merging with existed on install,
  + demonstrating new options
  + auto-detecting system console character set
- (RE) Lev's extension adapted and improved (L-2_1):
  + understands "windows-*" encoding names
  + has 7-bit KOI option
- making docs (text and HTML)

* Fri Nov 3  2000 Ivan Z. <vanyaz@mccme.ru>
- Bug fixed: pine now works with no DEBUG compiled in ("init" patch).

* Wed Nov 1  2000 Ivan Z. <vanyaz@mccme.ru>
- The path patches, that were correcting the paths for Mandrake system
 (/var, /etc, no /usr/local), merged into one big patch with my additions.
 In fact, there were three of them: Lev's, RedHat's and "passwd"; I think
 the idea of patching in order to change the pathnames isn't good: better
 to write a script that would process the sources.
- vfs patch re-made for pine4.30.
- a small configuring patch made out of the old RedHat's patch (QUOTAS).

* Sun Oct 29 2000 Ivan Z. <vanyaz@mccme.ru>
- "maildir" patch that has been present in RE was even newer/better than that in Cooker (2 patches)
- two system-wide config files in one tar
- rpm-3.0.6 adaptations:
  + BuildRoot tag removed
  + compression of man-pages removed
  + rm -rf in build root not needed any more
- new version (4.30)
- spell patch was bad (the corrections were wrong), removed
- Lev's patch splitted into two: recoding and path adaptations for Mdk filesystem.
- merged with Cooker (here's the Mandrake's changelog):

###############################
# begin insertion from Mandrake

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.21-6mdk
- automatically added BuildRequires

* Thu Aug 03 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.21-5mdk
- rebuild for BM
- rebuild with macros
- tmppath
* Sun Apr 09 2000 Denis HAvlik <denis@mandrakesoft.com> 4.21-4mdk
- Group: Networking/Mail
- pine-tree icon + menu entries (for pine + pico)
- spec-helper

* Sat Feb 19 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 4.21-3mdk
- make patch to change os-lnx.h from /bin/passwd to /usr/bin/passwd

* Tue Dec 14 1999 John Buswell <johnb@mandrakesoft.com>
- add new maildir patches
- add vfs patch
- fixed non-existant directory seek problem (bug:#506)

* Tue Nov 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 4.21.
- Merge with recent redhat changes.

# end of insertion from Mandarke
################################

* Sun Nov 18 1999 AEN <aen@logic.ru>
- new version
- Lev Levitin's <lev@mccme.ru> recoding patch
- build for RE

* Tue Nov 02 1999 John Buswell <johnb@mandrakesoft.com>
- Rebuild and Repackage for oxygen (release 2)

* Thu Oct 14 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 4.20
- sync with RH

* Thu Aug 12 1999 Cristian Gafton <gafton@redhat.com>
- add maildir patch

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Fri Feb 26 1999 Cristian Gafton <gafton@redhat.com>
- fix buildroot and add cleanup section
- move config files to /etc/pine.conf

* Tue Feb 02 1999 Preston Brown <pbrown@redhat.com>
- turned off .pine-debugX files

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Fri Nov 13 1998 Cristian Gafton <gafton@redhat.com>
- patch to enable SIGWINCH processing (why do the pine folks keep
  disabling this stuff?!)

* Fri Oct 09 1998 Cristian Gafton <gafton@redhat.com>
- use termios instead of termio (patch used to be in here...)
- use terminfo instead of termcap and link against ncurses instead of termcap
- supply -lcrypt as a standard lib

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- upgrade to 4.04 (compatibility with some client imaps).

* Fri Sep 11 1998 Jeff Johnson <jbj@redhat.com>
- use only fcntl locking.

* Thu Sep 10 1998 Jeff Johnson <jbj@redhat.com>
- update to 4.03

* Fri Aug 14 1998 Jeff Johnson <jbj@redhat.com>
- patch to 4.02A.
- disable stupid EACCESS warnings.

* Wed Jul 22 1998 Jeff Johnson <jbj@redhat.com>
- update to 4.02.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jan 15 1998 Erik Troan <ewt@redhat.com>
- added patch to fix pine filters

* Tue Dec 30 1997 Erik Troan <ewt@redhat.com>
- fixed resizing in pine and pico

* Thu Dec 18 1997 Erik Troan <ewt@redhat.com>
- removed patch for SIGCHLD race -- it shouldn't be necessary
- added patch to avoid longjmp() from SIGCHLD handler -- SIGCHLD handling
  is sane now

* Thu Dec 11 1997 Cristian Gafton <gafton@redhat.com>
- added a patch for handling a SIGCHLD race condition

* Tue Nov 04 1997 Erik Troan <ewt@redhat.com>
- fix for locks w/ long st_dev field
- use termios rather then termio

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- removed exec bit from /usr/doc/pine-3.96-1/contrib/utils/pwd2pine

### Local Variables: 
### coding: koi8-r
### End: 
