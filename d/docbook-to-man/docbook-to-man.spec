Name: docbook-to-man
Version: 2.0.0
Release: alt1

Summary: Converter from DocBook SGML into roff man macros
License: MIT
Group: File tools

Url: http://www.oasis-open.org/docbook/tools/dtm/
# original: http://www.oasis-open.org/docbook/tools/dtm/%{name}.tar.gz
# we use ANS version, available in Debian
Source: http://ftp.debian.org/debian/pool/main/d/docbook-to-man/%{name}_%{version}.orig.tar.gz
Patch0: %name-debian.patch
Patch1: %name-opt.patch
Patch2: %name-addpath.patch
Patch3: %name-catalog.patch

%description
docbook-to-man is a batch converter that transforms UNIX-style
manpages from the DocBook SGML format into nroff/troff man macros.

This is not the original version by Fred Dalrymple, but one with the
modifications by David Bolen with Debian changes.

%prep
%setup -n %{name}-%{version}.orig
%patch0 -p1
%__patch -p1 -s < debian/patches/01-conglomeration.dpatch
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%make_build

%install
install -d %buildroot%_bindir %buildroot/usr/share/sgml
%make_install ROOT=%buildroot/usr install

%files
%_bindir/*
%_datadir/sgml/transpec

%changelog
* Fri Feb 08 2008 Victor Forsyuk <force@altlinux.org> 2.0.0-alt1
- Initial build.
