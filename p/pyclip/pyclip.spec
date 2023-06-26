%global pypi_name pyclip
%define _unpackaged_files_terminate_build 1

Name: %pypi_name
Version: 0.7.0
Release: alt3
Summary: Cross-platform Clipboard module for Python with binary support
Group: Development/Python

License: Apache-2.0
Url: https://github.com/spyoungtech/pyclip
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools python3-module-wheel

%package -n python3-module-%{pypi_name}
Summary: %summary
Group: Development/Python

# https://bugzilla.altlinux.org/46639
Requires: xclip

%description
Cross-platform clipboard utilities supporting both binary and text data.

%description -n python3-module-%{pypi_name}
Cross-platform clipboard utilities supporting both binary and text data.

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-module-%{pypi_name}
%_bindir/%pypi_name
%doc docs/README.md LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pypi_name}-%version.dist-info/

%changelog
* Mon Jun 26 2023 L.A. Kostis <lakostis@altlinux.ru> 0.7.0-alt3
- Fix xclip dependency (finally) (closes #46639).

* Fri Jun 23 2023 L.A. Kostis <lakostis@altlinux.ru> 0.7.0-alt2
- Added dependency to xclip (closes #46639).

* Sat Apr 01 2023 L.A. Kostis <lakostis@altlinux.ru> 0.7.0-alt1
- Initial build for ALTLinux.

