%def_disable bootstrap

Name: mono4
Version: 4.6.2.7
Release: alt1
Summary: Cross-platform, Open Source, .NET development framework

Group: Development/Other
License: MIT
Url: http://www.mono-project.com
Packager: Denis Medvedev <nbr@altlinux.org>

Source: mono4-%version.tar
# by running the following command:
# sn -k mono.snk
# Dec 2015 ALT
Source2: mono.snk
Source1: external.tar.gz
#Patch0: mono-4.0.0-ignore-reference-assemblies.patch
# ALT: for packaging, manually pack all external/* subpackage stuff into external.tar.gz because those are submodules and cannot be added normally to git tree without losing history.

BuildRequires(pre): rpm-build-mono4
BuildRequires(pre): gcc-c++
BuildRequires(pre): gettext-devel
BuildRequires(pre): libicu-devel
BuildRequires(pre): libgdiplus-devel >= 2.10
BuildRequires(pre): pkg-config
BuildRequires(pre): valgrind-devel
BuildRequires(pre): zlib-devel
BuildRequires(pre): python-modules-json

# http://www.mono-project.com/docs/about-mono/releases/4.0.0/#npgsql
#Obsoletes: mono-data-postgresql
# http://www.mono-project.com/docs/about-mono/releases/4.0.0/#entityframework
# Obsoletes: mono-entityframework

# Yes, mono actually depends on itself, because
# we deleted the bootstrapping binaries. If you
# need to bootstrap mono, comment out this BuildRequires
# and don't delete the binaries in %%prep.

%if_enabled bootstrap
# for bootstrap, use bundled monolite instead of local mono
%else
BuildRequires: mono4-core >= 4.0
%endif



