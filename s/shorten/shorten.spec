Name: shorten
Version: 3.6.1
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Low complexity and fast waveform coder
License: Distributable
Group: Sound

URL: http://www.etree.org/shnutils/shorten/
Source: %url/dist/src/shorten-%version.tar.gz

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
* Wed Aug 27 2008 Victor Forsyuk <force@altlinux.org> 3.6.1-alt1
- Initial build.
