Name: ipxe-chainload
Version: 1.0.0
Release: alt1
Summary: iPXE chainload modules
Group: System/Base
License: GPL or UBDL
URL: https://ipxe.org
# git://git.ipxe.org/ipxe.git
Source: %{name}-%{version}.tar.xz
BuildRequires: liblzma-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
ExclusiveArch: x86_64

%add_verify_elf_skiplist %_datadir/%name/*
%add_findreq_skiplist %_datadir/%name/*

%description
iPXE is the open source network boot firmware. This package
contains ipxe.efi and undionly.kpxe chainloaders.

%prep
%setup -q -n %{name}-%{version}

%build
cd src
%make bin/undionly.kpxe bin-x86_64-efi/ipxe.efi

%install
rm -rf %buildroot
mkdir -p %buildroot%_datadir/%name
install -m 644 \
  src/bin/undionly.kpxe \
  src/bin-x86_64-efi/ipxe.efi \
  %buildroot%_datadir/%name/

%clean
rm -rf %buildroot %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%dir %_datadir/%name
%_datadir/%name/*
%doc *.example COPYING.*

%changelog
* Thu Aug 09 2018 Gremlin from Kremlin <gremlin@altlinux.org> 1.0.0-alt1
- first build

