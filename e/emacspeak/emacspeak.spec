%define _unpackaged_files_terminate_build 1
%define _emacspeakdir %_datadir/emacs/site-lisp/emacspeak

Name:       emacspeak
Version:    60.0
Release:    alt1

Summary:    Speech output interface to Emacs.
License:    GPLv2+ and BSD
Group:      Accessibility
Url:        http://emacspeak.sourceforge.net
VCS:        https://github.com/tvraman/emacspeak

Source0: %name-%version.tar
Source1: %name-profile.sh
Source2: enable-%name

Requires: espeak
Requires: tclx
Requires: gcc
Conflicts: ru_emacspeak

%filter_from_requires \,/etc/emacspeak.conf,d

BuildRequires(pre): rpm-macros-emacs
BuildRequires: rpm-build-emacs
BuildRequires: emacs-speedbar
BuildRequires: gcc-c++
BuildRequires: libalsa-devel
BuildRequires: tcl-devel
BuildRequires: espeak-ng-devel
BuildRequires: makeinfo
BuildRequires: perl-libwww
BuildRequires: perl-HTML-TableExtract


%description
Emacspeak is a speech interface that allows visually impaired users to interact
independently and efficiently with the computer.

%prep
%setup

%build
make config SRC=`pwd`
make
make espeak 
makeinfo -o info/ info/emacspeak.texi

%install
install -d %buildroot%_datadir/emacs/site-lisp
install -d %buildroot%_emacspeakdir

install -d %buildroot%_emacspeakdir/lisp
install -d %buildroot%_emacspeakdir/lisp/g-client

install -d %buildroot%_emacspeakdir/etc
install -d %buildroot%_emacspeakdir/xsl
install -d %buildroot%_emacspeakdir/sounds

install -d %buildroot%_emacspeakdir/servers
install -d %buildroot%_emacspeakdir/servers/native-espeak

install -d %buildroot%_libdir/%name/servers
install -d %buildroot%_libdir/%name/servers/native-espeak

install -d %buildroot%_bindir
install -d %buildroot%_sysconfdir/profile.d

install -d %buildroot%_emacspeakdir/etc/forms
install -d %buildroot%_emacspeakdir/etc/tables


install -m 0644 lisp/*.el lisp/*.elc %buildroot%_emacspeakdir/lisp

cp -f etc/*.pl etc/*.sh etc/cbox* etc/pdf2text etc/emacspeak.xpm \
      etc/emacspeak.jpg %buildroot%_emacspeakdir/etc

install -m 0644 xsl/*.xsl %buildroot%_emacspeakdir/xsl

cp  -fR sounds/3d \
        %buildroot%_emacspeakdir/sounds

install -m 0755 servers/.servers servers/espeak \
                servers/speech-server servers/log-* \
                servers/cloud* %buildroot%_emacspeakdir/servers

install -m 0755 \
                servers/tts-lib.tcl \
                %buildroot%_emacspeakdir/servers
            
install -m 0755 \
                servers/native-espeak/*.cpp \
                %buildroot%_emacspeakdir/servers/native-espeak

install -m 0755 servers/native-espeak/tclespeak.so \
                %buildroot%_libdir/%name/servers/native-espeak
ln -s %_libdir/%name/servers/native-espeak/tclespeak.so \
      %buildroot%_emacspeakdir/servers/native-espeak

install -m 0755 %SOURCE1 %buildroot%_sysconfdir/profile.d/%name.sh
install -m 0755 %SOURCE2 %buildroot%_bindir/enable-%name

cp  -fR media %buildroot%_emacspeakdir/media

rm -f %buildroot%_emacspeakdir/media/.nosearch \
      %buildroot%_emacspeakdir/media/*/.nosearch \
      %buildroot%_emacspeakdir/sounds/*/.nosearch

install -m 0644 etc/forms/*.el %buildroot%_emacspeakdir/etc/forms
install -m 0644 etc/tables/*.tab %buildroot%_emacspeakdir/etc/tables

%post
chmod -R go+rX %_emacspeakdir/sounds
chmod -R go+rX %_emacspeakdir/media

%files
%doc README* info/*info*
%_bindir/enable-%name
%_libdir/%name/servers/native-espeak/*.so
%_emacspeakdir/*
%config %_sysconfdir/profile.d/*

%changelog
* Tue Jun 30 2026 Artem Semenov <savoptik@altlinux.org> 60.0-alt1
- new version 60.0 (thx: Aleksandr Dovydenkov)

* Fri Jun 05 2026 Artem Semenov <savoptik@altlinux.org> 58.0-alt2
- Added conflicts to ru_emacspeak

* Fri Sep 22 2023 Danil Shein <dshein@altlinux.org> 58.0-alt1
- new version 58.0
  + fix FTBFS

* Thu Apr 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 55.0-alt1
- 55.0 releaseed

* Thu Dec 30 2021 Igor Vlasenko <viy@altlinux.org> 50.0-alt2
- NMU: fixed build

* Mon Jul 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 50.0-alt1
- Build new version 50.0
