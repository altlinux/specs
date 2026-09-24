%define _dotnet_major 8.0
%define _dotnet_sdkrelease 8.0.130
%define _dotnet_corerelease 8.0.30
%define llvmver 18.1

Name:    dotnet-diagnostics
Version: %_dotnet_major.505301
Release: alt2

Summary: Various .NET Core runtime diagnostic tools
License: MIT
Group:   Development/Tools
Url:     https://github.com/dotnet/diagnostics

%filter_from_requires /\/usr\/lib64\/dotnet\/tools\/dotnet-\(dump\|sos\)\/dotnet-\(dump\|sos\)/d

Source0: %name-%version.tar
Source1: packages.tar
# Patches to fix fragile macro definitions (va_start/va_end) and VLA in PAL/SOS.
# Refactored for modern Clang and offline sandbox with AI Assistance.
Patch0:  fix-undefd-va-macros.patch
Patch1:  fix-var-length.patch
Patch2:  fix-nontrivial-memcall.patch

ExclusiveArch: x86_64

BuildRequires(pre): rpm-macros-dotnet
BuildRequires: cmake
BuildRequires: /proc
BuildRequires: clang%{llvmver}
BuildRequires: pkgconfig(icu-io)
BuildRequires: liblldb%llvmver-devel
BuildRequires: pkgconfig(libunwind)
BuildRequires: llvm-common
BuildRequires: llvm%llvmver
BuildRequires: libcxx-devel
BuildRequires: dotnet-%_dotnet_major
BuildRequires: dotnet-sdk-%_dotnet_major
BuildRequires: dotnet-aspnetcore-runtime-%_dotnet_major
BuildRequires: jq

Requires: dotnet-runtime-%_dotnet_major

%description
%summary.

%package -n dotnet-dump
Summary:  Simple cross-platform command line tool by .NET Global Tools to collect a dump
Group:    Development/Tools
Requires: dotnet-runtime-%_dotnet_major

%description -n dotnet-dump
This tool is important on restricted Linux platforms where a fully working
lldb isn't available. The dotnet-dump tool allows you to run SOS commands to
analyze crashes and the garbage collector (GC), but it isn't a native debugger
so things like displaying native stack frames aren't supported.

%package -n dotnet-sos
Summary:  SOS (Son of Strike) plugin for LLDB by .NET Global Tools
Group:    Development/Tools
Requires: lldb%llvmver
Requires: python3-module-lldb%llvmver

%description -n dotnet-sos
This extension lets you inspect managed .NET Core state from native debuggers
like LLDB.

%prep
%setup

# Restore preserved NuGet caches
test -d ~/.nuget && rm -rf ~/.nuget
%__mkdir_p ~/.nuget/NuGet
tar xf %SOURCE1 -C ~/.nuget

# Config points to local cache
cat << EOF > nuget.config
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <clear />
    <add key="local-cache" value="$HOME/.nuget/packages" />
  </packageSources>
  <config>
    <add key="globalPackagesFolder" value="$HOME/.nuget/packages" />
    <add key="signatureValidationMode" value="accept" />
  </config>
</configuration>
EOF

# Update toolset version
%__subst "s|%_dotnet_major.1[0-9][0-9]|%_dotnet_sdkrelease|" global.json

# Remove runtimes definition to use the system installed toolset
tee <<< $(jq 'del(.["tools"]["runtimes"])' global.json) > global.json

# Invoke dotnet
%__mkdir_p .dotnet
for dotnetfile in $(ls %_libdir/dotnet); do
    %__ln_s %_libdir/dotnet/$dotnetfile .dotnet/$dotnetfile
done

%autopatch

%build
# Make use the vendored cache and do not try to update
export NUGET_PACKAGES="$HOME/.nuget/packages"
export DOTNET_RESTORE_DISABLE_PARALLEL=true
export DOTNET_SKIP_FIRST_TIME_EXPERIENCE=1
# Some packages signed with outdated keys
export DOTNET_NUGET_SIGNATURE_VERIFICATION=false
# Needs to be used during cache update
export CheckEolTargetFramework=false
# Common preset to use llvm for native parts
export CC="clang"
export CXX="clang++"
export CFLAGS="$CFLAGS -stdlib=libc++ -Wno-macro-redefined -Wno-unused-command-line-argument"
export CXXFLAGS="$CXXFLAGS -stdlib=libc++ -Wno-unused-command-line-argument -Wno-macro-redefined"
export LDFLAGS="$LDFLAGS -stdlib=libc++ -L%_libdir -lc++ -lc++abi"
export LLDB_INCLUDE_DIR=/usr/lib/llvm-%llvmver/include
# Another wichcraft to use system toolset instead of attempts to download and
# install from cloud
export DOTNET_ROOT="%_libdir/dotnet"
export DOTNET_INSTALL_DIR=$DOTNET_ROOT
export PATH="$DOTNET_ROOT:$PATH"
bash -x ./build.sh /p:NoCache=true -c Release

