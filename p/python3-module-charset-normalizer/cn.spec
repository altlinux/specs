Name: python3-module-charset-normalizer
Version: 2.0.6
Release: alt1

Summary: The Real First Universal Charset Detector
License: MIT
Group: Development/Python
Url: https://pypi.org/project/charset-normalizer/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/charset_normalizer
%python3_sitelibdir/charset_normalizer-%version-*-info

%changelog
* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.6-alt1
- initial
