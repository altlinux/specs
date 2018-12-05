%define corerelease 2.1.6
%define sdkrelease 2.1.500

Name: dotnet-common
Version: 2.1.6
Release: alt2

Summary: Common dir and files for the .NET Core runtime and libraries

License: MIT
Group: Development/Other

Source: %name-%version.tar

%description
Common dir and files for the .NET Core runtime and libraries.

%package -n rpm-macros-dotnet
Summary: RPM macros for build dotnet packages
Group: Development/Other

%description -n rpm-macros-dotnet
RPM macros for build dotnet packages.

%prep
%setup

# make scripts happy
cat <<EOF >fake-os-release
NAME="GNU/Linux"
VERSION=""
ID=linux
VERSION_ID=""
EOF

cat <<EOF >fake-os-release-fedora
NAME="Fedora"
VERSION="26"
ID=fedora
VERSION_ID="26"
EOF

cat <<EOF >macros
%%_dotnet_corerelease %corerelease
%%_dotnet_sdkrelease %sdkrelease
%%_dotnetdir %_libdir/dotnet
%%_dotnet_hostfxr %%_dotnetdir/host/fxr/%%_dotnet_corerelease/
%%_dotnet_shared %%_dotnetdir/shared/Microsoft.NETCore.App/%%_dotnet_corerelease/
%%_dotnet_sdk %%_dotnetdir/sdk/%%_dotnet_sdkrelease/
EOF


%install
mkdir -p %buildroot%_libdir/dotnet/
mkdir -p %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/
mkdir -p %buildroot%_libdir/dotnet/host/fxr/

install -m644 fake-os-release %buildroot%_libdir/dotnet/fake-os-release
install -m644 fake-os-release-fedora %buildroot%_libdir/dotnet/fake-os-release-fedora


install -D -m644 macros %buildroot%_rpmmacrosdir/dotnet


%files
%dir %_libdir/dotnet/
%_libdir/dotnet/fake-os-release
%_libdir/dotnet/fake-os-release-fedora

%dir %_libdir/dotnet/host/
%dir %_libdir/dotnet/host/fxr/

%dir %_libdir/dotnet/shared/
%dir %_libdir/dotnet/shared/Microsoft.NETCore.App/

%files -n rpm-macros-dotnet
%_rpmmacrosdir/dotnet

%changelog
* Wed Dec 05 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt2
- move versioned dirs to the appropriate packages

* Tue Dec 04 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- .NET Core 2.1.6 release

* Fri Oct 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.5-alt1
- NMU: .NET Core 2.1.5 release (based on changes by lav@).

* Sat Sep 15 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.4-alt1
- .NET Core 2.1.4 release

* Mon Sep 03 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- .NET Core 2.1.3 release

* Tue Jan 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- build 2.0.5 release
- CVE-2018-0764, CVE-2018-0786

* Thu Nov 23 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- build 2.0.3 release

* Mon Aug 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt4
- .NET Core 2.0.0 release
- add subpackage rpm-macros-dotnet

* Wed Jul 12 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt3.preview2
- .NET Core 2.0.0 Preview 2 (2.0.0-preview2-25407-01)

* Tue Jun 13 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2
- use linux-64 in fake-os-release

* Thu May 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1.preview1
- use full corerelease

* Mon May 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.preview1
- .NET Core 2.0.0 Preview 1
