%define repo memory_allocator

Name: python3-module-memory-allocator
Version: 0.1.3
Release: alt1
Summary: An extension class to allocate memory easily with cython
License: LGPL-3.0+ and GPL-3.0
Group: Development/Python3
Url: https://github.com/sagemath/memory_allocator

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires: rpm-build-python3 python3-module-Cython python3-module-setuptools python3-module-wheel

%description
%summary.
This extension class started as part of the Sage software.

%prep
%setup -n %repo-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc AUTHORS LICENSE README.md
%python3_sitelibdir/%{repo}*

%changelog
* Tue Aug 16 2022 Leontiy Volodin <lvol@altlinux.org> 0.1.3-alt1
- New version (0.1.3).
- Ported to %%pyproject macros.

* Fri Oct 15 2021 Leontiy Volodin <lvol@altlinux.org> 0.1.2-alt1
- New version (0.1.2).

* Sat Oct 02 2021 Leontiy Volodin <lvol@altlinux.org> 0.1.1-alt1
- New version (0.1.1).

* Wed Sep 29 2021 Leontiy Volodin <lvol@altlinux.org> 0.1.0-alt1
- Initial build for ALT Sisyphus.
- Built as part of sagemath.
