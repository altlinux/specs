%global pypi_name jsonfield

Name:           python3-module-django-%pypi_name
Version:        2.0.2
Release:        alt1
Epoch:          1

Summary:        A reusable Django field that allows you to store validated JSON in your model
License:        BSD
Group:          Development/Python3
URL:            https://github.com/bradjasper/django-jsonfield
BuildArch:      noarch

Source0:        %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-django


%description
django-jsonfield is a reusable Django field that allows you to store validated
JSON in your model. It silently takes care of serialization. To use, simply
add the field to one of your models.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/*


%changelog
* Wed Dec 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:2.0.2-alt1
- Version updated to 2.0.2
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:1.0.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Lenar Shakirov <snejok@altlinux.ru> 1:1.0.1-alt1
- Build correct source (Epoch version up)

* Fri May 26 2017 Lenar Shakirov <snejok@altlinux.ru> 1.0.3-alt1
- Initial build for ALT (based on 1.0.3-4.fc26.src)
