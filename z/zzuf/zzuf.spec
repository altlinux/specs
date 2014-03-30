Name: zzuf
Version: 0.13
Release: alt1
Summary: Transparent application input fuzzer
License: DWTFYWTPL
Group: Toys
URL: http://sam.zoy.org/zzuf

Packager: Ilya Mashkin <oddity@altlinux.ru>
Source: %name-%version.tar.gz

%description
zzuf is a transparent application input fuzzer. It works by intercepting
file operations and changing random bits in the program's input. zzuf's
behaviour is deterministic, making it easy to reproduce bugs.

%prep
%setup

%build
%configure \
	--disable-static \
	--enable-shared

%make_build

%install

%make_install DESTDIR="%buildroot" install

find %buildroot -type f -name "*.la" -delete

%files
%doc README AUTHORS COPYING TODO NEWS
%_bindir/*
%_libdir/%name
%_man1dir/*
%_man3dir/*

%changelog
* Sun Mar 30 2014 Ilya Mashkin <oddity@altlinux.ru> 0.13-alt1
- 0.13

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.12-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.12-alt1
- 0.12 release.

* Tue Nov 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.10-alt1
- 0.10 release.

* Wed Aug 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.9-alt1
- 0.9 release.

* Sat Mar 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.1-alt1
- 0.8.1 release.

* Fri Feb 23 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.7-alt1
- Initial build for Sisyphus.

