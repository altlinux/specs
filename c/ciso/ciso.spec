Name:     ciso
Version:  1.0.2
Release:  alt1

Summary:  Simple commandline utility to compress PSP iso files
License:  GPLv2
Group:    File tools
Url:      https://github.com/jamie/ciso

Patch0: ciso-1.0.2-use-defined-CC.patch

# Source-url: https://github.com/jamie/ciso/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: pkgconfig(zlib)

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%make_build

%install
mkdir -p %buildroot%_bindir
%makeinstall_std

%files
%doc README.markdown
%_bindir/%name

%changelog
* Mon Apr 08 2024 Roman Alifanov <ximper@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus.
