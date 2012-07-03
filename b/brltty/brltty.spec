%def_with at_spi2
%def_without at_spi1
%def_without tcl
%global with_ocaml 0
BuildRequires: gcc-c++ libbluez-devel libalsa-devel libgpm-devel
# required for %%_jnidir macros
BuildRequires(pre): rpm-build-java rpm-build-python
%define pkg_version 4.3
%define api_version 0.5.6

%if_with tcl
%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %define tcl_sitearch %{_prefix}/%{_lib}/tcl%{tcl_version}}
%endif

%define _exec_prefix %{nil}

%define _jnidir        %{_prefix}/%{_lib}/java

# with speech dispatcher
%define with_speech_dispatcher 1

Name: brltty
Version: %{pkg_version}
Release: alt3
License: GPLv2+
Group: System/Servers
URL: http://mielke.cc/brltty/
Source: http://mielke.cc/brltty/releases/%{name}-%{version}.tar.gz
Source2: ru_brltty.tar
Patch0: brltty-cppflags.patch
Patch1: brltty-autoconf-quote.patch
#Patch2: brltty-4.2-S_ISCHR.patch
Patch3: brltty-parallel.patch
Summary: Braille display driver for Linux/Unix
BuildRequires: byacc glibc-kernheaders
BuildRequires: autoconf
# work around a bug in the install process:
Requires(post): coreutils
Source44: import.info

%description
BRLTTY is a background process (daemon) which provides
access to the Linux/Unix console (when in text mode)
for a blind person using a refreshable braille display.
It drives the braille display and provides complete
screen review functionality.
%if %{with_speech_dispatcher}
BRLTTY can also work with speech synthesizers; if you want to use it with
Speech Dispatcher, please install also package %{name}-speech-dispatcher.

%package speech-dispatcher
Summary: Speech Dispatcher driver for BRLTTY
Group: System/Servers
License: GPLv2+
BuildRequires: libspeechd-devel
Requires: %{name} = %{pkg_version}-%{release}
%description speech-dispatcher
This package provides the Speech Dispatcher driver for BRLTTY.
%endif

%package xw
Summary: XWindow driver for BRLTTY
Group: System/Servers
License: GPLv2+
BuildRequires: libSM-devel libICE-devel libX11-devel libXaw-devel libXext-devel libXt-devel libXtst-devel
Requires: %{name} = %{pkg_version}-%{release}
%description xw
This package provides the XWindow driver for BRLTTY.

%if_with at_spi1
%package at-spi
Summary: AtSpi driver for BRLTTY
Group: System/Servers
# The data files are licensed under LGPLv2+, see the README file.
License: GPLv2+ and LGPLv2+
BuildRequires: libat-spi-devel
Requires: %{name} = %{pkg_version}-%{release}
%description at-spi
This package provides the AtSpi driver for BRLTTY.
%endif

%if_with at_spi2
%package at-spi2
Summary: AtSpi2 driver for BRLTTY
Group: System/Servers
# The data files are licensed under LGPLv2+, see the README file.
License: GPLv2+ and LGPLv2+
BuildRequires: libat-spi2-core-devel
Requires: %{name} = %{pkg_version}-%{release}
%description at-spi2
This package provides the AtSpi2 driver for BRLTTY.
%endif

%package -n brlapi
Version: %{api_version}
Group: File tools
License: LGPLv2+
Summary: Application Programming Interface for BRLTTY
Requires: %{name} = %{pkg_version}-%{release}
%description -n brlapi
This package provides the run-time support for the Application
Programming Interface to BRLTTY.

Install this package if you have an application which directly accesses
a refreshable braille display.

%package -n brlapi-devel
Version: %{api_version}
Group: Development/C
License: LGPLv2+
Requires: brlapi = %{api_version}-%{release}
Summary: Headers, static archive, and documentation for BrlAPI

%description -n brlapi-devel
This package provides the header files, static archive, shared object
linker reference, and reference documentation for BrlAPI (the
Application Programming Interface to BRLTTY).  It enables the
implementation of applications which take direct advantage of a
refreshable braille display in order to present information in ways
which are more appropriate for blind users and/or to provide user
interfaces which are more specifically attuned to their needs.

Install this package if you are developing or maintaining an application
which directly accesses a refreshable braille display.

