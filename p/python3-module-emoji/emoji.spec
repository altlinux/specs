Name: python3-module-emoji
Version: 0.5.3
Release: alt1

Summary: Emoji for Python
License: BSD
Group: Development/Python
Url: https://pypi.org/project/emoji/

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
%python3_sitelibdir/emoji
%python3_sitelibdir/emoji-%version-*-info

%changelog
* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.3-alt1
- initial

