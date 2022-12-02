Name: python3-module-charset-normalizer
Version: 2.1.1
Release: alt1

Summary: The Real First Universal Charset Detector
License: MIT
Group: Development/Python
Url: https://pypi.org/project/charset-normalizer/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/normalizer
%python3_sitelibdir/charset_normalizer
%python3_sitelibdir/charset_normalizer-%version.dist-info

%changelog
* Fri Dec 02 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt1
- 2.1.1 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0-alt1
- 2.1.0 released

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.6-alt1
- initial
