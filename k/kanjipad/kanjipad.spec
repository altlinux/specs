Name: kanjipad
Version: 2.0.0
Release: alt1

Summary: enter Japanese hieroglyphs (kanji) graphically
License: GPL
Group: Education
Url: http://fishsoup.net/software/%name
Packager: Alex V. Myltsev <avm@altlinux.ru>

Source: %url/%name-%version.tar.gz
Source50: kanjipad.1
Source51: kpengine.1
Patch0: kanjipad-2.0.0-debian-gtkinc.patch

BuildRequires: libgtk+2-devel

%description
KanjiPad is a tiny application that allows the user to enter 
Japanese characters graphically. It uses the handwriting-recognition
algorithm from Todd Rudick's program JavaDic.

%prep
%setup -q
%patch0 -p2

%build
make BINDIR=%_bindir DATADIR=%_datadir OPTIMIZE="%optflags"

%install
make BINDIR=%_bindir DATADIR=%_datadir DESTDIR=%buildroot install
mkdir -p %buildroot%_man1dir
cp %SOURCE50 %SOURCE51 %buildroot%_man1dir/

%files
%_bindir/*
%_datadir/%name
%_man1dir/*
%doc README

%changelog
* Fri Sep 22 2006 Alex V. Myltsev <avm@altlinux.ru> 2.0.0-alt1
- Initial build for Sisyphus.

* Sun Aug 25 2002 Owen Taylor <otaylor@redhat.com>
- Version 2.0.0, clean up spec file

* Thu Apr 15 1999 Owen Taylor <otaylor@redhat.com>
- Up version to 1.2.2, added to tar file

* Wed Mar 31 1999 Owen Taylor <otaylor@redhat.com>
- Initial spec file 