%description
The Mono runtime implements a JIT engine for the ECMA CLI
virtual machine (as well as a byte code interpreter, the
class loader, the garbage collector, threading system and
metadata access libraries.

%package core
Summary: The Mono CIL runtime, suitable for running .NET code
Group: Development/Other
Requires: libgdiplus
Conflicts: mono < 3.0
Conflicts: mono-mscorlib  < 3.0
Conflicts: monodis < 3.0
Conflicts: libmono < 3.0

%description core
This package contains the core of the Mono runtime including its
Virtual Machine, Just-in-time compiler, C# compiler, security
tools and libraries (corlib, XML, System.Security, ZipLib,
I18N, Cairo and Mono.*).

%package winfx
Summary: Mono implementation of core WinFX APIs
Group: Development/Other
Requires: mono4-core = %version-%release

%description winfx
Open source implementation of core WinFX APIs

%package mvc
Summary: Mono implementation of ASP.NET MVC
Group: Development/Other
Requires: mono4-dyndata = %version-%release

%description mvc
This is the Mono implementation of ASP.NET MVC

%package mvc-devel
Summary: Development files for  ASP.NET MVC
Group: Development/Other
Requires: mono4-core = %version-%release

%description mvc-devel
This is the Mono implementation of ASP.NET MVC

%package dyndata
Summary: Dynamic data dll for both web and mvc
Group: Development/Other
Requires: mono4-core = %version-%release

%description dyndata
This is dll needed for implementation of ASP.NET MVC and for web services too

%package full
Summary: full runtime virtual package
Group: Development/Other
Requires: mono4-dyndata
Requires: mono4-data
Requires: mono4-mvc
Requires: mono4-extras
Requires: mono4-winfx
Requires: mono4-locale-extras
Requires: mono4-reactive
Requires: mono4-reactive-winforms
Requires: mono4-wcf
Requires: mono4-data-oracle
Requires: mono4-data-sqlite
Requires: mono4-ibm-data-db2
Requires: mono4-monodoc

%description full
Virtual package containing all non-devel packages from mono

%package devel-full
Summary: full development virtual package
Group:Development/Other
Requires: mono4-devel
Requires: mono4-reactive-devel
Requires: mono4-web-devel
Requires: mono4-mvc-devel
Requires: mono4-monodoc-devel

%description devel-full
Virtual package containing all devel packages from mono

%package devel
Summary: Development tools for Mono
Group: Development/Other
Requires: mono4-core = %version-%release
Requires: pkg-config
Requires: glib2-devel

%description devel
This package completes the Mono developer toolchain with the mono profiler,
assembler and other various tools.

%package locale-extras
Summary: Extra locale information for Mono
Group: Development/Other
Requires: mono4-core = %version-%release

%description locale-extras
This package contains assemblies to support I18N applications for
non-latin alphabets.

%package extras
Summary: Provides the infrastructure for running and building daemons and services with Mono as well as various stub assemblies
Group: Development/Other
Requires: mono4-core = %version-%release

%description extras
This package provides the library and application to run services
and daemons with Mono. It also includes stubs for the following
assemblies: Microsoft.Vsa,
System.Configuration.Install, System.Management, System.Messaging.

%package reactive
License: MIT License (or similar) ; Apache License 2.0
Summary: Reactive Extensions for Mono core libraries
Group: Development/Other
Requires: mono4-core = %version-%release

%description reactive
Reactive Extensions for Mono, this packages don't depend on
desktop-specific features.

%package reactive-winforms
License: MIT License (or similar) ; Apache License 2.0
Summary: Reactive Extensions for Mono desktop-specific libraries
Group: Development/Other
Requires: mono4-core = %version-%release
Requires: mono4-reactive = %version-%release

%description reactive-winforms
Reactive Extensions for Mono, desktop-specific packages (winforms,
windows threading).

%package reactive-devel
Summary: Development files for system.web
Group: Development/Other
Requires: mono4-core = %version-%release
Requires: mono4-reactive = %version-%release pkg-config

%description reactive-devel
This package provides the .pc file for mono4-rx

%package winforms
Summary: Windows Forms implementation for Mono
Group: Development/Other
Requires: mono4-core = %version-%release

%description winforms
This package provides a fully managed implementation of
System.Windows.Forms, the default graphical toolkit for .NET
applications.

%package wcf
Summary: Mono implementation of Windows Communication Foundation
Group: Development/Other
Requires: mono4-core = %version-%release

%description wcf
This package provides an implementation of WCF, the Windows Communication
Foundation.

%package web
Summary: ASP.NET, Remoting, and Web Services for Mono
Group: Development/Other
Requires: mono4-dyndata = %version-%release

%description web
This package provides the ASP.NET libraries and runtime for
development of web application, web services and remoting support.
%package web-devel
Summary: Development files for system.web
Group: Development/Other
Requires: mono4-core = %version-%release
Requires: mono4-web = %version-%release pkg-config

%description web-devel
This package provides the .pc file for mono4-web

%package data
Summary: Database connectivity for Mono
Group: Development/Other
Requires: mono4-core = %version-%release

%description data
This package provides a Mono assembly to facilitate data access
and manipulation with databases, LDAP compatible directory servers
and/or XML data exchange. Beyond the ADO.NET, Novell.LDAP and
System.DirectoryServices assemblies, it also includes a command
line sql application as well as the Microsoft SQL Server and ODBC
data providers.

%package data-sqlite
Summary: sqlite database connectivity for Mono
Group: Development/Other
Requires: mono4-core = %version-%release
Requires: sqlite

%description data-sqlite
This package contains the ADO.NET Data provider for the sqlite
database.

%package data-oracle
Summary: Oracle database connectivity for Mono
Group: Development/Other
Requires: mono4-core = %version-%release

%description data-oracle
This package contains the ADO.NET Data provider for the Oracle
database.

%package   ibm-data-db2
Summary: IBM DB2 database connectivity for Mono
Group: Development/Other
Requires: mono4-core = %version-%release

%description  ibm-data-db2
This package contains the ADO.NET Data provider for the IBM DB2
Universal database.

%package  monodoc
Summary: The mono4 documentation system
Group: Documentation
Requires: mono4-core = %version-%release

%description  monodoc
monodoc is the documentation package for the mono .NET environment

%package  monodoc-devel
Summary: .pc file for monodoc
Group: Documentation
Requires: mono4-monodoc = %version-%release pkg-config
Requires: mono4-core = %version-%release

%description  monodoc-devel
Development file for monodoc

%define gac_dll(dll)  %_monogacdir/%1 \
%_monodir/4.5/%1.dll \
%nil
%define gac_dll40(dll)  %_monogacdir/%1 \
%_monodir/4.0/%1.dll \
%nil
%define mono_bin(bin) %_bindir/%1 \
%_monodir/4.5/%1.exe \
%_monodir/4.5/%1.exe.* \
%nil

%prep
%setup -n mono4-%version

tar xzf /usr/src/RPM/SOURCES/external.tar.gz
#%patch0 -p1

# bash autogen.sh --prefix=%_prefix

chmod +x ./autogen.sh
%define _configure_script ./autogen.sh
%configure

# modifications for Mono 4
%__subst "s#mono/2.0#mono/4.5#g" data/mono-nunit.pc.in

# Add undeclared Arg
%__subst "61a #define ARG_MAX     _POSIX_ARG_MAX" mono/io-layer/wapi_glob.h

# Remove prebuilt binaries
#find . -name "*.dll" -not -path "./mcs/class/lib/monolite/*" -print -delete

find . -name "*.exe" -not -path "./mcs/class/lib/monolite/*" -print -delete
%if_enabled bootstrap
# for bootstrap, keep monolite. Mono 2.10 is too old to compile Mono 4.0
export PATH=$PATH:mcs/class/lib/monolite/
%else
rm -rf mcs/class/lib/monolite/*
%endif

%build
%add_optflags -fno-strict-aliasing

%configure --disable-rpath \
           --with-moonlight=no
# Profiler gives undef symbols, so it is temporarily disabled.

##__subst 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
##__subst 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
#unpack external.tgz one more time. Its contents has been overwritten
#tar xvzf /usr/src/RPM/SOURCES/external.tar.gz
%if_enabled bootstrap
# for bootstrap, keep monolite. Mono 2.10 is too old to compile Mono 4.0
export PATH=$PATH:mcs/class/lib/monolite/
%else
rm -rf mcs/class/lib/monolite/*
%endif
%makeinstall_std

# copy the mono.snk key into /etc/pki/mono
mkdir -p %buildroot%_sysconfdir/pki/mono
install -p -m0644 %SOURCE2 %buildroot%_sysconfdir/pki/mono/

# C5 is not installed, see commit 0af35dd5

# This was removed upstream:
# remove .la files (they are generally bad news)
#rm -f %buildroot%_libdir/*.la
# remove Windows-only stuff
rm -rf %buildroot%_monodir/*/Mono.Security.Win32*
rm -f %buildroot%_libdir/libMonoSupportW.*
# remove .a files for libraries that are really only for us
#rm %buildroot%_libdir/*.a
# remove libgc cruft
#rm -rf %buildroot%_datadir/libgc-mono
# remove stuff that we don't package
#rm -f %buildroot%_bindir/cilc
#rm -f %buildroot%_man1dir/cilc.1*
rm -f %buildroot%_monodir/*/browsercaps-updater.exe*
rm -f %buildroot%_monodir/*/culevel.exe*
rm -f %buildroot%_monodir/2.0/cilc.exe*

rm -f %buildroot%_monodir/*/mscorlib.dll.so
rm -f %buildroot%_monodir/*/mcs.exe.so
rm -f %buildroot%_monodir/*/gmcs.exe.so
rm -rf %buildroot%_monodir/xbuild/Microsoft
rm -f %buildroot%_monodir/4.0/dmcs.exe.so
rm -rf %buildroot%_bindir/mono-configuration-crypto
rm -rf %buildroot%_mandir/man?/mono-configuration-crypto*
#temporarily remove profiler iomap -bad symbols
rm -rf %buildroot%_libdir/libmono-profiler-iomap.so.0.0.0

# remove the mono-nunit files
rm -f %buildroot%_bindir/nunit-console
rm -f %buildroot%_bindir/nunit-console2
rm -f %buildroot%_bindir/nunit-console4
rm -f %buildroot%_monodir/4.5/nunit*
rm -Rf %buildroot%_monodir/gac/nunit*
rm -f %buildroot%_pkgconfigdir/mono-nunit.pc
#mkdir -p  %buildroot%_sysconfdir/mono-2.0/
mkdir -p  %buildroot%_sysconfdir/mono-4.5/
mkdir -p  %buildroot%_sysconfdir/mono-4.0/
mkdir -p  %buildroot%_monodir/3.5-api/
mkdir -p  %buildroot%_monodir/2.0-api/
mkdir -p  %buildroot%_monodir/4.0-api/
mkdir -p  %buildroot%_monodir/4.5-api/
%find_lang mcs


%files core -f mcs.lang
%doc  CONTRIBUTING.md LICENSE COPYING.LIB  NEWS README.md PATENTS.TXT
#%_sysconfdir/mono-2.0/
%_sysconfdir/mono-4.5/
%_sysconfdir/mono-4.0/
%dir %_sysconfdir/mono/4.5/
#%dir %_libexecdir/mono/4.0/
%dir %_monodir/4.5
%dir %_monodir/4.0
%_bindir/mono
%_bindir/mono-test-install
%_bindir/mono-gdb.py
%_bindir/mono-boehm
%_bindir/mono-service2
%_bindir/mono-sgen
%_bindir/mono-sgen-gdb.py
%mono_bin csharp
%mono_bin cert-sync
%mono_bin chktrust
%mono_bin gacutil
%mono_bin ikdasm
%mono_bin lc
%_monodir/4.5/linkeranalyzer*
%_bindir/gacutil2
%_bindir/mcs
%_monodir/4.5/mcs.exe*
%mono_bin mozroots
%mono_bin pdb2mdb
%mono_bin setreg
%mono_bin sn
%_bindir/mono-heapviz
%_bindir/mprof-report
%_man1dir/certmgr.1*
%_man1dir/chktrust.1*
%_man1dir/gacutil.1*
%_man1dir/mcs.1*
%_man1dir/mono.1*
%_man1dir/mozroots.1*
%_man1dir/setreg.1*
%_man1dir/sn.1*
%_man5dir/mono-config.5*
%_man1dir/csharp.1*
%_man1dir/pdb2mdb.1*
%_man1dir/lc.1*
%_man1dir/mprof-report.1*
%_libdir/libMonoPosixHelper.so*
%_monodir/4.0/Mono.Posix.dll
%_monodir/4.0/mscorlib.dll
%dir %_monodir
%dir %_monodir/4.0/


%dir %_monodir/gac
%gac_dll Commons.Xml.Relaxng
%gac_dll ICSharpCode.SharpZipLib
%gac_dll Mono.Debugger.Soft
%_monogacdir/Mono.Cecil
%gac_dll cscompmgd
%gac_dll Microsoft.VisualC
%gac_dll Mono.Cairo
%gac_dll Mono.CompilerServices.SymbolWriter
%gac_dll Mono.CSharp
%gac_dll System.Drawing
%gac_dll Mono.Management
%gac_dll Mono.Posix
%gac_dll Mono.Security
%gac_dll Mono.Simd
%gac_dll System
%gac_dll System.Configuration
%gac_dll System.Core
%gac_dll System.Security
%gac_dll System.Xml
%gac_dll System.Deployment
%gac_dll System.Reflection.Context
%gac_dll System.Runtime.InteropServices.RuntimeInformation
%gac_dll Mono.Tasklets
%gac_dll System.Net
%gac_dll System.Xml.Linq
%gac_dll SMDiagnostics
%gac_dll Mono.Security.Providers.DotNet
%gac_dll Mono.Security.Providers.NewSystemSource
%gac_dll Mono.Security.Providers.OldTls
%gac_dll Mono.Security.Providers.NewTls
%dir %_sysconfdir/mono
%dir %_sysconfdir/mono/mconfig
%config (noreplace) %_sysconfdir/mono/config
#%config (noreplace) %_sysconfdir/mono/2.0/machine.config
#%config (noreplace) %_sysconfdir/mono/2.0/settings.map
#%_libdir/libmono*-2.0.so.*
%config (noreplace) %_sysconfdir/mono/4.5/settings.map
%config (noreplace) %_sysconfdir/mono/4.0/DefaultWsdlHelpGenerator.aspx
%config (noreplace) %_sysconfdir/mono/4.5/DefaultWsdlHelpGenerator.aspx
%config (noreplace) %_sysconfdir/mono/4.5/machine.config
%config (noreplace) %_sysconfdir/mono/4.5/web.config
%config (noreplace) %_sysconfdir/mono/4.0/machine.config
%config (noreplace) %_sysconfdir/mono/4.0/web.config
%config (noreplace) %_sysconfdir/mono/4.0/settings.map
%dir %_sysconfdir/mono/4.0
#%dir %_sysconfdir/mono/2.0
%_bindir/dmcs
%mono_bin ccrewrite
%_man1dir/ccrewrite.1*
%dir %_monodir/4.5/Facades

%_monodir/4.5/mscorlib.dll
%_monodir/4.5/mscorlib.dll.mdb
%gac_dll Microsoft.CSharp
%gac_dll System.Dynamic
%gac_dll System.ComponentModel.Composition
%gac_dll System.Numerics
%gac_dll System.Runtime.Caching
%gac_dll System.Runtime.DurableInstancing
%gac_dll System.Xaml
%gac_dll Mono.CodeContracts

%dir %_monodir/mono-configuration-crypto/
%dir %_monodir/mono-configuration-crypto/4.5/
#%_monodir/2.0/*
#%_monodir/4.0/*
%_monodir/mono-configuration-crypto/4.5/*
%gac_dll CustomMarshalers
%gac_dll I18N.West
%gac_dll I18N
%gac_dll System.Json
%gac_dll Mono.Parallel
%gac_dll System.Json.Microsoft
%_monodir/4.5/Facades/*.dll
%gac_dll System.IO.Compression
%gac_dll System.IO.Compression.FileSystem
%gac_dll System.Net.Http
%gac_dll System.Net.Http.WebRequest
%gac_dll System.Threading.Tasks.Dataflow
%gac_dll System.Numerics.Vectors
%gac_dll System.ServiceModel.Internals
%exclude %_monodir/4.5/System.Runtime.Caching.dll
%exclude %_monodir/4.5/System.Xaml.dll
%exclude %_monogacdir/System.Runtime.Caching/*
%exclude %_monogacdir/System.Xaml/*
%exclude %_sysconfdir/mono/4.0/Browsers/Compat.browser

%files dyndata
%gac_dll System.Web.DynamicData

%files full

%files devel-full


%files devel
%_sysconfdir/pki/mono/
%_bindir/mono-api-info
%_monodir/4.5/mono-api-info.exe
%_monodir/4.5/mono-symbolicate.exe
%_monodir/4.5/mono-symbolicate.exe.mdb
%_monodir/2.0-api/*
%_monodir/4.0-api/*
%_monodir/4.5-api/*
%_monodir/3.5-api/*
%_bindir/mono-symbolicate
%mono_bin xbuild
%_monodir/4.5/xbuild.rsp
%mono_bin genxs
%_monodir/4.5/ictool*
%_monodir/4.5/mod*
%mono_bin al
%_bindir/al2
%mono_bin caspol
%mono_bin cert2spc
%mono_bin certmgr
%mono_bin dtd2rng
%mono_bin dtd2xsd
%mono_bin ilasm
%mono_bin installvst
%_monodir/4.5/installutil*
%mono_bin macpack
%mono_bin mkbundle
%mono_bin makecert
%mono_bin mono-cil-strip
%_bindir/mono-find-provides
%_bindir/mono-find-requires
%_bindir/monodis
%mono_bin monolinker
%mono_bin mono-shlib-cop
%mono_bin mono-xmltool
%mono_bin monop
%_bindir/monop2
%mono_bin permview
%_bindir/peverify
%_bindir/prj2make
%mono_bin resgen
%_bindir/resgen2
%mono_bin sgen
%mono_bin secutil
%mono_bin signcode
%mono_bin cccheck
%mono_bin crlupdate
%mono_bin mdbrebase
%_libexecdir/mono-source-libs/
%_bindir/pedump
%_man1dir/resgen.1*
%_man1dir/al.1*
%_man1dir/cert2spc.1*
%_man1dir/dtd2xsd.1*
%_man1dir/genxs.1*
%_man1dir/ilasm.1*
%_man1dir/macpack.1*
%_man1dir/makecert.1*
%_man1dir/mkbundle.1*
%_man1dir/mono-cil-strip.1*
%_man1dir/monodis.1*
%_datadir/mono-2.0/mono/cil/cil-opcodes.xml
%_man1dir/monolinker.1*
%_man1dir/mono-shlib-cop.1*
%_man1dir/mono-xmltool.1*
%_man1dir/monop.1*
%_man1dir/permview.1*
%_man1dir/prj2make.1*
%_man1dir/secutil.1*
%_man1dir/sgen.1*
%_man1dir/signcode.1*
%_man1dir/xbuild.1*
%_man1dir/mono-api-info.1*
%_man1dir/cccheck.1*
%_man1dir/crlupdate.1*
%gac_dll PEAPI
%gac_dll Microsoft.Build
%gac_dll Microsoft.Build.Engine
%gac_dll Microsoft.Build.Framework
%_monogacdir/Microsoft.Build.Tasks.Core
%gac_dll Microsoft.Build.Tasks.v4.0
%gac_dll Microsoft.Build.Utilities.v4.0
%_monogacdir/Microsoft.Build.Utilities.Core
%_monogacdir/Microsoft.Build.Tasks.v12.0
%_monogacdir/Microsoft.Build.Utilities.v12.0
%gac_dll Mono.XBuild.Tasks
%gac_dll System.Windows
%gac_dll System.Xml.Serialization
%_monodir/4.5/Microsoft.Common.tasks
%_monodir/4.5/MSBuild/Microsoft.Build*
%_monodir/4.5/Microsoft.Build.xsd
%_monodir/4.5/Microsoft.CSharp.targets
%_monodir/4.5/Microsoft.Common.targets
%_monodir/4.5/Microsoft.VisualBasic.targets
%_monodir/xbuild/
%_monodir/xbuild-frameworks/
%_libdir/libikvm-native.so
# disabled profiler right now
#%_libdir/libmono-profiler-*.so
%_libdir/libmono*-2.0.so
%_libdir/libmonosgen*
%_libdir/libmonoboehm*
%_pkgconfigdir/dotnet.pc
%_pkgconfigdir/mono-cairo.pc
%_pkgconfigdir/mono.pc
#%_pkgconfigdir/mono-2.pc
%_pkgconfigdir/monosgen-2.pc
%_pkgconfigdir/cecil.pc
%_pkgconfigdir/dotnet35.pc
%_pkgconfigdir/mono-lineeditor.pc
%_pkgconfigdir/mono-options.pc
%_pkgconfigdir/wcf.pc
%_pkgconfigdir/xbuild12.pc
%_includedir/mono-2.0/mono/jit/jit.h
%_includedir/mono-2.0/mono/metadata/*.h
%_includedir/mono-2.0/mono/utils/*.h
%_includedir/mono-2.0/mono/cil/opcode.def

%files locale-extras
%gac_dll I18N.CJK
%gac_dll I18N.MidEast
%gac_dll I18N.Other
%gac_dll I18N.Rare

%files extras
%mono_bin mono-service
%_monogacdir/mono-service
%gac_dll System.Configuration.Install
%gac_dll System.Management
%gac_dll System.Messaging
%gac_dll System.ServiceProcess
%gac_dll System.Runtime.Caching
%gac_dll System.Xaml
%gac_dll Mono.Messaging.RabbitMQ
%gac_dll Mono.Messaging
%gac_dll RabbitMQ.Client
%_monodir/4.5/RabbitMQ.Client.Apigen*
%_man1dir/mono-service.1*

%files reactive
%gac_dll System.Reactive.Core
%gac_dll System.Reactive.Debugger
%gac_dll System.Reactive.Experimental
%gac_dll System.Reactive.Interfaces
%gac_dll System.Reactive.Linq
%gac_dll System.Reactive.Observable.Aliases
%gac_dll System.Reactive.PlatformServices
%gac_dll System.Reactive.Providers
%gac_dll System.Reactive.Runtime.Remoting

%files reactive-winforms
%gac_dll System.Reactive.Windows.Forms
%gac_dll System.Reactive.Windows.Threading

%files reactive-devel
%_pkgconfigdir/reactive.pc

%files wcf
%gac_dll System.IdentityModel
%gac_dll System.IdentityModel.Selectors
%gac_dll System.ServiceModel
%gac_dll System.ServiceModel.Activation
%gac_dll System.ServiceModel.Discovery
%gac_dll System.ServiceModel.Routing
%gac_dll System.ServiceModel.Web

%files web
%mono_bin disco
%mono_bin httpcfg
%mono_bin mconfig
%mono_bin soapsuds
%mono_bin svcutil
%mono_bin wsdl
%_bindir/wsdl2
%mono_bin xsd
%mono_bin mono-api-html
%mono_bin mono-api-info
%gac_dll Microsoft.Web.Infrastructure
%gac_dll Mono.Http
%gac_dll System.ComponentModel.DataAnnotations
%gac_dll System.Net.Http.Formatting
%gac_dll System.Runtime.Remoting
%gac_dll System.Runtime.Serialization.Formatters.Soap
%gac_dll System.Web
%gac_dll System.Web.Abstractions
%gac_dll System.Web.Routing
%gac_dll System.Web.Services
%gac_dll System.Web.ApplicationServices
%gac_dll System.Web.Http
%gac_dll System.Web.Http.SelfHost
%gac_dll System.Web.Http.WebHost
%gac_dll System.Web.Razor
%gac_dll System.Web.WebPages
%gac_dll System.Web.WebPages.Deployment
%gac_dll System.Web.WebPages.Razor
%gac_dll System.Web.Mobile
%gac_dll System.Web.RegularExpressions
%gac_dll System.Workflow.Activities
%gac_dll System.Workflow.ComponentModel
%gac_dll System.Workflow.Runtime

%_man1dir/disco.1*
%_man1dir/httpcfg.1*
%_man1dir/mconfig.1*
%_man1dir/soapsuds.1*
%_man1dir/wsdl.1*
%_man1dir/xsd.1*
%config (noreplace) %_sysconfdir/mono/browscap.ini
%config (noreplace) %_sysconfdir/mono/2.0/Browsers/Compat.browser
%config (noreplace) %_sysconfdir/mono/4.0/Browsers/Compat.browser
%config (noreplace) %_sysconfdir/mono/4.5/Browsers/Compat.browser
%config (noreplace) %_sysconfdir/mono/2.0/DefaultWsdlHelpGenerator.aspx
%config (noreplace) %_sysconfdir/mono/mconfig/config.xml
#%config (noreplace) %_sysconfdir/mono/2.0/web.config

%files web-devel
%_pkgconfigdir/aspnetwebstack.pc

%files winforms
%gac_dll Accessibility
%gac_dll Mono.WebBrowser
%gac_dll System.Design
%gac_dll System.Drawing.Design
%gac_dll System.Windows.Forms
%gac_dll System.Windows.Forms.DataVisualization

%files mvc
%gac_dll System.Web.Extensions
%gac_dll System.Web.Extensions.Design
%gac_dll System.Web.Mvc

%files mvc-devel
%_pkgconfigdir/system.web.extensions.design_1.0.pc
%_pkgconfigdir/system.web.extensions_1.0.pc
%_pkgconfigdir/system.web.mvc.pc
%_pkgconfigdir/system.web.mvc2.pc
%_pkgconfigdir/system.web.mvc3.pc

%files winfx
%gac_dll WindowsBase

%files data
%mono_bin sqlsharp
%mono_bin sqlmetal
%gac_dll System.Data
%gac_dll System.Data.DataSetExtensions
%gac_dll System.Data.Entity
%gac_dll System.Data.Linq
%gac_dll System.Data.Services
%gac_dll System.Data.Services.Client
%gac_dll System.DirectoryServices
%gac_dll System.DirectoryServices.Protocols
%gac_dll System.EnterpriseServices
%gac_dll System.Runtime.Serialization
%gac_dll System.Transactions
%gac_dll Mono.Data.Tds
%gac_dll Novell.Directory.Ldap
%gac_dll WebMatrix.Data
%_man1dir/sqlsharp.1*

%files data-sqlite
%gac_dll Mono.Data.Sqlite

%files data-oracle
%gac_dll System.Data.OracleClient

%files  ibm-data-db2
%gac_dll IBM.Data.DB2

%files  monodoc
%_monogacdir/monodoc
%_monodir/monodoc/*
%ifnarch  ppc
%_libexecdir/monodoc
%endif
%mono_bin mdoc
%_bindir/mod
%_bindir/mdoc-*
%_bindir/mdass*
%_bindir/mdval*
%_bindir/monodoc*
%_man1dir/monodocer.1*
%_man5dir/mdoc.5*
%_man1dir/mdoc-*
%_man1dir/mdoc*
%_man1dir/mdassembler*
%_man1dir/monodocs2html.1*
%_man1dir/mdvalidater.1*
%_man1dir/mono-symbolicate.1*


%files  monodoc-devel
%_pkgconfigdir/monodoc.pc

%changelog
* Thu Oct 06 2016 Denis Medvedev <nbr@altlinux.org> 4.6.2.7-alt1
- new version.

* Sun Jul 17 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt9
- Moved library libMonoPosixHelper to arch-depended dir (fixes #32246).

* Sun Jan 24 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt8
- Removing remains of mono2

* Tue Jan 19 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt7
- rpm-build-mono4 integration

* Mon Jan 18 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt6
- Added missing mono4-data to mono4-full

* Fri Jan 15 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt4
- Fixed dependence on mono4-full

* Thu Jan 14 2016 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt3
- Virtual packages mono4-full and mono4-devel added

* Sun Dec 27 2015 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt2
- Self compile

* Mon Dec 07 2015 Denis Medvedev <nbr@altlinux.org> 4.3.1.1-alt1
- Initial build of 4.* version (based on Fedora core spec)


:
