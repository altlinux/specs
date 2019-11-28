%define modulename pydenticon

%def_without check

Name: python3-module-pydenticon
Version: 0.3.1
Release: alt2

Summary: Library for generating identicons
License: BSD
Group: Development/Python3
Url: https://github.com/azaghal/pydenticon
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Pydenticon is a small utility library that can be used for deterministically
enerating identicons based on the hash of provided data.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*


%changelog
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.1-alt2
- python2 disabled

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1.qa1
- NMU: applied repocop patch

* Sun Oct 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- new version 0.3.1 (with rpmrb script)

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- initial build for ALT Sisyphus

