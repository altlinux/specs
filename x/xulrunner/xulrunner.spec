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
Version:	41.0.2
Release:	alt1

License:	MPL/GPL/LGPL
Group:		Networking/Other
Url:		http://developer.mozilla.org/En/XULRunner
Packager:	Andrey Cherepanov <cas@altlinux.org>

Source0:	xulrunner-source.tar
Source1:	rpm-build.tar
Source2:	update-sdk.sh
Source3:	xulrunner-mozconfig
Source4:	xpi-mimeinfo.xml

Patch0:		xulrunner-no-version.patch
Patch1:		mozilla-js-makefile.patch
Patch10:	rhbz-966424.patch
Patch100:	mozilla-192-path.patch

Requires:	%name-libs = %version-%release

Requires:	hunspell-en
Requires:	libnspr       >= 4.10.1-alt1
Requires:	libnss        >= 3.15.2-alt1

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
BuildRequires: zip unzip
BuildRequires: bzlib-devel zlib-devel
BuildRequires: libcairo-devel libpixman-devel
BuildRequires: libGL-devel
BuildRequires: libwireless-devel
BuildRequires: libalsa-devel
BuildRequires: libnotify-devel
BuildRequires: libevent-devel
BuildRequires: libproxy-devel
BuildRequires: libshell
BuildRequires: libvpx-devel
BuildRequires: libgio-devel
BuildRequires: libfreetype-devel fontconfig-devel
BuildRequires: libstartup-notification-devel
BuildRequires: libffi-devel
BuildRequires: gstreamer-devel gst-plugins-devel
BuildRequires: libopus-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel

# Python requires
BuildRequires: python-module-distribute
BuildRequires: python-modules-compiler
BuildRequires: python-modules-logging
BuildRequires: python-modules-sqlite3
BuildRequires: python-modules-json

# Mozilla requires
BuildRequires: libnspr-devel >= 4.10.1-alt1
BuildRequires: libnss-devel  >= 3.15.2-alt1

BuildRequires: libnss-devel-static

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
%patch1 -p1 -b .fix
#patch2 -p1

%patch10 -p1

%patch100 -p2
#patch101 -p1
#patch104 -p1

#echo 5.0.1 > config/milestone.txt

cp -f %SOURCE3 .mozconfig

%ifnarch %{ix86} x86_64 armh
echo "ac_add_options --disable-methodjit" >> .mozconfig
echo "ac_add_options --disable-monoic" >> .mozconfig
echo "ac_add_options --disable-polyic" >> .mozconfig
echo "ac_add_options --disable-tracejit" >> .mozconfig
%endif

%build
%add_optflags %optflags_shared
cd %_builddir/%name-%version/mozilla

export MOZ_BUILD_APP=xulrunner

export PREFIX='%_prefix'
export LIBDIR='%_libdir'
export INCLUDEDIR='%_includedir'
export LIBIDL_CONFIG='/usr/bin/libIDL-config-2'
export srcdir="$PWD"
export SHELL=/bin/sh

sed -i \
	-e 's,^MOZ_APP_NAME[[:space:]]*=.*,MOZ_APP_NAME = %xulr_name,' \
	config/autoconf.mk.in

cat >> xulrunner/confvars.sh <<EOF
MOZ_UPDATER=
MOZ_JAVAXPCOM=
MOZ_NATIVE_NSPR=1
MOZ_ENABLE_WARNINGS_AS_ERRORS=
MOZ_SERVICES_COMMON=1
MOZ_SERVICES_CRYPTO=1
MOZ_SERVICES_FXACCOUNTS=1
MOZ_SERVICES_HEALTHREPORT=1
MOZ_SERVICES_METRICS=1
MOZ_SERVICES_SYNC=1
EOF

%__autoconf

cd js/src
%__autoconf
cd -

MOZ_SMP_FLAGS=-j1
# On x86 architectures, Mozilla can build up to 4 jobs at once in parallel,
# however builds tend to fail on other arches when building in parallel.
%ifarch %ix86 x86_64 armh
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

mkdir -p -- %buildroot/%_rpmmacrosdir
sed \
	-e 's,@xulr_name@,%xulr_name,g' \
	-e 's,@xulr_version@,%version,g' \
	-e 's,@xulr_release@,%release,g' \
	rpm-build/rpm.macros.standalone > %buildroot/%_rpmmacrosdir/%xulr_name

