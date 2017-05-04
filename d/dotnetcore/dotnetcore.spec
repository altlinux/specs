# TODO: drop libuv build
# TODO: build managed libraries too
# http://destek.serbestinternet.com/rhel7/rhel-7-server-dotnet-rpms/Packages/
Name: dotnetcore
Version: 1.1.0
Release: alt2

Summary: .NET Core CLI tools and run-time

Group: Development/Other
Url: https://github.com/dotnet/
License: MIT and ASL 2.0

ExclusiveArch: x86_64

#Requires:	bash
#Requires:	libcurl
#Requires:	libunwind
#Requires:	libuv

AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib

%add_verify_elf_skiplist *.dbg

# TODO:
# verify-elf: WARNING: ./usr/lib64/dotnet/shared/Microsoft.NETCore.App/1.1.1/Linux.x64.Release/libcoreclr.so: eu-elflint failed
# the file containing the function 'CoreDllMain' might not be compiled with -fpic/-fPIC
# verify-elf: ERROR: ./usr/lib64/dotnet/shared/Microsoft.NETCore.App/1.1.1/Linux.x64.Release/libcoreclr.so: TEXTREL entry found: 0x0000000000000000
%set_verify_elf_method relaxed

BuildRequires: clang = 3.8.0
BuildRequires: cmake llvm gcc-c++ libstdc++-devel libunwind-devel liblttng-ust-devel liblwp-devel
#BuildRequires: liblldb-devel
BuildRequires: libicu-devel libuuid-devel zlib-devel libcurl-devel libkrb5-devel openssl-devel
BuildRequires: git-core python-base python-modules-json python-modules-xml

BuildRequires: dotnet-bootstrap

# for /etc/os-release
#BuildRequires(pre): branding-alt-sisyphus-release
# fedora-release

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: dotnetcore-%version.tar
#%global		rhel_srpm 		rh-dotnetcore11-dotnetcore-1.1-3.el7.src.rpm
#%global		payload_tarball 	dotnet-dev-rhel-x64.1.0.0-preview2-1-003175.tar.gz
#%global		srpm_sha256 		514a5b36e777172965aed9c3575abaf26f61feec22bf771075abde9878b75436
#%define payload_tarball dotnet-dev.tar.gz
# dotnet build script compat
%define distro altlinux.sisyphus
#define distro %((cat /etc/os-release ; echo 'echo "$ID.$VERSION_ID"') | sh -)
%define payload_tarball dotnet-dev-%distro-x64.%version-preview2-002733.tar.gz
# Use the upstream license file.
# https://github.com/dotnet/core-setup/issues/676
#Source1: 	https://raw.githubusercontent.com/dotnet/core-setup/release/%version/LICENSE

%define bootstrap_commit 	c5b6d002c1b3c9466041c3491ea04c83b7349cf8
%define coreclr_commit 		1735a1d453677717e68803da6a85284d15dca891
%define corefx_commit 		e02adc60844d53991bfba296b738d2e007f470f7
%define core_setup_commit 	928f77c4bc3f49d892459992fb6e1d5542cb5e86

# Source2-url: 	%{url}core/archive/%bootstrap_commit.tar.gz
Source2: %name-%version-bootstrap.tar

# Source3-url:	%{url}coreclr/archive/%coreclr_commit.tar.gz
Source3: %name-%version-coreclr.tar

# Source4-url:	%{url}corefx/archive/%corefx_commit.tar.gz
Source4: %name-%version-corefx.tar

# Source5-url:	%{url}core-setup/archive/%core_setup_commit.tar.gz
Source5: %name-%version-core-setup.tar

# https://github.com/dotnet/core/blob/bootstrap/tools/dotnet-bootstrap/dotnet.bootstrap.py#L363
%global		libuv_version 		1.9.0
%global		libuv_commit 		229b3a4cc150aebd6561e6bd43076eafa7a03756
# Source6-url:	https://github.com/libuv/libuv/archive/%libuv_commit.tar.gz
Source6: %name-%version-libuv.tar

# This patch fixes wrong corefx path in the rover tool
# Not in the upstream yet
Patch: dotnetcore-1.1-rover.patch
# This patch is for adding Fedora 25 and Fedora 26 to Microsoft.NETCore.App supported runtimes in the payload
# Upstream: Not in the upstream yet
Patch1: dotnetcore-1.1-RIL-payload.patch
# This patch is for including debug info into shared object files. That info is then stripped into a separate package.
# Upstream: Not in the upstream yet
Patch2: dotnetcore-1.1-debuginfo-fix.patch
# This patch is for adding Fedora 25 and Fedora 26 to corefx platform runtimes.json
# Upstream: Not in the upstream yet
Patch3: dotnetcore-1.1-RIL-fix.patch
# https://github.com/dotnet/coreclr/pull/8470
Patch4: dotnetcore-1.1-lttng-ust-header.patch
# https://github.com/dotnet/coreclr/pull/8311
Patch5: dotnetcore-1.1-clang3.9.patch
# https://github.com/dotnet/coreclr/pull/7865
Patch6: dotnetcore-1.1-ex.patch

