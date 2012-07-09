#set_verify_elf_method relaxed

%define firefox_cid                    \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%define firefox_version                13.0.1
%define firefox_prefix                 %_libdir/firefox
%define firefox_datadir                %_datadir/firefox
%define firefox_arch_extensionsdir     %firefox_prefix/extensions
%define firefox_noarch_extensionsdir   %firefox_datadir/extensions

Summary:              The Mozilla Firefox project is a redesign of Mozilla's browser
Summary(ru_RU.UTF-8): Интернет-браузер Mozilla Firefox

Name:           firefox
Version:        13.0.1
Release:        alt1
License:        MPL/GPL/LGPL
Group:          Networking/WWW
URL:            http://www.mozilla.org/projects/firefox/

Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	firefox-source.tar
Source1:	rpm-build.tar
Source2:	searchplugins.tar
Source4:	firefox-mozconfig
Source6:	firefox.desktop
Source7:	firefox.c
Source8:	firefox-prefs.js

Patch6:		firefox3-alt-disable-werror.patch
Patch14:	firefox-fix-install.patch
Patch16:	firefox-cross-desktop.patch
#Patch17:	mozilla-703633.patch

BuildRequires(pre): mozilla-common-devel
BuildRequires(pre): rpm-build-mozilla.org
BuildRequires(pre): browser-plugins-npapi-devel

BuildRequires: doxygen gcc-c++ imake libIDL-devel makedepend
BuildRequires: libXt-devel libX11-devel libXext-devel libXft-devel libXScrnSaver-devel
BuildRequires: libcurl-devel libgtk+2-devel libhunspell-devel libjpeg-devel
BuildRequires: xorg-cf-files chrpath alternatives yasm
BuildRequires: python-modules-compiler python-modules-logging
BuildRequires: bzlib-devel zlib-devel
BuildRequires: libcairo-devel libpixman-devel
BuildRequires: libGL-devel
BuildRequires: libwireless-devel
BuildRequires: libalsa-devel
BuildRequires: libnotify-devel
BuildRequires: libevent-devel
BuildRequires: zip unzip
BuildRequires: libshell
BuildRequires: libvpx-devel
BuildRequires: libgio-devel
BuildRequires: libfreetype-devel fontconfig-devel
BuildRequires: libstartup-notification-devel
BuildRequires: rpm-macros-alternatives

BuildRequires: xulrunner-devel     >= 11.0
BuildRequires: libnspr-devel       >= 4.9.0-alt1
BuildRequires: libnss-devel        >= 3.13.4-alt1
BuildRequires: libnss-devel-static >= 3.13.4-alt1

BuildRequires: autoconf_2.13
%set_autoconf_version 2.13

Obsoletes:	firefox-3.6 firefox-4.0 firefox-5.0
Conflicts:	firefox-settings-desktop

Provides:	webclient
Requires:	mozilla-common

# Protection against fraudulent DigiNotar certificates
Requires: libnss >= 3.12.11-alt3

%description
The Mozilla Firefox project is a redesign of Mozilla's browser component,
written using the XUL user interface language and designed to be
cross-platform.

%description -l ru_RU.UTF8
Интернет-браузер Mozilla Firefox - кроссплатформенная модификация браузера Mozilla,
созданная с использованием языка XUL для описания интерфейса пользователя.

%package -n rpm-build-firefox
Summary:	RPM helper macros to rebuild firefox packages
Group:		Development/Other
BuildArch:	noarch

Requires:	mozilla-common-devel
Requires:	rpm-build-mozilla.org

%description -n rpm-build-firefox
These helper macros provide possibility to rebuild
firefox packages by some Alt Linux Team Policy compatible way.

%prep
%setup -q -n firefox-%version -c
cd mozilla

tar -xf %SOURCE1
tar -xf %SOURCE2

%patch6 -p1 -b .fix6
%patch14 -p1 -b .fix14
%patch16 -p1 -b .fix16
#patch17 -p1 -b .fix17

#echo %firefox_version > browser/config/version.txt

cp -f %SOURCE4 .mozconfig

%build
cd mozilla

%add_optflags %optflags_shared

export MOZ_BUILD_APP=browser

cat >> browser/confvars.sh <<EOF
MOZ_UPDATER=
MOZ_EXTENSIONS_DEFAULT=' gio'
MOZ_CHROME_FILE_FORMAT=jar
EOF

# Mozilla builds with -Wall with exception of a few warnings which show up
# everywhere in the code; so, don't override that.
#
# Disable C++ exceptions since Mozilla code is not exception-safe
#
MOZ_OPT_FLAGS=$(echo $RPM_OPT_FLAGS | \
                sed -e 's/-Wall//' -e 's/-fexceptions/-fno-exceptions/g')
export CFLAGS="$MOZ_OPT_FLAGS"
export CXXFLAGS="$MOZ_OPT_FLAGS"
export LDFLAGS='-Wl,-rpath-link,%xulr_develdir/lib'

export PREFIX="%_prefix"
export LIBDIR="%_libdir"
export XULSDK="%xulr_develdir"
export LIBIDL_CONFIG=/usr/bin/libIDL-config-2
export srcdir="$PWD"

%__autoconf

