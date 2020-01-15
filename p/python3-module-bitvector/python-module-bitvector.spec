%define oname bitvector

Name: python3-module-%oname
Version: 3.4.4
Release: alt2

Summary: A pure-Python memory-efficient packed representation for bit arrays

License: Python Software Foundation License
Group: Development/Python3
Url: https://engineering.purdue.edu/kak/dist/BitVector-3.4.4.html
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setupdocs


%description
The BitVector.py module is for a memory-efficient packed
representation of bit vectors and for the processing of such
vectors.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python3_build

%install
%python3_install

%files
%doc README
%python3_sitelibdir/*


%changelog
* Wed Jan 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.4.4-alt2
- porting on python3

* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 3.4.4-alt1
- Initial build for ALT

