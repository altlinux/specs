# TODO:
# * Implement parts of Mono Debian Policy
# * split into smaller packages
# * make *.config files for unsafe assemblies
# * use system libgc
# * AOT ?

# may use --with-gc=boehm,included,none
#define libgc boehm
%define libgc included

Name: mono
Version: 2.10.8
Release: alt1
License: %gpllgpl2only %mit %mpl
Url: http://www.mono-project.com/
Group: Development/Other
Packager: Mono Maintainers Team <mono@packages.altlinux.org>

Summary: The mono CIL runtime, suitable for running .NET code

Source: http://www.go-mono.com/sources/%name/%name-%version.tar
Source13: System.Windows.Forms.dll.config
Source14: System.Data.dll.config

Patch1: %name-%version-alt-cecil-install.patch
Patch2: %name-%version-alt-dllmap.patch
Patch3: %name-%version-alt-manpages.patch
Patch4: %name-%version-alt-monodoc-sourcesdir.patch
#Patch5: %name-%version-rh-BigInteger-CVE-2007-5197.patch.patch
Patch6: %name-%version-fix-link.patch

BuildPreReq: rpm-build-mono >= 1.2
BuildPreReq: rpm-build-licenses

%if %libgc == boehm
BuildPreReq: libgc-devel
%endif

# Automatically added by buildreq on Sun Dec 20 2009
BuildRequires: gcc-c++ glib2-devel imake libX11-devel libattr-devel libncurses-devel xorg-cf-files zlib-devel

BuildRequires: libgdiplus-devel >= 2.10
# BuildRequires: libgluezilla

# Yes, mono actually depends on itself, because
# we deleted the bootstrapping binaries. If you
# need to bootstrap mono, comment out this BuildRequires
# and don't delete the binaries in %%prep.
BuildRequires: mono-mcs

Requires: /proc
BuildPreReq: /proc

Obsoletes: mono-ikvm < %version
Provides: mono-ikvm = %version
Provides: mono-core = %version

Obsoletes: mono-jscript < 2.8
Obsoletes: mono-jay < 2.8

Requires: libmono = %version-%release
Requires: %name-mscorlib = %version-%release

%description
This package contains the core of the Mono runtime including its
Virtual Machine, Just-in-time compiler, security tools and libraries
(corlib, XML, System.Security, System.Drawing, ZipLib, I18N, Cairo 
and Mono.*).

%files
%dir %_sysconfdir/mono
%dir %_sysconfdir/mono/2.0
%dir %_sysconfdir/mono/4.0
%config(noreplace) %_sysconfdir/mono/*/machine.config
%config(noreplace) %_sysconfdir/mono/*/settings.map
%config(noreplace) %_sysconfdir/mono/config
%_bindir/mono
%_bindir/mono-test-install
%_bindir/certmgr
%_bindir/chktrust
%_bindir/gacutil
%_bindir/gacutil2
%_bindir/mozroots
%_bindir/setreg
%_bindir/sn
%_libdir/libikvm-native.so
%_libdir/libMonoPosixHelper.so
%_libdir/libMonoSupportW.so
%dir %_monodir/compat-*
%dir %_monodir/gac
%_monodir/*/certmgr.exe*
%_monodir/*/chktrust.exe*
%_monodir/*/gacutil.exe*
%_monodir/*/mozroots.exe*
%_monodir/*/setreg.exe*
%_monodir/*/sn.exe*
%_monodir/*/Mono.C5
%_monodir/*/Mono.C5.dll*
%_monodir/*/Mono.Posix
%_monodir/*/Mono.Posix.dll*
%_monodir/*/Mono.Cairo
%_monodir/*/Mono.Cairo.dll*
%_monodir/*/ICSharpCode.SharpZipLib
%_monodir/*/ICSharpCode.SharpZipLib.dll*
%_monodir/*/Microsoft.VisualC
%_monodir/*/Microsoft.VisualC.dll*
%_monodir/*/Commons.Xml.Relaxng
%_monodir/*/Commons.Xml.Relaxng.dll*
%_monodir/*/CustomMarshalers
%_monodir/*/CustomMarshalers.dll*
%_monodir/*/I18N
%_monodir/*/I18N.dll*
%_monodir/*/I18N.MidEast
%_monodir/*/I18N.MidEast.dll*
%_monodir/*/I18N.Other
%_monodir/*/I18N.Other.dll*
%_monodir/*/I18N.Rare
%_monodir/*/I18N.Rare.dll*
%_monodir/*/I18N.West
%_monodir/*/I18N.West.dll*
%_monodir/*/Mono.Security
%_monodir/*/Mono.Security.dll*
%_monodir/*/OpenSystem.C
%_monodir/*/OpenSystem.C.dll
%_monodir/*/System
%_monodir/*/System.dll*
%_monodir/*/System.Core
%_monodir/*/System.Core.dll*
%_monodir/*/System.Drawing
%_monodir/*/System.Drawing.dll*
%_monodir/*/Mono.Simd
%_monodir/*/Mono.Simd.dll*
%_monodir/*/Mono.Management
%_monodir/*/Mono.Management.dll*
%_monodir/*/System.Security
%_monodir/*/System.Security.dll*
%_monodir/*/System.Configuration
%_monodir/*/System.Configuration.dll*
%_monodir/*/System.Transactions
%_monodir/*/System.Transactions.dll*
%_monodir/*/System.Net
%_monodir/*/System.Net.dll*
%_monodir/*/System.Xml
%_monodir/*/System.Xml.dll*
%_monodir/*/System.Xml.Linq
%_monodir/*/System.Xml.Linq.dll*
%_monodir/*/cscompmgd
%_monodir/*/cscompmgd.dll*
%_monodir/*/mscorlib.dll.*
%_monodir/*/Mono.Tasklets
%_monodir/*/Mono.Tasklets.dll*
%_monodir/*/System.Dynamic
%_monodir/*/System.Dynamic.dll*
%_monodir/*/System.Numerics
%_monodir/*/System.Numerics.dll*

%_man1dir/mono.*
%_man1dir/certmgr.*
%_man1dir/chktrust.*
%_man1dir/setreg.*
%_man1dir/gacutil.*
%_man1dir/sn.*
%_man5dir/mono-config.*
%_man1dir/mozroots.*
%doc AUTHORS COPYING.LIB ChangeLog NEWS README
%exclude %_monodir/*/Mono.Security.Win32*