%package -n tcl-brlapi
Version: %{api_version}
Group: Development/Tcl
License: LGPLv2+
Requires: brlapi = %{api_version}-%{release}
BuildRequires: tcl-devel
Summary: Tcl binding for BrlAPI
%description -n tcl-brlapi
This package provides the Tcl binding for BrlAPI.

%package -n python-module-brlapi
Version: %{api_version}
Group: Development/Python
License: LGPLv2+
Requires: brlapi = %{api_version}-%{release}
BuildRequires: python-module-Pyrex
Summary: Python binding for BrlAPI
%description -n python-module-brlapi
This package provides the Python binding for BrlAPI.

%package -n brlapi-java
Version: %{api_version}
Group: Development/Java
License: LGPLv2+
Requires: brlapi = %{api_version}-%{release}
## temporary work around, java-devel is not resolved consistently across archs
#BuildRequires: jpackage-utils
BuildRequires: java-devel
#BuildRequires: java-1.5.0-gcj-devel
Summary: Java binding for BrlAPI
%description -n brlapi-java
This package provides the Java binding for BrlAPI.

%if 0%{?with_ocaml}
%package -n ocaml-brlapi
Version: %{api_version}
Group: Development/Other
License: LGPLv2+
Requires: brlapi = %{api_version}-%{release}
BuildRequires: ocaml
BuildRequires: findlib
Summary: OCaml binding for BrlAPI
%description -n ocaml-brlapi
This package provides the OCaml binding for BrlAPI.
%endif


%define version %{pkg_version}

%prep
%setup -q
%patch0 -p1 -b .cppflags
%patch1 -p1 -b .quote
#%%patch2 -p1 -b .S_ISCHR
%patch3 -p1 -b .parallel

%build
# Patch6 changes aclocal.m4:
autoconf
for i in -I/usr/lib/jvm/java/include{,/linux}; do
      java_inc="$java_inc $i"
done
# there is no curses packages in BuildRequires, so the package builds
# without them in mock; let's express this decision explicitly
%configure CPPFLAGS="$java_inc" --disable-stripping --without-curses \
	--libdir=/%{_lib} \
%if %{with_speech_dispatcher}
  --with-speechd=%{_prefix} \
%endif
  --with-install-root="${RPM_BUILD_ROOT}"
make %{?_smp_mflags}

find . \( -path ./doc -o -path ./Documents \) -prune -o \
  \( -name 'README*' -o -name '*.txt' -o -name '*.html' -o \
     -name '*.sgml' -o -name '*.patch' -o \
     \( -path './Bootdisks/*' -type f -perm +ugo=x \) \) -print |
