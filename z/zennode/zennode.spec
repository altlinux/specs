Name: zennode
Version: 1.2.1
Release: alt1.1
Summary: ZenNode is a node/blockmap/reject builder
Group: Development/Tools
License: GPL2
Url: https://www.mrousseau.org/programs/ZenNode/

Source: %name-%version.tar

BuildRequires: gcc gcc-c++
BuildRequires: make

Conflicts: ImageMagick-tools

%description
ZenNode is a node/blockmap/reject builder written
by Marc Rousseau. It is very fast
(especially the reject builder) and produces nodes
that work well with GL source ports. For example,
it makes OpenGL holes disappear almost entirely in Doom Legacy.

ZenNode supports both Doom and Hexen level formats

%prep
%setup

%build
cd ZenNode
%make_build

%install
rm -f ZenNode/*.cpp ZenNode/*.o ZenNode/*.hpp ZenNode/makefile
mkdir -p %buildroot%_bindir
install -Dm0755 ZenNode/* %buildroot%_bindir

%files
%doc COPYING README
%_bindir/bspdiff
%_bindir/bspinfo
%_bindir/compare
%_bindir/ZenNode

%changelog
* Thu Aug 22 2024 Artyom Bystrov <arbars@altlinux.org> 1.2.1-alt1.1
- Add conflict with ImageMagick-tools (ALTBUG#51233)

* Sat Jan 09 2021 Artyom Bystrov <arbars@altlinux.org> 1.2.1-alt1
- initial build for ALT Sisyphus
 
