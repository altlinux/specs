#set_verify_elf_method relaxed
%define _unpackaged_files_terminate_build 1

%def_without	debug
%def_without	mozldap

%define xulr_name                   xulrunner
%define xulr_prefix                 %_libdir/%xulr_name
%define xulr_datadir                %_datadir/%xulr_name
%define xulr_idldir                 %_datadir/idl/%xulr_name
%define xulr_includedir             %_includedir/%xulr_name
%define xulr_develdir               %xulr_prefix-devel

Summary:	XUL Runner
Name:		xulrunner
Version:	13.0.2
Release:	alt1

License:	MPL/GPL/LGPL
Group:		Networking/Other
Url:		http://wiki.mozilla.org/XUL:Xul_Runner
Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	xulrunner-source.tar
Source1:	rpm-build.tar
Source2:	update-sdk.sh
Source3:	xulrunner-mozconfig
Source4:	xpi-mimeinfo.xml

Patch0:		xulrunner-no-version.patch
Patch2:		xulrunner-noarch-extensions.patch

Patch100:	mozilla-192-path.patch
#Patch101:	mozilla-pkgconfig.patch
Patch104:	mozilla-nongnome-proxies.patch
Patch105:	mozilla-libjpeg-turbo.patch
Patch106:	mozilla-check-libvpx.patch
#Patch106:	mozilla-omnijar.patch
#Patch107:	firefox-4.0-gnome3.patch

Requires:	%name-libs = %version-%release

Requires:	hunspell-en
Requires:	libnspr       >= 4.9.0-alt1
Requires:	libnss        >= 3.13.4-alt2

Obsoletes:	xulrunner-192
Obsoletes:	xulrunner-2.0
Obsoletes:	xulrunner-5.0

Provides:	xulrunner-gnome-support = %version-%release
Obsoletes:	xulrunner-gnome-support
Obsoletes:	xulrunner-192-gnome-support
Obsoletes:	xulrunner-2.0-gnome-support

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
BuildRequires: libproxy-devel
BuildRequires: zip unzip
BuildRequires: libshell
BuildRequires: libvpx-devel
BuildRequires: libgio-devel
BuildRequires: libfreetype-devel fontconfig-devel
BuildRequires: libstartup-notification-devel
BuildRequires: libffi-devel

BuildRequires: libnspr-devel       >= 4.8.7-alt1
BuildRequires: libnss-devel        >= 3.13.4-alt2
BuildRequires: libnss-devel-static >= 3.13.4-alt2

BuildRequires: autoconf_2.13
%set_autoconf_version 2.13

%description
XULRunner is a single "gecko runtime" installable package
that can be used to bootstrap multiple XUL+XPCOM applications


%package libs
Summary:	XULRunner libraries.
Group:		System/Libraries

Obsoletes:	xulrunner-192-libs
Obsoletes:	xulrunner-2.0-libs
Obsoletes:	xulrunner-5.0-libs

%description libs
XULRunner  libraries.


%package devel
Summary:	XULRunner development kit.
Group:		Development/C++

Requires:	python-base
AutoReq:	yes, nopython

Requires:	%name = %version-%release
Conflicts:	seamonkey-devel

Obsoletes:	xulrunner-192-devel
Obsoletes:	xulrunner-2.0-devel
Obsoletes:	xulrunner-5.0-devel

%description devel
XULRunner development kit.


%package -n rpm-build-mozilla.org
Summary:	RPM helpers to build Mozilla.org packages
Group:		Development/Other
BuildArch:	noarch
Requires:	raptor rpm-utils

%description -n rpm-build-mozilla.org
These helpers provide possibility to build Mozilla.org packages
by some Alt Linux Team Policy compatible way.


%prep
%setup -q -c -n %name-%version
cd %_builddir/%name-%version/mozilla

tar -xf %SOURCE1

%patch0 -p1
%patch2 -p1

%patch100 -p1
#patch101 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
#patch107 -p1

#echo 5.0.1 > config/milestone.txt

cp -f %SOURCE3 .mozconfig