# On x86 architectures, Mozilla can build up to 4 jobs at once in parallel,
# however builds tend to fail on other arches when building in parallel.
MOZ_SMP_FLAGS=-j1
%ifarch %{ix86} x86_64
[ "${NPROCS:+0}" -ge 2 ] && MOZ_SMP_FLAGS=-j2
[ "${NPROCS:+0}" -ge 4 ] && MOZ_SMP_FLAGS=-j4
%endif

make -f client.mk \
	build STRIP="/bin/true" \
	MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS"

%__cc %optflags \
	-Wall -Wextra \
	-DMOZ_PLUGIN_PATH=\"%browser_plugins_path\" \
	-DXUL_APP_FILE=\"%firefox_prefix/application.ini\" \
	%SOURCE7 -o firefox


%install
cd mozilla

%__mkdir_p \
	%buildroot/%firefox_prefix/plugins \
	%buildroot/%firefox_arch_extensionsdir \
	%buildroot/%firefox_noarch_extensionsdir \
	%buildroot/%mozilla_arch_extdir/%firefox_cid \
	%buildroot/%mozilla_noarch_extdir/%firefox_cid \
	#

%makeinstall \
    mozappdir=%buildroot/%firefox_prefix \
    #

ln -sf -- $(relative "%firefox_noarch_extensionsdir" "%firefox_prefix/") \
        %buildroot/%firefox_prefix/extensions-noarch

# install altlinux-specific configuration
install -D -m 644 %SOURCE8 %buildroot/%firefox_prefix/defaults/preferences/all-altlinux.js

cat > %buildroot/%firefox_prefix/defaults/preferences/firefox-l10n.js <<EOF
pref("intl.locale.matchOS",		true);
pref("general.useragent.locale",	"chrome://global/locale/intl.properties");
EOF

# icons
for s in 16 22 24 32 48 256; do
	install -D -m 644 \
		browser/branding/official/default$s.png \
		%buildroot/%_iconsdir/hicolor/${s}x${s}/apps/firefox.png
done