%description
.NET Core is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, Mac and Windows.

.NET Core contains a run-time conforming to the .NET standards, a set
of framework libraries, an SDK containing compilers and a 'dotnet'
application to drive everything.

%prep
%setup

# FIXME
cat <<EOF >os-release
NAME="Sisyphus"
VERSION="sisyphus"
ID=altlinux
VERSION_ID="sisyphus"
EOF

export BASEDIR=$(pwd)

# Unpack rover script and patch it
tar xf %SOURCE2 && mv %name-%version-bootstrap core-bootstrap
cd core-bootstrap/tools/dotnet-bootstrap
%patch0

# SRPM check against the known checksum / unpack it for patching
#echo "%srpm_sha256  %_builddir/%name-%version/%rhel_srpm" | sha256sum -c
#rpm2cpio %_builddir/%name-%version/%rhel_srpm | cpio -idm

# Patch the payload (Microsoft.NETCore.App supported runtimes are carried over...) and repack it
#tar xf %payload_tarball && rm %payload_tarball
#%patch1
cp -a %_libdir/dotnet-bootstrap/* .
tar czf %payload_tarball LICENSE.txt ThirdPartyNotices.txt dotnet host sdk shared

mkdir -p %distro-x64-dotnet/src && cd %distro-x64-dotnet/src

tar xf %SOURCE3 && mv %name-%version-coreclr coreclr
tar xf %SOURCE4 && mv %name-%version-corefx corefx
tar xf %SOURCE5 && mv %name-%version-core-setup core-setup
tar xf %SOURCE6 && mv %name-%version-libuv libuv

%patch2
%patch3
%patch4
%patch5
%patch6

# temp. disable lldb using
%__subst "s|add_subdirectory.*lldbplugin.*||" coreclr/CMakeLists.txt

cp -a $BASEDIR/coreclr/init-tools.sh coreclr/

cd $BASEDIR
find -type f -name "*.sh" | xargs subst "s|/etc/os-release|$BASEDIR/os-release|g"
# python build script
find -type f -name "*.py" | xargs subst "s|/etc/os-release|$BASEDIR/os-release|g"

%build
# export CFLAGS=${RPM_OPT_FLAGS} - Fedora/RH enforced compiler flags (build fails with them...)
cd core-bootstrap/tools/dotnet-bootstrap/
./dotnet.bootstrap.py -payload %payload_tarball

%install
install -d -m 0755 %buildroot%_libdir/%name/
cp -arf core-bootstrap/tools/dotnet-bootstrap/%distro-x64-dotnet/bin/* %buildroot%_libdir/%name/
%__subst "s|.*libsosplugin.so.*||g" %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/1.1.1/Microsoft.NETCore.App.deps.json
install -m 0644 LICENSE %buildroot%_libdir/%name/

install -d -m 0755 %buildroot%_bindir
ln -s %_libdir/%name/dotnet %buildroot/%_bindir/

# FIXME: version mismatch
cp -f %_libdir/dotnet-bootstrap/shared/Microsoft.NETCore.App/1.1.1/libhostpolicy.so %buildroot%_libdir/%name/shared/Microsoft.NETCore.App/1.1.1/libhostpolicy.so

%files
%_libdir/%name
%_bindir/dotnet
%doc LICENSE
%doc core-bootstrap/tools/dotnet-bootstrap/README.md
%doc core-bootstrap/tools/dotnet-bootstrap/ThirdPartyNotices.txt

%changelog
* Thu May 04 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- add fake /etc/os-release
- override libhostpolicy.so

* Fri Apr 21 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version (1.1.0) with rpmgs script

* Thu Mar 16 2017 Nemanja Milošević <nmilosevnm@gmail.com> - 1.1.0-7
- rebuilt with latest libldb
* Wed Feb 22 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-6
- compat-openssl 1.0 for F26 for now
* Sun Feb 19 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-5
- Fix wrong commit id's
* Sat Feb 18 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-4
- Use commit id's instead of branch names
* Sat Feb 18 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-3
- Improper patch5 fix
* Sat Feb 18 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-2
- SPEC cleanup
- git removal (using all tarballs for reproducible builds)
- more reasonable versioning
* Thu Feb 09 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-1
- Fixed debuginfo going to separate package (Patch1)
- Added F25/F26 RIL and fixed the version info (Patch2)
- Added F25/F26 RIL in Microsoft.NETCore.App suported runtime graph (Patch3)
- SPEC file cleanup
* Wed Jan 11 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-0
- Initial RPM for Fedora 25/26.

