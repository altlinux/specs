Name: pxz
Version: 4.999.9beta
Release: alt2

Summary: Parallel LZMA compressor using liblzma
License: GPLv2+
Group: Archiving/Compression
Url: http://jnovy.fedorapeople.org/pxz/
Packager: Michael Shigorin <mike@altlinux.org>
# git://github.com/jnovy/pxz.git
# git://git.altlinux.org/gears/p/pxz.git
Source: %url/%name-%version.tar

BuildRequires: liblzma-devel libgomp-devel

%description
Parallel XZ is a compression utility that takes advantage
of running XZ compression simultaneously on different parts
of an input file on multiple cores and processors.
This significantly reduces compression time.

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*

%changelog
* Thu Nov 18 2010 Dmitry V. Levin <ldv@altlinux.org> 4.999.9beta-alt2
- Rebuilt with liblzma.so.5.

* Fri Sep 24 2010 Michael Shigorin <mike@altlinux.org> 4.999.9beta-alt1
- built for ALT Linux (git commit a1688e0 dated 20100604)