# searchplugins
cp -a -- \
	searchplugins/* \
	%buildroot/%firefox_prefix/searchplugins/

# install rpm-build-firefox
mkdir -p -- \
	%buildroot/%_sysconfdir/rpm/macros.d

cp -a -- \
	rpm-build/rpm.macros.firefox.standalone \
	%buildroot/%_sysconfdir/rpm/macros.d/firefox

install -m755 firefox %buildroot/%_bindir/firefox

cd %buildroot

sed -i \
	-e 's,@firefox_version@,%version,' \
	-e 's,@firefox_release@,%release,' \
	./%_sysconfdir/rpm/macros.d/firefox

#sed -i \
#	-e 's,\(MinVersion\)=.*,\1=5.0.1,g' \
#	-e 's,\(MaxVersion\)=.*,\1=5.0.1,g' \
#	./%firefox_prefix/application.ini

# install menu file
%__install -D -m 644 %SOURCE6 ./%_datadir/applications/firefox.desktop

# Add alternatives
mkdir -p ./%_altdir
printf '%_bindir/xbrowser\t%_bindir/firefox\t100\n' >./%_altdir/firefox

rm -f -- \
	./%firefox_prefix/firefox \
	./%firefox_prefix/removed-files

%pre
for n in defaults browserconfig.properties; do
	[ ! -L "%firefox_prefix/$n" ] || rm -f "%firefox_prefix/$n"
done

%files
%_altdir/firefox
%_bindir/firefox
%firefox_prefix
%firefox_arch_extensionsdir
%firefox_noarch_extensionsdir
%mozilla_arch_extdir/%firefox_cid
%mozilla_noarch_extdir/%firefox_cid
%_datadir/applications/firefox.desktop
%_iconsdir/hicolor/16x16/apps/firefox.png
%_iconsdir/hicolor/22x22/apps/firefox.png
%_iconsdir/hicolor/24x24/apps/firefox.png
%_iconsdir/hicolor/32x32/apps/firefox.png
%_iconsdir/hicolor/48x48/apps/firefox.png
%_iconsdir/hicolor/256x256/apps/firefox.png

%files -n rpm-build-firefox
%_sysconfdir/rpm/macros.d/firefox

%changelog
* Sun Jul 01 2012 Alexey Gladkov <legion@altlinux.ru> 13.0.1-alt1
- New release (13.0.1).
- Fixed:
  + MFSA 2012-40 Buffer overflow and use-after-free issues found using Address Sanitizer
  + MFSA 2012-39 NSS parsing errors with zero length items
  + MFSA 2012-38 Use-after-free while replacing/inserting a node in a document
  + MFSA 2012-37 Information disclosure though Windows file shares and shortcut files
  + MFSA 2012-36 Content Security Policy inline-script bypass
  + MFSA 2012-35 Privilege escalation through Mozilla Updater and Windows Updater Service
  + MFSA 2012-34 Miscellaneous memory safety hazards

* Tue May 08 2012 Alexey Gladkov <legion@altlinux.ru> 12.0-alt1
- New release (12.0).
- Fixed:
  + MFSA 2012-33 Potential site identity spoofing when loading RSS and Atom feeds
  + MFSA 2012-32 HTTP Redirections and remote content can be read by javascript errors
  + MFSA 2012-31 Off-by-one error in OpenType Sanitizer
  + MFSA 2012-30 Crash with WebGL content using textImage2D
  + MFSA 2012-29 Potential XSS through ISO-2022-KR/ISO-2022-CN decoding issues
  + MFSA 2012-28 Ambiguous IPv6 in Origin headers may bypass webserver access restrictions
  + MFSA 2012-27 Page load short-circuit can lead to XSS
  + MFSA 2012-26 WebGL.drawElements may read illegal video memory due to FindMaxUshortElement error
  + MFSA 2012-25 Potential memory corruption during font rendering using cairo-dwrite
  + MFSA 2012-24 Potential XSS via multibyte content processing errors
  + MFSA 2012-23 Invalid frees causes heap corruption in gfxImageSurface
  + MFSA 2012-22 use-after-free in IDBKeyRange
  + MFSA 2012-21 Multiple security flaws fixed in FreeType v2.4.9
  + MFSA 2012-20 Miscellaneous memory safety hazards (rv:12.0/ rv:10.0.4)

* Thu Apr 19 2012 Alexey Gladkov <legion@altlinux.ru> 11.0-alt1
- New release (11.0).
- Fixed:
  + MFSA 2012-19 Miscellaneous memory safety hazards (rv:11.0/ rv:10.0.3 / rv:1.9.2.28)
  + MFSA 2012-18 window.fullScreen writeable by untrusted content
  + MFSA 2012-17 Crash when accessing keyframe cssText after dynamic modification
  + MFSA 2012-16 Escalation of privilege with Javascript: URL as home page
  + MFSA 2012-15 XSS with multiple Content Security Policy headers
  + MFSA 2012-14 SVG issues found with Address Sanitizer
  + MFSA 2012-13 XSS with Drag and Drop and Javascript: URL
  + MFSA 2012-12 Use-after-free in shlwapi.dll

* Tue Feb 21 2012 Alexey Gladkov <legion@altlinux.ru> 10.0.2-alt1
- New release (10.0.2).
- Fixed:
  + MFSA 2012-11 libpng integer overflow
  + MFSA 2012-10 use after free in nsXBLDocumentInfo::ReadPrototypeBindings
  + MFSA 2012-09 Firefox Recovery Key.html is saved with unsafe permission
  + MFSA 2012-08 Crash with malformed embedded XSLT stylesheets
  + MFSA 2012-07 Potential Memory Corruption When Decoding Ogg Vorbis files
  + MFSA 2012-06 Uninitialized memory appended when encoding icon images may cause information disclosure
  + MFSA 2012-05 Frame scripts calling into untrusted objects bypass security checks
  + MFSA 2012-04 Child nodes from nsDOMAttribute still accessible after removal of nodes
  + MFSA 2012-03 <iframe> element exposed across domains via name attribute
  + MFSA 2012-01 Miscellaneous memory safety hazards (rv:10.0/ rv:1.9.2.26)

* Mon Jan 09 2012 Alexey Gladkov <legion@altlinux.ru> 9.0.1-alt1
- New release (9.0.1).
- Check default browser (ALT#26195).
- Change location for noarch extensions (ALT#26702).
- Add translation for summary and description (ALT#22789).
- Fixed:
  + MFSA 2011-58 Crash scaling <video> to extreme sizes
  + MFSA 2011-57 Crash when plugin removes itself on Mac OS X
  + MFSA 2011-56 Key detection without JavaScript via SVG animation
  + MFSA 2011-55 nsSVGValue out-of-bounds access
  + MFSA 2011-54 Potentially exploitable crash in the YARR regular expression library
  + MFSA 2011-53 Miscellaneous memory safety hazards (rv:9.0)

* Mon Nov 14 2011 Alexey Gladkov <legion@altlinux.ru> 8.0-alt1
- New release (8.0).
- Fixed:
  + MFSA 2011-52 Code execution via NoWaiverWrapper
  + MFSA 2011-51 Cross-origin image theft on Mac with integrated Intel GPU
  + MFSA 2011-50 Cross-origin data theft using canvas and Windows D2D
  + MFSA 2011-49 Memory corruption while profiling using Firebug
  + MFSA 2011-48 Miscellaneous memory safety hazards (rv:8.0)
  + MFSA 2011-47 Potential XSS against sites using Shift-JIS

* Wed Oct 19 2011 Alexey Gladkov <legion@altlinux.ru> 7.0.1-alt2
- Drop depends for extensions.

* Thu Oct 06 2011 Alexey Gladkov <legion@altlinux.ru> 7.0.1-alt1
- New release (7.0.1).
- Fixed:
  + MFSA 2011-45 Inferring Keystrokes from motion data
  + MFSA 2011-44 Use after free reading OGG headers
  + MFSA 2011-43 loadSubScript unwraps XPCNativeWrapper scope parameter
  + MFSA 2011-42 Potentially exploitable crash in the YARR regular expression library
  + MFSA 2011-41 Potentially exploitable WebGL crashes
  + MFSA 2011-40 Code installation through holding down Enter
  + MFSA 2011-39 Defense against multiple Location headers due to CRLF Injection
  + MFSA 2011-36 Miscellaneous memory safety hazards (rv:7.0 / rv:1.9.2.23)

* Tue Sep 06 2011 Alexey Gladkov <legion@altlinux.ru> 6.0.2-alt1
- New release (6.0.2).

* Tue Sep 06 2011 Alexey Gladkov <legion@altlinux.ru> 6.0.1-alt1
- New release (6.0.1).
- Fixed:
  + MFSA 2011-34 Protection against fraudulent DigiNotar certificates

* Mon Aug 22 2011 Alexey Gladkov <legion@altlinux.ru> 6.0-alt1
- New release (6.0).
- Add Conflict to firefox-settings-desktop (ALT#25473).
- Fixed:
  + MFSA 2011-29 Security issues addressed in Firefox6.

* Wed Jul 13 2011 Alexey Gladkov <legion@altlinux.ru> 5.0.1-alt1
- New release (5.0.1).
- Fixed:
  + MFSA 2011-28 Non-whitelisted site can trigger xpinstall
  + MFSA 2011-27 XSS encoding hazard with inline SVG
  + MFSA 2011-26 Multiple WebGL crashes
  + MFSA 2011-25 Stealing of cross-domain images using WebGL textures
  + MFSA 2011-22 Integer overflow and arbitrary code execution in Array.reduceRight()
  + MFSA 2011-21 Memory corruption due to multipart/x-mixed-replace images
  + MFSA 2011-20 Use-after-free vulnerability when viewing XUL document with script disabled
  + MFSA 2011-19 Miscellaneous memory safety hazards (rv:3.0/1.9.2.18)

* Mon May 02 2011 Alexey Gladkov <legion@altlinux.ru> 4.0.1-alt1
- New release (4.0.1).
- Update desktop file (ALT#25530).
- Fixed:
  + MFSA 2011-18 XSLT generate-id() function heap address leak
  + MFSA 2011-17 WebGLES vulnerabilities
  + MFSA 2011-12 Miscellaneous memory safety hazards (rv:2.0.1/ 1.9.2.17/ 1.9.1.19)

* Fri Apr 22 2011 Alexey Gladkov <legion@altlinux.ru> 4.0-alt3
- Set some settings in Firefox to default values (ALT#22148).

* Tue Apr 19 2011 Alexey Gladkov <legion@altlinux.ru> 4.0-alt2
- Fix plugins path.
- Fix alternatives for %_bindir/xbrowser.

* Fri Apr 01 2011 Alexey Gladkov <legion@altlinux.ru> 4.0-alt1
- New release (4.0).
- Remove alternatives for configuration.

* Tue Mar 08 2011 Alexey Gladkov <legion@altlinux.ru> 3.6.15-alt1.20110308
- New release (3.6.15).
- Fixed:
  + MFSA 2011-10 CSRF risk with plugins and 307 redirects
  + MFSA 2011-09 Crash caused by corrupted JPEG image
  + MFSA 2011-08 ParanoidFragmentSink allows javascript: URLs in chrome documents
  + MFSA 2011-07 Memory corruption during text run construction (Windows)
  + MFSA 2011-06 Use-after-free error using Web Workers
  + MFSA 2011-05 Buffer overflow in JavaScript atom map
  + MFSA 2011-04 Buffer overflow in JavaScript upvarMap
  + MFSA 2011-03 Use-after-free error in JSON.stringify
  + MFSA 2011-02 Recursive eval call causes confirm dialogs to evaluate to true
  + MFSA 2011-01 Miscellaneous memory safety hazards (rv:1.9.2.14/ 1.9.1.17)

* Wed Dec 22 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.13-alt1.20101222
- New release (3.6.13).
- Fixed:
  + MFSA 2010-84 XSS hazard in multiple character encodings
  + MFSA 2010-83 Location bar SSL spoofing using network error page
  + MFSA 2010-82 Incomplete fix for CVE-2010-0179
  + MFSA 2010-81 Integer overflow vulnerability in NewIdArray
  + MFSA 2010-80 Use-after-free error with nsDOMAttribute MutationObserver
  + MFSA 2010-79 Java security bypass from LiveConnect loaded via data: URL meta refresh
  + MFSA 2010-78 Add support for OTS font sanitizer
  + MFSA 2010-77 Crash and remote code execution using HTML tags inside a XUL tree
  + MFSA 2010-76 Chrome privilege escalation with window.open and <isindex> element
  + MFSA 2010-75 Buffer overflow while line breaking after document.write with long string
  + MFSA 2010-74 Miscellaneous memory safety hazards (rv:1.9.2.13/ 1.9.1.16)

* Sun Nov 14 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.13-alt1.20101110
- New release (3.6.12).
- Fixed:
  + MFSA 2010-73 Heap buffer overflow mixing document.write and DOM insertion

* Tue Oct 26 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.12-alt1.20101025
- New release (3.6.11).
- Fixed:
  + MFSA 2010-72 Insecure Diffie-Hellman key exchange
  + MFSA 2010-71 Unsafe library loading vulnerabilities
  + MFSA 2010-70 SSL wildcard certificate matching IP addresses
  + MFSA 2010-69 Cross-site information disclosure via modal calls
  + MFSA 2010-68 XSS in gopher parser when parsing hrefs
  + MFSA 2010-67 Dangling pointer vulnerability in LookupGetterOrSetter
  + MFSA 2010-66 Use-after-free error in nsBarProp
  + MFSA 2010-65 Buffer overflow and memory corruption using document.write
  + MFSA 2010-64 Miscellaneous memory safety hazards (rv:1.9.2.11/ 1.9.1.14)

* Tue Sep 21 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.11-alt1.20100920
- New release (3.6.10).

* Sun Sep 12 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.10-alt1.20100909
- New release (3.6.9).
- Fixed:
  + MFSA 2010-63 Information leak via XMLHttpRequest statusText
  + MFSA 2010-62 Copy-and-paste or drag-and-drop into designMode document allows XSS
  + MFSA 2010-61 UTF-7 XSS by overriding document charset using <object> type attribute
  + MFSA 2010-59 SJOW creates scope chains ending in outer object
  + MFSA 2010-58 Crash on Mac using fuzzed font in data: URL
  + MFSA 2010-57 Crash and remote code execution in normalizeDocument
  + MFSA 2010-56 Dangling pointer vulnerability in nsTreeContentView
  + MFSA 2010-55 XUL tree removal crash and remote code execution
  + MFSA 2010-54 Dangling pointer vulnerability in nsTreeSelection
  + MFSA 2010-53 Heap buffer overflow in nsTextFrameUtils::TransformText
  + MFSA 2010-52 Windows XP DLL loading vulnerability
  + MFSA 2010-51 Dangling pointer vulnerability using DOM plugin array
  + MFSA 2010-50 Frameset integer overflow vulnerability
  + MFSA 2010-49 Miscellaneous memory safety hazards (rv:1.9.2.9/ 1.9.1.12)

* Thu Jul 29 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.9-alt1.20100725
- New release (3.6.8).
- Fixed:
  + MFSA 2010-48 Dangling pointer crash regression from plugin parameter array fix
  + MFSA 2010-47 Cross-origin data leakage from script filename in error messages
  + MFSA 2010-46 Cross-domain data theft using CSS
  + MFSA 2010-45 Multiple location bar spoofing vulnerabilities
  + MFSA 2010-44 Characters mapped to U+FFFD in 8 bit encodings cause subsequent character to vanish
  + MFSA 2010-43 Same-origin bypass using canvas context
  + MFSA 2010-42 Cross-origin data disclosure via Web Workers and importScripts
  + MFSA 2010-41 Remote code execution using malformed PNG image
  + MFSA 2010-40 nsTreeSelection dangling pointer remote code execution vulnerability
  + MFSA 2010-39 nsCSSValue::Array index integer overflow
  + MFSA 2010-38 Arbitrary code execution using SJOW and fast native function
  + MFSA 2010-37 Plugin parameter EnsureCachedAttrParamArrays remote code execution vulnerability
  + MFSA 2010-36 Use-after-free error in NodeIterator
  + MFSA 2010-35 DOM attribute cloning remote code execution vulnerability
  + MFSA 2010-34 Miscellaneous memory safety hazards (rv:1.9.2.7/ 1.9.1.11)

* Sun Jun 27 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.6-alt1.20100626
- New release (3.6.6).
- Fixed:
  + MFSA 2010-33 User tracking across sites using Math.random()
  + MFSA 2010-32 Content-Disposition: attachment ignored if Content-Type: multipart also present
  + MFSA 2010-31 focus() behavior can be used to inject or steal keystrokes
  + MFSA 2010-30 Integer Overflow in XSLT Node Sorting
  + MFSA 2010-29 Heap buffer overflow in nsGenericDOMDataNode::SetTextInternal
  + MFSA 2010-28 Freed object reuse across plugin instances
  + MFSA 2010-26 Crashes with evidence of memory corruption (rv:1.9.2.4/ 1.9.1.10)

* Mon Apr 05 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.3-alt1.20100404
- New release (3.6.3).
- Fixed:
  + MFSA 2009-25 Re-use of freed object due to scope confusion

* Mon Mar 29 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.2-alt1.20100328
- New release (3.6.2).
- Fix for Transport Layer Security (ALT#22994).
- Fix addons search (ALT#22878).
- Fix release notes (ALT#22883).
- Fixed:
  + MFSA 2010-15 Asynchronous Auth Prompt attaches to wrong window
  + MFSA 2010-14 Browser chrome defacement via cached XUL stylesheets
  + MFSA 2010-13 Content policy bypass with image preloading
  + MFSA 2010-12 XSS using addEventListener and setTimeout on a wrapped object
  + MFSA 2010-11 Crashes with evidence of memory corruption (rv:1.9.2.2/ 1.9.1.8/ 1.9.0.18)
  + MFSA 2010-10 XSS via plugins and unprotected Location object
  + MFSA 2010-09 Deleted frame reuse in multipart/x-mixed-replace image
  + MFSA 2010-08 WOFF heap corruption due to integer overflow

* Fri Jan 22 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.0-alt1
- New release (3.6.0).
- Fix process name (ALT#22731).

* Thu Jan 07 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.0-alt0.20100113
- New snapshot (3.6.0 20100113).

* Mon Nov 24 2009 Alexey Gladkov <legion@altlinux.ru> 3.6.0-alt0.20091124
- New major branch (3.6.0 b4pre).

* Sun Oct 11 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.3-alt0.20091010
- New snapshot (3.5.3 20091010).
- KDE: Update patches (ALT#21509).

* Mon Sep 28 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.3-alt0.20090918.1
- Rebuild with new browser-plugins-npapi.

* Sun Sep 20 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.3-alt0.20090918
- New snapshot (3.5.3 20090918).
- Set firefox as default KDE/KDE4 browser (ALT#21509).
- Update desktop file (ALT#21510).
- Update requires (ALT#21533).

* Tue Sep 01 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.3-alt0.20090831
- New snapshot (3.5.3 20090831).

* Fri Jul 17 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.1-alt1
- New release (3.5.1).

* Wed Jul 01 2009 Alexey Gladkov <legion@altlinux.ru> 3.5-alt2
- New release (3.5).

* Thu Jun 04 2009 Alexey Gladkov <legion@altlinux.ru> 3.5-alt1.20090601
- New snapshot (3.5 20090601).

* Wed Apr 24 2009 Alexey Gladkov <legion@altlinux.ru> 3.5-alt1.20090424
- New snapshot (3.5 20090424).

* Sun Jan 18 2009 Alexey Gladkov <legion@altlinux.ru> 3.1-alt1.20090312
- New snapshot (3.1 20090312).

* Tue Nov 18 2008 Alexey Gladkov <legion@altlinux.ru> 3.0.4-alt1
- New release (3.0.4).
- Fixed:
  + MFSA 2008-58 Parsing error in E4X default namespace
  + MFSA 2008-57 -moz-binding property bypasses security checks on codebase principals
  + MFSA 2008-56 nsXMLHttpRequest::NotifyEventListeners() same-origin violation
  + MFSA 2008-55 Crash and remote code execution in nsFrameManager
  + MFSA 2008-54 Buffer overflow in http-index-format parser
  + MFSA 2008-53 XSS and JavaScript privilege escalation via session restore
  + MFSA 2008-52 Crashes with evidence of memory corruption (rv:1.9.0.4/1.8.1.18)
  + MFSA 2008-51 file: URIs inherit chrome privileges when opened from chrome
  + MFSA 2008-47 Information stealing via local shortcut files

* Wed Oct 08 2008 Alexey Gladkov <legion@altlinux.ru> 3.0.3-alt1
- New release (3.0.3).
- Firefox set itself as default browser correctly (ALT#17384).
- Reload new plugins.
- Fixed:
  + MFSA 2008-44 resource: traversal vulnerabilities
  + MFSA 2008-43 BOM characters stripped from JavaScript before execution
  + MFSA 2008-42 Crashes with evidence of memory corruption (rv:1.9.0.2/1.8.1.17)
  + MFSA 2008-41 Privilege escalation via XPCnativeWrapper pollution
  + MFSA 2008-40 Forced mouse drag

* Tue Sep 09 2008 Alexey Gladkov <legion@altlinux.ru> 3.0.1-alt2
- New bugfix build.
- Update desktop file (ALT#10558).

* Fri Jul 18 2008 Alexey Gladkov <legion@altlinux.ru> 3.0.1-alt1
- New version (3.0.1).
- Fixed:
  + MFSA 2008-36 Crash with malformed GIF file on Mac OS X
  + MFSA 2008-35 Command-line URLs launch multiple tabs when Firefox not running
  + MFSA 2008-34 Remote code execution by overflowing CSS reference counter

* Sun Jul 13 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt2.20080704
- New bugfix build.
- Add searchplugins: bugzilla@altlinux, wikipedia-ru, yandex.
- Remove RPATH.

* Fri Jul 04 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20080704
- New cvs snapshot 3.0 (20080704).

* Sat May 31 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20080530
- New cvs snapshot 20080530.

* Tue May 20 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20080519
- New cvs snapshot (3.0 rc1).

* Sun Feb 03 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.b3pre
- New cvs snapshot.

* Thu Dec 20 2007 Alexey Gladkov <legion@altlinux.ru> 3.0.b2-alt1
- New major beta version 3.0.b2

* Wed Nov 28 2007 Alexey Gladkov <legion@altlinux.ru> 3.0.b1-alt1
- New major beta version 3.0.b1

* Sun Feb 25 2007 Alexey Gladkov <legion@altlinux.ru> 2.0.0.2-alt1
- New bugfix version 2.0.0.2
- Remove version from requires in *.pc.
- Fixed:
    + MFSA 2007-07  Embedded nulls in location.hostname confuse same-domain checks
    + MFSA 2007-06 Mozilla Network Security Services (NSS) SSLv2 buffer overflow
    + MFSA 2007-05 XSS and local file access by opening blocked popups
    + MFSA 2007-04 Spoofing using custom cursor and CSS3 hotspot
    + MFSA 2007-03 Information disclosure through cache collisions
    + MFSA 2007-02 Improvements to help protect against Cross-Site Scripting attacks
    + MFSA 2007-01 Crashes with evidence of memory corruption (rv:1.8.0.10/1.8.1.2)

* Sun Jan 28 2007 Alexey Gladkov <legion@altlinux.ru> 2.0.0.1-alt1
- New minor version 2.0.0.1
- Fixed:
    + MFSA 2006-76  XSS using outer window's Function object
    + MFSA 2006-75 RSS Feed-preview referrer leak
    + MFSA 2006-73 Mozilla SVG Processing Remote Code Execution
    + MFSA 2006-72 XSS by setting img.src to javascript: URI
    + MFSA 2006-71 LiveConnect crash finalizing JS objects
    + MFSA 2006-70 Privilege escalation using watch point
    + MFSA 2006-69 CSS cursor image buffer overflow (Windows only)
    + MFSA 2006-68 Crashes with evidence of memory corruption (rv:1.8.0.9/1.8.1.1)

* Thu Nov 23 2006 Alexey Gladkov <legion@altlinux.ru> 2.0-alt2
- Add %%pre script.
- Remove version specific paths.

* Sat Oct 28 2006 Alexey Gladkov <legion@altlinux.ru> 2.0-alt1
- New major version 2.0 .
- Don't build libxul.
- Add support for printing via Pango.
- Change printer paper size at A4.
- Check compatibility disabled.
- Patch disabling OS_TEST autoguessing for %%ix86 builds on x86_64 host.

* Fri Sep 15 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.7-alt1
- New version 1.5.0.7 .
- Fixed:
    + MFSA 2006-64  Crashes with evidence of memory corruption (rv:1.8.0.7)
    + MFSA 2006-62 Popup-blocker cross-site scripting (XSS)
    + MFSA 2006-61 Frame spoofing using document.open()
    + MFSA 2006-60 RSA Signature Forgery
    + MFSA 2006-59 Concurrency-related vulnerability
    + MFSA 2006-58 Auto-Update compromise through DNS and SSL spoofing
    + MFSA 2006-57 JavaScript Regular Expression Heap Corruption

* Wed Aug 30 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.6-alt4
- Add libgtkembedmoz.so, firefox-gtkembedmoz.pc .
- Update BuildRequires.

* Wed Aug 16 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.6-alt3
- bugfix build.
- Patch to enable intl.locale.matchOS was removed.
- Added default download directory.

* Wed Aug 09 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.6-alt2
- bugfix build.
- Added patch to handle #9863 (history #4352).

* Sat Aug 05 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.6-alt1
- New version 1.5.0.6 . 
- Fixed:
    + Fixed an issue with playing Windows Media content
    + MFSA 2006-56  chrome: scheme loading remote content
    + MFSA 2006-55 Crashes with evidence of memory corruption (rv:1.8.0.5)
    + MFSA 2006-54 XSS with XPCNativeWrapper(window).Function(...)
    + MFSA 2006-53 UniversalBrowserRead privilege escalation
    + MFSA 2006-52 PAC privilege escalation using Function.prototype.call
    + MFSA 2006-51 Privilege escalation using named-functions and redefined "new Object()"
    + MFSA 2006-50 JavaScript engine vulnerabilities
    + MFSA 2006-48 JavaScript new Function race condition
    + MFSA 2006-47 Native DOM methods can be hijacked across domains
    + MFSA 2006-46 Memory corruption with simultaneous events
    + MFSA 2006-45 Javascript navigator Object Vulnerability
    + MFSA 2006-44 Code execution through deleted frame reference

* Thu Jun 08 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.4-alt1
- New version.
- Fixed:
    + MFSA 2006-43 Privilege escalation using addSelectionListener
    + MFSA 2006-42 Web site XSS using BOM on UTF-8 pages
    + MFSA 2006-41 File stealing by changing input type (variant)
    + MFSA 2006-39 "View Image" local resource linking (Windows)
    + MFSA 2006-38 Buffer overflow in crypto.signText()
    + MFSA 2006-37 Remote compromise via content-defined setter on object prototypes
    + MFSA 2006-36 PLUGINSPAGE privileged JavaScript execution 2
    + MFSA 2006-35 Privilege escalation through XUL persist
    + MFSA 2006-34 XSS viewing javascript: frames or images from context menu
    + MFSA 2006-33 HTTP response smuggling
    + MFSA 2006-32 Fixes for crashes with potential memory corruption
    + MFSA 2006-31 EvalInSandbox escape (Proxy Autoconfig, Greasemonkey)

* Fri May 12 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.3-alt1
- New version.
- Build libxul library.
- Fixed:
    + MFSA 2006-30 Deleted object reference when designMode="on".

* Wed Mar 15 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.1-alt2
- bugfix build.
- include fix
- plugins directory fix;

* Mon Feb 13 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.1-alt1
- New version 1.5.0.1
- Buildrequires updated for xorg-7.0 
- run-firefox script bugfix:
  * usage update
  * plugins search path (x86_64)
  * unparseable commands handling
- bugfix: #7334, #7682, #8757, #8784, #9017

* Sun Dec 04 2005 Alexey Gladkov <legion@altlinux.ru> 1.5-alt1
- New version 1.5 .
- Spec cleanup.
- Build with external rpm-build-firefox .
- Build with system NSS and NSPR.
- Unused libraries removed.
- Rpm mascros bugfix.
  * fix for new rpm.
  * change extension installation sheme (again).
- Default preference tunning.
- Startup script rewritten. Now it is single script.
  * command line shortcut added: altfaq:NUM .
- SVG support enabled.
- directory /usr/share/firefox-@version@/extensions was added to extensions search path .
  * this location is controled by the option extensions.dir.extensions .
- Bug: #7682, #7801, #7856, #7949 fixed.

* Tue Aug 16 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt4
- major bugfix.
- build with official branding.
- x86_64 compatibility addon (patch20, patch21).

* Sun Aug 07 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt3
- release version.
- firsttime script added.
- SVG support disabled.
- Patch #2 bugfix (bug: #7682)

* Sun Jul 24 2005 LAKostis <lakostis at altlinux.ru> 1.0.6-alt2.cvs
- fix -nox patch.
- add gssapi detection and build fixes from mhz@.

* Tue Jul 19 2005 LAKostis <lakostis at altlinux.ru> 1.0.6-alt1.cvs
- new version from aviary branch fixing various bugs:
  + MFSA2005-54
  + Restore API compatibility for extensions and web applications 
    that did not work in Firefox 1.0.5.
  
* Mon Jul 11 2005 LAKostis <lakostis at altlinux.ru> 1.0.5-alt2.cvs
- new version from aviary branch;

* Wed Jun 22 2005 LAKostis <lakostis at altlinux.ru> 1.0.5-alt1.cvs
- new version from aviary branch fixing various security bugs;
- fix: #4846, #5101, #7126 (legion).
- if_{with,without} debug - added (legion).
- keyword 'altbug:' added, patch2 updated (legion).
- postin/postun-scripts scripts bugfixes (legion).
- triggers added for trash cleanup (legion).

* Mon Jun 20 2005 LAKostis <lakostis at altlinux.ru> 1.0.5-alt0.cvs
- new version from aviary branch;
- fix #6595;
- add switches for svg/xprint easy builds.
- update alt-prefs-tuning.patch (disable annoying default browser dialog).

* Sun Jun 12 2005 LAKostis <lakostis at altlinux.ru> 1.0.4-alt1
- new version;
- SA15601 security fix;
- BuildRequires cleanup (remove xorg-x11-libs-static).

* Thu Apr 21 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.3-alt1
- new version;
- requires fix;

* Wed Apr 13 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.2-alt1
- new version;
- RPATH fix;
- NoX patch was rewritten;

* Sun Mar 06 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.1-alt2
- rpm macros was updated;

* Fri Feb 25 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.1-alt1
- new version;
- patch9 was added (mozilla Bug #123315);
- patch10, patch11 was added (#6151);

* Mon Feb 14 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt7
- plugins path bugfix;
- svg support added;
- x86_64 compatibility added (thx mouse@);

* Tue Feb 01 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt6
- update patch firefox-1.0-20050201-alt-nox.patch 
  * uninstall-global-theme command-line option was added;
  * update-register command-line option was added;
- firefox-1.0-alt-rpm-scripts.tar.bz2 bugfix;

* Thu Jan 27 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt5
- disable svg support becouse svg layout lead to segfault 
  when mozilla compile with gcc3.4 .
- search plugins was moved into the standalone rpm package.

* Wed Jan 19 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt4
- Rebuilt with libstdc++.so.6.

* Wed Jan 05 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt3
- new version;
- browser-plugins-npapi support added;
- new icons default icons(thx shrek@);
- option uninstall-global-extension was fixed;

* Wed Nov 03 2004 Alexey Gladkov <legion@altlinux.ru> 1.0-alt2.rc1
- extension sheme changes;
- postin/preun scripts chenges;

* Mon Oct 18 2004 Alexey Gladkov <legion@altlinux.ru> 1.0-alt2.PR
- new default extensions added;
- protocol 'mailto' external handler added; 
- firefox.macro changed;
- postun script changed;
- icons changed;

* Thu Sep 30 2004 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1.PR
- New version 1.0PR;
- New extension scheme;
- Add:
    * New option 'run-without-x' added (mouse, legion);
    * SVG support added;
    * Certificate (ALT Linux CA Root) added;
    * ALT Linux BTS search plugin added;
    * RPATH added to all binary files;
- bug #4284 fixed;

* Fri May 28 2004 Alexey Gladkov <legion@altlinux.ru> 0.8-alt4
- Move back some changes at alt3 build.
- Bug #4157 fixed.

* Fri Apr 30 2004 Alexey Gladkov <legion@altlinux.ru> 0.8-alt3.1
- viewsource protocol was added.

* Thu Apr 29 2004 Alexey Gladkov <legion@altlinux.ru> 0.8-alt3
- Minimize buildin extensions;
- Disable debug output;
- Disable some options:
  + disable JavaScript debug library;
  + disable LDAP support;
  + disable logging facilities;
- Necko protocols cleanup;

* Tue Feb 24 2004 Alexey Gladkov <legion@altlinux.ru> 0.8-alt2
- Splash screen added (thx sadist@);
- Search plugins added;
- Remove devel package Conflicts;
- Change rebuild-database.sh script. Script must be run only as root;
- Change locale hack.

* Wed Feb 11 2004 Alexey Gladkov <legion@altlinux.ru> 0.8-alt1
- Mozilla Firebird becomes Mozilla Firefox. Mozilla's next 
  generation browser has changed names (again);
- New version;

* Sun Jan 11 2004 Alexey Gladkov <legion@altlinux.ru> 0.7-alt2
- Spec changes.
- run-mozilla.sh script patch.

* Tue Dec 30 2003 Alexey Gladkov <legion@altlinux.ru> 0.7-alt1
- first build for ALT Linux.
- rpm macro created.
- new scheme loading extensions added (thx force@)
