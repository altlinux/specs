%global pypi_name glad

Name: %pypi_name
Version: 2.0.4
Release: alt0.1
Summary: Vulkan/GL/GLES/EGL/GLX/WGL Loader-Generator
Group: Development/Python

License: MIT
Url: https://glad.dav1d.de
Source0: https://github.com/Dav1dde/%pypi_name/archive/refs/tags/%version.tar.gz#/%name-%version.tar
Patch0: %name-%version-%release.patch
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools python3-module-wheel python3-module-jinja2

%package -n python3-module-%{pypi_name}2
Summary: %summary
Group: Development/Python

%description
Multi-Language Vulkan/GL/GLES/EGL/GLX/WGL Loader-Generator based on the official specs.

%description -n python3-module-%{pypi_name}2
Multi-Language Vulkan/GL/GLES/EGL/GLX/WGL Loader-Generator based on the official specs.

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-module-%{pypi_name}2
%doc README.md LICENSE
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pypi_name}2-%version.dist-info/

%changelog
* Tue Mar 07 2023 L.A. Kostis <lakostis@altlinux.ru> 2.0.4-alt0.1
- 2.0.4.

* Fri Dec 09 2022 L.A. Kostis <lakostis@altlinux.ru> 2.0.2-alt0.1
- Initial build for ALTLinux.
