Name: zdbsp
Version: 1.19
Release: alt1
Summary: Nodebuilder for ZDoom
License: GPL-2.0+
Group: Games/Other
Url: https://zdoom.org/

Source: %name-%version.tar
BuildRequires: cmake >= 2.4
BuildRequires: gcc-c++
BuildRequires: zlib-devel

%description
ZDBSP is ZDoom's (internal and external) node builder. This node
builder was written with two design goals in mind: speed and
minimization of polyobject bleeding.

%prep
%setup

%build
%cmake_insource

%make_build

%install
%cmake_install

%files
%doc zdbsp.html poly_*.png
%doc COPYING
%_bindir/%name

%changelog
* Sat Aug 28 2021 Artyom Bystrov <arbars@altlinux.org> 1.19-alt1
- initial build for ALT Sisyphus