%package configuration-crypto
Summary: Mono utility classes to encrypt/decrypt configuration file sections
Group: Development/Other
Provides: mono(Mono.Configuration.Crypto) = 4.0.0.0

%description configuration-crypto
Utility classes to encrypt/decrypt configuration file sections
Classes in this namespace provide tools for manipulation of Mono key store (both local and global) as well
as encryption/decryption of configuration file sections.

%files configuration-crypto
%_bindir/mono-configuration-crypto
%dir %_monodir/mono-configuration-crypto
%_monodir/mono-configuration-crypto/*
%_man1dir/mono-configuration-crypto.*

%package mscorlib
Summary: Multilanguage Standard Common Object Runtime Library
Group: Development/Other
Conflicts: libmono < %version-%release

%description mscorlib
This pacakge provides Multilanguage Standard Common Object Runtime
Library (mscorlib.dll) for Mono/.Net framework.

%files mscorlib
%dir %_monodir
%dir %_monodir/2.0
%dir %_monodir/4.0
%_monodir/2.0/mscorlib.dll
%_monodir/4.0/mscorlib.dll

%package -n libmono
Summary: libmono-2.0.so.1 shared library
Group: System/Libraries
Conflicts: %name < %version-%release
# due to mini_init()
Requires: /proc
# due to mono_init_internal()
Requires: %name-mscorlib = %version-%release

%description -n libmono
This package contains libmono-2.0.so.1 shared library.

%files -n libmono
%_libdir/libmono-2.0.so.1*

%package -n libmono-devel
Summary: Header files for libmono.so.0 shared library
Group: Development/C
Requires: libmono = %version-%release
Requires: pkgconfig(glib-2.0) pkgconfig(gthread-2.0)
Requires: /usr/include/glib-2.0

%description -n libmono-devel
This package contains header files for libmono.so.0 shared library.

%files -n libmono-devel
%_includedir/mono-2.0
%_libdir/libmono-2.0.so
%_pkgconfigdir/mono-2.pc

%package -n monodis
Summary: CIL image content dumper and disassembler
Group: Development/Other
Requires: libmono = %version-%release

%description -n monodis
The monodis program is used to dump the contents a CIL image (contained
in .EXE files that contain extended PE/COFF CIL code).

%files -n monodis
%_bindir/monodis
%_man1dir/monodis.*

%package mcs
Summary: C# language compiler for Mono
Group: Development/Other
License: %gpl2only %mit
Requires: %name = %version-%release
# using mono compiler should automatically enable support for mono dependencies
Requires: rpm-build-mono
Provides: mcs = %version
Obsoletes: mcs < %version
# workaround for mono-csharp
Provides: mono(dmcs) = %version
Provides: mono(dmcs) = %version.0

%description mcs
This package contains the C# .NET compiler. This allows you to compile C#
.NET application and assemblies.

%files mcs -f mcs.lang
%_bindir/mcs
%_bindir/gmcs
%_bindir/dmcs
%_monodir/2.0/mcs.exe
%_monodir/*/gmcs.exe*
%_monodir/*/dmcs.exe*
%_man1dir/mcs.*

%package csharp
Summary: Interactive C# Shell for Mono
Group: Development/Other
License: %gpl2only %mit
Requires: %name = %version-%release

%description csharp
This package contains an interactive C# shell that allows the user to enter and
evaluate C# statements and expressions from  the  command  line.

%files csharp
%_bindir/csharp
%_bindir/csharp2
%_monodir/*/csharp.exe*
%_man1dir/csharp.*
%_monodir/*/Mono.CSharp
%_monodir/*/Mono.CSharp.dll*

%package winforms
Summary: Windows Forms implementation for Mono
Group: Development/Other
Requires: %name = %version-%release
Provides: mono-window-forms = %version
Obsoletes: mono-window-forms < %version

%description winforms
This package provides a fully managed implementation of
System.Windows.Forms, the default graphical toolkit for .NET
applications.

%files winforms
%_monodir/*/System.Windows.Forms
%_monodir/*/System.Windows.Forms.dll*
%_monodir/*/Accessibility
%_monodir/*/Accessibility.dll*
%_monodir/*/System.Design
%_monodir/*/System.Design.dll*
%_monodir/*/System.Drawing.Design
%_monodir/*/System.Drawing.Design.dll*
%_monodir/*/System.Windows.Forms.DataVisualization
%_monodir/*/System.Windows.Forms.DataVisualization.dll*
%_monodir/*/Mono.WebBrowser
%_monodir/*/Mono.WebBrowser.dll*

%package wcf
Summary: Mono implementation of WCF, Windows Communication Foundation
Group: Development/Other
Requires: %name = %version-%release

%description wcf
Mono implementation of WCF, Windows Communication Foundation

