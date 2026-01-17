Name: shntool
Version: 3.0.10
Release: alt2

Summary: Multi-purpose WAVE data processing and reporting utility
License: GPLv2+
Group: Sound

URL: http://shnutils.freeshell.org/shntool/
Source: shntool-%version.tar
Patch0: shntool-3.0.10-debian-add-wave-format-extensible.patch
Patch1: shntool-3.0.10-upstream-fix-mmssff-non-cd.patch
Patch2: shntool-3.0.10-debian-fix-large-files.patch
Patch3: shntool-3.0.10-debian-fix-large-times.patch
Patch4: shntool-3.0.10-debian-join-allow-single-file.patch


Requires: bonk flac mac shorten sox ttaenc wavpack

# Automatically added by buildreq on Wed Sep 24 2008
BuildRequires: bonk flac mac shorten sox ttaenc wavpack

%description
shntool is a multi-purpose WAVE data processing and reporting utility. File
formats are abstracted from its core, so it can process any file that contains
WAVE data, compressed or not - provided there exists a format module to handle
that particular file type.

%prep
%setup
%autopatch -p1

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

pushd %buildroot%_man1dir
for i in `ls %buildroot%_bindir | grep -v shntool | sed -e 's|%buildroot%_bindir||'`; do
  echo '.so shntool.1' >$i.1
done
popd

%files
%_bindir/*
%_man1dir/*

%changelog
* Sat Jan 17 2026 Anton Farygin <rider@altlinux.org> 3.0.10-alt2
- applied fixes from Debian and upstream (closes: #56802):
  * support WAVE_FORMAT_EXTENSIBLE in WAV parser
  * fix integer overflows when processing large files and long durations
  * allow mm:ss:ff format for non-CD-quality audio (error -> warning)
  * allow single input file in join mode

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.0.10-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Jul 24 2009 Victor Forsyuk <force@altlinux.org> 3.0.10-alt1
- 3.0.10

* Wed Sep 24 2008 Victor Forsyuk <force@altlinux.org> 3.0.8-alt1
- 3.0.8
- Build with mac and shorten.

* Thu Mar 27 2008 Victor Forsyuk <force@altlinux.org> 3.0.7-alt1
- 3.0.7

* Thu Jul 26 2007 Victor Forsyuk <force@altlinux.org> 3.0.3-alt1
- 3.0.3
- Add Requires for flac and sox (shorten and other helpers not in repo yet).

* Wed May 26 2004 Alexey Morozov <morozov@altlinux.org> 2.0.3-alt1
- Initial build for ALT Linux
- A patch to correctly handle [some of] extended CUEs when performing split
- Added links to shortcut shntool commands
