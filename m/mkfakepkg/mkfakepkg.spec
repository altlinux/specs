Name: mkfakepkg
Version: 0.1
Release: alt1

Summary: Make fake requires-only package from set of files
License: GPL
Group: Development/Other
Source0: mkfakepkg
BuildArch: noarch
Requires: rpm-build

%description
Make fake requires-only package from set of files to
control unmanaged files dependences

%prep

%build

%install
mkdir -p %buildroot%_bindir
install %SOURCE0 %buildroot%_bindir

%files
%_bindir/*

%changelog
* Thu Sep 20 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.1-alt1
- first build



