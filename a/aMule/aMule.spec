%define		_name	amule
%define		_rc	rc8
Name:		aMule
Version:	2.3.1
Release:	alt1.1

Summary:	aMule - eMule client.
License:	GPL
Group: 		Networking/File transfer

Url:		http://www.amule.org
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source:		%name-%version.tar.bz2

Conflicts:	xmule

Patch2:		%name-2.0.0%_rc-alt-up-down-ratio.patch

# Automatically added by buildreq on Mon Jun 16 2008
BuildRequires: flex gcc-c++ imake libcryptopp-devel libpng-devel libreadline-devel libwxGTK2.9-devel xorg-cf-files
BuildRequires: libupnp-devel

#BuildRequires: rpm-build-compat >= 0.95

%description
The "all-platform eMule", it is a eMule-like client for ed2k network, 
supporting Linux, *BSD platforms, Solaris, *MacOSX and *Win32 (*soon). 
It was forked from xMule project back in September 2003 (not related 
to it anymore, except little bits of old code), to drive it to a brand 
new direction and quality. Uses wxWidgets (formerly known as wxWindows) 
for multiplatform support.

%prep
%setup -q -n %name-%version
%__subst "s,aMuleConv(wxT(\"iso8859-1\")),aMuleConv(wxLocale::GetSystemEncodingName())," src/utils/aLinkCreator/src/alcc.h
%__subst "s,aMuleConv(wxT(\"iso8859-1\")),aMuleConv(wxLocale::GetSystemEncodingName())," src/utils/aLinkCreator/src/ed2khash.cpp
%__subst "s,#include <wx/strconv\.h>,#include <wx/strconv\.h>\n#include <wx/intl\.h>," src/utils/aLinkCreator/src/alcc.h
%__subst "s,#include <wx/strconv\.h>,#include <wx/strconv\.h>\n#include <wx/intl\.h>," src/utils/aLinkCreator/src/ed2khash.cpp
#patch2 -p1


%build
%configure 	--enable-amulecmd \
		--enable-amulecmdgui \
		--enable-optimize \
		--disable-gsocket \
		--enable-alcc \
		--enable-alc \
		--enable-amule-daemon \
		--enable-webserver \
		--enable-webservergui \
		--enable-amule-gui \
		--disable-debug \
		--with-wx-config=%_bindir/wx-config
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang --with-man %_name


%files -f %_name.lang
%doc %_defaultdocdir/amule/*
%_bindir/*
#%_menudir/*
%_datadir/applications/*
%_datadir/pixmaps/*
%_datadir/man/*/man1/*
%dir %_datadir/%_name
%_datadir/%_name/*
%doc %_man1dir/*
%dir %_docdir/amule

%changelog
* Fri May 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1.1
- Rebuilt with new wxGTK 2.9

* Mon Nov 14 2011 Ilya Mashkin <oddity@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Sun Dec 27 2009 Ilya Mashkin <oddity@altlinux.ru> 2.2.6-alt3
- build with libupnp (Closes: #22038)

* Mon Dec 14 2009 Ilya Mashkin <oddity@altlinux.ru> 2.2.6-alt2
- rebuild with new libcryptopp

* Sat Sep 19 2009 Ilya Mashkin <oddity@altlinux.ru> 2.2.6-alt1
- 2.2.6

* Wed Aug 26 2009 Ilya Mashkin <oddity@altlinux.ru> 2.2.5-alt1.1
- Rebuild with new wxGTK

* Tue May 26 2009 Ilya Mashkin <oddity@altlinux.ru> 2.2.5-alt0.M41.1
- Build for ALT Linux 4.1

* Sun May 24 2009 Ilya Mashkin <oddity@altlinux.ru> 2.2.5-alt0.M50.1
- Build for ALT Linux 5.0

* Mon May 18 2009 Ilya Mashkin <oddity@altlinux.ru> 2.2.5-alt1
- 2.2.5 
- fixed CVE-2009-1440 (Closes: #19829)

* Sat May 02 2009 Ilya Mashkin <oddity@altlinux.ru> 2.2.4-alt1
- 2.2.4
- remove unneeded macros

* Mon Jun 16 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Wed Aug 01 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.1.3-alt2
-  #11851 fix. 10x to php-coder@.

* Tue Jul 31 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.1.3-alt1
- 2.1.3. wxGTK2u 2.6.x build. 

* Thu Aug 31 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.1.2-alt1.1
-  rebuild with wxGTK 2.7.0 testing.

* Mon May 29 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.1.2-alt1
-  2.1.2.

* Tue Jan 31 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.1.0-alt1
-  2.1.0
-  old-style menu file removed.

* Tue Aug 02 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.3-alt1
-  2.0.3.

* Wed Jun 08 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.2-alt1.1
-  small fix for #7027.

* Mon Jun 06 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.2-alt1
-  2.0.2.
-  amuled, amuleweb added (rquested by Ivan Adzhubey).
-  %name remote gui added.

* Fri May 20 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.1-alt1.1
-  build with wxGTK2u 2.6.

* Wed May 18 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.1-alt1
-  2.0.1.

* Wed May 04 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0-alt3
-  2.0.0 release.

* Mon Apr 18 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0-alt2.rc8
-  build with wxGTK 2.5.5.

* Fri Apr 01 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0-alt1.3.rc8
-  up/down ratio values changed.

* Thu Feb 03 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0-alt1.1.rc8
- new buildrequires.

* Wed Feb 02 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0-alt1.rc8
-  rc8.

* Wed Nov 10 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0-alt0.2.rc7
-  invalid build requires fixed.

* Wed Nov 10 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0-alt0.1.rc7
-  rc7.

* Thu Sep 23 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0rc5-alt6.1
-  cvs.

* Tue Sep 21 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0rc5-alt6
-  new cvs snapshot.
-  rebuild with new wxGTK2.

* Thu Sep 16 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0rc5-alt5
-  full timer bugfix.
-  cvs version.

* Tue Sep 14 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0rc5-alt4
-  partial timer bugfix. timer now works correctly. no segfault on first start/exit.

* Mon Sep 13 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0rc5-alt3
-  fixed timer bug (segfault on first start).
-  changed server.met uri.

* Thu Sep 09 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0rc5-alt2
-  rebuild with new wxWidgets pgAdmin snapshot.

* Wed Aug 11 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 2.0.0rc5-alt1
-  initial build.
