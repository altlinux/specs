%define _unpackaged_files_terminate_build 1

Name: msbuild
Version: 15.6
Release: alt1%ubt.2018.01.17.14.14
Summary: Microsoft Build Engine (MSBuild), XML-based platform for building applications

Group: Development/Other
License: MIT
Url: https://github.com/Microsoft/msbuild

# https://download.mono-project.com/repo/ubuntu/pool/main/m/msbuild/msbuild_15.6+xamarinxplat.2018.01.17.14.14-0xamarin2+ubuntu1404b1_all.deb
Source: %name-%version.tar

BuildRequires(pre): rpm-build-mono >= 2.0
BuildRequires(pre): rpm-build-ubt
BuildRequires: mono-devel-full

Requires: mono-devel-full

%add_findprov_skiplist %_monodir/xbuild/Microsoft/*
%add_findprov_skiplist %_monodir/msbuild/15.0/bin/System.IO.Compression.dll
%add_findprov_skiplist %_monodir/msbuild/15.0/bin/System.Reflection.Metadata.dll

%add_findreq_skiplist  %_monodir/xbuild/Microsoft/*
%add_findreq_skiplist  %_monodir/msbuild/15.0/bin/System.IO.Compression.dll
%add_findreq_skiplist  %_monodir/msbuild/15.0/bin/System.Reflection.Metadata.dll

# Interfaces of slightly older versions are required, upstream corrects it by modifying 'Requires'
%define __find_provides sh -c '/usr/lib/rpm/find-provides | sort | uniq'
%define __find_requires sh -c '/usr/lib/rpm/find-requires | sort | uniq | grep ^... | \
	sed "s/mono\(System.IO.Compression\).*/mono\(System.IO.Compression\) = 4.0.0.0/" | \
	sed "s/mono\(System.Runtime.InteropServices.RuntimeInformation\).*/mono\(System.Runtime.InteropServices.RuntimeInformation\) = 4.0.3.0/" | \
	sed "s/mono\(System.Security.AccessControl\).*/mono\(System.Security.AccessControl\) = 4.1.0.0/" | \
	sed "s/mono\(System.Security.Principal.Windows\).*/mono\(System.Security.Principal.Windows\) = 4.1.0.0/"'

%description
Microsoft Build Engine (MSBuild), XML-based platform for building applications

%prep
%setup

%install
mkdir -p %buildroot
cp -r . %buildroot/

rm -rf %buildroot%_datadir

%files
%doc usr/share/doc/msbuild/*
%_bindir/msbuild
%_monodir/msbuild/15.0/bin/*
%_monodir/xbuild/*

%changelog
* Tue Jul 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 15.6-alt1%ubt.2018.01.17.14.14
- Initial build for ALT.