%ifarch armv7hl
echo "ac_add_options --with-arch=armv7-a" >> .mozconfig
echo "ac_add_options --with-float-abi=hard" >> .mozconfig
echo "ac_add_options --with-fpu=vfpv3-d16" >> .mozconfig
echo "ac_add_options --disable-elf-hack" >> .mozconfig
%endif
%ifarch armv7hnl
echo "ac_add_options --with-arch=armv7-a" >> .mozconfig
echo "ac_add_options --with-float-abi=hard" >> .mozconfig
echo "ac_add_options --with-fpu=neon" >> .mozconfig
echo "ac_add_options --disable-elf-hack" >> .mozconfig
%endif
%ifarch armv5tel
echo "ac_add_options --with-arch=armv5te" >> .mozconfig
echo "ac_add_options --with-float-abi=soft" >> .mozconfig
echo "ac_add_options --disable-elf-hack" >> .mozconfig
%endif

%ifnarch %{ix86} x86_64
echo "ac_add_options --disable-methodjit" >> .mozconfig
echo "ac_add_options --disable-monoic" >> .mozconfig
echo "ac_add_options --disable-polyic" >> .mozconfig
echo "ac_add_options --disable-tracejit" >> .mozconfig
%endif


%build
%add_optflags %optflags_shared
cd %_builddir/%name-%version/mozilla

export MOZ_BUILD_APP=xulrunner

# -fpermissive is needed to build with gcc 4.6+ which has become stricter
#
# Mozilla builds with -Wall with exception of a few warnings which show up
# everywhere in the code; so, don't override that.
#
# Disable C++ exceptions since Mozilla code is not exception-safe
#
MOZ_OPT_FLAGS=$(echo "%optflags -fpermissive" | \
                      sed -e 's/-Wall//' -e 's/-fexceptions/-fno-exceptions/g')
export CFLAGS="$MOZ_OPT_FLAGS"
export CXXFLAGS="$MOZ_OPT_FLAGS"

export PREFIX='%_prefix'
export LIBDIR='%_libdir'
export INCLUDEDIR='%_includedir'
export LIBIDL_CONFIG='/usr/bin/libIDL-config-2'
export srcdir="$PWD"

sed -i \
	-e 's,^MOZ_APP_NAME[[:space:]]*=.*,MOZ_APP_NAME = %xulr_name,' \
	config/autoconf.mk.in

cat >> xulrunner/confvars.sh <<EOF
MOZ_UPDATER=
MOZ_JAVAXPCOM=
MOZ_NATIVE_NSPR=1
MOZ_SERVICES_SYNC=1
MOZ_EXTENSIONS_DEFAULT=" gio"
EOF

%__autoconf

cd js/src
%__autoconf
cd -

MOZ_SMP_FLAGS=-j1
# On x86 architectures, Mozilla can build up to 4 jobs at once in parallel,
# however builds tend to fail on other arches when building in parallel.
%ifarch %ix86 x86_64
[ "%__nprocs" -ge 2 ] && MOZ_SMP_FLAGS=-j2
[ "%__nprocs" -ge 4 ] && MOZ_SMP_FLAGS=-j4
%endif

make -f client.mk build \
	mozappdir=%xulr_prefix \
	STRIP="/bin/true" \
	MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS"


%install
cd %_builddir/%name-%version/mozilla
%__mkdir_p \
	%buildroot/%_datadir/mime/packages \
	#

%makeinstall -C objdir \
	idldir=%buildroot/%xulr_idldir \
	includedir=%buildroot/%xulr_includedir \
	mozappdir=%buildroot/%xulr_prefix \
	#

if [ ! -d "%buildroot/%xulr_prefix-devel/sdk/bin" ]; then
	mkdir -p -- "%buildroot/%xulr_prefix-devel/sdk/bin"
	find dist/sdk/bin/ '!' -type d \
		-exec install -t "%buildroot/%xulr_prefix-devel/sdk/bin" '{}' '+'
fi

