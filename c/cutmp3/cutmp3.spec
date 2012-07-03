# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: cutmp3
Version: 2.0.2
Release: alt1

Summary: small console editor mp3 files without quality loss
License: GPLv2
Group: Sound
Url: http://www.puchalla-online.de/cutmp3.html
Packager: Slava Semushin <php-coder@altlinux.ru>

Source: http://www.puchalla-online.de/%name-%version.tar.bz2

Requires: mpg123

# Automatically added by buildreq on Tue Apr 27 2004
BuildRequires: libncurses-devel libreadline-devel

%description
This is a small program to edit mp3 files without quality loss.
Playback is realized via mpg123. You can mark beginning and end of a
segment with 'a' and 'b' and save the segment with 's'.

%prep
%setup

%build
export CFLAGS="%optflags"
%make_build

%install
install -pD -m 755 %name %buildroot%_bindir/%name
install -pD -m 644 %name.1 %buildroot%_man1dir/%name.1

%files
%doc BUGS README* Changelog TODO USAGE
%_bindir/%name
%_man1dir/%name.1.*

%changelog
* Wed Aug 11 2010 Slava Semushin <php-coder@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Tue Jul 14 2009 Slava Semushin <php-coder@altlinux.ru> 2.0.1-alt1
- 2.0.1
  + Fixed insecure temporary files creation (Closes: #20768)

* Sat Jul 04 2009 Slava Semushin <php-coder@altlinux.ru> 2.0-alt1
- 2.0

* Mon Mar 09 2009 Slava Semushin <php-coder@altlinux.ru> 1.9.4-alt1
- 1.9.4
- More proper License tag

* Sun Nov 04 2007 Slava Semushin <php-coder@altlinux.ru> 1.9.2-alt1
- 1.9.2
- New maintainer
- Package manual page
- Use flags from %%optflags during build
- Added mpg123 to Requires
- Spec cleanup:
  + Added full url to Source tag
  + Corrected %%description
  + s/%%setup -q/%%setup/
  + s/%%make/%%make_build/
- Enable _unpackaged_files_terminate_build


* Mon Feb 20 2006 Andrey Semenov <mitrofan@altlinux.ru> 1.8.6-alt1
- 1.8.6

* Mon Feb 13 2006 Andrey Semenov <mitrofan@altlinux.ru> 1.8.5-alt1
- 1.8.5

* Mon Nov 28 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.8.4-alt1
- new version

* Mon May 16 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.8.3-alt1
- 1.8.3

* Tue May 03 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Tue Nov 09 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Thu Oct 07 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.8-alt1
- 1.8

* Tue Oct 05 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.7.0-alt1
- new version

* Tue Aug 03 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.6.4-alt1
- new version
- file info also shows ID3 tag
- ID3 V1 tag is being imported

* Wed Jul 21 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.6.3-alt1
- 'i' shows file info
- fixed a time bug in exact mode
- 'o' overwrites existing file the next time

* Mon Jul 12 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.6.2-alt1
- new version

* Sun Jul 4 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.6.1-alt1
- fixed a small bug in silence seeking
- speeded up silence seeking

* Tue Jun 15 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.6-alt1
- fixed time counting in exact mode
- fixed time display in exact mode
- more output for -F switch
- verbose writing of configuration file

* Wed Jun 9 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.5.1-alt1
- fixed some small bugs in timetable cutting

* Tue Jun 8 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.5-alt1
- added switch to only print sampling frequency and total number of frames
- added switch to write to an exactly specified filename
- fixed a bug which caused a crash
- several translations were added

* Tue Apr 27 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.4-alt1
- 1.4
- added function to search for beginning of next silence
- silence seeking stops when silence is already much longer than wanted
- noninteractive cutting now supports higher time resolution
- added support for output to other soundcard

* Tue Feb 10 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.3-alt1
- 1.3
- when saving with (already included) tag, filename is $artist - $title.mp3
- fixed a bug in tag seeking
- fixed a bug which made it impossible to write many files
- code cleanups

* Thu Feb 5 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.2-alt1
- 1.2
- improved stability of silence seeking a lot
- some other small changes

* Mon Nov 24 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.1.1-alt1
- fixed another bug in silence seeking

* Sat Nov 12 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.1-alt1
- 1.1
- introduced a quiet mode, toggable with '#'
- introduced an exact mode, useful for VBR files!
- cutmp3 does not wait anymore until playback has finished

* Sun Nov 2 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.0-alt1
- 1.0
- bugs fixed

* Mon Oct 27 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.9.6-alt1
- 0.9.6
- fixed some nasty bugs in silence seeking, still not perfect however
- improved ID3 tag searching
- small changes in the UI

* Wed Sep 24 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Tue Sep 23 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Wed May 07 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.7-alt1
- First version of RPM package.