install -D -m644 \
	%SOURCE4 \
	%buildroot/%_datadir/mime/packages/%xulr_name-mimeinfo.xml

cd %buildroot
rm -f -- \
	./%xulr_prefix/run-mozilla.sh \
	./%xulr_prefix/LICENSE \
	./%xulr_prefix/README.txt \
	./%xulr_prefix/README.xulrunner \
	./%xulr_prefix/js-gdb.py \
	./%xulr_prefix/dictionaries/* \
	./%_libdir/pkgconfig/gtkmozembed*.pc \
	#

ln -sf -- $(relative "%xulr_prefix/xulrunner" "%_bindir/%xulr_name") \
	./%_bindir/%xulr_name

# Fix *.pc
sed -i -e 's,%{buildroot},,g' ./%_libdir/pkgconfig/*.pc

# Fix SDK
#ln -sf $(relative "%xulr_prefix/libmozalloc.so" "%xulr_develdir/sdk/lib/libmozalloc.so") \
#	.%xulr_develdir/sdk/lib/libmozalloc.so

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

%files libs
%_libdir/*.so*

%files devel
%_libdir/pkgconfig/*
%xulr_includedir
%xulr_develdir
%xulr_idldir

%files -n rpm-build-mozilla.org
%_bindir/installrdf.sh
%_bindir/applicationini.sh
%_rpmmacrosdir/xulrunner
#_rpmlibdir/xulrunner.req*
%_datadir/rpm-build-mozilla/mozilla-sh-functions

%changelog
* Wed Feb 24 2016 Andrey Cherepanov <cas@altlinux.org> 41.0.2-alt1
- New version

* Wed Jul 23 2014 Alexey Gladkov <legion@altlinux.ru> 31.0-alt1
- New release (31.0).
- Fixed:
  + MFSA 2014-66 IFRAME sandbox same-origin access through redirect
  + MFSA 2014-65 Certificate parsing broken by non-standard character encoding
  + MFSA 2014-64 Crash in Skia library when scaling high quality images
  + MFSA 2014-63 Use-after-free while when manipulating certificates in the trusted cache
  + MFSA 2014-62 Exploitable WebGL crash with Cesium JavaScript library
  + MFSA 2014-61 Use-after-free with FireOnStateChange event
  + MFSA 2014-60 Toolbar dialog customization event spoofing
  + MFSA 2014-59 Use-after-free in DirectWrite font handling
  + MFSA 2014-58 Use-after-free in Web Audio due to incorrect control message ordering
  + MFSA 2014-57 Buffer overflow during Web Audio buffering for playback
  + MFSA 2014-56 Miscellaneous memory safety hazards (rv:31.0 / rv:24.7)

* Tue Jun 24 2014 Alexey Gladkov <legion@altlinux.ru> 30.0-alt1
- New release (30.0).
- Fixed:
  + MFSA 2014-54 Buffer overflow in Gamepad API
  + MFSA 2014-53 Buffer overflow in Web Audio Speex resampler
  + MFSA 2014-52 Use-after-free with SMIL Animation Controller
  + MFSA 2014-51 Use-after-free in Event Listener Manager
  + MFSA 2014-50 Clickjacking through cursor invisability after Flash interaction
  + MFSA 2014-49 Use-after-free and out of bounds issues found using Address Sanitizer
  + MFSA 2014-48 Miscellaneous memory safety hazards (rv:30.0 / rv:24.6)

* Tue May 06 2014 Alexey Gladkov <legion@altlinux.ru> 29.0-alt1
- New release (29.0).
- Fixed:
  + MFSA 2014-47 Debugger can bypass XrayWrappers with JavaScript
  + MFSA 2014-46 Use-after-free in nsHostResolve
  + MFSA 2014-45 Incorrect IDNA domain name matching for wildcard certificates
  + MFSA 2014-44 Use-after-free in imgLoader while resizing images
  + MFSA 2014-43 Cross-site scripting (XSS) using history navigations
  + MFSA 2014-42 Privilege escalation through Web Notification API
  + MFSA 2014-41 Out-of-bounds write in Cairo
  + MFSA 2014-40 Firefox for Android addressbar suppression
  + MFSA 2014-39 Use-after-free in the Text Track Manager for HTML video
  + MFSA 2014-38 Buffer overflow when using non-XBL object as XBL
  + MFSA 2014-37 Out of bounds read while decoding JPG images
  + MFSA 2014-36 Web Audio memory corruption issues
  + MFSA 2014-35 Privilege escalation through Mozilla Maintenance Service Installer
  + MFSA 2014-34 Miscellaneous memory safety hazards (rv:29.0 / rv:24.5)

* Fri Mar 21 2014 Alexey Gladkov <legion@altlinux.ru> 28.0-alt1
- New release (28.0).
- Fixed:
  + MFSA 2014-32 Out-of-bounds write through TypedArrayObject after neutering
  + MFSA 2014-31 Out-of-bounds read/write through neutering ArrayBuffer objects
  + MFSA 2014-30 Use-after-free in TypeObject
  + MFSA 2014-29 Privilege escalation using WebIDL-implemented APIs
  + MFSA 2014-28 SVG filters information disclosure through feDisplacementMap
  + MFSA 2014-27 Memory corruption in Cairo during PDF font rendering
  + MFSA 2014-26 Information disclosure through polygon rendering in MathML
  + MFSA 2014-25 Firefox OS DeviceStorageFile object vulnerable to relative path escape
  + MFSA 2014-24 Android Crash Reporter open to manipulation
  + MFSA 2014-23 Content Security Policy for data: documents not preserved by session restore
  + MFSA 2014-22 WebGL content injection from one domain to rendering in another
  + MFSA 2014-21 Local file access via Open Link in new tab
  + MFSA 2014-20 onbeforeunload and Javascript navigation DOS
  + MFSA 2014-19 Spoofing attack on WebRTC permission prompt
  + MFSA 2014-18 crypto.generateCRMFRequest does not validate type of key
  + MFSA 2014-17 Out of bounds read during WAV file decoding
  + MFSA 2014-16 Files extracted during updates are not always read only
  + MFSA 2014-15 Miscellaneous memory safety hazards (rv:28.0 / rv:24.4)

* Fri Feb 07 2014 Alexey Gladkov <legion@altlinux.ru> 27.0-alt1
- New release (27.0).
- Fixed:
  + MFSA 2014-13 Inconsistent JavaScript handling of access to Window objects
  + MFSA 2014-12 NSS ticket handling issues
  + MFSA 2014-11 Crash when using web workers with asm.js
  + MFSA 2014-10 Firefox default start page UI content invokable by script
  + MFSA 2014-09 Cross-origin information leak through web workers
  + MFSA 2014-08 Use-after-free with imgRequestProxy and image proccessing
  + MFSA 2014-07 XSLT stylesheets treated as styles in Content Security Policy
  + MFSA 2014-06 Profile path leaks to Android system log
  + MFSA 2014-05 Information disclosure with *FromPoint on iframes
  + MFSA 2014-04 Incorrect use of discarded images by RasterImage
  + MFSA 2014-03 UI selection timeout missing on download prompts
  + MFSA 2014-02 Clone protected content with XBL scopes
  + MFSA 2014-01 Miscellaneous memory safety hazards (rv:27.0 / rv:24.3)

* Sat Dec 21 2013 Alexey Gladkov <legion@altlinux.ru> 26.0-alt1
- New release (26.0).
- Fixed:
  + MFSA 2013-117 Mis-issued ANSSI/DCSSI certificate
  + MFSA 2013-116 JPEG information leak
  + MFSA 2013-115 GetElementIC typed array stubs can be generated outside observed typesets
  + MFSA 2013-114 Use-after-free in synthetic mouse movement
  + MFSA 2013-113 Trust settings for built-in roots ignored during EV certificate validation
  + MFSA 2013-112 Linux clipboard information disclosure though selection paste
  + MFSA 2013-111 Segmentation violation when replacing ordered list elements
  + MFSA 2013-110 Potential overflow in JavaScript binary search algorithms
  + MFSA 2013-109 Use-after-free during Table Editing
  + MFSA 2013-108 Use-after-free in event listeners
  + MFSA 2013-107 Sandbox restrictions not applied to nested object elements
  + MFSA 2013-106 Character encoding cross-origin XSS attack
  + MFSA 2013-105 Application Installation doorhanger persists on navigation
  + MFSA 2013-104 Miscellaneous memory safety hazards (rv:26.0 / rv:24.2)

* Wed Nov 20 2013 Alexey Gladkov <legion@altlinux.ru> 25.0.1-alt1
- New release (25.0.1).
- Fixed:
  + MFSA 2013-103 Miscellaneous Network Security Services (NSS) vulnerabilities

* Fri Nov 01 2013 Alexey Gladkov <legion@altlinux.ru> 25.0-alt1
- New release (25.0).
- Fixed:
  + MFSA 2013-102 Use-after-free in HTML document templates
  + MFSA 2013-101 Memory corruption in workers
  + MFSA 2013-100 Miscellaneous use-after-free issues found through ASAN fuzzing
  + MFSA 2013-99 Security bypass of PDF.js checks using iframes
  + MFSA 2013-98 Use-after-free when updating offline cache
  + MFSA 2013-97 Writing to cycle collected object during image decoding
  + MFSA 2013-96 Improperly initialized memory and overflows in some JavaScript functions
  + MFSA 2013-95 Access violation with XSLT and uninitialized data
  + MFSA 2013-94 Spoofing addressbar though SELECT element
  + MFSA 2013-93 Miscellaneous memory safety hazards (rv:25.0 / rv:24.1 / rv:17.0.10)

* Thu Sep 26 2013 Alexey Gladkov <legion@altlinux.ru> 24.0-alt1
- New release (24.0).
- Add gstreamer support (ALT#29454).
- Fixed:
  + MFSA 2013-92 GC hazard with default compartments and frame chain restoration
  + MFSA 2013-91 User-defined properties on DOM proxies get the wrong "this" object
  + MFSA 2013-90 Memory corruption involving scrolling
  + MFSA 2013-89 Buffer overflow with multi-column, lists, and floats
  + MFSA 2013-88 compartment mismatch re-attaching XBL-backed nodes
  + MFSA 2013-87 Shared object library loading from writable location
  + MFSA 2013-86 WebGL Information disclosure through OS X NVIDIA graphic drivers
  + MFSA 2013-85 Uninitialized data in IonMonkey
  + MFSA 2013-84 Same-origin bypass through symbolic links
  + MFSA 2013-83 Mozilla Updater does not lock MAR file after signature verification
  + MFSA 2013-82 Calling scope for new Javascript objects can lead to memory corruption
  + MFSA 2013-81 Use-after-free with select element
  + MFSA 2013-80 NativeKey continues handling key messages after widget is destroyed
  + MFSA 2013-79 Use-after-free in Animation Manager during stylesheet cloning
  + MFSA 2013-78 Integer overflow in ANGLE library
  + MFSA 2013-77 Improper state in HTML5 Tree Builder with templates
  + MFSA 2013-76 Miscellaneous memory safety hazards (rv:24.0 / rv:17.0.9)

* Thu Aug 08 2013 Alexey Gladkov <legion@altlinux.ru> 23.0-alt1
- New release (23.0).
- Fixed:
  + MFSA 2013-75 Local Java applets may read contents of local file system
  + MFSA 2013-74 Firefox full and stub installer DLL hijacking
  + MFSA 2013-73 Same-origin bypass with web workers and XMLHttpRequest
  + MFSA 2013-72 Wrong principal used for validating URI for some Javascript components
  + MFSA 2013-71 Further Privilege escalation through Mozilla Updater
  + MFSA 2013-70 Bypass of XrayWrappers using XBL Scopes
  + MFSA 2013-69 CRMF requests allow for code execution and XSS attacks
  + MFSA 2013-68 Document URI misrepresentation and masquerading
  + MFSA 2013-67 Crash during WAV audio file decoding
  + MFSA 2013-66 Buffer overflow in Mozilla Maintenance Service and Mozilla Updater
  + MFSA 2013-65 Buffer underflow when generating CRMF requests
  + MFSA 2013-64 Use after free mutating DOM during SetBody
  + MFSA 2013-63 Miscellaneous memory safety hazards (rv:23.0 / rv:17.0.8)

* Thu Jun 20 2013 Alexey Gladkov <legion@altlinux.ru> 22.0-alt1
- New release (22.0).
- Fixed:
  + MFSA 2013-62 Inaccessible updater can lead to local privilege escalation
  + MFSA 2013-61 Homograph domain spoofing in .com, .net and .name
  + MFSA 2013-60 getUserMedia permission dialog incorrectly displays location
  + MFSA 2013-59 XrayWrappers can be bypassed to run user defined methods in a privileged context
  + MFSA 2013-58 X-Frame-Options ignored when using server push with multi-part responses
  + MFSA 2013-57 Sandbox restrictions not applied to nested frame elements
  + MFSA 2013-56 PreserveWrapper has inconsistent behavior
  + MFSA 2013-55 SVG filters can lead to information disclosure
  + MFSA 2013-54 Data in the body of XHR HEAD requests leads to CSRF attacks
  + MFSA 2013-53 Execution of unmapped memory through onreadystatechange event
  + MFSA 2013-52 Arbitrary code execution within Profiler
  + MFSA 2013-51 Privileged content access and execution via XBL
  + MFSA 2013-50 Memory corruption found using Address Sanitizer
  + MFSA 2013-49 Miscellaneous memory safety hazards (rv:22.0 / rv:17.0.7)

* Tue Jun 18 2013 Alexey Gladkov <legion@altlinux.ru> 21.0-alt2
- Add missing healthreport service (ALT#29062).
- Remove extensions-noarch support.

* Fri May 31 2013 Alexey Gladkov <legion@altlinux.ru> 21.0-alt1
- New release (21.0).
- Fixed:
  + MFSA 2013-48 Memory corruption found using Address Sanitizer
  + MFSA 2013-47 Uninitialized functions in DOMSVGZoomEvent
  + MFSA 2013-46 Use-after-free with video and onresize event
  + MFSA 2013-45 Mozilla Updater fails to update some Windows Registry entries
  + MFSA 2013-44 Local privilege escalation through Mozilla Maintenance Service
  + MFSA 2013-43 File input control has access to full path
  + MFSA 2013-42 Privileged access for content level constructor
  + MFSA 2013-41 Miscellaneous memory safety hazards (rv:21.0 / rv:17.0.6)

* Wed Apr 10 2013 Alexey Gladkov <legion@altlinux.ru> 20.0-alt1
- New release (20.0).
- Fixed:
  + MFSA 2013-40 Out-of-bounds array read in CERT_DecodeCertPackage
  + MFSA 2013-39 Memory corruption while rendering grayscale PNG images
  + MFSA 2013-38 Cross-site scripting (XSS) using timed history navigations
  + MFSA 2013-37 Bypass of tab-modal dialog origin disclosure
  + MFSA 2013-36 Bypass of SOW protections allows cloning of protected nodes
  + MFSA 2013-35 WebGL crash with Mesa graphics driver on Linux
  + MFSA 2013-34 Privilege escalation through Mozilla Updater
  + MFSA 2013-33 World read and write access to app_tmp directory on Android
  + MFSA 2013-32 Privilege escalation through Mozilla Maintenance Service
  + MFSA 2013-31 Out-of-bounds write in Cairo library
  + MFSA 2013-30 Miscellaneous memory safety hazards (rv:20.0 / rv:17.0.5)

* Sat Mar 09 2013 Alexey Gladkov <legion@altlinux.ru> 19.0.2-alt1
- New release (19.0.2).
- Fixed:
  + MFSA 2013-29 Use-after-free in HTML Editor

* Thu Feb 28 2013 Alexey Gladkov <legion@altlinux.ru> 19.0.1-alt1
- New release (19.0.1).

* Thu Feb 28 2013 Alexey Gladkov <legion@altlinux.ru> 19.0-alt1
- New release (19.0).
- Fixed:
  + MFSA 2013-28 Use-after-free, out of bounds read, and buffer overflow issues found using Address Sanitizer
  + MFSA 2013-27 Phishing on HTTPS connection through malicious proxy
  + MFSA 2013-26 Use-after-free in nsImageLoadingContent
  + MFSA 2013-25 Privacy leak in JavaScript Workers
  + MFSA 2013-24 Web content bypass of COW and SOW security wrappers
  + MFSA 2013-23 Wrapped WebIDL objects can be wrapped again
  + MFSA 2013-22 Out-of-bounds read in image rendering
  + MFSA 2013-21 Miscellaneous memory safety hazards (rv:19.0 / rv:17.0.3)

* Mon Feb 04 2013 Alexey Gladkov <legion@altlinux.ru> 18.0.2-alt1
- New release (18.0.2).

* Sun Jan 27 2013 Alexey Gladkov <legion@altlinux.ru> 18.0.1-alt1
- New release (18.0.1).

* Thu Jan 10 2013 Alexey Gladkov <legion@altlinux.ru> 18.0-alt1
- New release (18.0).
- Fixed:
  + MFSA 2013-20 Mis-issued TURKTRUST certificates
  + MFSA 2013-19 Use-after-free in Javascript Proxy objects
  + MFSA 2013-18 Use-after-free in Vibrate
  + MFSA 2013-17 Use-after-free in ListenerManager
  + MFSA 2013-16 Use-after-free in serializeToStream
  + MFSA 2013-15 Privilege escalation through plugin objects
  + MFSA 2013-14 Chrome Object Wrapper (COW) bypass through changing prototype
  + MFSA 2013-13 Memory corruption in XBL with XML bindings containing SVG
  + MFSA 2013-12 Buffer overflow in Javascript string concatenation
  + MFSA 2013-11 Address space layout leaked in XBL objects
  + MFSA 2013-10 Event manipulation in plugin handler to bypass same-origin policy
  + MFSA 2013-09 Compartment mismatch with quickstubs returned values
  + MFSA 2013-08 AutoWrapperChanger fails to keep objects alive during garbage collection
  + MFSA 2013-07 Crash due to handling of SSL on threads
  + MFSA 2013-06 Touch events are shared across iframes
  + MFSA 2013-05 Use-after-free when displaying table with many columns and column groups
  + MFSA 2013-04 URL spoofing in addressbar during page loads
  + MFSA 2013-03 Buffer Overflow in Canvas
  + MFSA 2013-02 Use-after-free and buffer overflow issues found using Address Sanitizer
  + MFSA 2013-01 Miscellaneous memory safety hazards (rv:18.0/ rv:10.0.12 / rv:17.0.2)
  + MFSA 2012-98 Firefox installer DLL hijacking

* Fri Nov 30 2012 Alexey Gladkov <legion@altlinux.ru> 17.0.1-alt1
- New release (17.0.1).

* Sun Nov 18 2012 Alexey Gladkov <legion@altlinux.ru> 17.0-alt1
- New release (17.0).
- Fixed:
  + MFSA 2012-106 Use-after-free, buffer overflow, and memory corruption issues found using Address Sanitizer
  + MFSA 2012-105 Use-after-free and buffer overflow issues found using Address Sanitizer
  + MFSA 2012-104 CSS and HTML injection through Style Inspector
  + MFSA 2012-103 Frames can shadow top.location
  + MFSA 2012-102 Script entered into Developer Toolbar runs with chrome privileges
  + MFSA 2012-101 Improper character decoding in HZ-GB-2312 charset
  + MFSA 2012-100 Improper security filtering for cross-origin wrappers
  + MFSA 2012-99 XrayWrappers exposes chrome-only properties when not in chrome compartment
  + MFSA 2012-98 Firefox installer DLL hijacking
  + MFSA 2012-97 XMLHttpRequest inherits incorrect principal within sandbox
  + MFSA 2012-96 Memory corruption in str_unescape
  + MFSA 2012-95 Javascript: URLs run in privileged context on New Tab page
  + MFSA 2012-94 Crash when combining SVG text on path with CSS
  + MFSA 2012-93 evalInSanbox location context incorrectly applied
  + MFSA 2012-92 Buffer overflow while rendering GIF images
  + MFSA 2012-91 Miscellaneous memory safety hazards (rv:17.0/ rv:10.0.11)

* Thu Nov 01 2012 Alexey Gladkov <legion@altlinux.ru> 16.0.2-alt1
- New release (16.0.2).
- Fixed:
  + MFSA 2012-90 Fixes for Location object issues

* Fri Oct 19 2012 Alexey Gladkov <legion@altlinux.ru> 16.0.1-alt1
- New release (16.0.1).
- Fixed:
  + MFSA 2012-89 defaultValue security checks not applied
  + MFSA 2012-88 Miscellaneous memory safety hazards (rv:16.0.1)
  + MFSA 2012-87 Use-after-free in the IME State Manager
  + MFSA 2012-86 Heap memory corruption issues found using Address Sanitizer
  + MFSA 2012-85 Use-after-free, buffer overflow, and out of bounds read issues found using Address Sanitizer
  + MFSA 2012-84 Spoofing and script injection through location.hash
  + MFSA 2012-83 Chrome Object Wrapper (COW) does not disallow acces to privileged functions or properties
  + MFSA 2012-82 top object and location property accessible by plugins
  + MFSA 2012-81 GetProperty function can bypass security checks
  + MFSA 2012-80 Crash with invalid cast when using instanceof operator
  + MFSA 2012-79 DOS and crash with full screen and history navigation
  + MFSA 2012-78 Reader Mode pages have chrome privileges
  + MFSA 2012-77 Some DOMWindowUtils methods bypass security checks
  + MFSA 2012-76 Continued access to initial origin after setting document.domain
  + MFSA 2012-75 select element persistance allows for attacks
  + MFSA 2012-74 Miscellaneous memory safety hazards (rv:16.0/ rv:10.0.8)

* Thu Sep 06 2012 Alexey Gladkov <legion@altlinux.ru> 15.0-alt2
- Disable gstreamer for now.

* Tue Aug 28 2012 Alexey Gladkov <legion@altlinux.ru> 15.0-alt1
- New release (15.0).
- Fixed:
  + MFSA 2012-72 Web console eval capable of executing chrome-privileged code
  + MFSA 2012-71 Insecure use of __android_log_print
  + MFSA 2012-70 Location object security checks bypassed by chrome code
  + MFSA 2012-69 Incorrect site SSL certificate data display
  + MFSA 2012-68 DOMParser loads linked resources in extensions when parsing text/html
  + MFSA 2012-67 Installer will launch incorrect executable following new installation
  + MFSA 2012-66 HTTPMonitor extension allows for remote debugging without explicit activation
  + MFSA 2012-65 Out-of-bounds read in format-number in XSLT
  + MFSA 2012-64 Graphite 2 memory corruption
  + MFSA 2012-63 SVG buffer overflow and use-after-free issues
  + MFSA 2012-62 WebGL use-after-free and memory corruption
  + MFSA 2012-61 Memory corruption with bitmap format images with negative height
  + MFSA 2012-60 Escalation of privilege through about:newtab
  + MFSA 2012-59 Location object can be shadowed using Object.defineProperty
  + MFSA 2012-58 Use-after-free issues found using Address Sanitizer
  + MFSA 2012-57 Miscellaneous memory safety hazards (rv:15.0/ rv:10.0.7)

* Mon Jul 23 2012 Alexey Gladkov <legion@altlinux.ru> 14.0.1-alt1
- New release (14.0.1).
- Fixed:
  + MFSA 2012-56 Code execution through javascript: URLs
  + MFSA 2012-55 feed: URLs with an innerURI inherit security context of page
  + MFSA 2012-53 Content Security Policy 1.0 implementation errors cause data leakage
  + MFSA 2012-52 JSDependentString::undepend string conversion results in memory corruption
  + MFSA 2012-51 X-Frame-Options header ignored when duplicated
  + MFSA 2012-50 Out of bounds read in QCMS
  + MFSA 2012-49 Same-compartment Security Wrappers can be bypassed
  + MFSA 2012-48 use-after-free in nsGlobalWindow::PageHidden
  + MFSA 2012-47 Improper filtering of javascript in HTML feed-view
  + MFSA 2012-46 XSS through data: URLs
  + MFSA 2012-45 Spoofing issue with location
  + MFSA 2012-44 Gecko memory corruption
  + MFSA 2012-43 Incorrect URL displayed in addressbar through drag and drop
  + MFSA 2012-42 Miscellaneous memory safety hazards (rv:14.0/ rv:10.0.6)

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
