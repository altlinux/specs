%define modname django-js-asset

Name: python3-module-%modname
Version: 1.2.2
Release: alt1

Summary: script tag with additional attributes for django.forms.Media
License: BSD License
Group: Development/Python3
Url: https://pypi.org/project/django-js-asset/
# https://github.com/matthiask/django-js-asset
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
django-js-asset -- script tag with additional attributes for django.forms.Media

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE README.*
%python3_sitelibdir/*


%changelog
* Tue Jul 13 2021 Alexey Shabalin <shaba@altlinux.org> 1.2.2-alt1
- Build python3 only package.

* Fri May 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.1-alt1
- Initial build for Sisyphus
