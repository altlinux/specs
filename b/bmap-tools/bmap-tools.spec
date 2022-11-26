Name: bmap-tools
Version: 3.6
Release: alt2

Summary: The better dd for embedded projects, based on block maps.

License: GPL-2.0
Group: Development/Python3
Url: https://github.com/intel/bmap-tools

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: rpm-build-python3

%description
bmaptool is a generic tool for creating the block map (bmap) for
a file and copying files using the block map. The idea is that
large files, like raw system image files, can be copied or flashed
a lot faster and more reliably with bmaptool than with traditional
tools, like dd or cp.

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install
install -d %{buildroot}/%{_mandir}/man1
install -m644 docs/man1/bmaptool.1 %{buildroot}/%{_mandir}/man1

%files
%_bindir/bmaptool
%{_mandir}/man1/bmaptool.1*
%python3_sitelibdir/bmaptools/
%python3_sitelibdir/*.egg-*

%changelog
* Sat Nov 26 2022 Vladimir Didenko <cow@altlinux.org> 3.6-alt2
- Pack man page

* Fri Nov 25 2022 Vladimir Didenko <cow@altlinux.org> 3.6-alt1
- Initial build for Sisyphus
