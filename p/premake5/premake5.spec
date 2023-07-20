Name: premake5
Version: 5.0.0.beta2
Release: alt1
Summary: Cross-platform build configuration tool

Group: Development/Tools
License: BSD
Url: https://premake.github.io
Source0:%name-%version.tar
Patch0: premake-4.3-system-lua-5.1.patch
Patch1: premake-4.3-system-lua.patch

BuildRequires: make gcc lua5.1-devel liblua5.1-compat-devel libreadline-devel unzip libuuid-devel libssl-devel libcurl libcurl-devel

%description
Premake5 is a build configuration tool that can generate project files for:
 - GNU make
 - Code::Blocks
 - CodeLite
 - MonoDevelop
 - SharpDevelop
 - Apple XCode
 - Microsoft Visual Studio

%prep
%setup -n %name-%version
#%%patch0 -p1
#%%patch1 -p1

%build

# bootstrap your first Premake executable
make -f Bootstrap.mak linux
# generate makefiles
./bin/release/premake5 gmake
# embed and compile Lua scripts into the Premake executable to ship a single
# file instead of a whole bunch of scripts.
./bin/release/premake5 embed
# rebuild
%make_build config=release

%install
rm -rf %buildroot
install -m 755 -Dp ./bin/release/premake5 %buildroot/%_bindir/premake5
install -m 644 -Dp ./packages/debian/premake.1 %buildroot/%_mandir/man1/premake5.1

%files
%_bindir/premake5
%_mandir/man1/premake5.1.xz
%doc LICENSE.txt README.md CHANGES.txt

%changelog
* Tue Jun 20 2023 Artyom Bystrov <arbars@altlinux.org> 5.0.0.beta2-alt1
- initial build for ALT Sisyphus
