%define modname django-js-asset

Name: python-module-%modname
Version: 1.1
Release: alt1

Summary: script tag with additional attributes for django.forms.Media
License: BSD License
Group: Development/Python
Url: https://pypi.org/project/django-js-asset/
# https://github.com/matthiask/django-js-asset
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools


%description
django-js-asset -- script tag with additional attributes for django.forms.Media

%package -n python3-module-%modname
Summary: script tag with additional attributes for django.forms.Media
Group: Development/Python3

%description -n python3-module-%modname
django-js-asset -- script tag with additional attributes for django.forms.Media

%prep
%setup

cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc LICENSE README.*
%python_sitelibdir/*

%files -n python3-module-%modname
%doc LICENSE README.*
%python3_sitelibdir/*


%changelog
* Fri May 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.1-alt1
- Initial build for Sisyphus
