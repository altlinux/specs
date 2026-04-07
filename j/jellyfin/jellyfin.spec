%define dotnetver 9.0
%define OutputPath64 server

Name:    jellyfin
Version: 10.11.8
Release: alt1

Summary: The Free Software Media System - Server Backend & API
License: GPL-2.0
Group:   Video
Url:     https://jellyfin.org
Vcs:     https://github.com/jellyfin/jellyfin.git

Source0: %name-%version.tar
Source1: packages.tar
Source2: %name.service
Source3: %name.sysusers

BuildRequires: dotnet-sdk-%dotnetver
BuildRequires: /proc
BuildRequires: pkgconfig(fontconfig)

Requires: %name-web
Requires: ffmpeg
Requires: ffprobe

ExclusiveArch: x86_64

%description
%summary.

%prep
%setup
# Restore preserved NuGet caches
test -d ~/.nuget && rm -rf ~/.nuget
%__mkdir_p ~/.nuget/NuGet
tar xf %SOURCE1 -C ~/.nuget

# Config points to local cache
cat >> ~/.nuget/NuGet/NuGet.Config <<EOF
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <clear />
    <add key="local" value="$HOME/.nuget/NuGet" />
  </packageSources>
  <config>
    <add key="signatureValidationMode" value="accept" />
  </config>
</configuration>
EOF

%build
export DOTNET_NUGET_SIGNATURE_VERIFICATION=false
export DOTNET_CLI_TELEMETRY_OPTOUT=1
export DOTNET_SKIP_FIRST_TIME_EXPERIENCE=1

dotnet publish Jellyfin.Server --arch x64 --configuration Release \
    --output=%OutputPath64 --self-contained \
    -p:NuGetAudit=false \
    -p:DebugSymbols=false -p:DebugType=none

%install
mkdir -p %buildroot%_libexecdir/%name
cp -Rfv server/* %buildroot%_libexecdir/%name
mkdir -p %buildroot%_bindir
ln -s %_libexecdir/%name/%name %buildroot%_bindir/%name
install -Dp %SOURCE2 %buildroot%_unitdir/%name.service
install -Dp %SOURCE3 %buildroot%_sysusersdir/%name.conf
install -d %buildroot%_sharedstatedir/%name

%pre
if [ $1 -eq 1 ]; then
    %sysusers_create_package %name %SOURCE3
fi

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service
%files
%doc *.md
%_bindir/%name
%_libexecdir/%name
%_unitdir/%name.service
%_sysusersdir/%name.conf
%dir %attr(2770,%name,%name) %_sharedstatedir/%name

%changelog
* Tue Apr 07 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 10.11.8-alt1
- Initial build for Sisyphus(Closes: #45039, #55283).
