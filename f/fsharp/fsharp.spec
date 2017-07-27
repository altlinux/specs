Name: fsharp
Version: 4.0.0.4
Release: alt1

Summary:        F# compiler, core library and core tools
License:        Apache-2.0
Group:          Development/Other
Url:            http://fsharp.github.io/fsharp/

Source: %name-%version.tar.gz
Patch1: %name-%version-debian-mono5.patch
Patch2: %name-%version-debian-bootstrap.patch
Patch3: %name-%version-debian-no-nuget.patch
Patch4: %name-%version-debian-cli-policy.patch

BuildPreReq: rpm-build-mono >= 2.0.0
BuildPreReq: mono-core >= 5.0.0.0
BuildPreReq: mono-devel >= 5.0.0.0
BuildPreReq: mono-winforms >= 5.0.0.0
BuildPreReq: mono-monodoc-devel >= 1.0

BuildRequires: /proc
BuildRequires: autoconf
BuildRequires: automake

%description
F# is a mature, open source, functional-first programming language
which empowers users and organizations to tackle complex computing
problems with simple, maintainable and robust code. It is used in
a wide range of application areas and is available across multiple
platforms.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%autoreconf
%configure
%make

%install
%makeinstall_std
rm -rf %buildroot%_monodir/monodroid
rm -rf %buildroot%_monodir/monotouch

%files
%_bindir/fsharp*
%_monodir/4.5/*
%_monodir/fsharp*
%_monodir/Microsoft*
%_monodir/gac/FSharp.*/
%_monodir/gac/policy.*.FSharp.Core/
%_monodir/xbuild/Microsoft/VisualStudio/

%changelog
* Mon Jul 24 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0.4-alt1
- Initial build for ALT
