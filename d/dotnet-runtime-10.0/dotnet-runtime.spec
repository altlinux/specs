%define _unpackaged_files_terminate_build 1
%def_enable dotnet_host

%define _dotnet_major 10.0
%define _dotnet_coreversion 10.0.13
%define _dotnet_sdkversion 10.0.402

%define _dotnet_corerelease 10.0.13
# used for build
%define _dotnet_sdkrelease 10.0.402
%define upstream_tag v%_dotnet_corerelease
%define commithash %version-%release

# Debug Release
%define debrel Release
# -debug -release
%define debrelopt -release

%def_with bootstrap
# TODO:
%def_with skipmanaged
%if_feature unwind 1.5
%def_with libunwind
%else
%def_without libunwind
%endif

Name: dotnet-runtime-%_dotnet_major
Version: %_dotnet_coreversion
Release: alt1

Summary: Microsoft .NET 10 Runtime and Microsoft.NETCore.App

License: MIT
Url: https://github.com/dotnet/runtime
Group: Development/Other

# Source-url: https://github.com/dotnet/runtime/archive/v%{_dotnet_corerelease}.tar.gz
Source: %name-%version.tar

# Full upstream information about release
#Source1: https://github.com/dotnet/dotnet/releases/download/%{upstream_tag}/release.json

ExclusiveArch: aarch64 x86_64

AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

# TODO:
BuildRequires(pre): rpm-macros-dotnet
BuildRequires(pre): rpm-macros-features >= 0.6

BuildRequires: /proc

BuildRequires: clang llvm
BuildRequires: python3 >= 3.7.1

# cmake_minimum_required for Native and mono
BuildRequires: rpm-build-cmake

BuildRequires: libstdc++-devel
%if_with libunwind
BuildRequires: libunwind-devel >= 1.5
%endif
BuildRequires: liblttng-ust-devel

#BuildRequires: lldb-devel
BuildRequires: libicu-devel libuuid-devel zlib-devel libcurl-devel libkrb5-devel libssl-devel

# it is not linked directly (the same like in libicu-devel)
# there are icu detection in a version range
Requires: libicu
Requires: libssl >= 1.1

%if_with bootstrap
BuildRequires: dotnet-bootstrap-sdk-%_dotnet_major = %_dotnet_sdkversion
%define bootstrapdir %_libdir/dotnet-bootstrap-%_dotnet_major
%else
BuildRequires: dotnet-%_dotnet_major
%define bootstrapdir %_dotnetdir
%endif

# TODO
Requires: dotnet-common
# = %version

Requires: dotnet-hostfxr-%_dotnet_major = %EVR


%description
This package contains the .NET Core runtime, called CoreCLR,
and the base library, called mscorlib.

