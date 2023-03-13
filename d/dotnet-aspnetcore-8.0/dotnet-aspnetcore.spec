%define _unpackaged_files_terminate_build 1

%define _dotnet_major 8.0
%define _dotnet_corerelease 8.0.0-preview.1.23110.8
%define _dotnet_aspnetcorerelease 8.0.0-preview.1.23112.2
%define _dotnet_aspnetcoreapprefrelease 8.0.0-preview.1.23112.2
%define preview .preview.1.23115.2
%define _dotnet_coreshortrelease 8.0.0%preview

# FIXME: build from sources
%def_with bootstrap

Name: dotnet-aspnetcore-%_dotnet_major
Version: 8.0.0%preview
Release: alt1

Summary: ASP.NET is a cross-platform .NET framework for building modern cloud-based web application

License: MIT
Url: https://github.com/dotnet/aspnetcore
Group: Development/Other

Source: %name-%version.tar

ExclusiveArch: aarch64 x86_64

BuildRequires(pre): rpm-macros-dotnet
# TODO = %version

%if_with bootstrap
BuildRequires: dotnet-bootstrap-runtime-%_dotnet_major = %_dotnet_coreshortrelease
#= %version
%define bootstrapdir %_libdir/dotnet-bootstrap-%_dotnet_major
%else
BuildRequires: dotnet
%define bootstrapdir %_dotnetdir
%endif

Requires: dotnet-common = %version

# BuildRequires: libuv

#%remove_optflags -frecord-gcc-switches
#BuildRequires: clang llvm cmake libstdc++-devel

#BuildRequires: libcurl-devel libssl-devel zlib-devel libkrb5-devel

%description
ASP.NET is an open-source and cross-platform framework
for building modern cloud based internet connected applications,
such as web apps, IoT apps and mobile backends.

ASP.NET is a fast, lightweight and modular platform for creating
cross platform web applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.

Just copied managed binaries now.

%package -n dotnet-aspnetcore-runtime-%_dotnet_major
Summary: ASP.NET 6 runtime
Group: Development/Other
#AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoReq: no
AutoProv: no

Requires: dotnet-runtime-%_dotnet_major = %version

%description -n dotnet-aspnetcore-runtime-%_dotnet_major
The ASP.NET runtime contains everything needed to run .NET Core
web applications. It includes a high performance Virtual Machine as
well as the framework libraries used by .NET Core applications.

ASP.NET is a fast, lightweight and modular platform for creating
cross platform web applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.


%package -n dotnet-aspnetcore-targeting-pack-%_dotnet_major
Summary: ASP.NET 6 targeting pack
Group: Development/Other
#AutoReq: yes,nomingw32,nomingw64,nomono,nomonolib
AutoReq: no
AutoProv: no

#Requires: dotnet-targeting-pack-%_dotnet_major

%description -n dotnet-aspnetcore-targeting-pack-%_dotnet_major
The ASP.NET runtime contains everything needed to run .NET Core
web applications. It includes a high performance Virtual Machine as
well as the framework libraries used by .NET Core applications.

ASP.NET is a fast, lightweight and modular platform for creating
cross platform web applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.


%prep
%setup

%install
mkdir -p %buildroot%_dotnet_aspnetcoreapp

%if_with bootstrap
cp -a %bootstrapdir/shared/Microsoft.AspNetCore.App/%_dotnet_aspnetcorerelease/.version %buildroot%_dotnet_aspnetcoreapp
cp -a %bootstrapdir/shared/Microsoft.AspNetCore.App/%_dotnet_aspnetcorerelease/*.dll %buildroot%_dotnet_aspnetcoreapp
cp -a %bootstrapdir/shared/Microsoft.AspNetCore.App/%_dotnet_aspnetcorerelease/*.json %buildroot%_dotnet_aspnetcoreapp

mkdir -p %buildroot%_dotnet_aspnetcoreappref/
cp -a %bootstrapdir/packs/Microsoft.AspNetCore.App.Ref/%_dotnet_aspnetcoreapprefrelease/* %buildroot%_dotnet_aspnetcoreappref/
%endif


%files -n dotnet-aspnetcore-runtime-%_dotnet_major
%dir %_dotnetdir/shared/Microsoft.AspNetCore.App/
%dir %_dotnet_aspnetcoreapp/
%_dotnet_aspnetcoreapp/.version
%_dotnet_aspnetcoreapp/Microsoft.AspNetCore.App.deps.json
%_dotnet_aspnetcoreapp/Microsoft.AspNetCore.App.runtimeconfig.json
%_dotnet_aspnetcoreapp/*.dll

%files -n dotnet-aspnetcore-targeting-pack-%_dotnet_major
%dir %_dotnetdir/packs/
%dir %_dotnetdir/packs/Microsoft.AspNetCore.App.Ref/
%_dotnet_aspnetcoreappref/

%changelog
* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 8.0.0.preview.1.23115.2-alt1
- ASP.NET 8.0.0 preview
- initial release for ALT Sisyphus
