%define oname hawkmoth

Name:    python3-module-%oname
Version: 0.22.0
Release: alt1

Summary: Hawkmoth - Sphinx Autodoc for C

Group:   Development/Python3
License: BSD-2-Clause
URL:     https://pypi.org/project/hawkmoth/
Vcs:     https://github.com/jnikula/hawkmoth

Source0: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel python3-module-sphinx
BuildRequires: python3-module-hatchling

%description
Hawkmoth is a minimalistic Sphinx C and C++ Domain autodoc directive extension
to incorporate formatted C and C++ source code comments written in
reStructuredText into Sphinx based documentation. It uses Clang Python Bindings
for parsing, and generates C and C++ Domain directives for C and C++ API
documentation, and more. In short, Hawkmoth is Sphinx Autodoc for C/C++.

Hawkmoth aims to be a compelling alternative for documenting C and C++ projects
using Sphinx, mainly through its simplicity of design, implementation and use.

%prep
%setup -n %oname-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst LICENSE
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Fri Nov 14 2025 L.A. Kostis <lakostis@altlinux.ru> 0.22.0-alt1
- 0.22.0.
- Update SPDX License type.

* Tue Oct 29 2024 L.A. Kostis <lakostis@altlinux.ru> 0.19.0-alt1
- 0.19.0.
- BR: added hatchling module.

* Thu Aug 22 2024 L.A. Kostis <lakostis@altlinux.ru> 0.18.0-alt1
- Initial build for ALTLinux.
