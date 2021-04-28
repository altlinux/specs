%define _unpackaged_files_terminate_build 1

Name:           nuget
Version:        2.8.7
Release:        alt1
Summary:        Package manager for .Net/Mono development platform
Group:          Development/Other
License:        Apache-2.0
Url:            http://nuget.org/

# http://download.mono-project.com/sources/%name/%name_%{version}+md510+dhx1.orig.tar.bz2
Source0:        %name-%version.tar
Source1:        nuget-core.pc
Source2:        nuget.sh
Patch0:         nuget-fix_xdt_hintpath.patch

BuildRequires(pre): rpm-build-mono
BuildRequires: mono-devel mono-winfx

%description
NuGet is the package manager for the Microsoft
development platform including .NET. The NuGet client
tools provide the ability to produce and consume
packages. The NuGet Gallery is the central package
repository used by all package authors and consumers.

%package        devel
Summary:        Development files for %name
Group:          Development/Other
Requires:       %name = %EVR

%description devel
Development package for %name

%prep
%setup
sed -i "s/\r//g" src/Core/Core.csproj
%patch0 -p1

# fix compile with Mono4
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;

%build
xbuild xdt/XmlTransform/Microsoft.Web.XmlTransform.csproj
xbuild src/Core/Core.csproj /p:Configuration="Mono Release"
xbuild src/CommandLine/CommandLine.csproj /p:Configuration="Mono Release"

%install
mkdir -p %buildroot%_monodir/nuget
mkdir -p %buildroot%_libdir/pkgconfig
mkdir -p %buildroot%_bindir
install -m0644 %{SOURCE1} %buildroot%_pkgconfigdir/
install -m0755 %{SOURCE2} %buildroot%_bindir/$(basename -s .sh %{SOURCE2})
sed -i -e 's/cli/mono/' %buildroot%_bindir/*
install -m0755 src/CommandLine/bin/Release/NuGet.Core.dll %buildroot%_monodir/nuget/
install -m0755 xdt/XmlTransform/bin/Debug/Microsoft.Web.XmlTransform.dll %buildroot%_monodir/nuget/
install -m0755 src/CommandLine/bin/Release/NuGet.exe %buildroot%_monodir/nuget/

%files
%doc LICENSE.txt COPYRIGHT.txt
%doc acknowledgements.md changelog.md CREDITS.txt
%_monodir/nuget
%_bindir/*

%files devel
%_pkgconfigdir/nuget-core.pc

%changelog
* Fri Apr 23 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.7-alt1
- Initial build for ALT.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.7-2
- mono rebuild for aarch64 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.8.7-0
- upgrade to 2.8.7 for MonoDevelop 5.10

* Mon Jul 06 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.8.5-2
- Split pc file into devel subpackage
- Use license macro
- Move pc file to _libdir instead datadir

* Fri Jul 03 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.8.5-1
- Update to 2.8.5
- Move nuget into monodir
- Fix licence

* Wed Jun 03 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.8.3-3
- Fix empty debug_package

* Wed May 20 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.8.3-2
- Use xbuild option to build with mono 4
- Use global insted define

* Thu Apr 16 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.8.3-1
- build with Mono4

* Thu Apr 16 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.8.3-0
- copy from Xamarin nuget spec
