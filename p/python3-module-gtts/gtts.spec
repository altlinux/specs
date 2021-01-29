Name: python3-module-gtts
Version: 2.2.1
Release: alt1

Summary: Python interface with Google Translate's TTS API
License: MIT
Group: Development/Python
Url: https://pypi.org/project/gTTS/

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
%_bindir/gtts-cli
%python3_sitelibdir/gtts
%python3_sitelibdir/gTTS-%version-*-info

%changelog
* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt1
- initial
