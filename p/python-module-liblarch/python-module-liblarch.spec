%define module_name liblarch

Name: python-module-%module_name
Version: 0.1
Release: alt1
Summary: Liblarch, a python library to easily handle data structure.
License: LGPLv3
Group: Development/Python
Url: https://live.gnome.org/liblarch

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-devel python-module-distribute

%setup_python_module %module_name

%description
Liblarch is a python library built to easily handle
data structure such are lists, trees and acyclic graphs
(tree where nodes can have multiple parents)

%package -n python-module-%{module_name}_gtk
Summary: GTK binding for Liblarch.
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-%{module_name}_gtk
GTK binding for Liblarch.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc AUTHORS LICENSE README
%python_sitelibdir/%module_name
%python_sitelibdir/%module_name-*.egg-info

%files -n python-module-%{module_name}_gtk
%python_sitelibdir/%{module_name}_gtk
%python_sitelibdir/%{module_name}_gtk-*.egg-info

%changelog
* Thu Oct 04 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux
