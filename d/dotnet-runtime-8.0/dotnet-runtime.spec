%define _unpackaged_files_terminate_build 1
%def_enable dotnet_host

%define _dotnet_major 8.0
%define _dotnet_corerelease 8.0.8
# used for build
%define _dotnet_sdkrelease 8.0.108
%define preview %nil
%define _dotnet_sdkshortrelease %_dotnet_sdkrelease%preview

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
Version: 8.0.8%preview
Release: alt1

Summary: Microsoft .NET Runtime and Microsoft.NETCore.App

License: MIT
Url: https://github.com/dotnet/runtime
Group: Development/Other

# Source-url: https://github.com/dotnet/runtime/archive/v%{_dotnet_corerelease}.tar.gz
Source: %name-%version.tar

# Full upstream information about release
#Source1: https://github.com/dotnet/dotnet/releases/download/%{upstream_tag}/release.json

Patch1: genmoduleindex.sh.patch

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
BuildRequires: cmake >= 3.14.5

BuildRequires: libstdc++-devel
%if_with libunwind
BuildRequires: libunwind-devel >= 1.5
%endif
BuildRequires: liblttng-ust-devel liblwp-devel

#BuildRequires: lldb-devel
BuildRequires: libicu-devel libuuid-devel zlib-devel libcurl-devel libkrb5-devel libssl-devel

# it is not linked directly (the same like in libicu-devel)
# there are icu detection in a version range
Requires: libicu
Requires: libssl >= 1.1

%if_with bootstrap
BuildRequires: dotnet-bootstrap-sdk-%_dotnet_major = %_dotnet_sdkshortrelease
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
%patch1 -p2

#release_json_tag="$(grep tag %SOURCE1 | cut -d: -f2 | sed -E 's/[," ]*//g')"
#if [ ${release_json_tag} != %{upstream_tag} ]; then
#   echo "error: tag in release.json doesn't match tag in spec file"
#   exit 1
#fi

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
* Mon Sep 16 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.8-alt1
- .NET 8.0.8 release
- CVE-2024-38168: .NET Denial of Service Vulnerability
- CVE-2024-38167: .NET Information Disclosure Vulnerability
- CVE-2024-38095: .NET Denial of Service Vulnerability
- CVE-2024-35264: .NET Remote Code Execution Vulnerability

* Sat May 18 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.5-alt1
- .NET 8.0.5 release
- CVE-2024-21409: .NET Elevation of Privilege Vulnerability
- CVE-2024-30046: .NET Denial of Service Vulnerability
- CVE-2024-30045: .NET Remote Code Execution Vulnerability
- enable build dotnet-host here

* Fri Apr 05 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.3-alt1
- new version (8.0.3) with rpmgs script

* Sun Feb 18 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.2-alt1
- .NET 8.0.2 release
- CVE-2023-36038: .NET Denial of Service Vulnerability
- CVE-2023-36049: .NET Elevation of Privilege Vulnerability
- CVE-2023-36558: .NET Security Feature Bypass Vulnerability
- CVE-2024-0056: Microsoft.Data.SqlClient and System.Data.SqlClient SQL Data provider Information Disclosure Vulnerability
- CVE-2024-0057: .NET Security Feature bypass Vulnerability
- CVE-2024-21319: .NET Denial of Service Vulnerability
- CVE-2024-21386: .NET Denial of Service Vulnerability
- CVE-2024-21404: .NET Denial of Service Vulnerability

* Mon Jan 08 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0.0.rc.2.23502.2-alt1
- .NET 8.0.0 RC2
- CVE-2023-44487: .NET Denial of Service Vulnerability
- CVE-2023-38171: .NET Denial of Service Vulnerability
- CVE-2023-36435: .NET Denial of Service Vulnerability
- CVE-2023-36792: .NET Remote Code Execution Vulnerability
- CVE-2023-36793: .NET Remote Code Execution Vulnerability
- CVE-2023-36794: .NET Remote Code Execution Vulnerability
- CVE-2023-36796: .NET Remote Code Execution Vulnerability
- CVE-2023-36799: .NET Denial of Service Vulnerability

* Fri Jul 28 2023 Vitaly Lipatov <lav@altlinux.ru> 8.0.0.preview.6.23330.14-alt1
- .NET 8.0.0 preview 6

* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 8.0.0.preview.1.23115.2-alt1
- .NET 8.0.0 preview 1
- initial build for ALT Sisyphus
