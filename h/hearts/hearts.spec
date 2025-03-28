Name: hearts
Version: 1.9.4
Release: alt1
Summary: The card game Hearts
License: MIT
Group: Games/Other

Url: https://github.com/Rescator7/Hearts
Vcs: https://github.com/Rescator7/Hearts.git

ExcludeArch: %ix86

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-qt6
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel
BuildRequires: liballegro5.2-devel

%description
The card game Hearts.
Playing online or offline against computers.

%prep
%setup

%build
%qmake_qt6
%make_build

%install
mkdir -p %buildroot%_bindir
cp Hearts %buildroot%_bindir/

%files
%doc README.md
%_bindir/Hearts

%changelog
* Tue Mar 27 2025 Vitaly Churkin <chur1q@altlinux.org> 1.9.4-alt1
- Initial build for Sisyphus.
