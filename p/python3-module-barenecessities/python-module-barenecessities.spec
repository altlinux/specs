%define oname barenecessities

Name:       python3-module-barenecessities
Version:    0.2.8
Release:    alt2

Summary:    Provides the bn module containing a dictionary allowing attribute access to values
License:    MIT
Group:      Development/Python3
Url:        http://jimmyg.org/work/code/barenecessities/index.html
BuildArch:  noarch

# Source-url: https://pypi.python.org/packages/ab/7d/6e82e68c7e3be857006b219746d61bd8b72f463d871de1a83c07c6bacf57/BareNecessities-%{version}.tar.gz
Source:     %name-%version.tar
Patch0:     port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
Provides the ``bn`` module containing a dictionary allowing attribute access to
values - I use it so much I've made into a package.

%prep
%setup
%patch0 -p1

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*


%changelog
* Fri Jan 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.8-alt2
- porting on python3

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.8-alt1.qa1
- NMU: applied repocop patch

* Sun Oct 02 2016 Vitaly Lipatov <lav@altlinux.ru> 0.2.8-alt1
- initial build for ALT Linux Sisyphus with rpmgs script