while read file; do
   mkdir -p doc/${file%/*} && cp -rp $file doc/$file || exit 1
done

find . -name '*.sgml' |
while read file; do
   iconv -f iso8859-1 -t utf-8 $file > $file.conv && mv -f $file.conv $file
done
find . -name '*.txt' |
while read file; do
   iconv -f iso8859-1 -t utf-8 $file > $file.conv && mv -f $file.conv $file
done
find . -name 'README*' |
while read file; do
   iconv -f iso8859-1 -t utf-8 $file > $file.conv && mv -f $file.conv $file
done

%install
# does not seem to be parallel safe
make JAVA_JNI_DIR=%_jnidir install
#ln -s ../../%{_lib}/libbrlapi.so.0.5 "$RPM_BUILD_ROOT%{_prefix}/%{_lib}/libbrlapi.so"
install -d -m 755 "${RPM_BUILD_ROOT}%{_sysconfdir}" "$RPM_BUILD_ROOT%{_mandir}/man5"
install -m 644 Documents/brltty.conf "${RPM_BUILD_ROOT}%{_sysconfdir}"
echo ".so man1/brltty.1" > $RPM_BUILD_ROOT%{_mandir}/man5/brltty.conf.5

%if %{_lib} == "lib64"
	#Manually place java plugin on 64-bit arches
	mkdir -p $RPM_BUILD_ROOT%{_prefix}/%{_lib}/java/
	install -m 755 Bindings/Java/libbrlapi_java.so "$RPM_BUILD_ROOT%{_prefix}/%{_lib}/java/"
%endif

# clean up the manuals:
rm Documents/Manual-*/*/{*.mk,*.made,Makefile*}
mv Documents/BrlAPIref/{html,BrlAPIref}

# Don't want static lib
rm -rf $RPM_BUILD_ROOT/%{_lib}/libbrlapi.a

mkdir -p %buildroot/lib/udev/devices/vcc
touch %buildroot/lib/udev/devices/vcsa
touch %buildroot/lib/udev/devices/vcsa0
touch %buildroot/lib/udev/devices/vcc/a

%__subst s/'#text-table.ru'/'text-table ru'/ %buildroot/etc/brltty.conf 
%__cp %SOURCE2 ru_brltty.tar
tar xf ru_brltty.tar
%__cp ru_brltty/* %buildroot%_sysconfdir/brltty/

%files
%attr(0660, root, tty) %dev(c, 7, 128) /lib/udev/devices/vcsa
%attr(0660, root, tty) %dev(c, 7, 128) /lib/udev/devices/vcsa0
%attr(0660, root, tty) %dev(c, 7, 128) /lib/udev/devices/vcc/a

%config(noreplace) %{_sysconfdir}/brltty.conf
%{_sysconfdir}/brltty/
%{_bindir}/brltty
%{_bindir}/brltty-*
/%{_lib}/brltty/
%exclude //%{_lib}/brltty/libbrlttybba.so
%exclude //%{_lib}/brltty/libbrlttybxw.so
%if %{with_speech_dispatcher}
%exclude /%{_lib}/brltty/libbrlttyssd.so
%endif
%if_with at_spi1
%exclude /%{_lib}/brltty/libbrlttyxas.so
%endif
%if_with at_spi2
%exclude /%{_lib}/brltty/libbrlttyxa2.so
%endif
%doc LICENSE-GPL LICENSE-LGPL
%doc Documents/ChangeLog Documents/TODO
%doc Documents/Manual-BRLTTY/
%doc doc/*
%doc %{_mandir}/man[15]/brltty.*

%if %{with_speech_dispatcher}
%files speech-dispatcher
%doc Drivers/Speech/SpeechDispatcher/README
/%{_lib}/brltty/libbrlttyssd.so
%endif

%files xw
%doc Drivers/Braille/XWindow/README
/%{_lib}/brltty/libbrlttybxw.so

%if_with at_spi1
%files at-spi
/%{_lib}/brltty/libbrlttyxas.so
%endif

%if_with at_spi2
%files at-spi2
/%{_lib}/brltty/libbrlttyxa2.so
%endif

%files -n brlapi
%{_bindir}/vstp
%{_bindir}/xbrlapi
/%{_lib}/brltty/libbrlttybba.so
/%{_lib}/libbrlapi.so.*
%doc Drivers/Braille/XWindow/README
%doc Documents/Manual-BrlAPI/
%doc %{_mandir}/man1/xbrlapi.*
%doc %{_mandir}/man1/vstp.*

%files -n brlapi-devel
#%{_prefix}/%{_lib}/libbrlapi.so
/%{_lib}/libbrlapi.so
%{_includedir}/brltty
%{_includedir}/brlapi*.h
%doc %{_mandir}/man3/brlapi_*.3*
%doc Documents/BrlAPIref/BrlAPIref/

%if_with tcl
%files -n tcl-brlapi
%{tcl_sitearch}/brlapi-%{api_version}
%endif

%files -n python-module-brlapi
%{python_sitelibdir}/brlapi.so
%{python_sitelibdir}/Brlapi-%{api_version}-py%{__python_version}.egg-info

%files -n brlapi-java
%{_jnidir}/libbrlapi_java.so
%{_javadir}/brlapi.jar

%if 0%{?with_ocaml}
%files -n ocaml-brlapi
%defattr(-,root,root)
%{_prefix}/%{_lib}/ocaml/brlapi/
#%{_prefix}/%{_lib}/ocaml/stublibs/
%endif

%changelog
* Mon Apr 09 2012 Igor Vlasenko <viy@altlinux.ru> 4.3-alt3
- build with speech-dispatcher

* Sun Apr 08 2012 Igor Vlasenko <viy@altlinux.ru> 4.3-alt2
- build with at-spi2 instead of at-spi1

* Sun Apr 08 2012 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1
- new version

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 4.2-alt3
- fixed build (use system %%_jnidir)

* Thu Jan 12 2012 Michael Pozhidaev <msp@altlinux.ru> 4.2-alt2
- Added tables for Russian language

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.2-alt1_4.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1_4
- initial release by fcimport
- build w/o tcl bindings