%files wcf
%_bindir/svcutil
%_monodir/*/svcutil.exe*
%_monodir/*/System.IdentityModel
%_monodir/*/System.IdentityModel.dll*
%_monodir/*/System.IdentityModel.Selectors
%_monodir/*/System.IdentityModel.Selectors.dll*
%_monodir/*/System.Runtime.DurableInstancing
%_monodir/*/System.Runtime.DurableInstancing.dll*
%_monodir/*/System.ServiceModel.Discovery
%_monodir/*/System.ServiceModel.Discovery.dll*
%_monodir/*/System.ServiceModel.Routing
%_monodir/*/System.ServiceModel.Routing.dll*
%_monodir/*/System.Runtime.Serialization
%_monodir/*/System.Runtime.Serialization.dll*
%_monodir/*/System.ServiceModel
%_monodir/*/System.ServiceModel.dll*
%_monodir/*/System.ServiceModel.Web
%_monodir/*/System.ServiceModel.Web.dll*
%_monodir/*/System.Data.Services
%_monodir/*/System.Data.Services.dll*

%package wcf-devel
Summary: Mono implementation of WCF, Windows Communication Foundation
Group: Development/Other
Requires: %name-wcf = %version-%release

%description wcf-devel
Mono implementation of WCF, Windows Communication Foundation

This package contains development pkg-config files for %name-wcf

%files wcf-devel
%_pkgconfigdir/wcf.pc

%package winfxcore
Summary: Mono implementation of core WinFX APIs
Group: Development/Other
Requires: %name = %version-%release

%description winfxcore
Mono implementation of core WinFX APIs

%files winfxcore
%_monodir/*/WindowsBase
%_monodir/*/WindowsBase.dll*

%package web
Summary: ASP.NET, Remoting, and Web Services for Mono
Group: Development/Other
Requires: %name = %version-%release

%description web
This package provides the ASP.NET libraries and runtime for
development of web application, web services and remoting support.

%files web
%dir %_sysconfdir/mono/mconfig
%dir %_sysconfdir/mono/2.0/Browsers
%config(noreplace) %_sysconfdir/mono/browscap.ini
%config(noreplace) %_sysconfdir/mono/*/DefaultWsdlHelpGenerator.aspx
%config(noreplace) %_sysconfdir/mono/*/web.config
%config(noreplace) %_sysconfdir/mono/2.0/Browsers/Compat.browser
%config(noreplace) %_sysconfdir/mono/mconfig/config.xml
%_bindir/soapsuds
%_bindir/disco
%_bindir/wsdl
%_bindir/wsdl2
%_bindir/xsd
%_bindir/mconfig
%_monodir/*/soapsuds.exe*
%_monodir/*/disco.exe*
%_monodir/*/wsdl.exe*
%_monodir/*/xsd.exe*
%_monodir/*/httpcfg.exe*
%_monodir/*/mconfig.exe*
%_monodir/*/System.Web
%_monodir/*/System.Web.dll*
%_monodir/*/Mono.Http
%_monodir/*/Mono.Http.dll*
%_monodir/*/Mono.Web
%_monodir/*/Mono.Web.dll*
%_monodir/*/System.Runtime.Remoting
%_monodir/*/System.Runtime.Remoting.dll*
%_monodir/*/System.Runtime.Serialization.Formatters.Soap
%_monodir/*/System.Runtime.Serialization.Formatters.Soap.dll*
%_monodir/*/System.Web.Services
%_monodir/*/System.Web.Services.dll*
%_monodir/*/System.Web.Abstractions
%_monodir/*/System.Web.Abstractions.dll*
%_monodir/*/System.Web.ApplicationServices
%_monodir/*/System.Web.ApplicationServices.dll*
%_monodir/*/System.Web.Routing
%_monodir/*/System.Web.Routing.dll*
%_monodir/*/System.ComponentModel.DataAnnotations
%_monodir/*/System.ComponentModel.DataAnnotations.dll*
%_monodir/*/System.ComponentModel.Composition
%_monodir/*/System.ComponentModel.Composition.dll*
%_monodir/*/Microsoft.Web.Infrastructure
%_monodir/*/Microsoft.Web.Infrastructure.dll*
%_man1dir/soapsuds.*
%_man1dir/disco.*
%_man1dir/wsdl.*
%_man1dir/xsd.*
%_man1dir/mconfig.*

%package web-devel
Summary: ASP.NET, Remoting, and Web Services for Mono
Group: Development/Other
Requires: %name-web = %version-%release

%description web-devel
This package provides the ASP.NET libraries and runtime for
development of web application, web services and remoting support.

This package contains development pkg-config files for %name-web


%files web-devel
%_pkgconfigdir/mono.web.pc

%package -n mono-mvc
Summary: Mono implementation of ASP.NET MVC
Group: Development/Other
Requires: %name = %version-%release

%description -n mono-mvc
Mono implementation of ASP.NET MVC.

%files -n mono-mvc
%_monodir/*/System.Web.DynamicData
%_monodir/*/System.Web.DynamicData.dll*
%_monodir/*/System.Web.Extensions.Design
%_monodir/*/System.Web.Extensions.Design.dll*
%_monodir/*/System.Web.Extensions
%_monodir/*/System.Web.Extensions.dll*
%_monodir/*/System.Web.Mvc
%_monodir/*/System.Web.Mvc.dll*

%package -n mono-mvc-devel
Summary: Mono implementation of ASP.NET MVC
Group: Development/Other
Requires: mono-mvc = %version-%release

%description -n mono-mvc-devel
Mono implementation of ASP.NET MVC.

This package contains development pkg-config files for %name-mvc

%files -n mono-mvc-devel
%_pkgconfigdir/system.web.extensions.design_1.0.pc
%_pkgconfigdir/system.web.extensions_1.0.pc
%_pkgconfigdir/system.web.mvc.pc
%_pkgconfigdir/system.web.mvc2.pc

%package extras
Summary: Provides the infrastructure for running and building daemons and services with Mono as well as various stub assemblies
Group: Development/Other
Requires: %name = %version-%release

%description extras
This package provides the libary and application to run services
and daemons with Mono. It also includes stubs for the following
.NET 1.1 and 2.0 assemblies: System.Configuration.Install, System.Management, System.Messaging.

%files extras
%_bindir/mono-service*
%_bindir/mono-xmltool
%_monodir/*/installutil.exe*
%_monodir/*/mono-service
%_monodir/*/mono-service.exe*
%_monodir/*/mono-xmltool.exe*
%_monodir/*/RabbitMQ.Client
%_monodir/*/RabbitMQ.Client.dll*
%_monodir/*/RabbitMQ.Client.Apigen.exe*
%_monodir/*/System.Management
%_monodir/*/System.Management.dll*
%_monodir/*/System.Messaging
%_monodir/*/System.Messaging.dll*
%_monodir/*/Mono.Messaging
%_monodir/*/Mono.Messaging.dll*
%_monodir/*/System.Runtime.Caching
%_monodir/*/System.Runtime.Caching.dll*
%_monodir/*/Mono.Messaging.RabbitMQ
%_monodir/*/Mono.Messaging.RabbitMQ.dll*
%_monodir/*/System.ServiceProcess
%_monodir/*/System.ServiceProcess.dll*
%_monodir/*/System.Xaml
%_monodir/*/System.Xaml.dll*
%_monodir/*/System.Configuration.Install
%_monodir/*/System.Configuration.Install.dll*
%_man1dir/mono-service.*
%_man1dir/mono-xmltool*

