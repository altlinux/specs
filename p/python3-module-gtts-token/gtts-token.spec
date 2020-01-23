Name: python3-module-gtts-token
Version: 1.1.3
Release: alt1

Summary: A python implementation of the token validation of Google Translate
License: MIT
Group: Development/Python
Url: https://pypi.org/project/gTTS-token/

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
%doc LICENSE* README.*
%python3_sitelibdir/gtts_token
%python3_sitelibdir/gTTS_token-%version-*-info

%changelog
* Thu Jan 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.3-alt1
- initial
