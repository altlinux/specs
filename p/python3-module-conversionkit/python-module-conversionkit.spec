%define oname conversionkit

Name:       python3-module-%oname
Version:    0.3.4
Release:    alt2

Summary:    A general purpose conversion library
License:    MIT
Group:      Development/Python3
Url:        http://jimmyg.org/work/code/conversionkit/index.html
BuildArch:  noarch

# Source-url: https://pypi.python.org/packages/d7/fb/eb3b0824f42bf032900f9e7e32072429f1bf0b51f1caf3471a87784c8171/ConversionKit-%{version}.tar.gz
Source:     %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
ConversionKit is a general purpose conversion library designed as an
improvement to the functionality in FormEncode but using simple functions
rather than complex schema and validators and avoiding the use of exceptions to
flag errors. See the introducion in the manual for full details.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*


%changelog
* Fri Jan 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3.4-alt2
- porting on python3

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt1.qa1
- NMU: applied repocop patch

* Sun Oct 02 2016 Vitaly Lipatov <lav@altlinux.ru> 0.3.4-alt1
- initial build for ALT Linux Susyphus with rpmgs script