%package -n ibm-data-db2
Summary: BM DB2 database connectivity for Mono
Group: Development/Other
Requires: %name = %version-%release

%description -n ibm-data-db2
This package contains the ADO.NET Data provider for the IBM DB2
Universal database.

%files -n ibm-data-db2
%_monodir/*/IBM.Data.DB2
%_monodir/*/IBM.Data.DB2.dll*

%package devel
Summary: Development tools and headers for Mono
Group: Development/Other
Requires: %name = %version-%release
Requires: monodis = %version-%release

%description devel
This package includes all Mono library headers and completes the
Mono developer toolchain (with the mono profiler, assembler and
other various tools)

%files devel
# Shell wrappers
%_bindir/al*
%_bindir/caspol
%_bindir/ccrewrite
%_bindir/mono-cil-strip
%_bindir/cert2spc
%_bindir/dtd2rng
%_bindir/dtd2xsd
%_bindir/genxs
%_bindir/httpcfg
%_bindir/ilasm
%_bindir/installvst
%_bindir/macpack
%_bindir/makecert
%_bindir/mkbundle
%_bindir/monolinker
%_bindir/mono-api-info
%_bindir/monograph
%_bindir/monop
%_bindir/monop2
%_bindir/mono-heapviz
%_bindir/mono-shlib-cop
%_bindir/mprof-report
%_bindir/pedump
%_bindir/peverify
%_bindir/permview
%_bindir/prj2make
%_bindir/resgen*
%_bindir/secutil
%_bindir/sgen
%_bindir/signcode
%_bindir/xbuild
%_bindir/lc
%_bindir/pdb2mdb
%_bindir/mono-gdb.py
%_libdir/libmono-profiler-cov.*
%_libdir/libmono-profiler-aot.*
# %_libdir/libmono-profiler-logging.*
%_libdir/libmono-profiler-log.*
%_libdir/libmono-profiler-iomap.*
%_monodir/*/al.exe*
%_monodir/*/genxs.exe*
%_monodir/*/ilasm.exe*
%_monodir/*/makecert.exe*
%_monodir/*/monop.exe*
%_monodir/*/cert2spc.exe*
%_monodir/*/mono-cil-strip*
%_monodir/*/signcode.exe*
%_monodir/*/secutil.exe*
%_monodir/*/sgen.exe*
%_monodir/*/resgen.exe*
%_monodir/*/dtd2rng.exe*
%_monodir/*/dtd2xsd.exe*
%_monodir/*/mkbundle.exe*
%_monodir/*/permview.exe*
%_monodir/*/caspol.exe*
%_monodir/*/ccrewrite.exe*
%_monodir/*/macpack.exe*
%_monodir/*/culevel.exe*
%_monodir/*/installvst.exe*
%_monodir/*/ictool.exe*
%_monodir/*/browsercaps-updater.exe*
%_monodir/*/mono-shlib-cop.exe*
%_monodir/*/xbuild.exe*
%_monodir/*/lc.exe*
%_monodir/*/pdb2mdb.exe*
%_monodir/*/mono-api-info.exe
%_monodir/*/Microsoft.Build
%_monodir/*/Microsoft.Build.dll*
%_monodir/*/Microsoft.Build.Tasks
%_monodir/*/Microsoft.Build.Tasks.dll*
%_monodir/*/Microsoft.Build.Tasks.v*.*
%_monodir/*/Microsoft.Build.Tasks.v*.*.dll*
%_monodir/*/Microsoft.Build.Framework
%_monodir/*/Microsoft.Build.Framework.dll*
%_monodir/*/Microsoft.Build.Utilities
%_monodir/*/Microsoft.Build.Utilities.dll*
%_monodir/*/Microsoft.Build.Utilities.v*.*
%_monodir/*/Microsoft.Build.Utilities.v*.*.dll*
%_monodir/*/Microsoft.Build.Engine
%_monodir/*/Microsoft.Build.Engine.dll*
%_monodir/*/Mono.CompilerServices.SymbolWriter
%_monodir/*/Mono.CompilerServices.SymbolWriter.dll*
%_monodir/*/Mono.CodeContracts
%_monodir/*/Mono.CodeContracts.dll*
%_monodir/*/PEAPI
%_monodir/*/PEAPI.dll*
%_monodir/*/Mono.Cecil
%_monodir/*/Mono.Cecil.dll*
%_monodir/*/Mono.Cecil.Mdb
%_monodir/*/Mono.Cecil.Mdb.dll*
%_monodir/*/MSBuild
%_monodir/*/Microsoft.Build.xsd
%_monodir/*/Microsoft.*.targets
%_monodir/*/Microsoft.*.tasks
%_monodir/*/Microsoft.CSharp
%_monodir/*/Microsoft.CSharp.dll*
%_monodir/*/Mono.Debugger.Soft
%_monodir/*/Mono.Debugger.Soft.dll*
%_monodir/*/xbuild.rsp
%_monodir/xbuild
%_monodir/xbuild-frameworks
%_monodir/*/monolinker.exe*
%_pkgconfigdir/dotnet.pc
%_pkgconfigdir/dotnet35.pc
%_pkgconfigdir/cecil.pc
%_pkgconfigdir/mono-lineeditor.pc
%_pkgconfigdir/mono-options.pc
%_pkgconfigdir/mono.pc
%_pkgconfigdir/mono-cairo.pc
%_datadir/mono-2.0/mono/cil/cil-opcodes.xml
%_prefix/lib/mono-source-libs
%_man1dir/al.*
%_man1dir/ilasm.*
%_man1dir/genxs.*
%_man1dir/httpcfg.*
%_man1dir/makecert.*
%_man1dir/monop.*
%_man1dir/cert2spc.*
%_man1dir/ccrewrite.*
%_man1dir/signcode.*
%_man1dir/secutil.*
%_man1dir/sgen.*
%_man1dir/cilc.*
%_man1dir/prj2make.*
%_man1dir/dtd2xsd.*
%_man1dir/mkbundle.*
%_man1dir/permview.*
%_man1dir/macpack.*
%_man1dir/mono-shlib-cop.*
%_man1dir/mprof-report.*
%_man1dir/monolinker.*
%_man1dir/mono-api-info.*
%_man1dir/resgen.*
%_man1dir/mono-cil-strip.*
%_man1dir/xbuild.*
%_man1dir/lc.*
%_man1dir/pdb2mdb.*

%package -n monodoc
Summary: monodoc
Group: Development/Other

%description -n monodoc
This is the MonoDoc module.  It contains the tools to produce and edit the
documentation, and a documentation browser.
The documentation browser consists of a library and two
front-ends: a Gtk\#-based one, and an ASP.NET-based version.

%triggerpostun -n monodoc -- monodoc < 2.0-alt2
[ $1 != 1 ] || exit 0
echo "Remove old monodoc index"
/bin/rm -f /usr/lib/monodoc/monodoc.index ||:

%files -n monodoc
%_bindir/mdassembler
%_bindir/mdoc
%_bindir/mdoc-assemble
%_bindir/mdoc-export-html
%_bindir/mdoc-export-msxdoc
%_bindir/mdoc-update
%_bindir/mdoc-validate
%_bindir/mdvalidater
%_bindir/mod
%_bindir/monodocer
%_bindir/monodocs2html
%_bindir/monodocs2slashdoc
%_monodir/*/mdoc.exe*
%_monodir/*/mod.exe*
%_monogacdir/monodoc
%_monodir/monodoc
%dir %_datadir/monodoc
%_datadir/monodoc/monodoc.xml
%dir %_monodocdir
%_man1dir/mdassembler.*
%_man1dir/mdoc-assemble.*
%_man1dir/mdoc-export-html.*
%_man1dir/mdoc-export-msxdoc.*
%_man1dir/mdoc-update.*
%_man1dir/mdoc-validate.*
%_man1dir/mdoc.*
%_man1dir/mdvalidater.*
%_man1dir/monodocer.*
%_man1dir/monodocs2html.*
%_man5dir/mdoc.*

%package -n monodoc-devel
Summary: monodoc
Group: Development/Other
Requires: monodoc = %version-%release

%description -n monodoc-devel
This is the MonoDoc module.  It contains the tools to produce and edit the
documentation, and a documentation browser.
The documentation browser consists of a library and two
front-ends: a Gtk\#-based one, and an ASP.NET-based version.

This package contains development pkg-config files for monodoc

%files -n monodoc-devel
%_pkgconfigdir/monodoc.pc

%package doc
Summary: Documentation for mono
Group: Documentation
BuildArch: noarch
Requires: monodoc >= 2.2

%description doc
This package contains the documentation for the Mono class libraries.

%files doc
%_monodocdir/*

%package data-oracle
Summary: Oracle database connectivity for Mono
Group: Development/Other
Requires: %name = %version-%release

%description data-oracle
This package contains the ADO.NET Data provider for the Oracle
database.

%files data-oracle
%_monodir/*/System.Data.OracleClient
%_monodir/*/System.Data.OracleClient.dll*

%package data
Summary: Database connectivity for Mono
Group: Development/Other
Requires: %name = %version-%release
Obsoletes: mono-data-sybase < 2.8
Obsoletes: mono-data-firebird < 2.8
Obsoletes: bytefx-data-mysql < 2.8

%description data
This package provides a Mono assembly to facilitate data access
and manipulation with databases, LDAP compatible directory servers
and/or XML data exchange. Beyond the ADO.NET, Novell.LDAP and
System.DirectoryServices assemblies, it also includes a command
line sql application as well as the Microsoft SQL Server and ODBC
data providers.

%files data
%_bindir/sqlsharp
%_bindir/sqlmetal
%_monodir/*/sqlsharp.exe*
%_monodir/*/sqlmetal.exe*
%_monodir/*/System.Data
%_monodir/*/System.Data.dll*
%_monodir/*/System.Data.Linq
%_monodir/*/System.Data.Linq.dll*
%_monodir/*/System.Data.Services.Client
%_monodir/*/System.Data.Services.Client.dll*
%_monodir/*/Mono.Data.Tds
%_monodir/*/Mono.Data.Tds.dll*
%_monodir/*/System.EnterpriseServices
%_monodir/*/System.EnterpriseServices.dll*
%_monodir/*/Novell.Directory.Ldap
%_monodir/*/Novell.Directory.Ldap.dll*
%_monodir/*/System.DirectoryServices
%_monodir/*/System.DirectoryServices.dll*
%_monodir/*/System.Data.DataSetExtensions
%_monodir/*/System.Data.DataSetExtensions.dll*
%_monodir/*/WebMatrix.Data
%_monodir/*/WebMatrix.Data.dll*
%_man1dir/sqlsharp.*

%package nunit
Summary: NUnit Testing Framework
Group: Development/Other
Requires: %name = %version-%release

%description nunit
NUnit is a unit-testing framework for all .Net languages.
Initially ported from JUnit, the current release, version 2.4,
is the fourth major release of this xUnit based unit testing tool
for Microsoft .NET. It is written entirely in C# and has been
completely redesigned to take advantage of many .NET language
features, for example custom attributes and other reflection
related capabilities. NUnit brings xUnit to all .NET languages.

%files nunit
%_bindir/nunit-console*
%_monodir/*/nunit-console.exe*
%_monodir/*/nunit.core
%_monodir/*/nunit.framework
%_monodir/*/nunit.util
%_monodir/*/nunit.core.dll
%_monodir/*/nunit.framework.dll
%_monodir/*/nunit.mocks
%_monodir/*/nunit.mocks.dll*
%_monodir/*/nunit.util.dll
%_monodir/*/nunit-console-runner
%_monodir/*/nunit-console-runner.dll*
%_monodir/*/nunit.core.extensions
%_monodir/*/nunit.core.extensions.dll*
%_monodir/*/nunit.core.interfaces
%_monodir/*/nunit.core.interfaces.dll*
%_monodir/*/nunit.framework.extensions
%_monodir/*/nunit.framework.extensions.dll*