.NET is a development platform that you can use to build command-line
applications, microservices and modern websites. It is open source,
cross-platform and is supported by Microsoft. We hope you enjoy using it!
If you do, please consider joining the active community of developers that are
contributing to the project on GitHub (https://github.com/dotnet/core).

# common for current version
%package -n dotnet-%_dotnet_major
Group: Development/Other
Summary: .NET %_dotnet_major full installation

Requires: dotnet-host
Requires: dotnet-runtime-%_dotnet_major = %EVR
Requires: dotnet-hostfxr-%_dotnet_major = %EVR
#Requires: dotnet-apphost-pack-%_dotnet_major = %EVR
%if_enabled dotnet_host
Provides: dotnet = %EVR
%endif

%description -n dotnet-%_dotnet_major
The .NET %_dotnet_major.

This is a virtual package to provide full installation of .NET %_dotnet_major.

.NET is a development platform that you can use to build command-line
applications, microservices and modern websites. It is open source,
cross-platform and is supported by Microsoft. We hope you enjoy using it!
If you do, please consider joining the active community of developers that are
contributing to the project on GitHub (https://github.com/dotnet/core).

# Note: one for all versions
%package -n dotnet-host
Group: Development/Other
Summary: .NET command line launcher

AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

Conflicts: dotnet <= 3.1.6-alt1
Requires: dotnet-common

%description -n dotnet-host
The .NET host is a command line program that runs a standalone
.NET core application or launches the SDK.

.NET is a development platform that you can use to build command-line
applications, microservices and modern websites. It is open source,
cross-platform and is supported by Microsoft. We hope you enjoy using it!
If you do, please consider joining the active community of developers that are
contributing to the project on GitHub (https://github.com/dotnet/core).


%package -n dotnet-hostfxr-%_dotnet_major
Group: Development/Other
Summary: Microsoft .NET Host FX Resolver
AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

Requires: dotnet-host

%description -n dotnet-hostfxr-%_dotnet_major
The .NET host resolver contains the logic to resolve and select
the right version of the .NET Core SDK or runtime to use.

.NET is a development platform that you can use to build command-line
applications, microservices and modern websites. It is open source,
cross-platform and is supported by Microsoft. We hope you enjoy using it!
If you do, please consider joining the active community of developers that are
contributing to the project on GitHub (https://github.com/dotnet/core).

%package -n dotnet-apphost-pack-%_dotnet_major
Group: Development/Other
Summary: Microsoft.NETCore.App.Host
AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoProv: no

%description -n dotnet-apphost-pack-%_dotnet_major
.NET is a development platform that you can use to build command-line
applications, microservices and modern websites. It is open source,
cross-platform and is supported by Microsoft. We hope you enjoy using it!
If you do, please consider joining the active community of developers that are
contributing to the project on GitHub (https://github.com/dotnet/core).


%prep
%setup

# set global runtime location
%__subst "s|/usr/share/dotnet|%_dotnetdir|" src/native/corehost/hostmisc/pal.unix.cpp

# replace obsoleted FindPythonInterp with FindPython3
find -name CMakeLists.txt | xargs sed -i -e 's|FindPythonInterp|FindPython3|' -e 's|PYTHON_EXECUTABLE|Python3_EXECUTABLE|'

%if_with libunwind
rm -rfv src/coreclr/pal/src/libunwind*
%endif

# be equal to our bootstrap version
%__subst "s|%_dotnet_major.1[0-9][0-9]|%_dotnet_sdkrelease|" global.json

%build
#export DotNetRunningInDocker=1
export DotNetCoreSdkDir=%bootstrapdir
export DotNetBuildToolsDir=%bootstrapdir

# Note: version-release instead of git commit
cat <<EOF >.version
%commithash
%_dotnet_corerelease
EOF

# build CLR
cd src/coreclr/
bash -x ./build-runtime.sh \
    %debrelopt -verbose -skipmanaged -ignorewarnings -skiprestoreoptdata -nopgooptimize -portablebuild 0\
    -cmakeargs -DENABLE_LLDBPLUGIN=0 \
%if_without single_file_diagnostics
    -cmakeargs -DFEATURE_SINGLE_FILE_DIAGNOSTICS=0 \
%endif
%if_with libunwind
    -cmakeargs -DCLR_CMAKE_USE_SYSTEM_LIBUNWIND=1 \
%endif
    %nil
cd -

# build Native libraries
cd src/native/libs/
bash -x ./build-native.sh %debrelopt
cd -

# FIXME: allow get the release info from release.json file
subst 's|Version N/A|Version %_dotnet_corerelease|' artifacts/obj/_version.c
subst 's|RuntimeProductVersion 0.0.0-dev|RuntimeProductVersion %_dotnet_corerelease|' artifacts/obj/runtime_version.h

# build host commands
export artifacts=$(pwd)/artifacts
cd src/native/corehost/
sh -x ./build.sh \
    %debrelopt \
    -portablebuild 0 \
    -coreclrartifacts $artifacts/bin/coreclr/Linux.%_dotnet_arch.%debrel \
    -nativelibsartifacts  $artifacts/bin/native/Linux-%_dotnet_arch-%debrel \
    -commithash %commithash \
%if_with libunwind
    -cmakeargs -DCLR_CMAKE_USE_SYSTEM_LIBUNWIND=1 \
%endif
    %nil
cd -

# TODO: run via common build.sh file
#echo ""> artifacts/toolset/%version.txt
# TODO: --build
#sh -x ./build.sh clr+libs --configuration Checked --clang --verbosity normal --cmakeargs -DFEATURE_SINGLE_FILE_DIAGNOSTICS=0 --cmakeargs -DENABLE_LLDBPLUGIN=0
#%if_with libunwind
#    --cmakeargs -DCLR_CMAKE_USE_SYSTEM_LIBUNWIND=1 \
#%endif
#%if_with skipmanaged
#    -skipmanaged \
#%endif
#    %nil


%install
mkdir -p %buildroot%_dotnet_shared/
# TODO: some publish use?
# TODO: drop SOS_README.md?
cp -a artifacts/bin/coreclr/linux.%_dotnet_arch.%debrel/{lib*.so,createdump} %buildroot%_dotnet_shared/
cp -a artifacts/bin/native/linux-%_dotnet_arch-%debrel/{libSystem.*Native*.so,libSystem.*Native*.a} %buildroot%_dotnet_shared/

mkdir -p %buildroot%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/
cp -a artifacts/bin/linux-%_dotnet_arch.%debrel/corehost/{coreclr_delegates.h,hostfxr.h,libnethost.so,libnethost.a,nethost.h} %buildroot%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/
cp -a artifacts/bin/linux-%_dotnet_arch.%debrel/corehost/apphost %buildroot%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/
cp -a artifacts/bin/coreclr/linux.%_dotnet_arch.%debrel/corehost/singlefilehost %buildroot%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/
cp -a artifacts/bin/linux-%_dotnet_arch.%debrel/corehost/{nethost.h,libhostpolicy.so,libnethost.a,coreclr_delegates.h,hostfxr.h} %buildroot%_dotnet_shared/
mkdir -p %buildroot%_dotnet_hostfxr/
cp -a artifacts/bin/linux-%_dotnet_arch.%debrel/corehost/libhostfxr.so %buildroot%_dotnet_hostfxr/

mkdir -p %buildroot%_dotnetdir/
%if_enabled dotnet_host
install -m755 artifacts/bin/linux-%_dotnet_arch.%debrel/corehost/dotnet %buildroot%_dotnetdir/

mkdir -p %buildroot%_bindir/
ln -sr %buildroot%_dotnetdir/dotnet %buildroot%_bindir/dotnet
%endif

install -D -m644 .version %buildroot%_dotnet_shared/.version

# copy managed libraries as is
%if_with bootstrap
# managed
cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/*.dll %buildroot%_dotnet_shared/

# FIXME: possible hack
cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/Microsoft.NETCore.App.deps.json %buildroot%_dotnet_shared/

# read during dotnet --version
#cp -a %bootstrapdir/shared/Microsoft.NETCore.App/%_dotnet_corerelease/System.Native.a %buildroot%_dotnet_shared/
%endif

# missed in the official package
rm -fv %buildroot%_dotnet_shared/libsuperpmi-shim-*.so
rm -fv %buildroot%_dotnet_shared/libprotononjit.so

%check
#%buildroot%_dotnetdir/dotnet --info
#%buildroot%_dotnetdir/dotnet --version

%files
%doc LICENSE.TXT PATENTS.TXT THIRD-PARTY-NOTICES.TXT README.md CONTRIBUTING.md
%dir %_dotnet_shared/

%_dotnet_shared/.version
%_dotnet_shared/Microsoft.NETCore.App.deps.json

# managed code
%_dotnet_shared/Microsoft.CSharp.dll
%_dotnet_shared/Microsoft.VisualBasic.Core.dll
%_dotnet_shared/Microsoft.VisualBasic.dll
%_dotnet_shared/Microsoft.Win32.Primitives.dll
%_dotnet_shared/Microsoft.Win32.Registry.dll
%_dotnet_shared/System.*.dll
%_dotnet_shared/System.dll
%_dotnet_shared/WindowsBase.dll
%_dotnet_shared/mscorlib.dll
%_dotnet_shared/netstandard.dll

# native code
%_dotnet_shared/libSystem.IO.Compression.Native.a
%_dotnet_shared/libSystem.IO.Compression.Native.so
%_dotnet_shared/libSystem.IO.Ports.Native.a
%_dotnet_shared/libSystem.IO.Ports.Native.so
%_dotnet_shared/libSystem.Globalization.Native.a
%_dotnet_shared/libSystem.Globalization.Native.so
%_dotnet_shared/libSystem.Native.a
%_dotnet_shared/libSystem.Native.so
%_dotnet_shared/libSystem.Net.Security.Native.a
%_dotnet_shared/libSystem.Net.Security.Native.so
# search for openssl dinamically
%_dotnet_shared/libSystem.Security.Cryptography.Native.OpenSsl.a
%_dotnet_shared/libSystem.Security.Cryptography.Native.OpenSsl.so

# not in bootstrap
%_dotnet_shared/libclrgc.so
#_dotnet_shared/libdbgshim.so
%_dotnet_shared/libjitinterface*.so

%_dotnet_shared/libclrgcexp.so
%_dotnet_shared/libclrjit*.so
%_dotnet_shared/libcoreclr.so
%_dotnet_shared/libcoreclrtraceptprovider.so
%_dotnet_shared/libmscordaccore.so
%_dotnet_shared/libmscordbi.so

%_dotnet_shared/libhostpolicy.so
%_dotnet_shared/libnethost.a

%_dotnet_shared/coreclr_delegates.h
%_dotnet_shared/hostfxr.h
%_dotnet_shared/nethost.h

%_dotnet_shared/createdump

%files -n dotnet-%_dotnet_major
%doc README.md

%if_enabled dotnet_host
%files -n dotnet-host
%doc LICENSE.TXT
%dir %_dotnetdir/
%_dotnetdir/dotnet
%_bindir/dotnet
%dir %_dotnetdir/host/
%dir %_dotnetdir/host/fxr/
%endif

%files -n dotnet-hostfxr-%_dotnet_major
%dir %_dotnet_hostfxr/
%_dotnet_hostfxr/libhostfxr.so

%files -n dotnet-apphost-pack-%_dotnet_major
%dir %_dotnetdir/
%dir %_dotnetdir/packs/
%dir %_dotnetdir/packs/Microsoft.NETCore.App.Host.%_dotnet_rid/
%dir %_dotnet_apphostdir/
%dir %_dotnet_apphostdir/runtimes/
%dir %_dotnet_apphostdir/runtimes/%_dotnet_rid/
%dir %_dotnet_apphostdir/runtimes/%_dotnet_rid/native/
%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/apphost
%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/coreclr_delegates.h
%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/hostfxr.h
%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/libnethost.a
%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/libnethost.so
%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/nethost.h
%_dotnet_apphostdir/runtimes/%_dotnet_rid/native/singlefilehost

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 10.0.13-alt1
- .NET Runtime 10.0.13
- BR: use rpm-build-cmake instead of plain cmake
- security fixes:
  + CVE-2026-66822, GHSA-wxxw-5cvc-53j7: .NET and Visual Studio Information Disclosure Vulnerability
  + CVE-2026-58280, GHSA-mc4q-93x5-f6hj: .NET and Visual Studio Denial of Service Vulnerability
  + CVE-2026-69651, GHSA-3rxq-g8rj-r2cf: .NET and Visual Studio Denial of Service Vulnerability
  + CVE-2026-96958, GHSA-r955-8q5j-3h83: .NET and Visual Studio Denial of Service Vulnerability
  + CVE-2026-96960, GHSA-7hqp-7c5m-4vq6: .NET and Visual Studio Denial of Service Vulnerability
  + CVE-2026-96959, GHSA-c399-9853-6jmj: .NET and Visual Studio Denial of Service Vulnerability
  + CVE-2026-84008, GHSA-846f-f764-76mx: .NET Denial of Service Vulnerability
  + CVE-2026-70174, GHSA-f749-vhgx-39h6: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-87697, GHSA-c27m-942f-rcfh: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-70035, GHSA-4j9v-h7pp-725h: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-83520, GHSA-4w5f-7jp2-w48g: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-96229, GHSA-5qr9-xxm9-6cmq: .NET and Visual Studio Information Disclosure Vulnerability
  + CVE-2026-96232, GHSA-f8qh-mqg4-9939: .NET and Visual Studio Information Disclosure Vulnerability
  + CVE-2026-96234, GHSA-fq6x-pvr9-888r: .NET and Visual Studio Information Disclosure Vulnerability
  + CVE-2026-70007, GHSA-pfwj-2f93-rf42: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-96224, GHSA-xq57-crx4-g373: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-96235, GHSA-g44w-h65v-4cw9: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-85363, GHSA-f63g-mx39-3r38: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-96233, GHSA-87vj-4hqv-22p9: .NET and Visual Studio Denial of Service Vulnerability
  + CVE-2026-70175, GHSA-x3vp-85cm-q97r: ASP.NET Core Elevation of Privilege Vulnerability
  + CVE-2026-70196, GHSA-57xr-hfxx-jw5x: ASP.NET Core Denial of Service Vulnerability
  + CVE-2026-70179, GHSA-vrrp-6v32-2p8g: ASP.NET Core Elevation of Privilege Vulnerability
  + CVE-2026-70181, GHSA-w5qq-qrpp-rf4c: ASP.NET Core Denial of Service Vulnerability
  + CVE-2026-70161: .NET SDK Elevation of Privilege Vulnerability
  + CVE-2026-70165: .NET SDK Elevation of Privilege Vulnerability
  + CVE-2026-70190: .NET SDK Elevation of Privilege Vulnerability
  + CVE-2026-96238: .NET SDK Security Feature Bypass Vulnerability
  + CVE-2026-96237: .NET SDK Remote Code Execution Vulnerability
  + CVE-2026-70159, GHSA-334f-vvp4-7g6p: ASP.NET Core Denial of Service Vulnerability
  + CVE-2026-70186, GHSA-mf4x-w4gh-4656: ASP.NET Core Denial of Service Vulnerability
  + CVE-2026-105016, GHSA-5gjq-3f94-rcf7: Microsoft QUIC Remote Code Execution Vulnerability
  + CVE-2026-85790, GHSA-2mxg-prvg-9jfg: .NET Information Disclosure Vulnerability
  + CVE-2026-70162, GHSA-2fmv-rv2c-59x7: .NET Denial of Service Vulnerability
  + CVE-2026-70183, GHSA-494h-xx7x-5frh: ASP.NET Core Security Feature Bypass Vulnerability
  + CVE-2026-88092, GHSA-rv87-ccxw-8ggf: ASP.NET Core Security Feature Bypass Vulnerability
  + CVE-2026-70188, GHSA-fpq8-4vhr-rcxx: ASP.NET Core Security Feature Bypass Vulnerability
  + CVE-2026-96957: .NET SDK Security Feature Bypass Vulnerability
  + CVE-2026-96230, GHSA-qjpx-jqm5-h2c4: ASP.NET Core Remote Code Execution Vulnerability
  + CVE-2026-92707: ASP.NET Core Denial of Service Vulnerability
  + CVE-2026-96231, GHSA-2j93-m82w-73j2: .NET and Visual Studio Elevation of Privilege Vulnerability
  + CVE-2026-96225, GHSA-w6wh-p4g7-mpj2: .NET and Visual Studio Elevation of Privilege Vulnerability
  + CVE-2026-70197, GHSA-4mpw-cpwj-hxxj: .NET and Visual Studio Remote Code Execution Vulnerability
  + CVE-2026-96236, GHSA-f4g7-52wc-p8x7: ASP.NET Core Denial of Service Vulnerability
  + CVE-2026-102870, GHSA-g27p-qf6j-c96c: ASP.NET Core Remote Code Execution Vulnerability

* Sat Sep 26 2026 Vitaly Lipatov <lav@altlinux.ru> 10.0.12-alt1
- .NET Runtime 10.0.12
- fixed CVEs:
 + CVE-2026-69439: .NET and Visual Studio Elevation of Privilege Vulnerability
 + CVE-2026-71328: .NET and Visual Studio Remote Code Execution Vulnerability
 + CVE-2026-69522: .NET and Visual Studio Remote Code Execution Vulnerability
 + CVE-2026-69304: ASP.NET Core Denial of Service Vulnerability
 + CVE-2026-58649: .NET Information Disclosure Vulnerability
 + CVE-2026-69806: .NET Elevation of Privilege Vulnerability

* Sun Aug 30 2026 Vitaly Lipatov <lav@altlinux.ru> 10.0.11-alt1
- .NET Runtime 10.0.11
- fixed CVEs:
 + CVE-2026-62898: .NET Information Disclosure Vulnerability
 + CVE-2026-62899: .NET Security Feature Bypass Vulnerability
 + CVE-2026-62900: .NET Information Disclosure Vulnerability
 + CVE-2026-62901: .NET Denial of Service Vulnerability
 + CVE-2026-62886: .NET Elevation of Privilege Vulnerability
 + CVE-2026-62871: .NET Elevation of Privilege Vulnerability
 + CVE-2026-70354: .NET Core Remote Code Execution Vulnerability
 + CVE-2026-62902: .NET Information Disclosure Vulnerability
 + CVE-2026-62897: .NET Remote Code Execution Vulnerability
 + CVE-2026-62909: .NET Elevation of Privilege Vulnerability
 + CVE-2026-50651: .NET Denial of Service Vulnerability
 + CVE-2026-50526: .NET Tampering Vulnerability
 + CVE-2026-50524: .NET Denial of Service Vulnerability
 + CVE-2026-50646: .NET Remote Code Execution Vulnerability
 + CVE-2026-50649: .NET Remote Code Execution Vulnerability
 + CVE-2026-50650: .NET Elevation of Privilege Vulnerability
 + CVE-2026-56158: .NET Remote Code Execution Vulnerability
 + CVE-2026-47302: .NET Denial of Service Vulnerability
 + CVE-2026-50648: .NET Denial of Service Vulnerability
 + CVE-2026-50527: .NET Denial of Service Vulnerability
 + CVE-2026-47304: .NET Security Feature Bypass Vulnerability
 + CVE-2026-50525: .NET Denial of Service Vulnerability
 + CVE-2026-57108: .NET Denial of Service Vulnerability
 + CVE-2026-50528: .NET Security Feature Bypass Vulnerability
 + CVE-2026-50659: .NET Spoofing Vulnerability
 + CVE-2026-47300: .NET Elevation of Privilege Vulnerability
 + CVE-2026-47303: .NET Elevation of Privilege Vulnerability
 + CVE-2026-45591: ASP.NET Core Denial of Service Vulnerability
 + CVE-2026-45491: .NET Elevation of Privilege Vulnerability
 + CVE-2026-45490: .NET Elevation of Privilege Vulnerability
 + CVE-2026-32177: .NET Denial of Service Vulnerability
 + CVE-2026-35433: .NET Elevation of Privilege Vulnerability
 + CVE-2026-32175: .NET Core Tampering Vulnerability
 + CVE-2026-42899: ASP.NET Core Denial of Service Vulnerability
 + CVE-2026-40372: ASP.NET Core Security Feature Bypass Vulnerability
 + CVE-2026-26171: .NET Denial of Service Vulnerability
 + CVE-2026-32203: .NET Denial of Service Vulnerability
 + CVE-2026-33116: .NET Denial of Service Vulnerability
 + CVE-2026-32178: .NET Spoofing Vulnerability

* Sat Aug 29 2026 Vitaly Lipatov <lav@altlinux.ru> 10.0.5-alt2
- Drop unused liblwp-devel build dependency on Linux.

* Sat Apr 04 2026 Vitaly Lipatov <lav@altlinux.ru> 10.0.5-alt1
- new version (no code changes really)
- enable build dotnet-host here

* Wed Apr 01 2026 Vitaly Lipatov <lav@altlinux.ru> 10.0.4-alt1
- new version (10.0.4)

* Mon Nov 17 2025 Vitaly Lipatov <lav@altlinux.ru> 10.0.0.rel-alt1
- .NET 10.0.0 release

* Tue Oct 28 2025 Vitaly Lipatov <lav@altlinux.ru> 10.0.0.rc2-alt1
- .NET 10.0.0.rc2
- initial build for ALT Sisyphus
