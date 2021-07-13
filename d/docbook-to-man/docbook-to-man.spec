Name: docbook-to-man
Version: 2.0.0
Release: alt1.qa2

Summary: Converter from DocBook SGML into roff man macros
License: MIT
Group: File tools

Url: http://www.oasis-open.org/docbook/tools/dtm/
# original: http://www.oasis-open.org/docbook/tools/dtm/%{name}.tar.gz
# we use ANS version, available in Debian
Source: http://ftp.debian.org/debian/pool/main/d/docbook-to-man/%{name}_%{version}.orig.tar.gz
Patch2: %name-addpath.patch
Patch3: %name-catalog.patch
Patch11: 0001-conglomeration.patch
Patch12: 0002-arg-req-space.patch
Patch13: 0003-userinput-font.patch
Patch14: 0004-instant-man.patch
Patch15: 0005-makefile.patch
Patch16: 0006-format-security.patch
Patch17: 0007-remove-timestamp.patch
Patch18: 0008-better-checking-of-return-value-of-Split-function.patch
Patch19: 0009-remove-sp-dependency.patch
Patch20: 0010-Prevent-undefined-behaviour-in-memcpy-parameter-over.patch
Patch21: 0011-Correct-spelling-mistakes-in-binary.patch
Patch22: 0012-Ensure-build-failures-in-subdirectories-cause-entire.patch

%description
docbook-to-man is a batch converter that transforms UNIX-style
manpages from the DocBook SGML format into nroff/troff man macros.

This is not the original version by Fred Dalrymple, but one with the
modifications by David Bolen with Debian changes.

%prep
%setup -n %{name}-%{version}.orig
%patch11 -p1
%patch2 -p1
%patch3 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1

%build
%make_build CFLAGS="-Wall -fcommon"

%install
install -d %buildroot%_bindir %buildroot/usr/share/sgml
%make_install ROOT=%buildroot/usr install

%files
%_bindir/*
%_datadir/sgml/transpec

%changelog
* Tue Jul 13 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1.qa2
- FTBFS: apply all latest patches from Debian (ALT #40418).

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Feb 08 2008 Victor Forsyuk <force@altlinux.org> 2.0.0-alt1
- Initial build.
