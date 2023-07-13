Name: ima-inspect
Summary: Output IMA/EVM extended attributes in a human readable format
License: LGPL-2.1-or-later
Group: System/Base
Version: 0.13
Release: alt2 
Url: https://github.com/mgerstner/ima-inspect
Source0: %{name}-%{version}.tar
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: libimaevm-devel
BuildRequires: openssl-devel
BuildRequires: libtclap-devel

%description
This is a small utility that supplements ima-evm-utils with a way to inspect
the security.ima and security.evm extended attributes in human readable
format.

%prep
%setup -q
%autopatch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
# match name of the package
( cd %{buildroot}%{_bindir}
  ln -s ima_inspect ima-inspect
)

%files
%doc README.md LICENSE
%{_bindir}/ima_inspect
%{_bindir}/ima-inspect

%changelog
* Thu Jul 13 2023 Artyom Bystrov <arbars@altlinux.org> 0.13-alt2
- Fix build on GCC13

* Thu Nov 05 2020 Mikhail Novosyolov <mikhailnov@altlinux.org> 0.13-alt1
- Initial build for Sisyphus (v0.13)

