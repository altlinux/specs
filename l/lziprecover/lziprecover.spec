Name: lziprecover
Version: 1.15
Release: alt1

Summary: LZMA compressed file recovery
License: GPL v3+
Group: Archiving/Compression

Url: http://savannah.nongnu.org/projects/lzip/
Source: http://download.savannah.gnu.org/releases/lzip/%name-%version.tar.gz
Source100: lziprecover.watch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Sep 20 2009
BuildRequires: gcc-c++

%description
Lzip is a lossless file compressor based on the LZMA
(Lempel-Ziv-Markov chain-Algorithm) algorithm designed by Igor Pavlov.

This package contains the recovery utility for LZMA archives.

%prep
%setup

%build
%configure
make all info

%install
%makeinstall_std install-man

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/%name
%_man1dir/%name.1*
%_infodir/%name.info*

%changelog
* Sun Oct 13 2013 Michael Shigorin <mike@altlinux.org> 1.15-alt1
- new version (watch file uupdate)

* Thu Feb 28 2013 Michael Shigorin <mike@altlinux.org> 1.14-alt1
- new version (watch file uupdate)

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 1.13-alt2
- added watch file

* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 1.13-alt1
- 1.13
