Name: pngbook
Version: 1.0
Release: alt1

Summary: PNG: The Definitive Guide
License: FDL
Group: Books/Computer books
Url: http://www.libpng.org/pub/png/pngbook.html
BuildArch: noarch

BuildPreReq: unzip

Source0: http://prdownloads.sourceforge.net/png-mng/pngbook-20030726-html.zip
Source1: gregbook.tar.bz2
Patch: gregbook-alt-makefile.patch

%description
PNG, the Portable Network Graphics image format, is one little piece of
the puzzle.  In PNG: The Definitive Guide, author attempts to make PNG a
little less puzzling by explaining the motivations behind PNG's creation,
the ways in which it can be used, and the tools that can manipulate it.
The intended audience is anyone who deals with PNG images, whether as
an artist, a programmer, or a surfer on the World Wide Web.

%prep
%setup -q -c -a1
%patch

%files
%doc --no-dereference *

%changelog
* Thu Nov 04 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt1
- Initial revision.
