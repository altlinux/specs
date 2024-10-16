# TODO: dropout dotnet-common package with dirs
%define _dotnet_archlist aarch64 x86_64

%ifarch x86_64
%define _dotnet_arch x64
%else
%ifarch aarch64
%define _dotnet_arch arm64
%else
%define _dotnet_arch %arch
%endif
%endif
%define _dotnet_rid linux-%_dotnet_arch

Name: dotnet-common
Version: 6.0.1
Release: alt2

Summary: Common dir and files for the .NET Core runtime and libraries

License: MIT
Group: Development/Other

Source: %name-%version.tar

#ExclusiveArch: %_dotnet_archlist

%description
Common dir and files for the .NET runtime and libraries.

%package -n rpm-macros-dotnet
Summary: RPM macros for build dotnet packages
Group: Development/Other

%description -n rpm-macros-dotnet
RPM macros for build dotnet packages.

%prep
%setup

cat <<EOF >macros
# define in your spec:
#_dotnet_major
#_dotnet_corerelease
#_dotnet_sdkrelease
#_dotnet_coreapprefrelease
#_dotnet_aspnetcorerelease
#_dotnet_aspnetcoreapprefrelease
#_dotnet_templatesrelease
#_dotnet_netstandartrelease
#_dotnet_sdkmanifestsrelease

%%dotnet_arches %_dotnet_archlist
%%_dotnet_archlist %_dotnet_archlist
%%_dotnet_rid %_dotnet_rid
%%_dotnet_arch %_dotnet_arch
%%_dotnetdir %_libdir/dotnet
%%_dotnet_hostfxr %%_dotnetdir/host/fxr/%%_dotnet_corerelease/
%%_dotnet_coreapp %%_dotnetdir/shared/Microsoft.NETCore.App/%%_dotnet_corerelease
%%_dotnet_coreapphost %%_dotnetdir/packs/Microsoft.NETCore.App.Host.%%_dotnet_rid/%%_dotnet_corerelease
%%_dotnet_coreappref %%_dotnetdir/packs/Microsoft.NETCore.App.Ref/%%_dotnet_coreapprefrelease
%%_dotnet_aspnetcoreapp %%_dotnetdir/shared/Microsoft.AspNetCore.App/%%_dotnet_aspnetcorerelease
%%_dotnet_aspnetcoreappref %%_dotnetdir/packs/Microsoft.AspNetCore.App.Ref/%%_dotnet_aspnetcoreapprefrelease
%%_dotnet_templates %%_dotnetdir/templates/%%_dotnet_templatesrelease
%%_dotnet_netstandart %%_dotnetdir/packs/NETStandard.Library.Ref/%%_dotnet_netstandartrelease
%%_dotnet_sdk %%_dotnetdir/sdk/%%_dotnet_sdkrelease
%%_dotnet_sdkmanifests %%_dotnetdir/sdk-manifests/%%_dotnet_sdkmanifestsrelease

%%_dotnet_corepkgrelease %%(echo "%%_dotnet_corerelease" | sed -e "s|\-|.|g")
%%_dotnet_sdkpkgrelease %%(echo "%%_dotnet_sdkrelease" | sed -e "s|\-|.|g")

# for compatibility
%%_dotnet_apphostdir %%_dotnetdir/packs/Microsoft.NETCore.App.Host.%%_dotnet_rid/%%_dotnet_corerelease
%%_dotnet_shared %%_dotnetdir/shared/Microsoft.NETCore.App/%%_dotnet_corerelease
%%_dotnet_appref %%_dotnetdir/packs/Microsoft.NETCore.App.Ref/%%_dotnet_apprefrelease
EOF

%install
mkdir -p %buildroot%_libdir/dotnet/
mkdir -p %buildroot%_libdir/dotnet/shared/Microsoft.NETCore.App/
mkdir -p %buildroot%_libdir/dotnet/host/fxr/
mkdir -p %buildroot%_libdir/dotnet/packs/
mkdir -p %buildroot%_libdir/dotnet/templates/

install -D -m644 macros %buildroot%_rpmmacrosdir/dotnet

%files
%dir %_libdir/dotnet/

%dir %_libdir/dotnet/host/
%dir %_libdir/dotnet/host/fxr/

%dir %_libdir/dotnet/packs/
%dir %_libdir/dotnet/templates/

%dir %_libdir/dotnet/shared/
%dir %_libdir/dotnet/shared/Microsoft.NETCore.App/

%files -n rpm-macros-dotnet
%_rpmmacrosdir/dotnet

%changelog
* Sat Apr 06 2024 Vitaly Lipatov <lav@altlinux.ru> 6.0.1-alt2
- add dotnet_arches (as other *_arches)

* Fri Jul 16 2021 Vitaly Lipatov <lav@altlinux.ru> 6.0.1-alt1
- cleanup to .NET 6
 + add _dotnet_sdk_manifests
 + add _dotnet_corepkgrelease, _dotnet_sdkpkgrelease

* Tue Feb 23 2021 Vitaly Lipatov <lav@altlinux.ru> 6.0-alt1
- improve _dotnet_ macros

* Sat Feb 20 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0-alt1
- cleanup to .NET 5

* Mon Aug 03 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.6-alt1
- .NET Core 3.1.6 release

* Mon Dec 30 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt2
- make rpm-macros-dotnet available on all arches

* Mon Dec 16 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- .NET Core 3.1.0 release

* Sat Oct 05 2019 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- .NET Core 3.0.0 release

* Wed Mar 13 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt1
- .NET Core 2.1.9 release

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
