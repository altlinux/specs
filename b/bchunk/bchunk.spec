Name: bchunk
Version: 1.2.0
Release: alt1

Summary: A CD image format converter from .bin/.cue to .iso/.cdr/.wav
Summary (ru_RU.UTF-8): Преобразователь образов CD из формата .bin/.cue в .iso/.cdr/.wav
License: GPL
Group: Archiving/Cd burning
Url: http://hes.iki.fi/bchunk/
Source: %name-%version.tar.gz

%description
The bchunk package contains a UNIX/C rewrite of the BinChunker program.
BinChunker converts a CD image in a .bin/.cue format (sometimes .raw/.cue)
into a set of .iso and .cdr/.wav tracks.  The .bin/.cue format is used by some
non-UNIX CD-writing software, but is not supported on most other
CD-writing programs.

%description -l ru_RU.UTF-8
Пакет bchunk содержит UNIX версию программы BinChunker. BinChunker
преобразует образы компакт-дисков в формате .bin/.cue (иногда .raw/.cue)
в набор .iso и .cdr/.wav файлов-дорожек. Формат .bin/.cue используется
в нескольких программах записи компакт-дисков не для UNIX.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS"
%make_build

%install
%__mkdir_p $RPM_BUILD_ROOT%_bindir
%__mkdir_p $RPM_BUILD_ROOT%_man1dir
%__install -s -m 755 bchunk $RPM_BUILD_ROOT%_bindir
%__install -m 644 bchunk.1 $RPM_BUILD_ROOT%_man1dir

%files
%doc COPYING README bchunk-%version.lsm
%_bindir/bchunk
%_man1dir/bchunk*

%changelog
* Thu Oct 28 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.2.0-alt1
- 1.2.0 thx to Aleksandr Blokhin!

* Thu Aug 28 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.1.1-alt1
- ALTLinux build