%package nunit-devel
Summary: NUnit Testing Framework
Group: Development/Other
Requires: %name-nunit = %version-%release

%description nunit-devel
NUnit is a unit-testing framework for all .Net languages.
Initially ported from JUnit, the current release, version 2.4,
is the fourth major release of this xUnit based unit testing tool
for Microsoft .NET. It is written entirely in C# and has been
completely redesigned to take advantage of many .NET language
features, for example custom attributes and other reflection
related capabilities. NUnit brings xUnit to all .NET languages.

This package contains development pkg-config files for %name-nunit

%files nunit-devel
%_pkgconfigdir/mono-nunit.pc

%package locale-extras
Summary: Extra Locale information
Group: Development/Other
Requires: %name = %version-%release

%description locale-extras
Extra Locale information

%files locale-extras
%_monodir/*/I18N.CJK
%_monodir/*/I18N.CJK.dll*

%package data-postgresql
Summary: Postgresql database connectivity for Mono
License: %lgpl2only
Group: Development/Other
Requires: %name = %version-%release

%description data-postgresql
This package contains the ADO.NET Data provider for the Postgresql
database.

%files data-postgresql
%_monodir/*/Npgsql
%_monodir/*/Npgsql.dll*

%package data-sqlite
Summary: sqlite database connectivity for Mono
Group: Development/Other
Requires: %name = %version-%release