%install
%__mkdir_p %buildroot%_bindir

diag_tools="dotnet-dump dotnet-gcdump dotnet-trace dotnet-counters \
            dotnet-dsrouter dotnet-stack"

for tool in $diag_tools; do
    ToolDir="%_libdir/dotnet/tools/$tool"
    %__mkdir_p "%buildroot$ToolDir"

    AppPath=""
    for config in Debug Release; do
        for tfm in net6.0 net8.0; do
            if [ -d "artifacts/bin/$tool/$config/$tfm/publish/linux-x64" ]; then
                AppPath="artifacts/bin/$tool/$config/$tfm/publish/linux-x64"
                break 2
            elif [ -d "artifacts/bin/$tool/$config/$tfm" ]; then
                AppPath="artifacts/bin/$tool/$config/$tfm"
                break 2
            fi
        done
    done

    if [ -z "$AppPath" ]; then
        echo "Error: Cannot find build artifacts for $tool" >&2
        exit 1
    fi

    if [ -f "$AppPath/$tool" ]; then
        cp -a "$AppPath/$tool" "%buildroot$ToolDir/"
    fi

    find "$AppPath" -maxdepth 1 \( -name "*.dll" -o -name "*.so" -o -name "*.json" \) \
    -exec cp -a {} "%buildroot$ToolDir/" \;

    if [ $tool != "dotnet-dump" ]; then
        %__ln_s "$ToolDir/$tool" "%buildroot%_bindir/$tool"
    fi
done

# Manually pack dotnet-dump
find ./artifacts/bin/dotnet-dump/Release/net6.0 \
-maxdepth 1 \( -name "*.dll" -o -name "*.json" \) \
-exec cp -a {} "%buildroot/%_libdir/dotnet/tools/dotnet-dump" \;

tee << EOF > %buildroot%_bindir/dotnet-dump
#!/bin/bash
DOTNET_HOST="%_bindir/dotnet"

if [ ! -x \$DOTNET_HOST ]; then
    echo "Error: .NET Runtime is not installed or not found at \$DOTNET_HOST" >&2
    exit 1
fi

exec \$DOTNET_HOST "%_libdir/dotnet/tools/dotnet-dump/dotnet-dump.dll" \$@
EOF

%pre -n dotnet-sos
if [ $1 -eq 1 ]; then
    echo "To load the native plugin for LLDB, you need to add the following line"
    echo "to the ~/.lldbinit startup configuration file or execute it in the "
    echo "debugger's command line: "
    echo "plugin load %_libdir/dotnet/tools/dotnet-dump/libsosplugin.so"
fi

%files
%doc README.md LICENSE.TXT
%_bindir/dotnet-gcdump
%_bindir/dotnet-trace
%_bindir/dotnet-counters
%_bindir/dotnet-dsrouter
%_bindir/dotnet-stack
%_libdir/dotnet/tools
%exclude %_libdir/dotnet/tools/dotnet-dump

%files -n dotnet-dump
%attr(755, root, root) %_bindir/dotnet-dump
%_libdir/dotnet/tools/dotnet-dump
%exclude %_libdir/dotnet/tools/dotnet-dump/libsos*.so
%exclude %_libdir/dotnet/tools/dotnet-dump/libdbgshim.so

%files -n dotnet-sos
%doc artifacts/bin/linux.x64.Release/sosdocsunix.txt
%_libdir/dotnet/tools/dotnet-dump/libsos*.so
%_libdir/dotnet/tools/dotnet-dump/libdbgshim.so

%changelog
* Thu Sep 24 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 8.0.505301-alt2
- Moved -dump and -sos components to subpackages (Closes: #60506).

* Thu Sep 03 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 8.0.505301-alt1
- Initial build for Sisyphus.
