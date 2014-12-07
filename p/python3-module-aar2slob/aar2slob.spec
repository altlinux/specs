%define oname aar2slob

Name: python3-module-%oname
Version: 0.01
Release: alt1.git.x.gf1956a
Summary: converts Aard Dictionary .aar files to slob format
BuildArch: noarch
Group: Development/Other
Url: http://aarddict.org
License: GPL3

#https://github.com/itkach/aar2slob.git
Source: %name.tar

Requires: python3.3(cssselect)
BuildPreReq: rpm-build-python3

%description
converts Aard Dictionary .aar files to slob format

%prep
%setup -n %name

%build
%python3_build

%install
%python3_install --install-lib %python3_sitelibdir --record=INSTALLED_FILES

%files
%python3_sitelibdir/%{oname}*
%doc README*

%changelog
* Sat Feb 14 2015 Ildar Mulyukov <ildar@altlinux.ru> 0.01-alt1.git.x.gf1956a
- initial build for ALT Linux Sisyphus