%description data-sqlite
his package contains the ADO.NET Data provider for the sqlite
database.

%files data-sqlite
%_monodir/*/Mono.Data.Sqlite
%_monodir/*/Mono.Data.Sqlite.dll*

%package complete
Summary: This package contains all runtime Mono packages
Group: Development/Other
BuildArch: noarch
Requires: %name-mscorlib = %version-%release
Requires: libmono = %version-%release
Requires: libmono-devel = %version-%release
Requires: monodis = %version-%release
Requires: %name = %version-%release
Requires: mono-locale-extras = %version-%release
Requires: mono-data = %version-%release
Requires: mono-data-sqlite = %version-%release
Requires: mono-data-oracle = %version-%release
Requires: mono-data-postgresql = %version-%release
Requires: ibm-data-db2 = %version-%release
Requires: mono-web = %version-%release
Requires: mono-mcs = %version-%release
Requires: mono-extras = %version-%release
Requires: mono-nunit = %version-%release
Requires: mono-web = %version-%release
Requires: mono-mvc = %version-%release
Requires: mono-winforms = %version-%release
Requires: mono-wcf = %version-%release
Requires: mono-csharp = %version-%release
Requires: mono-winfxcore = %version-%release

%description complete
This is a virtual package which depends on all the packages that
constitute the Mono runtime, core libraries, and command-line
tools.

