Name: python3-module-text-unidecode
Version: 1.3
Release: alt1

Summary: Python port of Text::Unidecode Perl library.
License: GPLv2
Group: Development/Python
Url: https://pypi.org/project/text-unidecode/

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
%python3_sitelibdir/text_unidecode
%python3_sitelibdir/text_unidecode-%version-*-info

%changelog
* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3-alt1
- initial
