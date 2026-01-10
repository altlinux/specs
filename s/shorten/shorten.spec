Name: shorten
Version: 3.6.1
Release: alt2

Summary: Low complexity and fast waveform coder
License: Distributable
Group: Sound

URL: http://shnutils.freeshell.org/shorten/
Source: shorten-%version.tar.gz

%description
shorten is a low complexity and fast waveform coder (i.e. audio compressor),
originally written by Tony Robinson at SoftSound. It can operate in both lossy
and lossless modes.

%prep
%setup

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*

%changelog
* Sat Jan 10 2026 Anton Farygin <rider@altlinux.org> 3.6.1-alt2
- fixed FTBFS: added missing includes for POSIX compatibility

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.6.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Aug 27 2008 Victor Forsyuk <force@altlinux.org> 3.6.1-alt1
- Initial build.