%files complete

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#%patch5 -p1
%patch6 -p1

%build
%ifdef __buildreqs
# workaround strace hanging
export with_sigaltstack=no
%endif
%add_optflags -fno-strict-aliasing
export CFLAGS="%optflags"

%autoreconf

# Add undeclared Arg
sed -i "61a #define ARG_MAX     _POSIX_ARG_MAX" mono/io-layer/wapi_glob.h

# %%undefine __libtoolize
%configure \
	--disable-static \
	--with-static_mono=no \
	--with-gc=%libgc \
	--with-sgen=no \
	--enable-parallel-mark=yes \
	--with-profile4=yes \
	--with-tls=pthread \
	--disable-quiet-build \
	--with-mcs-docs=yes

# temporary build without moonlight
# 	--with-moonlight=yes \

%make V=1

%install
%make_install DESTDIR=%buildroot install
%if %libgc == included
rm -rv %buildroot%_datadir/libgc-mono
%endif

# We put these inside rpm
rm -f %buildroot%_bindir/mono-find-provides
rm -f %buildroot%_bindir/mono-find-requires

# This was removed upstream:
rm -f %buildroot%_monodir/2.0/mcs.exe.so

%find_lang mcs

# install *.config files
for d in %buildroot%_monogacdir/System.Windows.Forms/* ; do install -m644 %SOURCE13 $d/; done
for d in %buildroot%_monogacdir/System.Data/* ; do install -m644 %SOURCE14 $d/; done


deps=$(pkg-config --print-{errors,requires} %buildroot%_pkgconfigdir/mono.pc)
: mono.pc should not have explicit pkgconfig dependencies
[ -z "$deps" ]

%changelog
* Wed Feb 08 2012 Alexey Shabalin <shaba@altlinux.ru> 2.10.8-alt1
- 2.10.8
- add mvc, configuration-crypto subpackages
- drop mono-data-sybase, mono-data-firebird, bytefx-data-mysql, mono-jscript, mono-jay

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.6.7-alt1.1
- Rebuild with Python-2.7

* Sun Aug 22 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.7-alt1
- 2.6.7

* Tue Apr 27 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Tue Mar 16 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Sun Dec 20 2009 Alexey Shabalin <shaba@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 2.6-alt1
- 2.6

* Mon Dec 14 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Sun Sep 06 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.2.3-alt2
- fix System.Data.dll to require libgda4

* Sat Aug 15 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.2.3-alt1
- 2.4.2.3. This release fixes issues with precompiled MVC applications.

* Wed Jul 22 2009 Ildar Mulyukov <ildar@altlinux.ru> 2.4.2.2-alt1
- Closes: #20787

* Tue Jul 07 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.2.1-alt1
- 2.4.2.1

* Tue Jun 30 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.2-alt1
- 2.4.2
- move all pkg-config files (*.pc) to devel packages (ALT#13863)

* Wed Apr 01 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4-alt1
- 2.4
- revert %%_libdir/glib-2.0/include to libmono-devel

* Thu Mar 19 2009 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt2
- fix requires in libmono-devel (drop %%_libdir/glib-2.0/include with glib2-devel-2.20.0)

* Thu Jan 15 2009 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1
- 2.2
- drop backported patch6 and patch7
- add monodoc package (upstream merged mono with monodoc)
- add mono-wcf package
- add config files for dll's (SOURCE10-14)

* Thu Nov 20 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt3
- patch for fixes nunit-2.4(and other) build (mono #425647)

* Thu Nov 20 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt2
- patch for fixes muine build
- remove post ldconfig

* Sat Oct 25 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Tue Oct 07 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- 2.0 release

* Fri Sep 12 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt0.rc1
- 2.0 RC1

* Mon Sep 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt0.pre2
- 2.0 preview2
- don't remove assemblies_dir from cecil.pc

* Tue Aug 12 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt0.pre1
- 2.0 preview1

* Tue Apr 22 2008 Alexey Shabalin <shaba@altlinux.ru> 1.9.1-alt1
- 1.9.1

* Fri Mar 21 2008 Alexey Tourbin <at@altlinux.ru> 1.9-alt2
- moved installutil.exe, which requires System.Configuration.Install.dll,
  from mono to mono-extras package

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 1.9-alt1
- 1.9
- update patch for cecil

* Tue Mar 11 2008 Alexey Tourbin <at@altlinux.ru> 1.2.6-alt4
- split mono-mscorlib package, required for monodis (cf. #14578)
- hacked mono.pc dependencies (#13863)
- fixed /usr/lib/mono/2.1 and /usr/lib/mono/compat-* dir ownership
- fixed unversioned provides and obsoletes, updated dependencies

* Wed Jan 09 2008 Alexey Shabalin <shaba@altlinux.ru> 1.2.6-alt3
- add cecil symlinks for mono/2.0

* Wed Jan 02 2008 Alexey Shabalin <shaba@altlinux.ru> 1.2.6-alt2
- fix cecil pkgconfig file (patch3) and add symlink

* Sun Dec 16 2007 Alexey Shabalin <shaba@altlinux.ru> 1.2.6-alt1
- build with  moonlight
- update files section
- move a some sysconfig files to web package
- add noreplace for sysconfig files
- change "%%doc %%mandir/man*" to %%man1dir in spec

* Tue Nov 20 2007 Alexey Tourbin <at@altlinux.ru> 1.2.5.2-alt2
- must really build with new rpm-build-mono-1.2
- packaged mono.pc into both mono and libmono-devel

* Sun Nov 11 2007 Alexey Tourbin <at@altlinux.ru> 1.2.5.2-alt1
- 1.2.5.1 -> 1.2.5.2 (fixes Windows-only CVE-2007-5473)
- applied fix for CVE-2007-5197 (buffer overflow in Mono.Math.BigInteger)
- build with new rpm-build-mono-1.2
- new packages: libmono, libmono-devel, monodis
- use "configure --disable-static" to prevent static linkage with libmono
- explicitly disabled valgrind support (it was supposed to work only on x86)
- fixed soname dependencies by adjusting /etc/mono/config DLL mappings
- updated dependencies, removed outdated dependencies; added dependency
  on rpm-build-mono to mono-mcs (using mono compiler will automatically
  enable support for mono dependencies)

* Tue Oct 09 2007 Alexey Shabalin <shaba@altlinux.ru> 1.2.5.1-alt1
- 1.2.5.1
- change buildreq from libgdiplus to libgdiplus-devel
- build with new rpm-build-mono-1.1-alt1
- fix BuildRequires
- add man for resgen
- add mono-api-diff,mono-api-info,mono-api-info2,installvst to %%bindir

* Sat Sep 08 2007 Alexey Shabalin <shaba@altlinux.ru> 1.2.5-alt1
- 1.2.5
- drop monodiet in devel package
- add monolinker to devel package
- add Mono.Cecil.dll to mono package

* Sat Jul 28 2007 Alexey Shabalin <shaba@altlinux.ru> 1.2.4-alt1
- 1.2.4
- add in %%files:
    + installvst.exe
    + culevel.exe
    + httpcfg.exe
    + Mono.Data.Sqlite.dll
    + System.Core.dll

* Sat Mar 17 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.3.1-alt1.0
- Rebuilt with file-4.20-alt2 and rpm-build-4.0.4-alt74 (#11088).

* Fri Feb 23 2007 Ildar Mulyukov <ildar@altlinux.ru> 1.2.3.1-alt1
- 1.2.3.1

* Wed Nov 15 2006 Ildar Mulyukov <ildar@altlinux.ru> 1.2-alt1
- 1.2

* Fri Oct 06 2006 Ildar Mulyukov <ildar@altlinux.ru> 1.1.17.2-alt1
- total spec re-lay-outing
- fix build for x86_64 platform

* Mon Oct 02 2006 Ildar Mulyukov <ildar@altlinux.ru> 1.1.17.1-alt1
- BuildRequires list fix
- mono-basic was moved into separate package
- some dependencies fixed
- build with rpm-build-mono

* Thu Mar 30 2006 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.13.6-alt1
- Update to release

* Mon Feb 06 2006 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.13.2-alt1
- Update to release
- Move architecture independent files to %_prefix/lib/mono

* Tue Nov 15 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.10-alt1
- Update to release
- Add requires mono-winforms to libgdiplus
- Add nunit and jscript packages

* Sat Oct 08 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.9.2-alt1
- update to release

* Thu Sep 29 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.9.1-alt1
- update to 1.1.9.1

* Thu Sep 22 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.9-alt1
- update to 1.1.9

* Wed Aug 03 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.8.3-alt1
- update to last bugfixes

* Sat Jun 18 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.8-alt1
- update release

* Sun May 15 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.7-alt1
- update release

* Sat Oct  9 2004 Pavel S. Mironchik <tibor@altlinux.ru> 1.0.1-alt1
- update release 

* Thu Jul 29 2004 Pavel S. Mironchik <tibor@altlinux.ru> 1.0-alt1
- release

* Tue May 11 2004 Pavel S. Mironchik <tibor@altlinux.ru> 0.91-alt1
- new version

* Mon Apr  5 2004 Pavel S. Mironchik <tibor@altlinux.ru> 0.31-alt1
- 0.31 version

* Thu Mar  4 2004 Pavel S. Mironchik <tibor@altlinux.ru> 0.30.2-alt1
- updated to 0.30.2

* Thu Feb 26 2004 Pavel S. Mironchik <tibor@altlinux.ru> 0.30.1-alt2
- posix description added

* Thu Feb 19 2004 Pavel S. Mironchik <tibor@altlinux.ru> 0.30.1-alt1
- updated 0.30

* Tue Feb 17 2004 Pavel S. Mironchik <tibor@altlinux.ru> 0.30-alt3
- man moved into mono dir

* Thu Feb 12 2004 Pavel S. Mironchik <tibor@altlinux.ru> 0.30-alt2
- man files rename added

* Wed Feb  4 2004 Pavel S. Mironchik <tibor@altlinux.ru> 0.30-alt1
- new version release

* Mon Dec 15 2003 Pavel S. Mironchik <tibor@altlinux.ru> 0.29-alt2
- buildreq check and DefaultWsdlHelpGenerator.aspx, allso adopted for fixed mcs 

* Fri Dec  5 2003 Pavel S. Mironchik <tibor@altlinux.ru> 0.29-alt1
- new release of mono

* Fri Nov 28 2003 Pavel S. Mironchik <tibor@altlinux.ru> 0.28-alt2
- fixed problem with pnet

* Tue Oct  7 2003 Pavel S. Mironchik <tibor@altlinux.ru> 0.28-alt1
- new version 0.28-alt1

* Thu Sep 18 2003 Pavel S. Mironchik <tibor@altlinux.ru> 0.26-alt1
- Adopted for ALTLinux form original Ximian spec and mono-0.16

* Tue Nov 19 2002 Stanislav Ievlev <inger@altlinux.ru> 0.16-alt1
- Initial release for ALT
