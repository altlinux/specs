Name: p7zip
Version: 9.20.1
Release: alt1

Summary: 7zip unofficial port - a file-archiver with highest compression ratio
License: Freely distributable
Group: Archiving/Compression

Url: http://p7zip.sourceforge.net/
Source: http://downloads.sourceforge.net/p7zip/p7zip_%{version}_src_all.tar.bz2

# Automatically added by buildreq on Sat Oct 08 2011
# optimized out: libstdc++-devel
BuildRequires: gcc-c++

%description
p7zip is a port of 7-Zip for Unix. 7-Zip is a file archiver
with a very high compression ratio.

%package standalone
Summary: Standalone p7zip executable without plugins
Group: Archiving/Compression
License: LGPLv2.1+
Requires: p7zip

%description standalone
p7zip is a port of 7-Zip for Unix. 7-Zip is a file archiver
with a very high compression ratio.

This package contains standalone version of p7zip.
It handles less archive formats than plugin capable version.

%prep
%setup -n p7zip_%version

%build
# Make p7zip looks for plugins in fixed directory. Upstream behavior was to
# look in current directory by default (when environment variable P7ZIP_HOME_DIR
# is not set)
find . -name '*.cpp' -exec \
subst 's@getenv("P7ZIP_HOME_DIR")@"%_libdir/p7zip/"@g' {} \;

# NB: 'all' is not default target in this makefile
%make_build OPTFLAGS="%optflags" all2

# NB: Someday I probably should build and package 7zG (7z GUI), but for now
# this GUI is far from useful.

%install
./install.sh %_bindir %_libdir/p7zip %_mandir %_docdir/%name-%version %buildroot
# Install script put shell wrappers in /usr/bin/ instead of executables.
# We don't want this, see comments to inline patch above to get idea of our way.
mv -f %buildroot%_libdir/p7zip/{7z,7za} %buildroot%_bindir/

# fixed in 9.20.1
#cp -a bin/Codecs %buildroot%_libdir/p7zip/

%files
%doc README ChangeLog DOCS
%_bindir/7z
%dir %_libdir/p7zip
%_libdir/p7zip/*.so
%_libdir/p7zip/*.sfx
%_libdir/p7zip/Codecs
%_man1dir/7z.*
%exclude %_man1dir/7zr.*

%files standalone
%_bindir/7za
%_man1dir/7za.*

%changelog
* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 9.20.1-alt1
- 9.20.1
- minor spec cleanup

* Mon Mar 14 2011 Victor Forsiuk <force@altlinux.org> 9.20-alt1
- 9.20

* Thu Jun 17 2010 Victor Forsiuk <force@altlinux.org> 9.13-alt1
- 9.13

* Mon Jul 06 2009 Victor Forsyuk <force@altlinux.org> 9.04-alt1
- 9.04

* Sun Feb 15 2009 Victor Forsyuk <force@altlinux.org> 4.65-alt1
- 4.65

* Mon Jun 09 2008 Victor Forsyuk <force@altlinux.org> 4.58-alt1
- 4.58

* Mon Dec 17 2007 Victor Forsyuk <force@altlinux.org> 4.57-alt1
- 4.57

* Mon Sep 17 2007 Victor Forsyuk <force@altlinux.org> 4.55-alt1
- 4.55
- Patch to make p7zip always look in specified directory for plugins
  (codecs and sfx stubs).
- Apply %%optflags.
- Build with SFX archives support.
- Build "7z with plugins" as main package instead of 7za. Package 7za
  as p7zip-standalone.

* Thu May 24 2007 Victor Forsyuk <force@altlinux.org> 4.45-alt1
- 4.45

* Tue Sep 26 2006 Andrey Semenov <mitrofan@altlinux.ru> 4.43-alt1
- 4.43

* Tue May 30 2006 Andrey Semenov <mitrofan@altlinux.ru> 4.42-alt1
- 4.42

* Wed Apr 19 2006 Andrey Semenov <mitrofan@altlinux.ru> 4.39-alt1
- 4.39

* Sat Feb 11 2006 Andrey Semenov <mitrofan@altlinux.ru> 4.33-alt1
- 4.33

* Mon Nov 28 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.30-alt1
- new version

* Wed Oct 12 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.29-alt1
- 4.29

* Sat Sep 24 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.27-alt1
- 4.27

* Thu Sep 15 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.20-alt2
- add man pages

* Mon Jun 06 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.20-alt1
- release version

* Fri May 13 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.18-alt1
- 4.18

* Fri Apr 08 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.16-alt1
- 4.16

* Wed Feb 02 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.14.01-alt1
- 4.14.01

* Sun Jan 23 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.14-alt1
- 4.14

* Tue Dec 21 2004 Andrey Semenov <mitrofan@altlinux.ru> 4.13-alt1
- 4.13

* Sun Nov 21 2004 Andrey Semenov <mitrofan@altlinux.ru> 4.12-alt1
- 4.12

* Mon Oct 25 2004 Andrey Semenov <mitrofan@altlinux.ru> 4.10-alt1
- new version

* Sat Aug 21 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.91-alt1
- new version
- add support for FreeBSD 5.2.1
- add support of filesystem that support case sensitive filenames

* Wed Jul 21 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.90-alt1
- First version of RPM package