%SOURCE2 \
	--develdir="%buildroot/%xulr_prefix-devel" \
	--bindir="%buildroot/%_bindir" \
	--libdir="%buildroot/%xulr_prefix" \
	--idldir="%buildroot/%xulr_idldir" \
	--includedir="%buildroot/%xulr_includedir" \
        --rpath="" \
        --verbose \
        #

# Install rpm-build-mozilla.org
mkdir -p -- %buildroot/%_datadir/%xulr_name %buildroot/%_rpmlibdir

for f in rpm-build/installrdf.sh rpm-build/applicationini.sh; do
	fn="${f##*/}"
	sed \
		-e 's,@require_gre_name@,%xulr_name,g' \
		-e 's,@rpmdatadir@,%_datadir/rpm-build-mozilla,g' \
		< "$f" > %buildroot/%_bindir/$fn
	chmod 755 -- %buildroot/%_bindir/$fn
done

install -D -m644 \
	rpm-build/mozilla-sh-functions \
	%buildroot/%_datadir/rpm-build-mozilla/mozilla-sh-functions

install -D -m755 \
	rpm-build/xulrunner.req* \
	%buildroot/%_rpmlibdir/

mkdir -p -- %buildroot/%_sysconfdir/rpm/macros.d
sed \
	-e 's,@xulr_name@,%xulr_name,g' \
	-e 's,@xulr_version@,%version,g' \
	-e 's,@xulr_release@,%release,g' \
	rpm-build/rpm.macros.standalone > %buildroot/%_sysconfdir/rpm/macros.d/%xulr_name

install -D -m644 \
	%SOURCE4 \
	%buildroot/%_datadir/mime/packages/%xulr_name-mimeinfo.xml

