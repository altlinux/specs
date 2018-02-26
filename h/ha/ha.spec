Name: ha
Version: 0.999
Release: alt2
Summary: HA archiver
Summary (ru_RU.UTF-8): Архиватор HA
License: GPL
Group: Archiving/Compression
Url: ftp://sunsite.unc.edu/pub/Linux/utils/compress/ha0999p-linux.tar.gz
Source: ha0999p-linux.tar

%description
This is the "HA" archiver, an arithmetic/Markov coder which typically
compresses better than any other archiver, but is somewhat slow.

%description -l ru_RU.UTF-8
Архиватор "HA" обычно достигает лучшего результата чем любой другой 
архиватор благодаря использованию арифметического кодирования Маркова, 
но скорость его работы оставляет желать лучшего.

%prep
%setup -q -n ha0999p-linux

%build
rm -f makefile machine.h
mv grr/Makefile Makefile
mv grr/machine.h machine.h
make ha CFLAGS="$RPM_OPT_FLAGS -D_UNIX"

%install
install -p -m755 -D %name $RPM_BUILD_ROOT%_bindir/%name
install -p -m644 -D %name.1 $RPM_BUILD_ROOT%_man1dir/%name.1

%files
%_bindir/*
%_man1dir/*
%doc *.txt

%changelog
* Fri Sep 10 2010 Anton Farygin <rider@altlinux.ru> 0.999-alt2
- added man page from Debian
- removed binary file from source tarball

* Mon Oct 14 2002 Vyacheslav Dikonov <slava@altlinux.ru> 0.999-alt1
- ALT Linux build.