cd %buildroot
rm -f -- \
	./%xulr_prefix/run-mozilla.sh \
	./%xulr_prefix/LICENSE \
	./%xulr_prefix/README.txt \
	./%xulr_prefix/dictionaries/* \
	./%_libdir/pkgconfig/gtkmozembed*.pc \
	#

ln -sf -- $(relative "%xulr_prefix/xulrunner-bin" "%_bindir/%xulr_name") \
	./%_bindir/%xulr_name

# Fix *.pc
sed -i -e 's,%{buildroot},,g' ./%_libdir/pkgconfig/*.pc

# Fix SDK
ln -sf $(relative "%xulr_prefix/libmozalloc.so" "%xulr_develdir/sdk/lib/libmozalloc.so") \
	./%xulr_develdir/sdk/lib/libmozalloc.so

(set +x
	for l in libmozalloc.so libmozjs.so libxpcom.so libxul.so libmozsqlite3.so; do
		[ -f .%xulr_prefix/$l ] ||
			continue
		mv -f -- .%xulr_prefix/$l .%_libdir/$l
		ln -vs -- "$(relative %_libdir/$l %xulr_prefix/$l)" .%xulr_prefix/$l
	done
)

(set +x
	for suf in aff dic; do
		t="$(relative %_datadir/myspell/en_US.$suf %xulr_prefix/dictionaries/)"
		ln -vs "$t" ./%xulr_prefix/dictionaries/en-US.$suf
	done
)

(set +x
	find -type l -printf '%%p %%l\n' |
		egrep '(\.\./){4,}' |
		cut -d\  -f1 |
	while read f; do
		t="$(readlink -ev "$f")";
		l="$(relative "${f#.}" "$t")";
		ln -vnsf "$l" "$f";
	done
)

%pre
[ ! -L '%xulr_prefix/defaults' ] || rm -f '%xulr_prefix/defaults'

%files
%_bindir/%xulr_name
%xulr_prefix
%_datadir/mime/packages/*.xml
%exclude %xulr_prefix/xpcshell

%files libs
%_libdir/*.so*

%files devel
%_libdir/pkgconfig/*
%xulr_prefix/xpcshell
%xulr_includedir
%xulr_develdir
%xulr_idldir

%files -n rpm-build-mozilla.org
%_bindir/installrdf.sh
%_bindir/applicationini.sh
%_sysconfdir/rpm/macros.d/xulrunner
%_rpmlibdir/xulrunner.req*
%_datadir/rpm-build-mozilla/mozilla-sh-functions

%changelog
* Tue Jun 26 2012 Alexey Gladkov <legion@altlinux.ru> 13.0.2-alt1
- New release (13.0.2).
- Fixed:
  + MFSA 2012-40 Buffer overflow and use-after-free issues found using Address Sanitizer
  + MFSA 2012-39 NSS parsing errors with zero length items
  + MFSA 2012-38 Use-after-free while replacing/inserting a node in a document
  + MFSA 2012-37 Information disclosure though Windows file shares and shortcut files
  + MFSA 2012-36 Content Security Policy inline-script bypass
  + MFSA 2012-35 Privilege escalation through Mozilla Updater and Windows Updater Service
  + MFSA 2012-34 Miscellaneous memory safety hazards 

* Wed Apr 25 2012 Alexey Gladkov <legion@altlinux.ru> 12.0-alt1
- New release (12.0).
- Use internal libcairo.
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

* Tue Apr 17 2012 Alexey Gladkov <legion@altlinux.ru> 11.0-alt1
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

* Fri Feb 17 2012 Alexey Gladkov <legion@altlinux.ru> 10.0.1-alt1
- New releaee (10.0.1).

* Tue Jan 31 2012 Alexey Gladkov <legion@altlinux.ru> 9.0.1-alt2
- Rebuilt with libvpx.

* Mon Jan 02 2012 Alexey Gladkov <legion@altlinux.ru> 9.0.1-alt1
- New releaee (9.0.1).
- Fixed:
  + MFSA 2011-58 Crash scaling <video> to extreme sizes
  + MFSA 2011-57 Crash when plugin removes itself on Mac OS X
  + MFSA 2011-56 Key detection without JavaScript via SVG animation
  + MFSA 2011-55 nsSVGValue out-of-bounds access
  + MFSA 2011-54 Potentially exploitable crash in the YARR regular expression library
  + MFSA 2011-53 Miscellaneous memory safety hazards (rv:9.0)

* Mon Nov 14 2011 Alexey Gladkov <legion@altlinux.ru> 8.0-alt1
- New releaee (8.0).
- Remove gtkmozembed*.pc (ALT#26441).
- Fixed:
  + MFSA 2011-52 Code execution via NoWaiverWrapper
  + MFSA 2011-51 Cross-origin image theft on Mac with integrated Intel GPU
  + MFSA 2011-50 Cross-origin data theft using canvas and Windows D2D
  + MFSA 2011-49 Memory corruption while profiling using Firebug
  + MFSA 2011-48 Miscellaneous memory safety hazards (rv:8.0)
  + MFSA 2011-47 Potential XSS against sites using Shift-JIS

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 7.0.1-alt1.1
- Rebuild with Python-2.7

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

* Sun Aug 21 2011 Alexey Gladkov <legion@altlinux.ru> 6.0-alt1
- New release (6.0).
- Add nsGIOProtocolHandler extension (ALT#26136)
- Fixed:
  + MFSA 2011-29 Security issues addressed in Firefox6.

* Tue Aug 09 2011 Alexey Gladkov <legion@altlinux.ru> 5.0.1-alt2
- Fix requires (ALT#26014).

* Thu Jul 14 2011 Alexey Gladkov <legion@altlinux.ru> 5.0.1-alt1
- New major release (5.0.1).
- Remove gnome-support subpackage.
- Fixed:
  + MFSA 2011-28 Non-whitelisted site can trigger xpinstall
  + MFSA 2011-27 XSS encoding hazard with inline SVG
  + MFSA 2011-26 Multiple WebGL crashes
  + MFSA 2011-25 Stealing of cross-domain images using WebGL textures
  + MFSA 2011-22 Integer overflow and arbitrary code execution in Array.reduceRight()
  + MFSA 2011-21 Memory corruption due to multipart/x-mixed-replace images
  + MFSA 2011-20 Use-after-free vulnerability when viewing XUL document with script disabled
  + MFSA 2011-19 Miscellaneous memory safety hazards (rv:3.0/1.9.2.18)
  + MFSA 2011-18 XSLT generate-id() function heap address leak
  + MFSA 2011-17 WebGLES vulnerabilities
  + MFSA 2011-12 Miscellaneous memory safety hazards (rv:2.0.1/ 1.9.2.17/ 1.9.1.19)

* Sun May 01 2011 Alexey Gladkov <legion@altlinux.ru> 2.0.1.0-alt1
- New major release (2.0.1).

* Sat Mar 26 2011 Alexey Gladkov <legion@altlinux.ru> 2.0.0.0-alt1
- New major release (2.0).
- Remove alternatives for configuration.

* Tue Mar 08 2011 Alexey Gladkov <legion@altlinux.ru> 1.9.2.15-alt1.20110308
- New development snapshot 1.9.2.16pre (20110308).
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

* Thu Feb 24 2011 Alexey Gladkov <legion@altlinux.ru> 1.9.2.14-alt1.20110224
- New development snapshot 1.9.2.15pre (20110224).

* Wed Dec 22 2010 Alexey Gladkov <legion@altlinux.ru> 1.9.2.14-alt1.20101222
- New development snapshot 1.9.2.14pre (20101222).
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

* Wed Nov 10 2010 Alexey Gladkov <legion@altlinux.ru> 1.9.2.13-alt1.20101110
- New development snapshot 1.9.2.13pre (20101110).
- Fixed:
  + MFSA 2010-73 Heap buffer overflow mixing document.write and DOM insertion

* Tue Oct 26 2010 Alexey Gladkov <legion@altlinux.ru> 1.9.2.12-alt1.20101025
- New development snapshot 1.9.2.12pre (20101025).
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

* Mon Sep 20 2010 Alexey Gladkov <legion@altlinux.ru> 1.9.2.11-alt1.20100920
- New development snapshot 1.9.2.11pre (20100920).

* Sun Sep 12 2010 Alexey Gladkov <legion@altlinux.ru> 1.9.2.9-alt1.20100909
- New development snapshot 1.9.2.10pre (20100909).
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

* Sun Jul 25 2010 Alexey Gladkov <legion@altlinux.ru> 1.9.2.9-alt1.20100725
- New development snapshot 1.9.2.7pre (20100725).
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

* Sun Jun 27 2010 Alexey Gladkov <legion@altlinux.ru> 1.9.2.7-alt1.20100626
- New development snapshot 1.9.2.7pre (20100626).

* Sun Apr 04 2010 Alexey Gladkov <legion@altlinux.ru> 1.9.2.4-alt1.20100404
- New development snapshot 1.9.2.4pre (20100404).

* Sun Mar 28 2010 Alexey Gladkov <legion@altlinux.ru> 1.9.2.3-alt1.20100328
- New development snapshot 1.9.2.3pre (20100328).

* Fri Mar 19 2010 Alexey Gladkov <legion@altlinux.ru> 1.9.2.0-alt1.20100122.1
- Fix pkgconfig file.

* Wed Jan 22 2010 Alexey Gladkov <legion@altlinux.ru> 1.9.2.0-alt1.20100122
- New development snapshot (20100122).

* Sun Nov 08 2009 Alexey Gladkov <legion@altlinux.ru> 1.9.2.0-alt1.20091124
- New branch (1.9.2.0 20091124).

* Fri Nov 06 2009 Alexey Gladkov <legion@altlinux.ru> 1.9.1.5-alt1.20091106
- Bugfix build up to Firefox 3.5.5.

* Sun Nov 01 2009 Alexey Gladkov <legion@altlinux.ru> 1.9.1.5-alt0.20091101
- New development snapshot (20091101).
- Fixed:
  + MFSA 2009-64  Crashes with evidence of memory corruption (rv:1.9.1.4/ 1.9.0.15)
  + MFSA 2009-63 Upgrade media libraries to fix memory safety bugs
  + MFSA 2009-62 Download filename spoofing with RTL override
  + MFSA 2009-61 Cross-origin data theft through document.getSelection()
  + MFSA 2009-59 Heap buffer overflow in string to number conversion
  + MFSA 2009-57 Chrome privilege escalation in XPCVariant::VariantDataToJS()
  + MFSA 2009-56 Heap buffer overflow in GIF color map parser
  + MFSA 2009-55 Crash in proxy auto-configuration regexp parsing
  + MFSA 2009-54 Crash with recursive web-worker calls
  + MFSA 2009-53 Local downloaded file tampering
  + MFSA 2009-52 Form history vulnerable to stealing

* Sun Oct 18 2009 Alexey Gladkov <legion@altlinux.ru> 1.9.1.5-alt0.20091018
- New development snapshot (20091018).

* Sat Oct 10 2009 Alexey Gladkov <legion@altlinux.ru> 1.9.1.4-alt0.20091010
- New development snapshot (20091010).
- KDE: Update patches (ALT#21678).

* Fri Sep 18 2009 Alexey Gladkov <legion@altlinux.ru> 1.9.1.4-alt0.20090918
- New development snapshot (20090918).
- Add KDE integration from SUSE (ALT#21511).
- Add mimeinfo for xpi files (ALT#21510).

* Mon Aug 31 2009 Alexey Gladkov <legion@altlinux.ru> 1.9.1.1-alt1.20090831
- New development snapshot (20090831).
- Fixed:
  + MFSA 2009-46  Chrome privilege escalation due to incorrectly cached wrapper
  + MFSA 2009-45 Crashes with evidence of memory corruption (rv:1.9.1.2/1.9.0.13)
  + MFSA 2009-44 Location bar and SSL indicator spoofing via window.open() on invalid URL
  + MFSA 2009-38 Data corruption with SOCKS5 reply containing DNS name longer than 15 characters
  + MFSA 2009-35  Crash and remote code execution during Flash player unloading

* Fri Jul 17 2009 Alexey Gladkov <legion@altlinux.ru> 1.9.1.1-alt1.20090717
- New development snapshot (20090717).
- Fixed:
  + MFSA 2009-41  Corrupt JIT state after deep return from native function.

* Tue Jun 30 2009 Alexey Gladkov <legion@altlinux.ru> 1.9.1-alt1.20090630
- New development snapshot (20090630).

* Wed Jun 03 2009 Alexey Gladkov <legion@altlinux.ru> 1.9.1-alt1.20090601
- New development snapshot.
- Fix extension directories check (closes: #20105).

* Tue Apr 24 2009 Alexey Gladkov <legion@altlinux.ru> 1.9.1-alt1.20090424
- New development snapshot.

* Thu Jan 08 2009 Alexey Gladkov <legion@altlinux.ru> 1.9.1-alt1.20090312
- Bugfix build.
- Build with system mozsqlite3 (sqlite3 unsupported).
- Spellchecker: Multiple language design (moz#69687).
- Spellchecker: Hunspell doesn't recognize misspelled words if they are
  in different encoding (moz#471799).

* Mon Dec 08 2008 Alexey Gladkov <legion@altlinux.ru> 1.9.0.5-alt1.20081205
- Bugfix build.
- Add patch for moz#358926 (closes: #18085).

* Tue Nov 18 2008 Alexey Gladkov <legion@altlinux.ru> 1.9.0.5-alt1.20081118
- Bugfix build up to firefox-3.0.4.
- Add confilct with seamonkey-devel (closes: #17682).
- Move jsapi.h to stable directory (closes: #17561).
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

* Mon Oct 06 2008 Alexey Gladkov <legion@altlinux.ru> 1.9.0.3-alt1.20081005
- Bugfix build up to firefox-3.0.3.
- Add python-module-xpcom subpackage.
- Firefox does not participate in accessibility on 64 bit Linux (moz#456541).
- Printing on linux should set SIMPLIFY_OPERATORS | DISABLE_SNAPPING (moz#435313).
- MAXPATHLEN too small for glibc's realpath() (moz#412610).
- New preference that allows users to set a preferred plugin
  for a given mime-type.
- Fixed:
  + MFSA 2008-44 resource: traversal vulnerabilities
  + MFSA 2008-43 BOM characters stripped from JavaScript before execution
  + MFSA 2008-42 Crashes with evidence of memory corruption (rv:1.9.0.2/1.8.1.17)
  + MFSA 2008-41 Privilege escalation via XPCnativeWrapper pollution
  + MFSA 2008-40 Forced mouse drag

* Mon Sep 08 2008 Alexey Gladkov <legion@altlinux.ru> 1.9.0.3-alt1.20080908
- Bugfix build.
- Fix BuildRequires.
- Rebuild with hunspell-1.2.7-alt1.
- Add libdir variable into *.pc (ALT#16634).
- Fix #13786.

* Fri Jul 18 2008 Alexey Gladkov <legion@altlinux.ru> 1.9-alt2.20080718
- Bugfix build up to firefox-3.0.1.
- Fixed:
  + MFSA 2008-36 Crash with malformed GIF file on Mac OS X
  + MFSA 2008-35 Command-line URLs launch multiple tabs when Firefox not running
  + MFSA 2008-34 Remote code execution by overflowing CSS reference counter

* Fri Jul 11 2008 Alexey Gladkov <legion@altlinux.ru> 1.9-alt2.20080704
- Bugfix build.
- Tune default settings.
- Stop double instantiation even earlier (BMO#438830).
- Build with --enable-oji (BMO#445063).
- Move libjemalloc.so libmozjs.so libxpcom.so libxul.so into %%_libdir
  and remove RPATH and LD_LIBRARY_PATH.
- Use hunspell-en dictionary.

* Fri Jul 04 2008 Alexey Gladkov <legion@altlinux.ru> 1.9-alt1.20080704
- New cvs snapshot.
- Dont use NetworkManager by default (BMO#424626).
- Allow change default settings.

* Thu Jun 05 2008 Alexey Gladkov <legion@altlinux.ru> 1.9-alt1.20080605
- New cvs snapshot.
- Add new sub-package: xulrunner-gnome-support.

* Thu May 29 2008 Alexey Gladkov <legion@altlinux.ru> 1.9-alt1.20080529
- New cvs snapshot.

* Sun Feb 03 2008 Alexey Gladkov <legion@altlinux.ru> 1.9-alt1.b3pre
- New cvs snapshot.
- Add SDK toolkit.

* Wed Nov 21 2007 Alexey Gladkov <legion@altlinux.ru> 1.8.1.10-alt1
- Build from cvs.

* Fri Sep 28 2007 Alexey Gladkov <legion@altlinux.ru> 1.8.0.4-alt5
- Fix buildrequires;

* Tue Feb 27 2007 Alexey Gladkov <legion@altlinux.ru> 1.8.0.4-alt4
- Remove requires nspr with version from *.pc

* Thu Oct 19 2006 Alexey Gladkov <legion@altlinux.ru> 1.8.0.4-alt3
- Add cookie and permissions extensions.

* Fri Sep 22 2006 Alexey Gladkov <legion@altlinux.ru> 1.8.0.4-alt2
- Fix Cflags in *.pc

* Wed Aug 30 2006 Alexey Gladkov <legion@altlinux.ru> 1.8.0.4-alt1
- New version (1.8.0.4-alt1).
- Update BuildRequires.

* Thu Jul 06 2006 Alexey Gladkov <legion@altlinux.ru> 1.8.0.1-alt2
- fixed build system.

* Sat Mar 25 2006 Alexey Gladkov <legion@altlinux.ru> 1.8.0.1-alt1
- new version.
- Build with system NSS and NSPR.
- Build libxul.
- Header bugfix.
- Directory /usr/share/xulrunner-@version@/extensions was added to extensions search path .
  * this location is controled by the option extensions.dir.extensions .

* Thu Jun 16 2005 Alexey Gladkov <legion@altlinux.ru> 0.0.0-alt1
- first build for ALT Linux.
